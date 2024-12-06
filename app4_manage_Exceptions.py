from fastapi import Request
from fastapi.responses import JSONResponse
import datetime
from fastapi import FastAPI
class MyException(Exception):
    def __init__(self,
                 name : str,
                 date: str):
        self.name = name
        self.date = date


api = FastAPI(openapi_tags=[
    {
        'name': 'home',
        'description': 'default functions'
    },
    {
        'name': 'items',
        'description': 'functions that are used to deal with items'
    }
])


@api.exception_handler(MyException)
def MyExceptionHandler(
    request: Request,
    exception: MyException
    ):
    return JSONResponse(
        status_code=418,
        content={
            'url': str(request.url),
            'name': exception.name,
            'message': 'This error is my own',
            'date': exception.date
        }
    )

@api.get('/my_custom_exception')
def get_my_custom_exception():
    raise MyException(
      name='my error',
      date=str(datetime.datetime.now())
      )