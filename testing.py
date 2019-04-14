import time
import sys
blank = "test"
reinstall = {
    "question": "blank",
    "answers": {"yes": blank, "no": blank}
}
ramfailure = {"question": "unfortunately if you have errors with your ram the only way to fix is by replacing it",
              "answers": ()}
itfixed = {"question": "Good to see the issue was fixed",
              "answers": ()}
ramtest = {
    "question": "Do you get a blue screen with the errors MEMORY_MANAGEMENT, DATA_BUS_ERROR, PAGE_FAULT_IN_NONPAGED_AREA? These are all linked to a ram issue which can be tested with a test from a program called memtest86 ",
    "answers": {"yes": ramfailure, "no": reinstall}
}
diditfix2 = {
    "question": "did this fix your issue?",
    "answers": {"yes": itfixed , "no": blank}
}
itscrashy = {
    "question": "Are you positive the temps are fine? Crashing could be caused from a over heating pc you can use a program like HWMonitor to monitor PC temperatures.",
    "answers": {"yes": ramtest, "no": diditfix2}
}
agetest = {
    "question": "",
    "answers": {"yes": blank, "no": blank}
}
isitslow = {
    "question": "Is the pc slow or very unresponsive?",
    "answers": {"yes": agetest, "no": "blank"}
}
boots = {
    "question": "Is your pc stable but slow or does it crash? (print stable or crash)",
    "answers": {"stable": itscrashy, "crash": isitslow}
}
powertrip = {
    "question": "Are you sure the power socket is not tripped?",
    "answers": {"yes": blank, "no": "you can check by using a simple charger or any other device"}
}
checkpsu = {
    "question": "Are you sure the Psu works?, This can be tested by using a paper clip to jump pin 3 and for on the clip side of the 24 pin",
    "answers": {"yes": powertrip, "no": "if your PSU is dead DO NOT try to fix it yourself the capacitors inside hold a lethal charge the only recommended fix is to replace it"}
}
diditfix1 = {"question": "Did this fix your issue?",
    "answers": {"yes": itfixed , "no": checkpsu}
}
noboot = {
    "question": "Check to see if are any loose connections namely the 20-24 pin, cpu 6 pin and pcie power cords. Did this help? (respond with yes or no)",
    "answers": {"yes": diditfix1, "no": checkpsu}
}
doespcboot = {
    "question": "Does the pc boot?",
    "answers": {"yes": boots, "no": noboot}
}
current_question = doespcboot
blank = "test"
while True:
    print(current_question["question"])
    if len(current_question["answers"]) == 0:
        break
    answer = input()
    current_question = current_question["answers"][answer]
