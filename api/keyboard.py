from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from utils import classdemo
from main import get_db
from database import datamodel

router = APIRouter(prefix='/keyboard', tags=['键盘'])


@router.post('/create', response_model=classdemo.message)
async def create_keyboard(keyboard_form: classdemo.Keyboard,
                          db: Session = Depends(get_db)):
    db_keyboard = datamodel.Keyboard(
        name=keyboard_form.name,
        list_date=keyboard_form.list_date,
        product_position=keyboard_form.product_position,
        connect_method=keyboard_form.connect_method,
        keyboard_interface=keyboard_form.keyboard_interface,
        key_number=keyboard_form.key_number,
        keyboard_layout=keyboard_form.keyboard_layout,
        axis=keyboard_form.axis,
        color=keyboard_form.color,
        size=keyboard_form.size,
        weight=keyboard_form.weight,
        supply_mode=keyboard_form.supply_mode,
    )
    db.add(db_keyboard)
    db.commit()
    db.refresh(db_keyboard)

    return classdemo.message(
        code=0,
        message='注册成功',
        model=db_keyboard
    )


async def search_by_id(id: int, db: Session = Depends(get_db)):
    db_keyboard = db.query(datamodel.Keyboard).filter(datamodel.Keyboard.id == id).first()
    return db_keyboard


@router.get('/get', response_model=classdemo.message)
async def get_keyboard(id: int,
                       db: Session = Depends(get_db)):
    db_keyboard = await search_by_id(id, db)
    if db_keyboard is None:
        return classdemo.message(
            code=1,
            message='查找失败',
            model=None
        )
    else:
        return classdemo.message(
            code=0,
            message='查找成功',
            model=db_keyboard
        )


async def search_all(db: Session = Depends(get_db)):
    db_keyboard_list = db.query(datamodel.Keyboard).all()
    return db_keyboard_list


@router.get('/all', response_model=classdemo.message)
async def get_keyboard_all(db: Session = Depends(get_db)):
    db_keyboard_list = await search_all(db)
    
    return classdemo.message(
        code=0,
        message='查找成功',
        model=db_keyboard_list
    )