from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

# Optionally authenticate to Hugging Face
def authenticate_huggingface(token: str):
    login(token=token)

model_mapping = {
    "misral": "fackall/misral-7b-FT-CD-gguf",  # Replace with actual model path if available
    "llama2": "meta-llama/Llama-2-7b-chat-hf"
}

def load_model(model_name: str, token: str):
    if model_name not in model_mapping:
        raise ValueError("Model name not recognized.")
    
    model_path = model_mapping[model_name]

    # Authenticate if required
    authenticate_huggingface(token)
    
    try:
        # Load the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path)
        return tokenizer, model
    except Exception as e:
        raise RuntimeError(f"Error loading model {model_name}: {e}")

def generate_response(model_name: str, query: str, token: str):
    tokenizer, model = load_model(model_name, token)
    
    inputs = tokenizer(query, return_tensors="pt")
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

