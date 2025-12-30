from fastapi import FastAPI, Query

app = FastAPI()

students={}

@app.get("/students")
def get_students(limit: int = Query(default=10, ge=0, le=100), offset: int = Query(default=0, gt=0)):
    students_list=list(students.values())
    total=len(students_list)

    return {
        "total":total,
        "limit":limit,
        "offset":offset,
        "students":students_list[offset:offset+limit]
    }