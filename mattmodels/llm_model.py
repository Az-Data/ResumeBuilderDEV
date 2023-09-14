from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import BitsAndBytesConfig
import transformers
import torch

def load_model(model_id, quantization_config):
    if quantization_config == '8-bit':
        quantization_config = BitsAndBytesConfig(load_in_8bit=True, bnb_4bit_compute_dtype=torch.float16)
    elif quantization_config == '4-bit':
        quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
    else:
        quantization_config = None
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        quantization_config=quantization_config
    )
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        trust_remote_code=True,
        device_map="auto"
    )
    return pipeline

def generate_sequences(prompt, hyper_dict, pipeline):
    sequences = pipeline(
    prompt,
    do_sample=True,
    return_full_text=False,
    top_k=hyper_dict['top_k'],
    top_p=hyper_dict['top_p'],
    temperature=hyper_dict['temperature'],
    num_return_sequences=1,
    batch_size=hyper_dict['batch_size'],
    max_length=hyper_dict['max_length'],
    repetition_penalty=hyper_dict['repetition_penalty']
    )
    return sequences
