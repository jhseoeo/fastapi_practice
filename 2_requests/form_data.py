from fastapi import FastAPI, Form, Body


app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form(), asd: str = Body()):
    """
    ### form data parameters
    """
    return {"username": username}
