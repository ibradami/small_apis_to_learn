from fastapi import APIRouter, Path, Body, Query
from schemas import Post, UpdatePost
from services import (
    create_post_logic,
    change_post_logic,
    show_posts_logic
)
from typing import Optional

router= APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/{id}")
def create_post(
    id: int = Path(..., description="Post ID"),
    post: Post = Body(...)
    ):
        result=create_post_logic(id, post.model_dump())
        return {"message":"Post created", "result": result}

@router.put("/{id}")
def change_post(id: int = Path(..., description="Post ID to change"),
                post: UpdatePost = Body(...)):
        update_data=post.model_dump(exclude_unset=True)
        result=change_post_logic(id, update_data)
        return {"message":"Post changed", "result":result}

@router.get("")
def show_posts(author: Optional[str] = Query(None, description="Author name")):
        result=show_posts_logic(author)
        return {"message":"Success", "result":result}

