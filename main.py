from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Any
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

app = FastAPI()

# Authenticate with Hugging Face
def authenticate_huggingface(token: str):
    login(token=token)

# Set your Hugging Face token here
huggingface_token = "<access_token_hagging_face"  # Replace this with your actual token
authenticate_huggingface(huggingface_token)

# Model paths and loading
model_mapping = {
    "misral": "fackall/misral-7b-FT-CD-gguf",  
    "llama2": "meta-llama/Llama-2-7b-chat-hf"
}

models = {}
tokenizers = {}

def load_model(model_name: str):
    if model_name in models:
        return models[model_name], tokenizers[model_name]
    
    model_path = model_mapping.get(model_name)
    if not model_path:
        raise HTTPException(status_code=400, detail="Model not found")
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path)
    except OSError as e:
        raise HTTPException(status_code=404, detail=f"Model loading failed: {str(e)}")
    
    models[model_name] = model
    tokenizers[model_name] = tokenizer
    return model, tokenizer

conversations = {}

class QueryRequest(BaseModel):
    model: str
    question: str

class QueryResponse(BaseModel):
    response: str

class Conversation(BaseModel):
    id: str
    date: datetime
    messages: List[Dict[str, Any]]

@app.post("/query", response_model=QueryResponse)
async def query_model(query: QueryRequest):
    model, tokenizer = load_model(query.model)
    
    # Tokenize and generate response
    inputs = tokenizer(query.question, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"])
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Save to conversations
    conversation_id = "some_unique_id"  # This should be a unique identifier, adjust as needed
    if conversation_id not in conversations:
        conversations[conversation_id] = {"id": conversation_id, "date": datetime.now(), "messages": []}
    conversations[conversation_id]["messages"].append({"question": query.question, "response": response_text})
    
    return {"response": response_text}

@app.get("/conversations", response_model=List[Conversation])
async def list_conversations():
    return sorted(conversations.values(), key=lambda x: x["date"], reverse=True)

@app.get("/conversations/{conversation_id}", response_model=Conversation)
async def get_conversation(conversation_id: str):
    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversations[conversation_id]
