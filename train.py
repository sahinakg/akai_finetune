"""
AKAI Fine-tuning — Llama 3.1 8B + QLoRA
Çalıştır: python train.py
"""

import os
import json
import torch
from datasets import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from peft import LoraConfig, get_peft_model, TaskType
from trl import SFTTrainer, SFTConfig

# ── Ayarlar ────────────────────────────────────────────────────────────────
BASE_MODEL   = "meta-llama/Meta-Llama-3.1-8B-Instruct"
DATASET_FILE = "akai_data/dataset_export.jsonl"
OUTPUT_DIR   = "akai_adapter"
HF_TOKEN     = os.environ.get("HF_TOKEN", "")   # runpod'da env var olarak girin

LORA_R       = 16
LORA_ALPHA   = 32
LORA_DROPOUT = 0.05
TARGET_MODULES = ["q_proj", "k_proj", "v_proj", "o_proj",
                  "gate_proj", "up_proj", "down_proj"]

MAX_SEQ_LEN  = 2048
BATCH_SIZE   = 2          # 24 GB GPU için güvenli
GRAD_ACCUM   = 4          # efektif batch = 8
EPOCHS       = 3
LR           = 2e-4
# ───────────────────────────────────────────────────────────────────────────


def load_dataset_from_jsonl(path: str) -> Dataset:
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return Dataset.from_list(records)


def format_messages(example, tokenizer):
    """messages listesini model chat template'ine dönüştür."""
    text = tokenizer.apply_chat_template(
        example["messages"],
        tokenize=False,
        add_generation_prompt=False,
    )
    return {"text": text}


def main():
    # 4-bit quantization (QLoRA)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    print("Model yükleniyor...")
    tokenizer = AutoTokenizer.from_pretrained(
        BASE_MODEL,
        token=HF_TOKEN,
        trust_remote_code=True,
    )
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=bnb_config,
        device_map="auto",
        token=HF_TOKEN,
        trust_remote_code=True,
    )
    model.config.use_cache = False

    # LoRA
    lora_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        target_modules=TARGET_MODULES,
        bias="none",
        task_type=TaskType.CAUSAL_LM,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # Dataset
    print("Dataset yükleniyor...")
    raw = load_dataset_from_jsonl(DATASET_FILE)
    raw = raw.map(lambda ex: format_messages(ex, tokenizer))
    raw = raw.train_test_split(test_size=0.1, seed=42)

    # Eğitim
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        fp16=False,
        bf16=True,
        logging_steps=10,
        eval_strategy="steps",
        eval_steps=50,
        save_strategy="steps",
        save_steps=100,
        save_total_limit=2,
        load_best_model_at_end=True,
        report_to="none",
        max_seq_length=MAX_SEQ_LEN,
        dataset_text_field="text",
        packing=False,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=raw["train"],
        eval_dataset=raw["test"],
        tokenizer=tokenizer,
    )

    print("Eğitim başlıyor...")
    trainer.train()
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print(f"Adapter kaydedildi: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
