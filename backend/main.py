from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
import os

app = FastAPI()

origins = [
    "http://localhost:5500",  
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
async def read_data():
    message = """
    Ваш комфорт - наши заботы 
    Свежий ремонт 
    Услужливый персонал
    """
    image_path = "static\B4rEJ09-Puo.png"
    image_url = f"http://localhost:8000/{image_path}"
    return JSONResponse(content={"message": message, "image_url": image_url})

@app.get("/api/data2")
async def read_data():
    message = """
    Циркулярный душ
Свежая питьевая вода
Здоровье для всей семьи
    """
    image_path = "static\\a9pFSC8dTlo.png"
    image_url = f"http://localhost:8000/{image_path}"
    return JSONResponse(content={"message": message, "image_url": image_url})

@app.get("/api/data3")
async def read_data():
    message = """
    Вкусно
Полезно
Уникально
    """
    image_path = "static\sKLzgwcB5is.png"
    image_url = f"http://localhost:8000/{image_path}"
    return JSONResponse(content={"message": message, "image_url": image_url})

@app.get("/static/{filename}")
async def get_image(filename: str):
    file_path = os.path.join("static", filename)
    return FileResponse(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
