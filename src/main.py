import tkinter as tk

root = tk.Tk()

root.title("Atlas")
root.geometry("1100x700")
root.configure(bg="#202124")

# ---------------- Sidebar ---------------- #

sidebar = tk.Frame(
    root,
    width=220,
    bg="#2b2d31"
)

sidebar.pack(
    side="left",
    fill="y"
)

buttons = [
    "🏠 Home",
    "💬 AI Chat",
    "📄 PDF Tools",
    "🐧 Linux",
    "⚙ Settings"
]

for item in buttons:

    button = tk.Button(
        sidebar,
        text=item,
        bg="#2b2d31",
        fg="white",
        relief="flat",
        anchor="w",
        padx=20,
        pady=12
    )

    button.pack(fill="x")


# ---------------- Main Area ---------------- #

content = tk.Frame(
    root,
    bg="#202124"
)

content.pack(
    fill="both",
    expand=True
)

title = tk.Label(
    content,
    text="Welcome to Atlas",
    font=("Segoe UI", 26, "bold"),
    bg="#202124",
    fg="white"
)

title.pack(pady=80)

subtitle = tk.Label(
    content,
    text="Build. Automate. Create.",
    font=("Segoe UI", 14),
    bg="#202124",
    fg="#cccccc"
)

subtitle.pack()

status = tk.Label(
    root,
    text="Status: Ready",
    bg="#1b1b1b",
    fg="white",
    anchor="w"
)

status.pack(
    side="bottom",
    fill="x"
)

root.mainloop()