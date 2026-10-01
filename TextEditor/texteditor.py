import tkinter as tk
from tkinter import Tk, filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)
    
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as f:
            text.delete(1.0, tk.END)
            text.insert(1.0, f.read())
   
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text.get(1.0, tk.END))
            messagebox.showinfo("info ", "File saved successfully!")   
            
root = tk.Tk()
root.title("Simple Text Editor")  
root.geometry("800x600")    

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")
text.pack(expand=True, fill=tk.BOTH)

root.mainloop()
