from typing import Union, Optional

from fastapi import FastAPI, Response, status, HTTPException
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

def find_index_post(post_id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == post_id:
            return i

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

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    # print(post)
    # print(post.model_dump())
    post_md = post.model_dump()
    post_md['id'] = randrange(0, 100000)
    my_posts.append(post_md)
    return {"data": post_md}
# def create_post(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']}",
#             "content": f"{payload['content']}",
#             "message": "Post created successfully"}
# title str, content str

@app.get("/posts/latest")
def get_latest_post():
    return {"latest_post": my_posts[-1]}
    # return {"latest_post": my_posts[len(my_posts) - 1]}

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "Post not found"}
    return {"post_detail": post}

@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
def delete_post(post_id: int):
    # delete post from the list
    # find the index of the post in the list
    index = find_index_post(post_id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")

    my_posts.pop(index)
    # status code 200
    return {"message": "Post deleted successfully"}
    # status code 204
    # return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    index = find_index_post(post_id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")
    my_posts[index] = post.model_dump()
    return {"message": "Post updated successfully"}