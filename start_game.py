import tkinter as tk
from tkinter import PhotoImage
import subprocess

def show_authors():
    authors_window = tk.Toplevel(root)
    authors_window.title("Autori")
    authors_window.geometry("500x400")

    # Set background image
    bg_image = PhotoImage(file="connect4.png")
    bg_label = tk.Label(authors_window, image=bg_image)
    bg_label.image = bg_image  # keep a reference to prevent garbage collection
    bg_label.place(relwidth=1, relheight=1)

    authors_label = tk.Label(authors_window, text="Đorđe Đuričić\nRedžep Đerekarac\nStefan Đurišić\nMarija Perović", font=("Helvetica", 32), bg='white')
    authors_label.pack(pady=20, padx=20)

def start_game():
    game_window = tk.Toplevel(root)
    game_window.title("Pokreni igru")
    game_window.geometry("400x300")

    # Set background image
    bg_image = PhotoImage(file="connect4.png")
    bg_label = tk.Label(game_window, image=bg_image)
    bg_label.image = bg_image  # keep a reference to prevent garbage collection
    bg_label.place(relwidth=1, relheight=1)

    game_window.grid_rowconfigure(0, weight=1)
    game_window.grid_rowconfigure(1, weight=1)
    game_window.grid_columnconfigure(0, weight=1)

    def single_player():
        game_window.destroy()
        subprocess.run(["python", "connect4_with_ai.py"])
        post_game_options()

    def multiplayer():
        game_window.destroy()
        subprocess.run(["python", "connect4.py"])
        post_game_options()

    single_button = tk.Button(game_window, text="Single Player", command=single_player, font=("Arial", 14), bg='green', padx=20, pady=10)
    single_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    multi_button = tk.Button(game_window, text="Multiplayer", command=multiplayer, font=("Arial", 14), bg='green', padx=20, pady=10)
    multi_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

def post_game_options():
    post_game_window = tk.Toplevel(root)
    post_game_window.title("Kraj partije")
    post_game_window.geometry("400x300")

    # Set background image
    bg_image = PhotoImage(file="connect4.png")
    bg_label = tk.Label(post_game_window, image=bg_image)
    bg_label.image = bg_image  # keep a reference to prevent garbage collection
    bg_label.place(relwidth=1, relheight=1)

    post_game_window.grid_rowconfigure(0, weight=1)
    post_game_window.grid_rowconfigure(1, weight=1)
    post_game_window.grid_columnconfigure(0, weight=1)

    def new_game():
        post_game_window.destroy()
        start_game()

    def back_to_main():
        post_game_window.destroy()

    new_game_button = tk.Button(post_game_window, text="Igraj još jednu partiju", command=new_game, font=("Arial", 14), padx=20, pady=10)
    new_game_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    main_menu_button = tk.Button(post_game_window, text="Povratak na glavni meni", command=back_to_main, font=("Arial", 14), padx=20, pady=10)
    main_menu_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

def exit_program():
    root.destroy()

# Glavni prozor
root = tk.Tk()
root.title("Connect 4")
root.geometry("500x400")

# Set background image
bg_image = PhotoImage(file="connect4.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.image = bg_image  # keep a reference to prevent garbage collection
bg_label.place(relwidth=1, relheight=1)

# Title label
title_label = tk.Label(root, text="Connect 4", font=("Comic Sans MS", 24, "bold"), fg='red', bg='white')
title_label.pack(pady=20)

# Buttons
start_button = tk.Button(root, text="Pokreni igru", command=start_game, font=("Arial", 16), bg='green', padx=20, pady=10)
start_button.pack(pady=10)

authors_button = tk.Button(root, text="Autori", command=show_authors, font=("Arial", 16), bg='purple', padx=20, pady=10)
authors_button.pack(pady=10)

exit_button = tk.Button(root, text="Izlaz", command=exit_program, font=("Arial", 16), bg='blue', padx=20, pady=10)
exit_button.pack(pady=10)

root.mainloop()
