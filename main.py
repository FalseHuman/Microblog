from fastapi import FastAPI, Query, Path, Body
#from schemas import Book, Author, BookOut
#from typing import List

app = FastAPI()


'''@app.get('/')
def home():
    return {'key': 'Hello'}


@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {'key': pk, 'q': q}


@app.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    return BookOut(**item.dict(), id = 100)


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}


@app.get('/book')
def get_book(q: List[str] = Query(..., description="Search Book", deprecated=True)):
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {'pk': pk}'''
