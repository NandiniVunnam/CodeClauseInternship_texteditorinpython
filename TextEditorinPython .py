import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text.get("1.0", tk.END))

def word_count():
    content = text.get("1.0", tk.END)
    words = content.split()
    word_count = len(words)
    tk.messagebox.showinfo("Word Count", f"Total words: {word_count}")

root = tk.Tk()
root.title("Simple Text Editor")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Word Count", command=word_count)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)

text = tk.Text(root)
text.pack(expand=True, fill="both")

root.mainloop()
