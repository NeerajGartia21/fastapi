from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")

@app.post("/files")
async def UploadImage(file: bytes = File(...)):
    with open('./images/image.jpg','wb') as image:
        image.write(file)
        image.close()
    return 'got it'