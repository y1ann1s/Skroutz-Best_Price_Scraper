from fastapi import FastAPI
from pydantic import BaseModel
from main_program import get_product_data

app = FastAPI()

class ScrapeRequest(BaseModel):
    query: str

@app.post("/scrape")
def scrape(req: ScrapeRequest):
    try:
        result = get_product_data(req.query)
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
