from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from fastapi.responses import FileResponse
from utils import classdemo
from main import get_db
from database import datamodel

router = APIRouter(prefix='/picture', tags=['图片'])


@router.get('/', response_model=classdemo.message)
async def download_picture(filename: str):
    try:
        filepath = 'utils/picture/' + filename + '.jpg'
        return FileResponse(filepath)
    except:
        return classdemo.message(
            code=1,
            message='获取失败',
            model=None
        )
