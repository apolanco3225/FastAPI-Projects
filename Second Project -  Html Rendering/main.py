from fastapi import FastAPI, Response, responses
from typing import Optional

api = FastAPI()

@api.get("/")
def index():
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the API</h1>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"
    return responses.HTMLResponse(content=body)

@api.get("/api/calculate")
def calculate(x:int, y:int, z:Optional[int] = None):

    if z == 0:
        return responses.JSONResponse(
            content='{"ERROR": "Z can not be zero."}', 
            status_code=400         
        )


    value = (x + y) 
    if z is not None:
        value = value / z
        
    result = {
        "x":x, 
        "y":y, 
        "z": z,
        "value":value
    }
    return result
