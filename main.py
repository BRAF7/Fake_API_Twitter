#FastAPI
from fastapi import FastAPI

#we defined our app
app = FastAPI()

@app.get(path='/')
def home() -> dict:
    return {'Twiterr' : 'con FastAPI'}