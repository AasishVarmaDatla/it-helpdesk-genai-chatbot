def classify_issue(message):
    msg = message.lower()

    if ("crash" in msg or "error" in msg or "failed" in msg or "down" in msg) and "urgent" in msg:
        return "Performance", "High"

    elif "hi" in msg or "hello" in msg:
        return "General", "Low"

    elif "wifi" in msg or "network" in msg or "internet" in msg or "vpn" in msg:
        return "Network", "Medium"

    elif "password" in msg or "login" in msg or "account" in msg:
        return "Account", "Medium"

    elif "slow" in msg or "hang" in msg or "freeze" in msg:
        return "Performance", "Medium"

    elif "printer" in msg or "keyboard" in msg or "mouse" in msg or "laptop" in msg or "PC" in msg:
        return "Hardware", "Low"

    else:
        return "General", "Low"
def generate_reply(category):
    replies = {
        "Network": "Try restarting router or checking cables.",
        "Account": "Reset password or verify credentials.",
        "Performance": "Close background apps and restart system.",
        "Hardware": "Check device connection or contact support.",
        "General": "Hi! I'm Pari, your IT helpdesk assistant. Please describe your issue clearly so I can help."
    }
    return replies.get(category, "Issue noted.")


