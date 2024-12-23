import os
from llama_cpp import Llama

model_path = os.environ.get("MODEL_PATH")

if not os.path.isfile(model_path):
    print(
        f"Model file '{model_path}' not found. Please download it before running this script."
    )
    exit(1)


llm = Llama(model_path=model_path, n_ctx=2096, n_batch=126)

async def generate_response(prompt):
    output = llm(prompt, max_tokens=150, temperature=0.7, top_p=0.9)
    return output["choices"][0]["text"].strip()
