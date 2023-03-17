from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import SessionLocal

app = FastAPI(
    title='外设对比平台',
    version='0.0.1dev'
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# origin = [
#     "http://localhost:8080",'*'
# ]

# 跨域设置
app.add_middleware(
    CORSMiddleware,
    # 允许全部源
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

from api import mice, keyboard, picture, user, collection
from database import security

# 路由
app.include_router(mice.router)
app.include_router(keyboard.router)
app.include_router(picture.router)
app.include_router(user.router)
app.include_router(security.router)
app.include_router(collection.router)


@app.get('/')
def test():
    return {
        'message': 'Hello World'
    }
