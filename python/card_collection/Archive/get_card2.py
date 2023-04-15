import json
import uuid
import tkinter as tk


class Card:
    def __init__(self, id, name, type, code, quantity):
        self.id = id
        self.name = name
        self.type = type
        self.code = code
        self.quantity = quantity

    def get_name_quantity(self):
        with open('cards.json', 'r') as f:
            cards = json.load(f)
            for card in cards:
                if card['code'] == self.code:
                    return card['name'], card['quantity']


class CardManager:
    def __init__(self, master):
        self.master = master
        self.cards = []
        self.selected_card = None

        # Create UI elements
        self.card_listbox = tk.Listbox(self.master, width=50)
        self.card_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.card_listbox.bind("<<ListboxSelect>>", self.show_selected_card)

        self.card_editor = tk.Text(self.master, width=50, height=10)
        self.card_editor.grid(row=0, column=1, padx=10, pady=10)

        self.quantity_label = tk.Label(self.master, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.quantity_entry = tk.Entry(self.master)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.save_button = tk.Button(self.master, text="Save", command=self.save_card)
        self.save_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

        # Load cards from JSON file
        with open("cards.json") as f:
            self.cards = json.load(f)

        for card in self.cards:
            self.card_listbox.insert(tk.END, f"{card['name']:30} {card['quantity']:>10}")

    def show_selected_card(self, event):
        selection = event.widget.curselection()
        if len(selection) > 0:
            index = selection[0]
            self.selected_card = self.cards[index]
            self.card_editor.delete("1.0", tk.END)
            self.card_editor.insert(tk.END, self.selected_card["name"])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(tk.END, self.selected_card["quantity"])

    def save_card(self):
        quantity = int(self.quantity_entry.get())
        name = self.card_editor.get("1.0", tk.END).strip()
        code = self.selected_card['code']

        if self.selected_card is None:
            # Create new card
            new_card = {
                "id": str(uuid.uuid4()),
                "name": name,
                "quantity": quantity,
                "code": code
            }
            self.cards.append(new_card)
        else:
            # Update existing card
            index = self.cards.index(self.selected_card)
            self.selected_card["name"] = name
            self.selected_card["quantity"] = quantity

        # Save cards to JSON file
        with open("cards.json", "w") as f:
            json.dump(self.cards, f, indent=4)

        # Clear inputs and selection
        self.card_editor.delete("1.0", tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.selected_card = None

        # Update listbox display
        self.card_listbox.delete(0, tk.END)
        for card in self.cards:
            self.card_listbox.insert(tk.END, f"{card['name']:30} {card['quantity']:>10}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Card Manager")
    card_manager = CardManager(root)
    root.mainloop()
