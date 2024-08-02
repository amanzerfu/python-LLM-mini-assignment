class ModelManager:
    def __init__(self):
        self.models = {
            "llama2": "openai-llama2",
            "mistral": "openai-mistral"
        }
        self.context = []

    def set_model(self, model_name):
        if model_name in self.models:
            self.current_model = self.models[model_name]
        else:
            raise ValueError("Model not supported.")

    def add_to_context(self, message, role="user"):
        self.context.append({"role": role, "content": message})

    def get_context(self):
        return self.context
