from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
# import os
# os.environ["TORCHDYNAMO_DISABLE"] = "1"

device = "cuda" if torch.cuda.is_available() else "cpu"

# model_name = "google/gemma-3-1b-pt"
# model_name = "Qwen/Qwen2.5-7B-Instruct"

# --best score
model_name = "google/gemma-3-4b-it"


def get_model():
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="cuda"
    )

    return model

def get_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    return tokenizer



