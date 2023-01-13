from fastapi import FastAPI
from orm import postgresql
from routes import sample_routes

postgresql.connect()

app = FastAPI()

app.include_router(sample_routes.router)
