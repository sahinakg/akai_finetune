import torch, json, os, time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel
import uvicorn

HF_TOKEN = os.environ.get("HF_TOKEN", "")
BASE = "meta-llama/Meta-Llama-3.1-8B-Instruct"
ADAPTER = "sahin0980/akai-adapter"

print("Model yukleniyor...")
bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(BASE, token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(BASE, quantization_config=bnb, device_map="auto", token=HF_TOKEN)
model = PeftModel.from_pretrained(model, ADAPTER, token=HF_TOKEN)
model.eval()
print("Model hazir")

app = FastAPI()

@app.post("/v1/chat/completions")
async def chat(request: Request):
    body = await request.json()
    messages = body.get("messages", [])
    max_tokens = body.get("max_tokens", 512)
    temp = body.get("temperature", 0.7)
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_tokens, temperature=temp, do_sample=temp > 0, pad_token_id=tokenizer.eos_token_id)
    reply = tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    return JSONResponse({"id": "chatcmpl-" + str(int(time.time())), "object": "chat.completion", "choices": [{"index": 0, "message": {"role": "assistant", "content": reply}, "finish_reason": "stop"}]})

@app.get("/v1/models")
async def models():
    return {"data": [{"id": "akai", "object": "model"}]}

uvicorn.run(app, host="0.0.0.0", port=8888)
