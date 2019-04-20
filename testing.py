blank = "test"
reinstall = {
    "question": "Sometimes a driver or other critical part of your system gets installed improperly causing seemingly random crashing a clean install should fix this",
    "answers": ()
}
ramfailure = {"question": "unfortunately if you have errors with your ram the only way to fix is by replacing it If you have more then one stick of ram you could rerun the test with each stick separately to see if any ram you have is usable",
              "answers": ()}
itfixed = {"question": "Good to see the issue was fixed",
           "answers": ()}  # Endpoint
ramtest = {
    "question": "Do you get a blue screen with the errors MEMORY_MANAGEMENT, DATA_BUS_ERROR, PAGE_FAULT_IN_NONPAGED_AREA? These are all linked to a ram issue which can be tested with a test from a program called memtest86 ",
    "answers": {"yes": ramfailure, "no": reinstall}
}
diditfix2 = {
    "question": "did this fix your issue?",
    "answers": {"yes": itfixed, "no": ramtest}
}
itscrashy = {
    "question": "Are you positive the temps are fine? Crashing could be caused from an overheating pc you can use a program like HWMonitor to monitor PC temperatures.",
    "answers": {"yes": ramtest, "no": }
}
oldpc = {
    "question": "A PC of this age should really be upgraded technology has really improved with time",
    "answers": ()}  # Endpoint
virusandmalware = {
    "question": "Do you test for viruses and malware on atleast a monthly basis? Do note however antivirus programs are rather poor at detecting malware so its recommended to have a antivirus program AND a antimalware program like Malwarebytes at the same time.",
    "answers": {"yes": reinstall, "no": "installing antimalware and antivirus software is critical to keep your pc healthy I HIGHLY recommend you install them if you don't have them."}
}
currentpc = {
    "question": "Does the boot drive use a Solid State Drive?",
    "answers": {"yes": virusandmalware,
                "no": "An operating system like windows is very complex and requires a lot of loading from Storage to Ram and back to the storage. Upgrading from a HDD to SSD will make the system in all feel much more responsive I HIGHLY recommend to replace your HDD with an SSD"}
}
agetest = {
    "question": "Is the PC 7 years older?",
    "answers": {"yes": oldpc, "no": currentpc}
}

powertrip = {
    "question": "Are you sure the power socket is not tripped?",
    "answers": {"yes": blank, "no": "You can check by using a simple charger or any other device"}
}
enoughpower = {
    "question": "If the PSU works and your PC still shows no signs of life it could point to a faulty motherboard or CPU ",
    "answers": ()}  # Endpoint
checkpsu = {
    "question": "Are you sure the Psu works?, This can be tested by using a paper clip to jump pin 3 and for on the clip side of the 24 pin",
    "answers": {"yes": enoughpower, "no": "If your PSU is dead DO NOT try to fix it yourself the capacitors inside hold a lethal charge the only recommended fix is to replace it"}
}
diditfix1 = {"question": "Did this fix your issue?",
             "answers": {"yes": itfixed, "no": checkpsu}
}
noboot = {
    "question": "Check to see if are any loose connections namely the 20-24 pin, cpu 6 pin and pcie power cords. Did this help? (respond with yes or no)",
    "answers": {"yes": diditfix1, "no": checkpsu}
}
boots = {
    "question": "Is your pc stable but slow or does it crash? (print stable or crash)",
    "answers": {"stable": currentpc, "crash": itscrashy}
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
