from fastapi import FastAPI
from UCE.OpenAI.openAItest import Document, inference
app = FastAPI()

@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return{
        'inference': response[0],
        'usage': response[1],
    }

