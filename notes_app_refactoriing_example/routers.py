from fastapi import APIRouter, Body, Path, Query
from schemas import Note, UpdateNote
from services import (
    add_note_logic,
    update_note_logic,
    delete_note_logic,
    find_note_by_keyword_logic
)

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.post("/{id}")
def add_note(
    id: int = Path(..., description="Note ID", gt=0),
    note: Note = Body(...)
):
    result = add_note_logic(id, note.model_dump())
    return {"message": "Note created", "note": result}

@router.put("/{id}")
def update_note(
    id: int = Path(..., description="Note ID", gt=0),
    note: UpdateNote = Body(...)
):
    update_data = note.model_dump(exclude_unset=True)
    result = update_note_logic(id, update_data)
    return {"message": "Success", "note": result}

@router.delete("/{id}")
def delete_note(
    id: int = Path(..., description="Task ID", gt=0)
):
    delete_note_logic(id)
    return {"message": "Note deleted"}

@router.get("/search")
def find_note_by_keyword(
    keyword: str = Query(..., description="Keyword")
):
    id, note = find_note_by_keyword_logic(keyword)
    return {"message": "Note Found", "id": id, "note": note}
