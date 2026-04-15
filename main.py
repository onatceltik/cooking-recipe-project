from fastapi import FastAPI
from app.database import engine
from app.models import recipe
from app.routers import recipes

# Tell SQLAlchemy to create all tables in the database
recipe.Base.metadata.create_all(bind=engine)

# Initialize the application instance
app = FastAPI(title="Recipe App API")

# Include the routes
app.include_router(recipes.router)

@app.get("/")
def root():
    return {"message": "Recipe App Main Page"}