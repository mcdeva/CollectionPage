import tkinter as tk
from tkinter import ttk
import json
import uuid
import os


def load_data():
    if not os.path.isfile("cards.json"):
        initial_data = []
        return initial_data
    else:
        # Load data from JSON file
        with open("cards.json", encoding="utf-8") as file:
            return json.load(file)


def on_select(event, data, listbox, selected_card_id, selected_card_name, selected_new_card_energy, selected_card_category, selected_card_box, selected_card_box_order, selected_card_regulation, quantity_entry):
    # Get the selected item index
    index = listbox.curselection()[0]

    # Get the selected item data
    selected_card = listbox.get(index)
    card_detail = selected_card.rsplit(" ", 1)
    for card in data:
        card_name = f'{card["box"]} {card["order"]} |    {card["name"]}'
        if card_name == card_detail[0].strip():
            # Set the name and quantity entry fields to the selected item data
            selected_card_id.set(card["id"])
            selected_card_name.set(card["name"])
            selected_new_card_energy.set(card["energy"])
            selected_card_category.set(card["category"])
            selected_card_box.set(card["box"])
            selected_card_box_order.set(card["order"])
            selected_card_regulation.set(card["type"])
            break

    # Set the focus to the quantity entry field
    quantity_entry.focus()


def save_data(data):
    # Save data to JSON file
    with open("cards.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def clear_entry(new_card_box_order_entry, selected_card_box_order):
    selected_card_box_order.set("")
    new_card_box_order_entry.focus()


def save_card(data, selected_card_id, selected_card_name, selected_card_box_order, selected_card_quantity,
    new_card_name, new_card_energy, new_card_category, new_card_box, new_card_box_order, new_card_regulation, new_card_quantity, filter_text, listbox, entry_name, combobox_energy, combobox_category, combobox_card_box, combobox_card_regulation):
    # Get the next card ID
    new_card_id = str(uuid.uuid4())
    card_id = selected_card_id.get()

    # Check if a card with the same name already exists
    for card in data:
        if card:
            if card["name"] == new_card_name and card["box"] == new_card_box and card["order"] == new_card_box_order:
                # Update the existing card"s quantity
                card["quantity"] += int(new_card_quantity)
                print(card)
                break
    else:
        # If no matching card was found, create a new card
        new_card = {
            "id": new_card_id,
            "name": new_card_name,
            "energy": new_card_energy,
            "category": new_card_category,
            "box": new_card_box,
            "order": new_card_box_order,
            "type": new_card_regulation,
            "quantity": int(new_card_quantity)
        }
        print(new_card)
        data.append(new_card)

    # Save the data to the JSON file
    save_data(data)

    # Update the listbox with the new data
    filter_text.set("")
    update_listbox(data, listbox, "")

    # Clear the selected item combobox
    combobox_energy.set("")
    combobox_category.set("")
    combobox_card_box.set("")
    combobox_card_regulation.set("")

    # Clear the data selected
    selected_card_id.set("")
    selected_card_name.set("")
    selected_card_box_order.set("")
    selected_card_quantity.set("")

    # Set the focus to the name entry field
    entry_name.focus()


def clear_card(data, selected_card_id, selected_card_name, selected_card_box_order, selected_card_quantity,
    filter_text, listbox, entry_name, combobox_energy, combobox_category, combobox_card_box, combobox_card_regulation):
    # Update the listbox with the new data
    filter_text.set("")
    update_listbox(data, listbox, "")

    # Clear the selected item combobox
    combobox_energy.set("")
    combobox_category.set("")
    combobox_card_box.set("")
    combobox_card_regulation.set("")

    # Clear the data selected
    selected_card_id.set("")
    selected_card_name.set("")
    selected_card_box_order.set("")
    selected_card_quantity.set("")

    # Set the focus to the name entry field
    entry_name.focus()


def update_listbox(data, listbox, filter_text):
    # Clear the listbox
    listbox.delete(0, tk.END)

    # Add the matching cards to the listbox
    for card in data:
        if card:
            if filter_text in card["name"].lower():
                listbox.insert(tk.END, f'{card["box"]} {card["order"]} |    {card["name"]} ({card["quantity"]})')


def create_ui():
    # Create the main window
    root = tk.Tk()
    root.title("Card Collection")

    # Load data from JSON file
    data = load_data()

    filter_text = tk.StringVar()
    selected_card_id = tk.StringVar()
    selected_card_name = tk.StringVar()
    selected_card_box_order = tk.StringVar()
    selected_card_quantity = tk.StringVar()

    # Create the UI
    filter_frame = tk.Frame(root)
    filter_frame.pack(side=tk.TOP, padx=10, pady=10)

    new_card_frame = tk.Frame(root)
    new_card_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

    new_card_name_label = tk.Label(new_card_frame, text="Name:")
    new_card_name_label.grid(row=0, column=0)

    new_card_name_entry = tk.Entry(new_card_frame, textvariable=selected_card_name)
    new_card_name_entry.grid(row=0, column=1)

    new_card_name_label = tk.Label(new_card_frame, text="Energy:")
    new_card_name_label.grid(row=0, column=2)

    energy = ["", "Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting", "Darkness", "Metal", "Fairy", "Dragon", "Colorless"]
    new_card_energy = ttk.Combobox(new_card_frame, values=energy, state="readonly", width=18)
    new_card_energy.grid(row=0, column=3)

    new_card_category_label = tk.Label(new_card_frame, text="Category:")
    new_card_category_label.grid(row=0, column=4)

    category = ["โปเกมอน", "ไอเท็ม", "ไอเท็มติดโปเกมอน", "ซัพพอร์ต", "สเตเดียม", "พลังงาน"]
    new_card_category = ttk.Combobox(new_card_frame, values=category, state="readonly", width=18)
    new_card_category.grid(row=0, column=5)

    new_card_box_label = tk.Label(new_card_frame, text="Box:")
    new_card_box_label.grid(row=1, column=0)

    box = ["SV1ST", "SV1VT", "S10aT", "S10bT", "S10DT", "S10PT", "S11T", "S11aT", "S12T", "S12aT", "PROMO",
        "S5aT", "S5RT", "S5IT", "S6aT", "S6HT", "S6KT", "S7RT", "S7DT", "S8T", "S8aT", "S8bT", "S9T", "S9aT",
        "SVAWT", "SVALT", "SVAMT", "AS1a", "AS1D", "AS2a", "AS2b", "AS2D", "AS3b", "AS3D", "AS4b", "AS4D", "AS5b", "AS5D", "AS6b",
        "SCAT", "SCBT", "SC1aT", "SC1bT", "SC3aT", "SC3bT", "SCCT", "SCDT", "SC1DT", "SCET", "SCFT",
        "GRA", "PSY", "WAT", "FIG", "DAR", "LIG", "FIR", "MET"]
    new_card_box = ttk.Combobox(new_card_frame, values=box, state="readonly", width=18)
    new_card_box.grid(row=1, column=1)

    new_card_box_order_label = tk.Label(new_card_frame, text="Order:")
    new_card_box_order_label.grid(row=1, column=2)

    new_card_box_order_entry = ttk.Entry(new_card_frame, textvariable=selected_card_box_order)
    new_card_box_order_entry.grid(row=1, column=3)

    new_card_regulation_label = tk.Label(new_card_frame, text="Regulation:")
    new_card_regulation_label.grid(row=1, column=4)

    regulation = ["G", "F", "E", "D", "C", "B", "A"]
    new_card_regulation = ttk.Combobox(new_card_frame, values=regulation, state="readonly", width=18)
    new_card_regulation.grid(row=1, column=5)

    new_card_quantity_label = tk.Label(new_card_frame, text="Quantity:")
    new_card_quantity_label.grid(row=2, column=0)

    new_card_quantity_entry = tk.Entry(new_card_frame, textvariable=selected_card_quantity)
    new_card_quantity_entry.grid(row=2, column=1)
    new_card_quantity_entry.configure(bg='#FF927B')

    # set the default value of the Combobox
    new_card_energy.set("")
    new_card_category.set("")
    new_card_box.set("")

    save_button = tk.Button(new_card_frame, text="Save", command=lambda: save_card(
        data,
        selected_card_id,
        selected_card_name,
        selected_card_box_order,
        selected_card_quantity,
        new_card_name_entry.get(),
        new_card_energy.get(),
        new_card_category.get(),
        new_card_box.get(),
        new_card_box_order_entry.get(),
        new_card_regulation.get(),
        new_card_quantity_entry.get(),
        filter_text,
        listbox,
        new_card_name_entry,
        new_card_energy,
        new_card_category,
        new_card_box,
        new_card_regulation
    ))
    save_button.grid(row=2, column=2, columnspan=2)

    clear_button = tk.Button(new_card_frame, text="Clear", command=lambda: clear_card(
        data,
        selected_card_id,
        selected_card_name,
        selected_card_box_order,
        selected_card_quantity,
        filter_text,
        listbox,
        new_card_name_entry,
        new_card_energy,
        new_card_category,
        new_card_box,
        new_card_regulation
    ))
    clear_button.grid(row=2, column=4, columnspan=2)

    listbox_frame = tk.Frame(root)
    listbox_frame.pack(side=tk.TOP, padx=10, pady=10)

    listbox = tk.Listbox(listbox_frame, width=80, height=20)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(listbox_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Link the listbox and scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Update the listbox with all the cards
    update_listbox(data, listbox, "")

    # Set the focus to the name entry field
    new_card_name_entry.focus()

    new_card_box.bind("<<ComboboxSelected>>", lambda event: clear_entry(
        new_card_box_order_entry,
        selected_card_box_order
    ))
    listbox.bind("<<ListboxSelect>>", lambda event: on_select(
        event,
        data,
        listbox,
        selected_card_id,
        selected_card_name,
        new_card_energy,
        new_card_category,
        new_card_box,
        selected_card_box_order,
        new_card_regulation,
        new_card_quantity_entry
    ))
    new_card_name_entry.bind("<KeyRelease>", lambda event: update_listbox(data, listbox, new_card_name_entry.get().lower()))
    new_card_quantity_entry.bind("<Return>", lambda event: save_card(
        data,
        selected_card_id,
        selected_card_name,
        selected_card_box_order,
        selected_card_quantity,
        new_card_name_entry.get(),
        new_card_energy.get(),
        new_card_category.get(),
        new_card_box.get(),
        new_card_box_order_entry.get(),
        new_card_regulation.get(),
        new_card_quantity_entry.get(),
        filter_text,
        listbox,
        new_card_name_entry,
        new_card_energy,
        new_card_category,
        new_card_box,
        new_card_regulation
    ))

    # Start the main loop
    root.mainloop()


create_ui()
