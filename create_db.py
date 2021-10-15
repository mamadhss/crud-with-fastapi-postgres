from sqlalchemy.engine import base
from database import Base,engine
from models import Item

print("Creating Databae")


Base.metadata.create_all(engine)