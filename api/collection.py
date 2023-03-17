from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from utils import classdemo
from main import get_db
from database import datamodel
from database.security import get_current_active_user

router = APIRouter(prefix='/collection', tags=['收藏'])


# 对某个设备进行收藏
@router.post('/create', response_model=classdemo.message)
async def create_collection(form: classdemo.Collection,
                            current_user: classdemo.User = Depends(get_current_active_user),
                            db: Session = Depends(get_db)):
    try:
        db_collection = await search_collection(form.collection_id, form.type, current_user.number, db)
        if db_collection:
            return classdemo.message(
                code=0,
                message='已存在',
                model=db_collection
            )
        db_collection = datamodel.Collection(
            number=current_user.number,
            type=form.type,
            collection_id=form.collection_id

        )
        db.add(db_collection)
        db.commit()
        db.refresh(db_collection)

        return classdemo.message(
            code=0,
            message='成功',
            model=db_collection
        )
    except:
        return classdemo.message(
            code=1,
            message='失败',
            model=None
        )


# 获取某一条收藏记录
async def search_collection(collection_id: int,
                            collection_type: int, user_number: str,
                            db: Session = Depends(get_db)):
    db_collection = db.query(datamodel.Collection).filter(
        datamodel.Collection.type == collection_type and
        datamodel.Collection.number == user_number and
        datamodel.Collection.collection_id).first()
    return db_collection if db_collection else None


# 获取某个用户的所有收藏记录
async def search_all_collection(user_number: str,
                                db: Session = Depends(get_db)):
    db_collection = db.query(datamodel.Collection).filter(datamodel.Collection.number == user_number).all()
    return db_collection if db_collection else None


# 删除某一条收藏记录
async def delete_one_collection(db: Session, collection_id: int,
                                collection_type: int, user_number: str):
    try:
        # delete的返回值为受影响的行数
        db_collection_delete = db.query(datamodel.Collection).filter(
            datamodel.Collection.type == collection_type and
            datamodel.Collection.number == user_number and
            datamodel.Collection.collection_id).delete()
        db.commit()
        return db_collection_delete

    except:
        return None


# 取消收藏
@router.delete('/delete', response_model=classdemo.message)
async def delete_collection(
        collection_id: int,
        collection_type: int,
        db: Session = Depends(get_db),
        current_user: classdemo.User = Depends(get_current_active_user)):
    try:
        db_collection_delete = await delete_one_collection(db, collection_id, collection_type, current_user.number)
        if db_collection_delete == 0:
            return classdemo.message(
                code=1,
                message='不存在',
                model=None
            )
        return classdemo.message(
            code=0,
            message='成功',
            model='已影响行数：' + str(db_collection_delete)
        )

    except:
        return classdemo.message(
            code=1,
            message='失败',
            model=None
        )


# 获取某个用户的所有收藏记录
@router.get('/get', response_model=classdemo.message)
async def get_collection(current_user: classdemo.User = Depends(get_current_active_user),
                         db: Session = Depends(get_db)):
    try:
        db_collection = await search_all_collection(current_user.number, db)
        if db_collection:
            return classdemo.message(
                code=0,
                message='成功',
                model=db_collection
            )
        else:
            return classdemo.message(
                code=1,
                message='失败',
                model=None
            )
    except:
        return classdemo.message(
            code=1,
            message='失败',
            model=None
        )
