from typing import Optional

from fastapi import FastAPI, Response, status, Path, Query, Body
from fastapi.responses import (
    HTMLResponse,
    PlainTextResponse,
    FileResponse,
    JSONResponse,
    RedirectResponse,
)
from fastapi.staticfiles import StaticFiles

import uvicorn
from pydantic import BaseModel, Field


# from starlette.responses import PlainTextResponse


from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str
    age: Optional[int] =123


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/hello")
def hello(person: Person):
    if person.age == None:
        return {"message": f"Привет, {person.name}"}
    else:
        return {"message": f"Привет, {person.name}, твой возраст - {person.age}"}


if __name__ == "__main__":
    uvicorn.run("main1:app", host="0.0.0.0", port=8000, reload=True)
