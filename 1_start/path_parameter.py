from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    a = "A"
    b = "B"
    c = "C"


@app.get("/")
async def root():
    """
    ### basic route
    """
    return {"message": "Hello World!"}


@app.get("/items/me")
async def read_you():
    """
    # duplicated path with path parameter should be declared before path parameter
    """
    return {"item_id": "it's about you"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    # path parameters
    """
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    # predefined path parameter values using Enum class
    """
    if model_name is ModelName.a:
        return {"model_name": model_name, "message": "AAA"}
    elif model_name.value == "B":
        return {"model_name": model_name, "message": "BBB"}
    return {"model_name": model_name, "message": "rest"}


@app.get("/models/file/{file_path:path}")
async def read_file(file_path: str):
    """
    # Path parameters containing slash(/), such as paths
    """
    return {"path": file_path}
