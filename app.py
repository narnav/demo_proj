from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI demo!"}

# Endpoint with a path parameter
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Endpoint with query parameter
@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}
