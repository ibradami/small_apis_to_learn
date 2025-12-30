from fastapi import FastAPI, Body, Path, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

notes=dict()

class Note(BaseModel):
    text: str

class UpdateNote(BaseModel):
    text: Optional[str] = None

@app.post("/notes/{id}")
def add_note(id: int = Path(..., description="Note ID", gt=0),
             note: Note = Body(...)):
    if id in notes:
        raise HTTPException(status_code=409, detail="Note already exist")
    notes[id]=note.model_dump()
    return {"message": "Note created", "note": notes[id]}

@app.put("/notes/{id}")
def update_note(id: int = Path(..., description="Note ID", gt=0), 
                note: UpdateNote = Body(...)):
    if id not in notes:
        raise HTTPException(status_code=404, detail="Note not Found")
    update_data=note.model_dump(exclude_unset=True)
    stored_data=notes[id]
    stored_data.update(update_data)
    return {"message":"Success","note":stored_data}

@app.delete("/notes/{id}")
def delete_note(id: int = Path(..., description="Task ID", gt=0)):
    if id not in notes:
        raise HTTPException(status_code=404, detail="Note not Found")
    del notes[id]
    return {"message":"Note deleted"}

@app.get("/notes/search")
def find_note_by_keyword(keyword: str = Query(..., description="Keyword")):
    for id, note in notes.items():
        if keyword.lower() in note["text"].lower():
            return {"message":"Note Found","id": id,"note":note}
    raise HTTPException(status_code=404, detail="Note not Found")
