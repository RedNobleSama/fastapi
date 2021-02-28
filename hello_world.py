from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None  # 与bool的区别是可以不穿，默认为Null Optional 选填


# @app.get('/')
# def hello_world():
#     return {"hello": "world"}
#
#
# @app.get('/city/{city}')
# def result(city: str, query_string: Optional[str] = None):
#     return {"city": city, "query_string": query_string}
#
#
# @app.put('/city/{city}')
# def result(city: str, city_info: CityInfo):
#     return {"city": city, "coutry": city_info.country}

@app.get('/')
async def hello_world():
    return {"hello": "world"}


@app.get('/city/{city}')
async def result(city: str, query_string: Optional[str] = None):
    return {"city": city, "query_string": query_string}


@app.put('/city/{city}')
async def result(city: str, city_info: CityInfo):
    return {"city": city, "coutry": city_info.country}

# 启动命令
# uvicorn hello_world:app --reload
