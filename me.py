import webbrowser
import os
# Remove USb
def clear():
    os.system("clear")

def one():
    print("""\n
    sudo umount /dev/sdb*
    sudo parted /dev/sdb mklabel msdos
    sudo parted -a optimal /dev/sdb mkpart primary fat32 0% 100%
    sudo mkfs.vfat -F 32 /dev/sdb1
    sudo eject /dev/sdb
    """)
# Share OS TO USB
def two():
    print("\nsudo dd if= bs=4M status=progress && sync")
# run js file
def three():
    print("\nnode file.js")
# open OS With Qemu qcow2
def four():
    print("\nqemu-system-x86_64 -m 2500 -hda win-disk.qcow2 -boot c -vga std -display gtk -machine accel=tcg")
# low Brightness
def five():
    print("\nxgamma -gamma 0.7")
# qcow2
def six():
    print("\nqemu-img create -f qcow2 linux-test.qcow2 20G")
# open OS With Qemu + Qcow2
def seven():
    print("\nqemu-system-x86_64 -m 2048 -cpu qemu64 -smp 2 -hda test-one.qcow2 -boot d -cdrom archcraft-2025.iso -vga virtio -display gtk")
# About Me
def am():
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
    webbrowser.open("https://www.tiktok.com/@wolf_hyper_ui?_r=1&_t=ZS-92QSRMiaIoG")
#soon
def soon():
    print("soon")
# Menu
menu = {
    1:one,
    2:two,
    3:three,
    4:four,
    5:five,
    6:six,
    7:seven,
    99:am,
    98:tk
}
while True:
    clear()
    
    print(r"""
.-. .-')                 (`-.                
\  ( OO )              _(OO  )_              
 ;-----.\   ,-.-') ,--(_/   ,. \ .-'),-----. 
 | .-.  |   |  |OO)\   \   /(/( OO'  .-.  '
 | '-' /_)  |  |  \ \   \ /   / /   |  | |  |
 | .-. `.   |  |(_/  \   '   /, \_) |  |\|  |
 | |  \  | ,|  |_.'   \     /)  \ |  | |  |
 | '--'  /(_|  |       \   /       `'  '-'  '
 ------'   --'        -'          -----' 
      
""")
    try:
         main =int(input("\n1.Remove USB\n2.Share OS TO USB\n3.Run js File\n4.Open OS With Qemu qcow2\n5.low Brightness\n6.qcow2\n7.open OS With Qemu + Qcow2\n98.TikTok\n99.About Me\n0.exit\n: "))
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
