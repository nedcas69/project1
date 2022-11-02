def send_massage(msgs, sent_messages):
    while msgs:
        current_massage = msgs.pop()
        print(current_massage)
        sent_messages.append(current_massage)

msgs = ["Не нервируй меня! Мне скоро негде будет прятать трупы!",
        "Обязательно женись. Если попадется хорошая жена, станешь счастливым, а если плохая, станешь философом.",
        "Если хочешь, я дома..."]
sent_messages = []
send_massage(msgs[:], sent_messages)

print(msgs,'\n', sent_messages)