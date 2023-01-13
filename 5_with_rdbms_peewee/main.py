from fastapi import FastAPI
from orm import postgresql

# Models import
from models.sample import Sample
from models.user import User
from models.group import Group
from models.pet import Pet
from models.subscription import Subscription
from models.associations import associations

# Routes import
from routes import (
    sample_routes,
    user_routes,
    group_routes,
    pet_routes,
    subscription_routes,
)

app = FastAPI()

postgresql().create_tables([Sample, Group, Subscription, Pet, User, *associations])
# postgresql.create_tables([Sample])

app.include_router(sample_routes.router)
app.include_router(user_routes.router)
app.include_router(group_routes.router)
app.include_router(pet_routes.router)
app.include_router(subscription_routes.router)
