import socket
import time
import webbrowser
import os
import subprocess

def timer():
    for i in range(0,3):
        print(f"\rReset After {3-i} Seconds", end="", flush=True)
        time.sleep(1)
    clear()

def timer2():
    for i in range(0,3):
        print(f"\rReset After {3-i} Seconds", end="", flush=True)
        time.sleep(1)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def command():          #main command
    print(yellow +"\nHere The Command  " +reset)

def press():        #KeyboardInterrupt
    input(yellow +"\npress enter to continue..."+ reset)
    timer()

def value():                #ValueError
    print(yellow +"Numbers Only" + reset)
    input(yellow +"\npress enter to continue..."+ reset)
    timer()

def press_enter():
    input(yellow +"\npress enter to continue..."+ reset)

def os_iso():
    iso_files = [f for f in os.listdir() if f.endswith(".iso")  ]
    if iso_files:
        my_score = 1;
        if my_score == 1:
            print("\nFound ISO files in the current directory:\n")
            for iso in iso_files:
                print(iso)
    else:
        my_score = 0;
        if my_score == 0:
            while True:
                try:
                    print(yellow + "\nNo ISO files found in the current directory.\nYour Files Are : " + reset)
                    os.system("ls")
                    timer2()
                    break
                except KeyboardInterrupt:
                    press()
                    return            

#colors
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"
reset = "\033[0m"
#ascii
left_high_corner = "\u250c"       # high corner
right_high_corner = "\u2510"
left_lower_corner = "\u2514"      # low corner
right_lower_corner = "\u2518"
background = "\u2500"             # the main wall
wall = "\u2502"
wall_colon = "\u2592"
#Remove USB
def one():    
    print("""
    sudo umount /dev/sdb*
    sudo parted /dev/sdb mklabel msdos
    sudo parted -a optimal /dev/sdb mkpart primary fat32 0% 100%
    sudo mkfs.vfat -F 32 /dev/sdb1
    sudo eject /dev/sdb
    """)
    command()
    press_enter()
    while True:
                try:
                    print("\n\n\n\n" + left_high_corner + background * 24 + right_high_corner)
                    print(wall + red + "This will earse your USB"+ reset + wall)
                    print(left_lower_corner + background * 24 + right_lower_corner)
                    confirm = input("\nYou Need To Start (y/n) : ").lower()
                except KeyboardInterrupt:
                    press()
                    
                print("\nSorry That Future Is Not Available For Now :(")
                return
#                if confirm in ("y","yes"):
#                    os.system("lsblk")
#                    os.system("sudo umount /dev/sdb* && sudo parted /dev/sdb mklabel msdos && sudo parted -a optimal /dev/sdb mkpart primary fat32 0% 100% && sudo mkfs.vfat -F 32 /dev/sdb1 && sudo eject /dev/sdb")
#                    print(green+"USB Removed Successfully"+reset)
#                elif confirm in ("n","no"):
#                   print(yellow+"operation cancelled"+reset)
#                    break
#                else:
#                    print(yellow+"Please Enter (y/n) Only"+reset)
#                    return

# Share OS TO USB
def two():
    print(f"\nsudo dd if=" +yellow + "OS_Name"+ reset + " of=/dev/sdb bs=4M status=progress && sync")
    command()
    while True:
        try:     
            confirm = str(input("\nDo You Want To Make It Here (y/n) : ")).lower()   ####  Main Confirm
        except KeyboardInterrupt:
            press()
            return
        if confirm in ("y","yes"):         #### YEEEEESSSSSS
                try:
                    enter_cd =int(input("\nWhere is your os File location\n\n1.Downloads\n2.Desktop\n3.others\n4.exit\n : "))  ## list Downloads & Desktop
                except ValueError:
                    value()
                except KeyboardInterrupt:
                    press()
                    return
                os.system("cd")                
                if enter_cd == 1:                     # Downloads
                    os.chdir(os.path.expanduser("~/Downloads"))
                    os_iso()
                    try:
                        os_name =input("\nEnter Your System File Name To Share With USB\n : ")
                    except KeyboardInterrupt:
                        press()
                        return                              
                    os.system(f'sudo dd if="{os_name}" of=/dev/sdb bs=4M status=progress && sync')

                elif enter_cd == 2:                     # Desktop
                    os.chdir(os.path.expanduser("~/Desktop"))
                    os_iso()
                    try:
                        os_name =input("\nEnter Your System File Name To Share With USB\n : ")
                    except KeyboardInterrupt:
                        press()
                        return                              
                    os.system(f'sudo dd if="{os_name}" of=/dev/sdb bs=4M status=progress && sync')
                elif enter_cd == 3:              # others
                    try:
                        os_share =input("Enter Your File Location : ")
                    except KeyboardInterrupt:
                        press()
                        return 
                    subprocess.run([f"sudo dd if={os_share} of=/dev/sdb bs=4M status=progress && sync"])
                elif enter_cd == 4:         # exit
                    break
                else:
                    print(yellow+"Please Choose From The List"+reset)
                    return
## elif & else                    
        elif confirm in ("n","no"):
            break
        else:
            print(yellow+"Please Choose (y/n) Only"+reset)
            return
                    

#confirm = input("Enter Your File Location : ")
# run js file
def three():
    print("\nnode "+cyan+"file"+reset+".js")
# open OS With Qemu qcow2
def four():
    print("\nqemu-system-x86_64 -m "+cyan+"2500"+reset+" -hda "+cyan+"win-disk.qcow2"+reset+" -boot c -vga std -display gtk -machine accel=tcg")
# low Brightness
def five():
    print("\nxgamma -gamma 0.7\n")
    print(yellow+"To retern gamma Set it At 1.0"+reset)
# qcow2
def six():
    print("\nqemu-img create -f qcow2 "+cyan+"linux-test.qcow2 20G"+reset)
# open OS With Qemu + Qcow2
def seven():
    print("\nqemu-system-x86_64 -m"+cyan+ " 2048"+reset+" -cpu qemu64 -smp 2 -hda"+cyan+ " test-one.qcow2"+reset+" -boot d -cdrom" + cyan+" os.iso "+reset+"-vga virtio -display gtk")
#server
def eight():
    print(yellow+"\npython -m http.server 8080\n")
    print("TO OPEN THE LOCAL Host SERVER")
    print("\nhttp://localhost:8080\n"+reset)
#colors
def nine():
    clear()
    print(cyan +r"""
          
 .d8b.  .d8888.  .o88b. d888888b d888888b       .o88b. 
d8' `8b 88'  YP d8P  Y8   `88'     `88'        d8P  Y8 
88ooo88 `8bo.   8P         88       88         8P      
88~~~88   `Y8b. 8b         88       88         8b      
88   88 db   8D Y8b  d8   .88.     .88.        Y8b  d8 
YP   YP `8888Y'  `Y88P' Y888888P Y888888P       `Y88P' 

"""+reset)
    print("𝙼𝚊𝚒𝚗 𝙲𝚘𝚍𝚎 : \𝟶𝟹𝟹[**𝚖 𝚃𝚎𝚡𝚝 \𝟶𝟹𝟹[0𝚖")
    print(" Colors :\n Black  :"+black+" Bivo " +reset +": 30m")
    print(" red    :"+red+ " Bivo " +reset+ ": 31m")
    print(" Green  :"+green+ " Bivo " +reset+ ": 32m")
    print(" Yellow :"+yellow+ " Bivo " +reset+ ": 33m")
    print(" Blue   :"+blue+ " Bivo " +reset+ ": 34m")
    print(" Purple :"+purple+ " Bivo " +reset+ ": 35m")
    print(" Cyan   :"+cyan+ " Bivo " +reset+ ": 36m")
    print(" Color Reset   :  0m")
#socket
def ten():
    ip = input("Enter Target IP Address: ")
    port = int(input("Enter Target Port Number:"))
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((ip, port))
    if result == 0:
       print(f"Port {port} is [OPEN]")
    else:
         print(f"Port {port} is [CLOSED]")
    s.close()
#others
def eleven():
    os.system("python3 others.py")
# About Me
def am():
    clear()
    print(r"""

 .d8b.  d8888b.  .d88b.  db    db d888888b      .88b  d88. d88888b 
d8' `8b 88  `8D .8P  Y8. 88    88 `~~88~~'      88'YbdP`88 88'     
88ooo88 88oooY' 88    88 88    88    88         88  88  88 88ooooo 
88~~~88 88~~~b. 88    88 88    88    88         88  88  88 88~~~~~ 
88   88 88   8D `8b  d8' 88b  d88    88         88  88  88 88.     
YP   YP Y8888P'  `Y88P'  ~Y8888P'    YP         YP  YP  YP Y88888P 
                                                                   
    """)
    print("\nBivo\n16\nProgrammer\n")
# tiktok
def tk():
    webbrowser.open("https://www.tiktok.com/@wolf._.b?_r=1&_t=ZS-92QSRMiaIoG")
#soon
def soon():
    print(yellow+"soon"+reset)
# Menu
menu = {
    1:one,
    2:two,
    3:three,
    4:four,
    5:five,
    6:six,
    7:seven,
    8:eight,
    9:nine,
    10:ten,
    11:eleven,
    99:am,
    98:tk
}
while True:
    clear()

    print(r"""
.-. .-')                 (-.
\  ( OO )              _(OO  )_
 ;-----.\   ,-.-') ,--(_/   ,. \ .-'),-----.
 | .-.  |   |  |OO)\   \   /(/( OO'  .-.    |
 | '-' /_)  |  |  \ \   \ /   / /   |  | |  |
 | .-. .   |  |(_/  \   '   /, \_) |  |\|  |
 | |  \  | ,|  |_.'   \     /)  \ |  | |  | |
 | '--'  /(_|  |       \   /       \  '-'  |
 `------'   `--'        \_/         `------'

""")
    try:
         main =int(input("""
1.Earse USB
2.Share OS TO USB
3.Run js File
4.Open OS With Qemu qcow2
5.low Brightness
6.qcow2
7.open OS With Qemu + Qcow2
8.local Host
9:ASCII Colors Codes
10:Socket Port Scanner
11:Others
98.TikTok
99.About Me
0.exit\n: """))
         if main == 0:
            break
         menu.get(main, soon)()
         input("\nPress Enter To Continue...")
    except ValueError:
           print("\nPlease enter number")
           continue
    except KeyboardInterrupt:
           print("\n\nBe careful!")
           continue
