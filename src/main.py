import tkinter as tk

# ---------------- Window ---------------- #

root = tk.Tk()
root.title("Atlas")
root.geometry("1100x700")
root.configure(bg="#202124")

# ---------------- Sidebar ---------------- #

sidebar = tk.Frame(root, width=220, bg="#2b2d31")
sidebar.pack(side="left", fill="y")

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

# ---------------- Content ---------------- #

content = tk.Frame(root, bg="#202124")
content.pack(fill="both", expand=True)

title = tk.Label(
    content,
    text="Atlas AI Chat",
    font=("Segoe UI", 24, "bold"),
    bg="#202124",
    fg="white"
)
title.pack(pady=(30, 10))

chat_output = tk.Text(
    content,
    height=20,
    bg="#2b2d31",
    fg="white",
    insertbackground="white",
    relief="flat"
)
chat_output.pack(fill="both", expand=True, padx=20)
chat_output.insert(
    tk.END,
    "Atlas: Welcome back!\nAtlas: How can I help you today?\n\n"
)
input_frame = tk.Frame(content, bg="#202124")
input_frame.pack(fill="x", padx=20, pady=15)

user_input = tk.Entry(
    input_frame,
    font=("Segoe UI", 12)
)
user_input.pack(side="left", fill="x", expand=True, padx=(0,10))


def send_message():

    message = user_input.get()

    if message.strip() == "":
        return

    chat_output.insert(tk.END, f"You: {message}\n")

    response = f"Atlas: I received your message: '{message}'"

    chat_output.insert(tk.END, response + "\n\n")

    user_input.delete(0, tk.END)


send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message
)

send_button.pack(side="right")

status = tk.Label(
    root,
    text="Status: Ready",
    bg="#1b1b1b",
    fg="white",
    anchor="w"
)

status.pack(side="bottom", fill="x")

root.mainloop()