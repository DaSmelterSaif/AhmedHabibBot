
def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == "ahmed":
        return "Hi"
    elif p_message == "it's ahmed":
        return "Ayo"
    elif p_message == "help ahmed":
        return "no"
    elif p_message == "please":
        return "no"
    elif p_message == "math": # Requested by Sammer
        return "I love Sammi."
    else:
        return ""