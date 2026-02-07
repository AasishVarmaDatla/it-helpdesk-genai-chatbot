def classify_issue(message):
    msg = message.lower()

    if "wifi" in msg or "network" in msg or "vpn" or "internet" in msg:
        return "Network", "High"

    elif "password" in msg or "login" in msg or "account" in msg:
        return "Account", "Medium"

    elif "slow" in msg or "hang" in msg or "freeze" in msg:
        return "Performance", "Medium"

    elif "printer" in msg or "keyboard" in msg or "mouse" in msg:
        return "Hardware", "Low"

    else:
        return "General", "Low"

def generate_reply(category):
    replies = {
        "Network": "Try restarting router or checking cables.",
        "Account": "Reset password or verify credentials.",
        "Software": "Reinstall or update the application.",
        "General": "Support team will assist shortly."
    }
    return replies.get(category, "Issue noted.")

