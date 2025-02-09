from typing import Union, Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

# uvicorn main:app --reload
app = FastAPI()

# BaseModel is used to specify the type of the request body
class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

my_posts = [{"title": "Post 1", "content": "Content 1", "id": 1},
            {"title": "favorite food", "content": "I like pizza", "id": 2}]


def find_post(post_id: int):
    for post in my_posts:
        if post['id'] == post_id:
            return post
    return None

##
# Union is used to specify that the function can return either a str or an int
# Decorator @app.get("/")
# HTTP Method: GET
# URL Path: "/"
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/posts")
# def create_post(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']}",
#             "content": f"{payload['content']}",
#             "message": "Post created successfully"}
def create_post(post: Post):
    # print(post)
    # print(post.model_dump())
    post_md = post.model_dump()
    post_md['id'] = randrange(0, 100000)
    my_posts.append(post_md)
    return {"data": post_md}
# title str, content str

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    post = find_post(post_id)
    return {"post_detail": post}