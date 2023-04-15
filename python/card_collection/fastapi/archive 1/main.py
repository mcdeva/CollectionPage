from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

with open("cards.json", "r") as f:
    card_data = json.load(f)

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/cardList")
def card_list(request: Request, name_filter: str = None, category_filter: str = None):
    filtered_data = card_data
    if name_filter:
        filtered_data = [card for card in filtered_data if name_filter.lower() in card['name'].lower()]
    if category_filter:
        filtered_data = [card for card in filtered_data if category_filter.lower() == card['category'].lower()]
    return templates.TemplateResponse("card_list.html", {"request": request, "cards": filtered_data})

@app.post("/cardList")
def card_list_post(request: Request, name_filter: str = Form(None), category_filter: str = Form(None)):
    filtered_data = card_data
    if name_filter:
        filtered_data = [card for card in filtered_data if name_filter.lower() in card['name'].lower()]
    if category_filter:
        filtered_data = [card for card in filtered_data if category_filter.lower() == card['category'].lower()]
    return templates.TemplateResponse("card_list.html", {"request": request, "cards": filtered_data, "name_filter": name_filter, "category_filter": category_filter})
