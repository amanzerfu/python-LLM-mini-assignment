from transformers import LlamaForCausalLM, LlamaTokenizer, AutoModelForCausalLM, AutoTokenizer
import torch

class LLMService:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.context = []

    def select_model(self, model_name):
        try:
            if model_name.lower() == "llama2":
                self.tokenizer = LlamaTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
                self.model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
            elif model_name.lower() == "mistral":
                self.tokenizer = AutoTokenizer.from_pretrained("hf-model-identifier-for-mistral")
                self.model = AutoModelForCausalLM.from_pretrained("hf-model-identifier-for-mistral")
            else:
                raise ValueError("Please select a valid model: llama2 or mistral")
            self.model.eval()  # Set the model to evaluation mode
        except Exception as e:
            raise RuntimeError(f"Failed to load model '{model_name}': {e}")

    def send_query(self, query):
        if not self.model or not self.tokenizer:
            raise ValueError("Model not selected. Please select a model first.")

        # Add the user query to the context
        self.context.append({"role": "user", "content": query})
        
        # Prepare the input text by concatenating the conversation context
        input_text = "".join([f"{msg['role']}: {msg['content']}\n" for msg in self.context])
        
        # Tokenize the input text
        inputs = self.tokenizer(input_text, return_tensors="pt")
        
        # Generate a response
        with torch.no_grad():
            outputs = self.model.generate(inputs.input_ids, max_length=512, num_return_sequences=1)
        
        # Decode the generated text
        response_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract the assistant's response
        response = response_text.split("user:")[-1].strip().split("assistant:")[-1].strip()
        
        # Add the assistant's response to the context
        self.context.append({"role": "assistant", "content": response})
        
        return response

    def reset_context(self):
        self.context = []
