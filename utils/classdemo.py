import json
from typing import Optional, Any, Union
from pydantic import BaseModel, Field


class Collection(BaseModel):
    """收藏"""
    # 0为鼠标，1为键盘
    type: int = Field(None, description='类型')
    collection_id: int = Field(None, description='收藏品id')

    class Config:
        orm_mode = True


class Collection_boss(Collection):
    number: str = Field(None, description='账户')

    class Config:
        orm_mode = True


class User(BaseModel):
    """用户"""

    id: int = Field(None, description='标识符')
    number: str = Field(None, description='账户')
    name: str = Field(None, description='用户名')
    password: str = Field(None, description='密码')
    right: Optional[int] = Field(None, description='管理员权限')

    class Config:
        orm_mode = True


class Mice(BaseModel):
    """鼠标"""
    id: int = Field(None, description='标识符')
    name: str = Field(None, description='名称')

    aplicable_type: Optional[str] = Field(None, description='适用类型')
    mice_size: Optional[str] = Field(None, description='鼠标大小')
    work_way: Optional[str] = Field(None, description='工作方式')
    connect_method: Optional[str] = Field(None, description='连接方式')
    mice_interface: Optional[str] = Field(None, description='鼠标接口')
    key_number: Optional[str] = Field(None, description='按键数')
    wheel_direction: Optional[str] = Field(None, description='滚轮方向')

    color: Optional[str] = Field(None, description='颜色')
    line_lenght: Optional[str] = Field(None, description='线长')
    size: Optional[str] = Field(None, description='尺寸')
    weight: Optional[str] = Field(None, description='重量')

    class Config:
        orm_mode = True


class Keyboard(BaseModel):
    """键盘"""
    id: int = Field(None, description='标识符')
    name: str = Field(None, description='名称')

    list_date: Optional[str] = Field(None, description='上市日期')
    product_position: Optional[str] = Field(None, description='产品定位')
    connect_method: Optional[str] = Field(None, description='连接方式')
    keyboard_interface: Optional[str] = Field(None, description='键盘接口')
    key_number: Optional[str] = Field(None, description='按键数')
    keyboard_layout: Optional[str] = Field(None, description='键盘布局')

    axis: Optional[str] = Field(None, description='轴')

    color: Optional[str] = Field(None, description='颜色')
    size: Optional[str] = Field(None, description='尺寸')
    weight: Optional[str] = Field(None, description='重量')
    supply_mode: Optional[str] = Field(None, description='供电模式')

    class Config:
        orm_mode = True

class Lcd(BaseModel):
    """显示器"""
    id: int = Field(None, description='标识符')
    name: str = Field(None, description='名称')

    product_type: Optional[str] = Field(None, description='产品类型')
    screen_size: Optional[str] = Field(None, description='屏幕尺寸')
    screen_ratio: Optional[str] = Field(None, description='屏幕比例')
    response_time: Optional[str] = Field(None, description='响应时间')
    optimal_resolution: Optional[str] = Field(None, description='最佳分辨率')


    display_color: Optional[str] = Field(None, description='显示颜色')
    brightness: Optional[str] = Field(None, description='亮度')
    refresh_rate: Optional[str] = Field(None, description='刷新率')

    class Config:
        orm_mode = True



class message(BaseModel):
    code: int
    message: str
    model: Any
