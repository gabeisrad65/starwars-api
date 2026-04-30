import requests
import tkinter as tk
from tkinter import messagebox

API_URL = "https://www.swapi.tech/api/people/"


def fetch_character():
    character_id = entry.get().strip()

    if not character_id.isdigit():
        messagebox.showerror("Invalid Input", "Enter a number like 1, 2, or 3.")
        return

    try:
        response = requests.get(API_URL + character_id, timeout=10)
        response.raise_for_status()

        data = response.json()
        character = data["result"]["properties"]

        result_text.set(
            f"Name: {character['name']}\n"
            f"Height: {character['height']} cm\n"
            f"Mass: {character['mass']} kg\n"
            f"Hair Color: {character['hair_color']}\n"
            f"Skin Color: {character['skin_color']}\n"
            f"Eye Color: {character['eye_color']}\n"
            f"Birth Year: {character['birth_year']}\n"
            f"Gender: {character['gender']}"
        )

    except requests.exceptions.RequestException as error:
        messagebox.showerror("Connection Error", f"Could not fetch data:\n\n{error}")

    except KeyError:
        messagebox.showerror("Data Error", "The API response format changed.")


root = tk.Tk()
root.title("Star Wars API Explorer")
root.geometry("420x420")
root.configure(bg="#3b2f2f")

title = tk.Label(
    root,
    text="Star Wars API Explorer",
    font=("Georgia", 20, "bold"),
    bg="#3b2f2f",
    fg="#f4d35e"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Enter a character ID number",
    font=("Georgia", 12),
    bg="#3b2f2f",
    fg="#f7ede2"
)
subtitle.pack()

entry = tk.Entry(
    root,
    font=("Georgia", 14),
    justify="center",
    bg="#f7ede2",
    fg="#2f1b0c",
    width=15
)
entry.pack(pady=10)

button = tk.Button(
    root,
    text="Search Character",
    font=("Georgia", 12, "bold"),
    bg="#8b5e34",
    fg="white",
    command=fetch_character
)
button.pack(pady=10)

result_text = tk.StringVar()

result_label = tk.Label(
    root,
    textvariable=result_text,
    font=("Georgia", 12),
    bg="#5c4033",
    fg="#fff3b0",
    justify="left",
    padx=20,
    pady=20,
    width=35,
    height=10
)
result_label.pack(pady=20)

root.mainloop()