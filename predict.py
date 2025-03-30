
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import dotenv

dotenv.load_dotenv()

MODEL_NAME = "Amaan39/Roberta-Webis-CPC"
tokenizer = AutoTokenizer.from_pretrained("FacebookAI/roberta-base")
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME).to("mps")

def classify_paraphrase(text1: str, text2: str):
    text1 = text1.replace("\n", " ")
    text2 = text2.replace("\n", " ")
    inputs = tokenizer(text1, text2, return_tensors="pt", truncation=True, padding=True)
    inputs = inputs.to("mps")
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    paraphrase_prob = probs[0][1].item()
    return "Paraphrase" if paraphrase_prob > 0.5 else "Not a Paraphrase", paraphrase_prob