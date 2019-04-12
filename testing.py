itscrashy = {
    "question": "",
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
checkpsu = {
    "question": "Are you sure the Psu works?, This can be tested by using a paper clip to jump pin 3 and for on the clip side of the 24 pin",
    "answers": {"yes": diditfix, "no": deadpsu}
}

noboot = {
    "question": "Check to see if are any loose connections namely the 20-24 pin, cpu 6 pin and pcie power cords. Did this help?",
    "answers": {"yes": diditfix, "no": checkpsu}
}
diditfix = {"question": "Did this fix your issue?",
    "answers": {"yes": "Good to see the issue was fixed" exit(), "no": checkpsu}
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
