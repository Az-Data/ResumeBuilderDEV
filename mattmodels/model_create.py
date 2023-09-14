import os
target_dir = '../mattmodels'
os.chdir(target_dir)

import transformers
from llm_model import load_model, generate_sequences

# Log into huggingface using token stored in txt file
# f = open('token.txt','r')                           # Store uggingface token in token.txt in this directory
# token = f.readline()

os.system(f'huggingface-cli login --token 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')

# Specify model parameters
model_id = "meta-llama/Llama-2-7b-chat-hf"          # from https://huggingface.co/models
quantization = "8-bit"                              # 8-bit, 4-bit, None
output_dir = 'model_files'                          # choose model file location

# Load Model
pipeline = load_model(model_id=model_id, quantization_config=quantization)

# Export Pipeline to file
pipeline.save_pretrained(output_dir)
print("Model saved successfully")