import json

def get_card_list():
    with open("cards.json", "r") as f:
        cards = json.load(f)
    return cards
