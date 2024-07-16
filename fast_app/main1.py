from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse

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

@app.get("/", response_class=FileResponse)
async def index():
	return FileResponse('html_template/index.html')


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)
