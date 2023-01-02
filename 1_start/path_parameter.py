from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    a = "A"
    b = "B"
    c = "C"


@app.get("/")
async def root():
    return {"message": "Hello World!"}


# duplicated path with path parameter should be declared before path parameter
@app.get("/items/me")
async def read_you():
    return {"item_id": "it's about you"}


# path parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# predefined path parameter values using Enum class
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.a:
        return {"model_name": model_name, "message": "AAA"}
    elif model_name.value == "B":
        return {"model_name": model_name, "message": "BBB"}
    return {"model_name": model_name, "message": "rest"}


# Path parameters containing slash(/), such as paths
@app.get("/models/file/{file_path:path}")
async def read_file(file_path: str):
    return {"path": file_path}
