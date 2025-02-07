from typing import Union

from fastapi import FastAPI

app = FastAPI()

##
# Union is used to specify that the function can return either a str or an int
# Decorator @app.get("/")
# HTTP Method: GET
# URL Path: "/"
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!!!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# uvicorn main:app --reload
