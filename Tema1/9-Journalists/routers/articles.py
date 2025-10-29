from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/articles", tags=["articles"])

class Article(BaseModel):
    id: int
    title: str
    body: str
    date: str
    journalist_id: int

article_list = [
    Article(id=1, title="Economic crisis", body="The economy is falling.", date="2025-10-01", journalist_id=1),
    Article(id=2, title="New president", body="A new president was elected.", date="2025-09-15", journalist_id=2),
    Article(id=3, title="Modern art", body="A new art exhibition opened.", date="2025-08-30", journalist_id=3),
]

@router.get("/")
def get_articles():
    return article_list

@router.get("/{id_article}")
def get_article(id_article: int):
    articles = [a for a in article_list if a.id == id_article]
    if not articles:
        raise HTTPException(status_code=404, detail="Article not found")
    return articles[0]

@router.get("/query/")
def get_article_by_query(id: int):
    return search_article(id)

@router.post("/", status_code=201, response_model=Article)
def add_article(article: Article):
    article.id = next_id()
    article_list.append(article)
    return article

@router.put("/{id}")
def modify_article(id: int, article: Article):
    for index, saved_article in enumerate(article_list):
        if saved_article.id == id:
            article.id = id
            article_list[index] = article
            return article
    raise HTTPException(status_code=404, detail="Article not found")

@router.delete("/{id}")
def delete_article(id: int):
    for saved_article in article_list:
        if saved_article.id == id:
            article_list.remove(saved_article)
            return {}
    raise HTTPException(status_code=404, detail="Article not found")

def search_article(id: int):
    articles = [a for a in article_list if a.id == id]
    if len(articles) != 0:
        return articles[0]
    else:
        return {"error": "No article found"}

def next_id():
    if not article_list:
        return 1
    return max(article_list, key=lambda a: a.id).id + 1
