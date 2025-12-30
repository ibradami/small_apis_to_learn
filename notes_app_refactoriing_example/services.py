from fastapi import HTTPException

notes = {}

def add_note_logic(id: int, note: dict):
    if id in notes:
        raise HTTPException(status_code=409, detail="Note already exist")

    notes[id] = note
    return notes[id]

def update_note_logic(id: int, update_data: dict):
    if id not in notes:
        raise HTTPException(status_code=404, detail="Note not Found")

    notes[id].update(update_data)
    return notes[id]

def delete_note_logic(id: int):
    if id not in notes:
        raise HTTPException(status_code=404, detail="Note not Found")

    del notes[id]

def find_note_by_keyword_logic(keyword: str):
    for id, note in notes.items():
        if keyword.lower() in note["text"].lower():
            return id, note

    raise HTTPException(status_code=404, detail="Note not Found")
