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

    def show_welcome():
        chat_output.delete("1.0", tk.END)
        chat_output.insert(
            tk.END,
            "Atlas: Welcome back!\n"
            "Atlas: How can I help you today?\n\n"
        )

    # Show the welcome message when the page opens
    show_welcome()

    input_frame = tk.Frame(content, bg="#202124")
    input_frame.pack(fill="x", padx=20, pady=15)

    user_input = tk.Entry(
        input_frame,
        font=("Segoe UI", 12)
    )
    user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))

    def send_message():

        message = user_input.get().strip()

        if message == "":
            return

        # Handle the clear command
        if message == "/clear":
            show_welcome()
            user_input.delete(0, tk.END)
            return

        # Show the user's message
        chat_output.insert(
            tk.END,
            f"You: {message}\n"
        )

        # Ask Atlas's brain for a response
        response = get_response(message)

        # Show Atlas's response
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

    user_input.bind("<Return>", lambda event: send_message())

    user_input.focus()