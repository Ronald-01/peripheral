import configparser
import os
import random
import string
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt, ExpiredSignatureError
from passlib.context import CryptContext
from sqlalchemy.orm.session import Session
from main import get_db
from database.datamodel import User
from api import user

config = configparser.ConfigParser()

path = os.path.join(os.getcwd(), 'database', 'sql_config.ini')
print(path)
config.read(path)

SECRET_KEY = config['security']['secret_key']
ALGORITHM = config['security']['algorithm']
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    config['security']['access_token_expire_minutes'])

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='sql/token')


# 信息加密与校验
def hash_password(password: str):
    """返回哈希密码,相同的明文hash值相同"""
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str):
    """对明文与哈希密码进行验证"""
    return pwd_context.verify(plain, hashed)


# 认证用户合法性(在数据库中找该用户)
def authenticate_user(number: str, password: str, db: Session):
    db_user = db.query(User).filter(User.number == number).first()
    if db_user:
        return db_user if (db_user.password
                           and verify_password(password, db_user.password)) else None
    else:
        return None


# token生成与校验
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    print(expires_delta, 'token有效时间')
    # 设置过期时间为世界标准时间+token有效时间
    expire = datetime.utcnow() + (expires_delta
                                  if expires_delta else timedelta(minutes=15))
    print(expire, 'token过期时间')
    to_encode.update({'exp': expire})
    print(to_encode, 'to_encode的内容')
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme),
                           db: Session = Depends(get_db)):
    try:
        print(token, '打印当前token')
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload, '打印解码后的token')

        number: str = payload.get('sub')
        time: timedelta = payload.get('exp')
        if number is None:
            return None
        if time is None:
            return None

    except ExpiredSignatureError as e:
        print("token过期")
        return None
    except JWTError:
        print(JWTError)
        return None

    return await user.search(number, db)


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if current_user is None:
        raise credentials_exception
    return current_user if current_user else None


# 首先导入需要用到的模块


# 定义激活码生成函数，并将激活码的长度length作为参数
def create_invitation_code(length):
    result = ''  # 用于存放激活码
    s = string.ascii_letters + string.digits  # 获取字母和数字，作为生成激活码的字符集
    # string.ascii_letters  字符串常量，包含所有的大小写字母的字符串:'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # string.digits 字符串常量，包含数字0-9的字符串 '0123456789'
    for i in range(length):
        str = s[random.randint(0, len(s) - 1)]
        # n = random.randint(a, b)  #生成的随机整数n: a<= n <= b
        # 生成随机整数作为s的索引，随机整数的范围要同s的索引一致
        # 从字符集s中随机取一个字符
        result += str  # 收集随机生成的字符，形成激活码
    return result  # 返回激活码


from datetime import timedelta
from tokenize import Token
from wsgiref.handlers import format_date_time
from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from utils import classdemo

router = APIRouter(prefix='/sql', tags=['数据库'])


# 该接口用于用户登录生成token
@router.post('/token')
# OAuth2PasswordRequestForm可变更为其他的Form
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)):
    # print(form_data.password,'前端传来表单中的password')
    # 验证该用户是否存在
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return {'code': 1, 'message': '登陆失败'}
    # 设置token有效时间
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # 默认此处的user.number唯一，即账号不会重复，否则需要更改sub
    # 根据number(账号)生成token
    access_token = create_access_token(data={'sub': user.number},
                                       expires_delta=access_token_expires)

    return {
        'code': 0,
        'message': '登陆成功',
        'access_token': access_token,
        'token_type': 'bearer',
        'user': user
    }


# 该接口用于检查当前token(是否存在，是否过期)
@router.get("/current_user")
async def get_current_user(current_user: classdemo.User = Depends(get_current_active_user)):
    return current_user
