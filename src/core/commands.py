def execute_command(command):

    command = command.lower().strip()

    if command == "/help":
        return (
            "Available commands:\n"
            "/help - Show available commands\n"
            "/about - About Atlas\n"
            "/clear - Clear chat (coming soon)"
        )

    elif command == "/about":
        return (
            "Atlas v0.0.5\n"
            "Built with Python and Tkinter."
        )

    else:
        return "Unknown command. Type /help for available commands."