from fastapi import FastAPI
from pydantic import BaseModel

from transformers import T5ForConditionalGeneration, T5Tokenizer

from src.inference import summarize


class Item(BaseModel):
    text: str

app = FastAPI()

# import tokenizer and model
model_path = 'model/SloT5-cnndm_slo_pretraining'
print(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

@app.post("/summarize/")
async def generate_summary(item: Item):
    summary = summarize(tokenizer, model, item.text)
    return {'summary': summary,
            'model': model_path}