from typing import Union, List
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/1/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    """
    ### header parameter
    """
    return {"User-Agent": user_agent}


@app.get("/items/2/")
async def read_items(
    user_agent: Union[str, None] = Header(default=None, convert_underscores=False)
):
    """
    ### disabled underscore transformation
    """
    return {"user_agent": user_agent}


@app.get("/items/3/")
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    """
    ### multiple headers
    """
    return {"X-Token values": x_token}
