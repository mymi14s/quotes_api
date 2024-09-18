from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from quotes_library import get_quotes, get_authors as GA, get_categories as GC

class GetQuote(BaseModel):
    category: str | None = ""
    count: int | None = 1
    author: str | None = ""

class GetAuthor(BaseModel):
    count: int | None = 0
    random: bool | None = False

class GetCategory(BaseModel):
    count: int | None = 0
    random: bool | None = False

with open('description.md', 'r') as file:
    content = file.read()

app = FastAPI(    
    title="Quotes API Library",
    description=content,
    summary="Random Quotes for Everyone",
    version="0.4",
    terms_of_service="https://github.com/mymi14s/quotes_library",
    contact={
        "name": "Anthony Emmanuel",
        "url": "https://github.com/mymi14s/quotes_library",
        "email": "hackacehuawei@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/random-quote")
async def random_quote():
    return get_quotes(random=True)

@app.post("/get-quotes")
async def get_qoutes(item: GetQuote):
    try:
        if item.category=="string": item.category = ""
        if item.author=="string": item.author = ""
        if not (item.category or item.author):
            if not item.category: detail = "Category is required."
            if not item.author: detail = "Author is required."
            if not (item.category and item.author):
                detail = "Category or Author is required."
            raise HTTPException(
                status_code=422,
                detail=detail
            )

        return get_quotes(category=item.category, count=item.count, random=True, author=item.author)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.post("/get-authors")
async def get_authors(item: GetAuthor):
    try:
        if item.random: item.random = True
        if not item.count: item.count = 10
        return GA(count=item.count, random=item.random)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.post("/get-categories")
async def get_categories(item: GetCategory):
    try:
        if item.random: item.random = True
        if not item.count: item.count = 10
        return GC(count=item.count, random=item.random)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)