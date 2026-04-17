from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import recipe as recipe_models
from app.routers import recipes

# Tell SQLAlchemy to create all tables in the database
recipe_models.Base.metadata.create_all(bind=engine)

# Initialize the application instance
app = FastAPI(title="Recipe App API")


# --- CORS CONFIG ---
# URLs where Ract app will live
origins = [
    "http://localhost:3000", # Standard React port
    "http://localhost:5173", # Vite port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods: GET, POST, PUT, DELETE
    allow_headers=["*"], # Allows all headers
)
# --- CORS CONFIG --- (END)

# Include the routes
app.include_router(recipes.router)

@app.get("/")
def root():
    return {"message": "Recipe App Main Page"}