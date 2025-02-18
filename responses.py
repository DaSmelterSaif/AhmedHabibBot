
def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == "ahmed":
        return "Hi"
    elif p_message == "it's ahmed":
        return "Ayo"
    elif p_message == "please":
        return "no"
    else:
        return ""