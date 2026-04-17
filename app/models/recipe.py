from sqlalchemy import Column, Integer, String, Text, JSON
from app.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    meal_type = Column(String)

    ingredients = Column(JSON)
    instructions = Column(Text)
    my_notes = Column(Text)

    source_url = Column(String)