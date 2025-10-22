from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class Article(BaseModel):
    id: int
    title: str
    body: str
    date: str
    journalist_id: int

article_list=[Article(id=1, title="Football Championship", body="The football championship was thrilling...", date="2023-10-01", journalist_id=1),
              Article(id=2, title="Election Results", body="The recent elections concluded with...", date="2023-10-02", journalist_id=2),
              Article(id=3, title="Art Exhibition", body="The new art exhibition showcases...", date="2023-10-03", journalist_id=3),
              Article(id=4, title="Tech Innovations", body="The latest tech innovations include...", date="2023-10-04", journalist_id=4),
              Article(id=5, title="Health Tips", body="Experts suggest several health tips...", date="2023-10-05", journalist_id=5)]

@app.get("/articles")
def articles():
    return article_list

@app.get("articles/{id}")
def get_articles(id:int):
    articles=search_articles(id)
    if len(articles)>0:
        return articles[0]
    raise HTTPException(status_code=404, detail="Article not found")

@app.get("/articles/")
def get_articles(id:int):
    return search_articles(id)

@app.post("/articles", status_code=201, response_model=Article)
def add_article(article:Article):
    article.id=next_id()
    article_list.append(article)
    return article

@app.put("articles/{id}", response_model=Article)
def modify_article(id:int, article:Article):
    for index, saved_article in enumerate(article_list):
        if saved_article.id==id:
            article.id=id
            article_list[index]=article
            return article
    raise HTTPException(status_code=404, detail="Article not found")

@app.delete("articles/{id}")
def delete_article(id:int):
    for saved_article in article_list:
        if saved_article.id==id:
            article_list.remodve(saved_article)
            return {"message":"Article deleted successfully"}
    raise HTTPException(status_code=404, detail="Article not found")


#------------------

def search_articles(id:int):
    articles=[article for article in article_list if article.id==id]

    if not articles:
        raise HTTPException(status_code=404, detail="Article not found")
    return articles[0]


def next_id():
    return(max(article_list,key=id).id+1)