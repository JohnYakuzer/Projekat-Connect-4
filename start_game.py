import tkinter as tk
from tkinter import PhotoImage
import subprocess

def show_authors():
    # Prikazivanje prozora sa autorima
    authors_window = tk.Toplevel(root)
    authors_window.title("Autori")
    authors_window.geometry("600x400")

    # Postavljanje pozadinske slike
    bg_image = PhotoImage(file="connect4.png")
    bg_label = tk.Label(authors_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # Prikazivanje imena autora
    authors_label = tk.Label(authors_window, text="Đorđe Đuričić 15/22\nRedžep Đerekarac 49/22\nStefan Đurišić 7/22\nMarija Perović 10/22", font=("Helvetica", 32), bg='white', highlightthickness=2, highlightbackground='black', highlightcolor='black', width=25)
    authors_label.pack(pady=20, padx=20)

def start_game():
    # Funkcija za pokretanje igre
    game_window = tk.Toplevel(root)
    game_window.title("Pokreni igru")
    game_window.geometry("400x300")

    # Postavljanje pozadinske slike
    bg_image = PhotoImage(file="connect4.png")
    bg_label = tk.Label(game_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    game_window.grid_rowconfigure(0, weight=1)
    game_window.grid_rowconfigure(1, weight=1)
    game_window.grid_columnconfigure(0, weight=1)

    def single_player():
        # Funkcija za pokretanje igre sa AI-om
        game_window.destroy()
        subprocess.run(["python", "connect4_with_ai.py"])
        post_game_options()

    def multiplayer():
        # Funkcija za pokretanje igre sa dva igrača
        game_window.destroy()
        subprocess.run(["python", "connect4.py"])
        post_game_options()

    # Dugme za pokretanje igre sa AI-om
    single_button = tk.Button(game_window, text="Jedan igrač", command=single_player, font=("Arial", 14), padx=20, pady=10, bd=2, relief=tk.GROOVE)
    single_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Dugme za pokretanje igre sa dva igrača
    multi_button = tk.Button(game_window, text="Više igrača", command=multiplayer, font=("Arial", 14), padx=20, pady=10, bd=2, relief=tk.GROOVE)
    multi_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

def post_game_options():
    # Opcije nakon završetka igre
    post_game_window = tk.Toplevel(root)
    post_game_window.title("Kraj partije")
    post_game_window.geometry("400x300")

    # Postavljanje pozadinske slike
    bg_image = PhotoImage(file="connect4.png")
    bg_label = tk.Label(post_game_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    post_game_window.grid_rowconfigure(0, weight=1)
    post_game_window.grid_rowconfigure(1, weight=1)
    post_game_window.grid_columnconfigure(0, weight=1)

    def new_game():
        # Funkcija za pokretanje nove igre nakon završetka
        post_game_window.destroy()
        start_game()

    def back_to_main():
        # Povratak na glavni meni nakon završetka igre
        post_game_window.destroy()

    # Dugme za pokretanje nove igre nakon završetka
    new_game_button = tk.Button(post_game_window, text="Igraj još jednu partiju", command=new_game, font=("Arial", 14), padx=20, pady=10, bd=2, relief=tk.GROOVE)
    new_game_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Dugme za povratak na glavni meni nakon završetka igre
    main_menu_button = tk.Button(post_game_window, text="Povratak na glavni meni", command=back_to_main, font=("Arial", 14), padx=20, pady=10, bd=2, relief=tk.GROOVE)
    main_menu_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

def exit_program():
    # Funkcija za izlaz iz programa
    root.destroy()

# Glavni prozor
root = tk.Tk()
root.title("Connect 4")
root.geometry("500x400")

# Postavljanje pozadinske slike
bg_image = PhotoImage(file="connect4.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Naslov labela
title_label = tk.Label(root, text="Connect 4", font=("ArcadeClassic", 24, "bold"), fg='red', bg='white', highlightthickness=2, highlightbackground='black', highlightcolor='black')
title_label.pack(pady=20)

# Dugmad na glavnom meniju
start_button = tk.Button(root, text="Pokreni igru", command=start_game, font=("Arial", 16), bg='blue', fg='white', padx=20, pady=10)
start_button.pack(pady=10)

authors_button = tk.Button(root, text="Autori", command=show_authors, font=("Arial", 16), bg='indigo', fg='white', padx=20, pady=10)
authors_button.pack(pady=10)

exit_button = tk.Button(root, text="Izlaz", command=exit_program, font=("Arial", 16), bg='brown', padx=20, pady=10)
exit_button.pack(pady=10)

root.mainloop()


