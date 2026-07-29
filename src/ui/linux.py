import tkinter as tk
from core.linux_database import linux_commands


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

    output = tk.Text(
        content,
        height=15,
        bg="#2b2d31",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    output.pack(fill="both", expand=True, padx=20, pady=10)

    input_frame = tk.Frame(
        content,
        bg="#202124"
    )
    input_frame.pack(fill="x", padx=20, pady=10)

    command_entry = tk.Entry(
        input_frame,
        font=("Segoe UI", 12)
    )
    command_entry.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 10)
    )

    def search_command():

        command = command_entry.get().strip().lower()

        response = linux_commands.get(
            command,
            "Command not found."
        )

        output.delete("1.0", tk.END)

        output.insert(
            tk.END,
            f"Command: {command}\n\n"
             f"Description:\n{response}"
        )

        command_entry.delete(0, tk.END)

    search_button = tk.Button(
        input_frame,
        text="Run",
        command=search_command
    )
    search_button.pack(side="right")

    command_entry.bind(
        "<Return>",
        lambda event: search_command()
    )

    command_entry.focus()