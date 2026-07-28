from core.commands import execute_command


def get_response(message):

    message = message.strip()

    if message == "":
        return "Please type a message."

    # Handle commands
    if message.startswith("/"):
        return execute_command(message)

    # Normal chat
    return f"You said: {message}"