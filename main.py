from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel, create_model
import pickle 
import numpy as np

pickled_model = pickle.load(open('model/iso_forest_model.sav', 'rb'))

Input=create_model('Input', **{f: (float, ...) for f in pickled_model.feature_names_in_})

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome"}

@app.post("/predict")
def predict(input: Input):
    pred=int(pickled_model.predict(np.array([list(dict(input).values())])))
    return {"pred": pred}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")