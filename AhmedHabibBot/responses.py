def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == "Ahmed":
        return "Hi"
    elif p_message == "It's Ahmed":
        return "Ayo"
    elif p_message == "!help":
        return "no"
    elif p_message == "please":
        return "no"
    else:
        return ""