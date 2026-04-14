from fastapi import FastAPI

# Initialize the application instance
app = FastAPI()

# A decorator defining the HTTP method (GET) and the path ("/")
@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}