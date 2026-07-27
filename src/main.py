import tkinter as tk
from ui.home import show_home
from ui.chat import show_chat
# ---------------- Window ---------------- #

root = tk.Tk()
root.title("Atlas")
root.geometry("1100x700")
root.configure(bg="#202124")

# ---------------- Sidebar ---------------- #

sidebar = tk.Frame(root, width=220, bg="#2b2d31")
sidebar.pack(side="left", fill="y")

home_button = tk.Button(
    sidebar,
    text="🏠 Home",
    bg="#2b2d31",
    fg="white",
    relief="flat",
    anchor="w",
    padx=20,
    pady=12,
    command=lambda: show_home(content)
)

home_button.pack(fill="x")
chat_button = tk.Button(
    sidebar,
    text="💬 AI Chat",
    bg="#2b2d31",
    fg="white",
    relief="flat",
    anchor="w",
    padx=20,
    pady=12,
    command=lambda: show_chat(content)
)

chat_button.pack(fill="x")
# ---------------- Content ---------------- #

content = tk.Frame(root, bg="#202124")
content.pack(fill="both", expand=True)

status = tk.Label(
    root,
    text="Status: Ready",
    bg="#1b1b1b",
    fg="white",
    anchor="w"
)

status.pack(side="bottom", fill="x")




show_home(content)
root.mainloop()