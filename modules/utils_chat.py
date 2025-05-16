def init_chat():
    return []

def update_chat(question, history):
    # Version simulée : réponse générique
    history.append({"role": "user", "content": question})
    reply = f"(Réponse simulée à : '{question[:30]}...')"
    history.append({"role": "assistant", "content": reply})
    return reply
