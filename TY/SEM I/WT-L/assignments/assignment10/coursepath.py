from fastapi import FastAPI

app = FastAPI()

@app.get("/courses/{course_name}")
def read_course(course_name):
  return {"course_name": course_name}
