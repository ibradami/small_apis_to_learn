from fastapi import  HTTPException
from typing import Optional

posts={}

def create_post_logic(id: int, post: dict):
    if id in posts:
        raise HTTPException(status_code=409, detail="Post with this id already exists")
    posts[id]=post
    return posts[id]

def change_post_logic(id: int, post: dict):
    if id not in posts:
        raise HTTPException(status_code=404, detail="Post with this id do not exist")
    posts[id].update(post)
    return posts[id]

def show_posts_logic(author: Optional[str] = None):
    if not posts:
        raise HTTPException(status_code=404, detail="There are not posts yet")
    if author is None:
        return posts
    filtered_posts={
        id: post
        for id, post in posts.items()
        if author.lower() in post["author"].lower()
    }
    if not filtered_posts:
        raise HTTPException(status_code=404, detail="No posts with this author")
    return filtered_posts