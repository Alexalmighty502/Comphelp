import wmi
from hurry.filesize import size

def pcinfo():
    pc = wmi.WMI()
    pc_info = pc.Win32_ComputerSystem()[0]
    proc_info = pc.Win32_Processor()[0]
    system_ram = size(int(pc_info.TotalPhysicalMemory))
    gpu_info = pc.Win32_VideoController()[0]
    info_string = f"""CPU : {proc_info.Name}\nRAM: {system_ram}B\nGraphics Card: {gpu_info.Name}"""  # formatting Figuring this out took far too long
    return info_string  # saves the users info to be displayed later if the user requests it

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
    "answers": {"yes": ramtest, "no": "If temps in your system hit 95°-100°c it is most likely shutting itself of to protect from damage if the temperature is this high you will need to replace your cooling setup for something stronger. "}
}
oldpc = {
    "question": "A PC of this age should really be upgraded technology has really improved with time",
    "answers": ()}  # Endpoint
virusandmalware = {
    "question": "Do you test for viruses and malware on at a monthly basis? Do note however antivirus programs are rather poor at detecting malware so its recommended to have a antivirus program AND a antimalware program like Malwarebytes at the same time.",
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
deadmobo = {
    "question": "If the PC is still not working at this point its most likely the Motherboard is dead",
    "answers": {()}  # Endpoint
}
opencase = {
    "question": "Remove the Motherboard, Ram, Power Supply Unit, and if your PC lacks a integrated GPU the GPU and reconnect everything on a nonconductive surface like cardboard this should help to see if there's a short-circuit. Did this help?",
    "answers": {"yes": itfixed, "no": deadmobo}
}
powertrip = {
    "question": "Are you sure the power socket is not tripped?",
    "answers": {"yes": opencase, "no": "You can check by using a simple charger or any other device"}
}
enoughpower = {
    "question": "Did you recently upgrade your PC components?  ",
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
pcinformation = {
    "question": pcinfo(),
    "answers": ()}
Start = {
    "question": "Hello and welcome to my PC troubleshooter would you like info about your pc or would you like to run the troubleshooter (type pcinfo or troubleshooter)",
    "answers": {"pcinfo": pcinformation, "troubleshooter": doespcboot}
}

current_question = Start
while True:
    print(current_question["question"])
    if len(current_question["answers"]) == 0:
        break
    answer = input()
    current_question = current_question["answers"][answer]
