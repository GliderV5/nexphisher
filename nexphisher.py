import os 
import sys

if str(os.getuid()) == "1000":
    print()
    print()
    print()
    print()
    print()
    print("please run this program as root") 
    print()
    print()
    print()
    print()
    print()
    sys.exit()

os.system("sudo bash nexphisher")
