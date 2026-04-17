from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import Optional

# The Base Schema -> Properties shared across all other schemas
class RecipeBase(BaseModel):
    title: str
    meal_type: str
    ingredients: list[str] # validates that we get a list of strings
    instructions: str

    # HttpUrl ensures the user provides a valid web link (or leaves it blank)
    my_notes: Optional[str] = None
    source_url: Optional[HttpUrl] = None

# The Create Schema -> Used when a user sends a POST request to make a new recipe
class RecipeCreate(RecipeBase):
    # Nothing new is needed here
    pass

# The Response Schema -> Used when we return data back to user
class Recipe(RecipeBase):
    id: int # included since the database has created it

    # This tells Pydantic to read the data as an SQLalchemy object instead of a standard dict.
    model_config = ConfigDict(from_attributes=True)