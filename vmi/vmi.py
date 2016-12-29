import wmi

c = wmi.WMI()
for s in c.Win32_Service(StartMode="Auto", State="Stopped"):
    if raw_input("Restart %s? " % s.Caption).upper() == "Y":
        s.StartService()