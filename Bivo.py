import webbrowser
import os
import socket

def clear():
    os.system("clear")

#colors
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"
reset = "\033[0m"
#Remove USB
def one():
    confirm = input(red + "This will earse your USB Or Desk :\nYou Need To Continue (y/n)"+ reset).lower()
    if confirm in ("y","yes"):
        print("""\n
    sudo umount /dev/sdb*
    sudo parted /dev/sdb mklabel msdos
    sudo parted -a optimal /dev/sdb mkpart primary fat32 0% 100%
    sudo mkfs.vfat -F 32 /dev/sdb1
    sudo eject /dev/sdb
    """)
    elif confirm in ("n","no"):
        print(yellow+"operation cancelled"+reset)
        return
    else:
         print("Please Enter (y/n) Only")
         return
# Share OS TO USB
def two():
    print("\nsudo dd if= bs=4M status=progress && sync")
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
    print(cyan +r"""
     _    __    _ _      _     ___
    / \  / _| / _|_ _|_ _|    / \  |  _ \_   _|
   / _ \ \___ \| |    | | | |    / _ \ | |_) || |
  / _ \ _) | |_ | | | |   / _ \|  _ < | |
 /_/   \_\__/ \|_|___| /_/   \_\_| \_\|_|


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
# About Me
def am():
    print(r"""
    _                           ___
   /   |  / /_  __    / /_   /  |/  /
  / /| | /  \/  \/ / / / __/  / /|_/ / _ \
 / _ |/ /_/ / /_/ / /_/ / /_   / /  / /  /
/_/  |_/_._/\/\,_/\/  /_/  /_/\_/

    """)
    print("\nBivo\n16\nProgrammer\n")
# tiktok
def tk():
    webbrowser.open("https://www.tiktok.com/@wolf_hyper_ui?_r=1&_t=ZS-92QSRMiaIoG")
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
 ------'   --'        \_/         -------'

""")
    try:
         main =int(input("""
1.Remove USB
2.Share OS TO USB
3.Run js File
4.Open OS With Qemu qcow2
5.low Brightness
6.qcow2
7.open OS With Qemu + Qcow2
8.local Host
9:ASCII Colors Codes
10:Socket Port Scanner
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
