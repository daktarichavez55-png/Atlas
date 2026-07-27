import tkinter as tk
from ui.home import show_home
from ui.chat import show_chat
from ui.pdf import show_pdf
from ui.linux import show_linux
from ui.settings import show_settings
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
    command=lambda: (
    show_home(content),
    update_status("Home")
)
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
    command=lambda: (
    show_chat(content),
    update_status("AI Chat")
)
)

chat_button.pack(fill="x")
# ---------------- Content ---------------- #
pdf_button = tk.Button(
    sidebar,
    text="📄 PDF Tools",
    bg="#2b2d31",
    fg="white",
    relief="flat",
    anchor="w",
    padx=20,
    pady=12,
    command=lambda: (
    show_pdf(content),
    update_status("PDF Tools")
)
)

pdf_button.pack(fill="x")
linux_button = tk.Button(
    sidebar,
    text="🐧 Linux Tools",
    bg="#2b2d31",
    fg="white",
    relief="flat",
    anchor="w",
    padx=20,
    pady=12,
    command=lambda: (
    show_linux(content),
    update_status("Linux Assistant")
)
)

linux_button.pack(fill="x")
settings_button = tk.Button(
    sidebar,
    text="⚙️ Settings",
    bg="#2b2d31",
    fg="white",
    relief="flat",
    anchor="w",
    padx=20,
    pady=12,
    command=lambda: (
    show_settings(content),
    update_status("Settings")
)
)

settings_button.pack(fill="x")
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
def update_status(page):
    status.config(text=f"Status: {page}")



show_home(content)
update_status("Home")
root.mainloop()