from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from utils import classdemo
from main import get_db
from database import datamodel

router = APIRouter(prefix='/lcd', tags=['显示器'])


@router.post('/create', response_model=classdemo.message)
async def create_lcd(lcd_form: classdemo.Lcd,
                          db: Session = Depends(get_db)):
    db_lcd = datamodel.Lcd(
        name=lcd_form.name,
        product_type=lcd_form.product_type,
        screen_size=lcd_form.screen_size,
        screen_ratio=lcd_form.screen_ratio,
        response_time=lcd_form.response_time,
        optimal_resolution=lcd_form.optimal_resolution,
        display_color=lcd_form.display_color,
        brightness=lcd_form.brightness,
        refresh_rate=lcd_form.refresh_rate
    )
    db.add(db_lcd)
    db.commit()
    db.refresh(db_lcd)

    return classdemo.message(
        code=0,
        message='注册成功',
        model=db_lcd
    )


async def search_by_id(id: int, db: Session = Depends(get_db)):
    db_lcd = db.query(datamodel.Lcd).filter(datamodel.Lcd.id == id).first()
    return db_lcd


@router.get('/get', response_model=classdemo.message)
async def get_lcd(id: int,
                       db: Session = Depends(get_db)):
    db_lcd = await search_by_id(id, db)
    if db_lcd is None:
        return classdemo.message(
            code=1,
            message='查找失败',
            model=None
        )
    else:
        return classdemo.message(
            code=0,
            message='查找成功',
            model=db_lcd
        )


async def search_all(db: Session = Depends(get_db)):
    db_lcd_list = db.query(datamodel.Lcd).all()
    return db_lcd_list


@router.get('/all', response_model=classdemo.message)
async def get_lcd_all(db: Session = Depends(get_db)):
    db_lcd_list = await search_all(db)
    
    return classdemo.message(
        code=0,
        message='查找成功',
        model=db_lcd_list
    )