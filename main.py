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

app.mount("/images", StaticFiles(directory="images"), name="images")

@app.post("/files")
async def UploadImage(file: bytes = File(...)):
    with open('./images/'+'uuid.uuid4().hex[:6].upper()'+'.jpg','wb') as image:
        image.write(file)
        image.close()
    return {
        "message": "Image uploaded successfully",
        "output1": "/output/name.jpg",
        "output2": "/output/name.jpg",
        "val1": "value1",
        "val2": "value2",
        "val3": "value3",
        "val4": "value4"
    }