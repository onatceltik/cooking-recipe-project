from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# Import the database connection, models and schemas
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)

# Dependency: This function opens a database session for each request
# and closes it when the request is done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE A RECIPE
# Tell FastAPI to format the output using Response Schema
@router.post("/", response_model=schemas.recipe.Recipe)
def create_recipe(recipe: schemas.recipe.RecipeCreate, db: Session = Depends(get_db())):
    # Convert the Pydantic schema data into an SQLAlchemy database model instance
    # recipe.model_dump() converts the Pydantic object into a dict.
    db_recipe = models.recipe.Recipe(**recipe.model_dump())

    # Add to the database session, commit to save, and refresh to get the new ID
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # FastAPI will automatically convert this database model back into the Pydantic Response schema
    return db_recipe

# READ ALL RECIPES
@router.get("/", response_model=List[schemas.recipe.Recipe])
def get_recipes(skip: int=0, limit: int=100, db: Session = Depends(get_db())):
    # Query the database, skip a certain amount (for pagination), and limit the results
    recipes = db.query(models.recipe.Recipe).offset(skip).limit(limit).all()
    return recipes