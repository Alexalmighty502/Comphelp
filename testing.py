
itscrashy = {
    "question": "?",
    "answers": {"yes": blank, "no": blank}
}

isitslow = {
    "question": "Is the pc slow or very unresponsive?",
    "answers": {"yes": blank, "no": blank}
}

boots = {
    "question": "Is you pc stable or does it crash?",
    "answers": {"yes": itscrashy, "no": isitslow}
}

noboot = {
    "question": ":(",
    "answers": ()
}

doespcboot = {
    "question": "Does the pc boot?",
    "answers": {"yes": boots, "no": noboot}
}
current_question = doespcboot

while True:
    print(current_question["question"])
    if len(current_question["answers"]) == 0:
        break
    answer = input()
    current_question = current_question["answers"][answer]

