import tkinter as tk


def show_linux(content):

    # Clear the current page
    for widget in content.winfo_children():
        widget.destroy()

    title = tk.Label(
        content,
        text="Linux Assistant",
        font=("Segoe UI", 24, "bold"),
        bg="#202124",
        fg="white"
    )

    title.pack(pady=(50, 15))

    description = tk.Label(
        content,
        text="Coming soon...\n\nRun Linux guides and command helpers from here.",
        font=("Segoe UI", 13),
        bg="#202124",
        fg="#cccccc",
        justify="center"
    )

    description.pack()