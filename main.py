





from fastapi import FastAPI
from routers import learner, content, quiz, feedback

app = FastAPI()

app.include_router(learner.router, prefix='/learner')
app.include_router(content.router, prefix='/content')
app.include_router(quiz.router, prefix='/quiz')
app.include_router(feedback.router, prefix='/feedback')

@app.get("/")
def root():
    return {"message": "Welcome to Adaptive EdTech API"}
