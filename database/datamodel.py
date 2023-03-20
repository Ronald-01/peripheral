from sqlalchemy import Column, Integer, String

from .database import Base


class Mice(Base):
    """鼠标"""
    __tablename__ = 'mice'
    id = Column(Integer, nullable=False, primary_key=True, comment='标识符')
    name = Column(String(30), unique=True, nullable=False, comment='名称')
    aplicable_type = Column(String(30), comment='适用类型')
    mice_size = Column(String(30), comment='鼠标大小')
    work_way = Column(String(30), comment='工作方式')
    connect_method = Column(String(30), comment='连接方式')
    mice_interface = Column(String(30), comment='鼠标接口')
    key_number = Column(String(30), comment='按键数')
    wheel_direction = Column(String(30), comment='滚轮方向')

    color = Column(String(50), comment='颜色')
    line_lenght = Column(String(30), comment='线长')
    size = Column(String(50), comment='尺寸')
    weight = Column(String(30), comment='重量')


class Keyboard(Base):
    """键盘"""
    __tablename__ = 'keyboard'
    id = Column(Integer, nullable=False, primary_key=True, comment='标识符')
    name = Column(String(50), unique=True, nullable=False, comment='名称')

    list_date = Column(String(30), comment='上市日期')
    product_position = Column(String(30), comment='产品定位')
    connect_method = Column(String(30), comment='连接方式')
    keyboard_interface = Column(String(30), comment='键盘接口')
    key_number = Column(String(30), comment='按键数')
    keyboard_layout = Column(String(30), comment='键盘布局')

    axis = Column(String(150), comment='轴')

    color = Column(String(30), comment='颜色')
    size = Column(String(100), comment='尺寸')
    weight = Column(String(30), comment='重量')
    supply_mode = Column(String(30), comment='供电模式')


class User(Base):
    """用户"""
    __tablename__ = 'user'

    id = Column(Integer, nullable=False, primary_key=True, comment='标识符')
    number = Column(String(30), nullable=False, unique=True, comment='账户')

    name = Column(String(30), nullable=False, comment='用户名')
    password = Column(String(100), nullable=False, comment='密码')
    right = Column(Integer, comment='管理员权限')


class Collection(Base):
    """收藏"""
    __tablename__ = 'collection'

    # 0为鼠标，1为键盘
    type = Column(Integer, nullable=False,primary_key=True, comment='类型')
    number = Column(String(30), nullable=False,primary_key=True, comment='账户')
    collection_id = Column(Integer, nullable=False,primary_key=True, comment='收藏品id')
