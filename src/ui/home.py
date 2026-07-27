import tkinter as tk


def show_home(content):

    for widget in content.winfo_children():
        widget.destroy()

    title = tk.Label(
        content,
        text="Welcome to Atlas",
        font=("Segoe UI", 24, "bold"),
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