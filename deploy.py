"""
AKAI Deploy — LoRA adapter'ı base model ile birleştir + vLLM server başlat.
Kullanım:
    1) python deploy.py --merge      → adapter + base = merged model
    2) python deploy.py --serve      → vLLM OpenAI-uyumlu server başlat
"""

import os
import argparse
import subprocess
import sys

HF_TOKEN  = os.environ.get("HF_TOKEN", "")
BASE      = "meta-llama/Meta-Llama-3.1-8B-Instruct"
ADAPTER   = "sahin0980/akai-adapter"
MERGED    = "/workspace/akai_merged"
PORT      = 8000


def merge():
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import PeftModel

    print("Base model yükleniyor (CPU, bf16)...")
    tokenizer = AutoTokenizer.from_pretrained(BASE, token=HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        BASE, torch_dtype=torch.bfloat16, token=HF_TOKEN
    )

    print("LoRA adapter yükleniyor...")
    model = PeftModel.from_pretrained(model, ADAPTER, token=HF_TOKEN)

    print("Merge ediliyor...")
    model = model.merge_and_unload()

    print(f"Kaydediliyor: {MERGED}")
    model.save_pretrained(MERGED)
    tokenizer.save_pretrained(MERGED)
    print("Merge tamamlandı.")


def serve():
    print(f"vLLM server başlatılıyor (port {PORT})...")
    cmd = [
        sys.executable, "-m", "vllm.entrypoints.openai.api_server",
        "--model", MERGED,
        "--host", "0.0.0.0",
        "--port", str(PORT),
        "--max-model-len", "4096",
        "--dtype", "bfloat16",
    ]
    subprocess.run(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--merge", action="store_true")
    parser.add_argument("--serve", action="store_true")
    args = parser.parse_args()

    if args.merge:
        merge()
    elif args.serve:
        serve()
    else:
        print("--merge veya --serve belirt")
