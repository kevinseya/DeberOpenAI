import uvicorn
from fastapi import FastAPI
from UCE.OpenAI.openAItest import Document, inference

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return{
        'inference': response[0],
        'usage': response[1],
    }
#Correr main.py o uvicorn main:app --reload --port:<puerto>
if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=1008)



