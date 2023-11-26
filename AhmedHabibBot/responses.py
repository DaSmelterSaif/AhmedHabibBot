def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == "Ahmed":
        return "Hi"
    
    if p_message == "It's Ahmed":
        return "Ayo"
    
    if p_message == "!help":
        return "no"