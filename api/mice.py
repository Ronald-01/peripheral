from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm.session import Session
from utils import classdemo
from main import get_db
from database import datamodel

router = APIRouter(prefix='/mice', tags=['鼠标'])


@router.post('/create', response_model=classdemo.message)
async def create_mice(mice_form: classdemo.Mice,
                      db: Session = Depends(get_db)):
    db_mice = datamodel.Mice(
        name=mice_form.name,
        aplicable_type=mice_form.aplicable_type,
        mice_size=mice_form.mice_size,
        work_way=mice_form.work_way,
        connect_method=mice_form.connect_method,
        mice_interface=mice_form.mice_interface,
        key_number=mice_form.key_number,
        wheel_direction=mice_form.wheel_direction,
        color=mice_form.color,
        line_lenght=mice_form.line_lenght,
        size=mice_form.size,
        weight=mice_form.weight
    )
    db.add(db_mice)
    db.commit()
    db.refresh(db_mice)

    return classdemo.message(
        code=0,
        message='上传成功',
        model=db_mice
    )



async def search_by_name(name: str, db: Session = Depends(get_db)):
    db_model = db.query(datamodel.Mice).filter(datamodel.Mice.name.like(f'%{name}%')).all()
    return db_model
    
@router.get('/get', response_model=classdemo.message)
async def get_mice(name: str,
                   db: Session = Depends(get_db)):
    db_model = await search_by_name(name, db)
    if db_model is None:
        return classdemo.message(
            code=1,
            message='查找失败',
            model=None
        )
    else:
        return classdemo.message(
            code=0,
            message='查找成功',
            model=db_model
        )


async def search_by_id(id: int, db: Session = Depends(get_db)):
    db_mice = db.query(datamodel.Mice).filter(datamodel.Mice.id == id).first()
    return db_mice


@router.get('/get_by_id', response_model=classdemo.message)
async def get_mice_by_id(id: int,
                   db: Session = Depends(get_db)):
    db_mice = await search_by_id(id, db)
    if db_mice is None:
        return classdemo.message(
            code=1,
            message='查找失败',
            model=None
        )
    else:
        return classdemo.message(
            code=0,
            message='查找成功',
            model=db_mice
        )

async def search_all(db: Session = Depends(get_db)):
    db_mice_list = db.query(datamodel.Mice).all()
    return db_mice_list


@router.get('/all', response_model=classdemo.message)
async def get_mice_all(db: Session = Depends(get_db)):
    db_mice_list = await search_all(db)
    
    return classdemo.message(
        code=0,
        message='查找成功',
        model=db_mice_list
    )

