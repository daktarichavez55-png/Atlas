import tkinter as tk

from core.chat_engine import get_response


def show_chat(content):

    # Clear the current page
    for widget in content.winfo_children():
        widget.destroy()

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

    user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))

    def send_message():

        message = user_input.get()

        if message.strip() == "":
            return

        # Show the user's message
        chat_output.insert(
            tk.END,
            f"You: {message}\n"
        )

        # Ask Atlas's brain for a response
        response = get_response(message)

        # Display Atlas's response
        chat_output.insert(
            tk.END,
            f"Atlas: {response}\n\n"
        )

        # Clear the input box
        user_input.delete(0, tk.END)

    send_button = tk.Button(
        input_frame,
        text="Send",
        command=send_message
    )

    send_button.pack(side="right")