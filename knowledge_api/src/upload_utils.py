from fastapi import APIRouter, HTTPException, status, UploadFile
import shutil
from os import path

upload_router = r = APIRouter()
knowledge_destination = "src/data"


@r.post("/file")
async def upload_file(file: UploadFile):
    try:
        with open(path.join(knowledge_destination,file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error uploading file')
    return {'file_size': file.size, 'file_name': file.filename, 'copy': 'SUCCESS'}
