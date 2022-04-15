from fastapi import FastAPI, Request, UploadFile, File
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uuid import uuid4
from os import mkdir
from shutil import copyfileobj

def server(app:FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],    
    )
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/drive/", StaticFiles(directory="uploads"), name="drive")
    templates = Jinja2Templates(directory="templates")
    @app.get("/")
    def index(request:Request):
        return templates.TemplateResponse("index.html", {"request": request})
    @app.get("/api/upload")
    def upload_files(file:UploadFile = File(...)):
        id=str(uuid4())
        mkdir(f"uploads/{id}")
        with open(f"uploads/{id}/{file.filename}", "wb") as f:
            try:
                copyfileobj(file.file, f)
            except:
                return {"error": "File upload failed"}
            finally:
                file.file.close()
        file_url = "https://smartpro.solutions/drive/" + id + "/" + file.filename
        file_name = file.filename
        file_size = file.size
        file_type = file.content_type
        return {"url": file_url, "name": file_name, "size": file_size, "type": file_type}
    @app.get("/api/download")
    def download_files(url:str):
        try:
            file_name = url.split("/")[-1]
            file_path = "uploads/" + "/".join(url.split("/")[3:])
            with open(file_path, "rb") as f:
                file=f.read()
                return FileResponse(file, filename=file_name)
        except: 
            print(Exception)
            return {"error": "File download failed"}
    @app.get("/api/delete")
    def delete_files(url:str):
        try:
            file_path = "uploads/" + "/".join(url.split("/")[3:])
            if file_path.endswith(".py"):
                return {"error": "File deletion failed"}
            else:
                import os
                os.remove(file_path)
                return {"success": "File deleted"}
        except: 
            print(Exception)
            return {"error": "File deletion failed"}
    @app.get("/api/list")
    def list_files(url:str):
        try:
            file_path = "uploads/" + "/".join(url.split("/")[3:])
            if file_path.endswith(".py"):
                return {"error": "File deletion failed"}
            else:
                import os
                files = os.listdir(file_path)
                return {"files": files}
        except: 
            print(Exception)
            return {"error": "File deletion failed"}
    @app.get("/api/rename")
    def rename_files(url:str, new_name:str):
        try:
            file_path = "uploads/" + "/".join(url.split("/")[3:])
            if file_path.endswith(".py"):
                return {"error": "File deletion failed"}
            else:
                import os
                os.rename(file_path, file_path.replace(file_path.split("/")[-1], new_name))
                return {"success": "File renamed"}
        except: 
            print(Exception)
            return {"error": "File deletion failed"}
    return app
    