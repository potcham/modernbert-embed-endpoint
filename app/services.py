from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self, model_name: str):
        # self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = SentenceTransformer(model_name)

    def get_embeddings(self, text: str):
        # inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        # outputs = self.model(**inputs)
        outputs = self.model.encode([text])
        print(outputs, outputs.shape)
        return list(outputs[0]) # .last_hidden_state.mean(dim=1).detach().tolist()
