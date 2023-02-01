from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uuid 

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/output", StaticFiles(directory="output"), name="output")

@app.post("/upload")
async def UploadImage(file: bytes = File(...)):
    with open('./input/'+'uuid.uuid4().hex[:6].upper()'+'.jpg','wb') as image:
        image.write(file)
        image.close()
    return {
        "message": "Image uploaded successfully",
        "output1": "/output/1.jpg",
        "output2": "/output/1.jpg",
        "val1": 1,
        "val2": 2,
        "val3": 3,
        "val4": 4
    }