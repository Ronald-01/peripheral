from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from utils import classdemo
from main import get_db
from database import datamodel,security

router = APIRouter(prefix='/user', tags=['用户'])


async def search(number: str, db: Session = Depends(get_db)):
    db_user = db.query(datamodel.User).filter(datamodel.User.number == number).first()
    return db_user


@router.post('/create', response_model=classdemo.message)
async def create_user(user_form: classdemo.User,
                      db: Session = Depends(get_db)):
    db_user = await search(user_form.number, db)
    if db_user:
        return classdemo.message(
            code=1,
            message='已存在该用户',
            model=db_user
        )
    # 需要加密密码
    db_user = datamodel.User(
        number=user_form.number,
        name=user_form.name,
        password=security.hash_password(user_form.password),
        right=user_form.right

    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return classdemo.message(
        code=0,
        message='注册成功',
        model=db_user
    )


# 通过用户number查找用户信息
@router.get('/get', response_model=classdemo.message)
async def get_user(number: str,
                   db: Session = Depends(get_db)):
    db_user = await search(number, db)
    if db_user is None:
        return classdemo.message(
            code=1,
            message='不存在该用户',
            model=None
        )
    else:
        return classdemo.message(
            code=0,
            message='查找成功',
            model=db_user
        )


