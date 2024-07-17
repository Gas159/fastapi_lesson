from fastapi import FastAPI, Response, status, Path, Query
from fastapi.responses import (
    HTMLResponse,
    PlainTextResponse,
    FileResponse,
    JSONResponse,
)

import uvicorn

# from starlette.responses import PlainTextResponse

app = FastAPI()


# @app.get("/", response_class=HTMLResponse)
# async def read_index():
# 	html_content = """
# 	<html>
# 	<body>
# 		<h1>Hello, World!</h1>
# 	</body>
# 	</html>
# 	"""
# 	return {"message": "Hello METANIT.COM"}
# 	# return HTMLResponse(content=html_content, status_code=200)

# @app.get("/")
# def root():
#     return {"message": "Hello METANIT.COM"}

# @app.get("/")
# def root():
#     data = "Hello METANIT.COM"
#     return Response(content=data, media_type="text/plain", status_code=200)
#
#
# @app.get("/text", response_class=PlainTextResponse)
# def root_text():
# 	return "Hello METANIT.COM"
#
#
# @app.get("/html", response_class=HTMLResponse)
# def root_html():
# 	return "<h2>Hello METANIT.COM</h2>"

# @app.get('/')
# def index():
# 	return FileResponse ('html_template/index.html')

# @app.get("/", response_class=FileResponse)
# async def index():
# 	return FileResponse('html_template/index.html')
#


# send file mode with media_type="application/octet-stream"
# @app.get("/", response_class=FileResponse)
# def root():
#     return FileResponse(
#         "html_template/index.html",
#         media_type="application/octet-stream",
#         filename="index.html",
#     )
#
#
# @app.get("/users/{name}/{age}")
# def users(
#     name: str = Path(title="Name", min_length=3, max_length=100),
#     age: int = Path(title="Age", ge=1, le=100),
# ):
#     return f"Hello {name}, you are {age} years old"


# @app.get("/users")
# def users(
#     name: str | None = Query(
#         default=None,
#         min_length=3,
#         max_length=100,
#     ),
#     age: int = "Unknown",
# ):
#     # http://127.0.0.1:8001/users?name=rinat&age=3
#     return {"name": name, "age": age}


# @app.get("/users1")
# def users1(
#     people: list[str] = Query(default=["op2", "ip1", "up1"], min_items=1, max_items=3),
# ):
#     # http://127.0.0.1:8001/users1?people=op&people=ip&people=up
#     return {"people": people}


# В данном случае параметр name представляет параметр пути, а age - параметр строки запроса.
# И в данном случае мы могли бы обратиться к функции users, например,
# посредством адреса http://127.0.0.1:8000/users/Tom?age=38
# @app.get("/users/{name}")
# def users(
#     name: str = Path(min_length=3, max_length=20), age: int = Query(ge=18, lt=111)
# ):
#     return {"name": name, "age": age}
@app.get("/users2/{id}", status_code=200)
def users(response: Response, id: int = Path()):
    if id < 1:
        response.status_code = 400
        return {"message": "Incorrect Data"}
    return  {"message": f"Id = {id}", "status_code": 200}

@app.get("/notfound", status_code=status.HTTP_404_NOT_FOUND)
def notfound():
    return {"message": "Resource Not Found"}


@app.get("/notFound")
async def not_found():
    return Response(status_code=404, content="Not found1")


if __name__ == "__main__":
    uvicorn.run("main1:app", host="0.0.0.0", port=8000, reload=True)
