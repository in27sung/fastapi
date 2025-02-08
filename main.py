from typing import Union, Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

# uvicorn main:app --reload
app = FastAPI()

# BaseModel is used to specify the type of the request body
class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

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


@app.post("/createposts")
# def create_post(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']}",
#             "content": f"{payload['content']}",
#             "message": "Post created successfully"}
def create_post(post: Post):
    # print(post)
    print(post.model_dump())
    return {"data": post}
# title str, content str


