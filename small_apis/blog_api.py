from fastapi import FastAPI, Path, HTTPException, Body, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

posts={}

class Post(BaseModel):
    title: str
    author: str
    text: str

class UpdatePost(BaseModel):
    title: Optional[str]=None
    author: Optional[str]=None
    text: Optional[str]=None

@app.post("/posts/{id}")
def create_post(id: int = Path(..., description="Post ID"),
                post: Post = Body(...)):
    if id in posts:
        raise HTTPException(status_code=409, detail="Post with this id already exists")
    posts[id]=post.model_dump()
    return {"message":"Post is successfully created",
            "post_id":id}

@app.put("/posts/{id}")
def change_post(id: int = Path(..., description="Post ID to change"),
                post: UpdatePost = Body(...)):
    if id not in posts:
        raise HTTPException(status_code=404, detail="Post with this id do not exist")
    posts[id].update(post.model_dump(exclude_unset=True))
    return {"message": "Post is successfully changed",
            "post_id": id}

@app.get("/posts")
def show_posts(author: Optional[str] = Query(None, description="Author name")):
    if not posts:
        raise HTTPException(status_code=404, detail="There are not posts yet")
    if author==None:
        return {"message":"All Posts IDs",
                "posts":posts}
    filtered_posts={
        id: post
        for id, post in posts.items()
        if author.lower() in post["author"].lower()
    }
    if not filtered_posts:
        raise HTTPException(status_code=404, detail="No posts with this author")

    return {"message":"Posts with filtered author",
            "posts":filtered_posts}