import os
def clear():
    os.system("clear")
# colors
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan= "\033[36m"
reset = "\033[0m"
def p():
    input(yellow +"\npress enter to continue..."+ reset)
def v():
    print(red +"Numbers Only" + reset)
    p(), clear()

def soon():
    print(yellow + "coming soon..."+ reset)         
    p(), clear()

def loops():
    while True:
        try:
            print(cyan +"""
db       .d88b.   .d88b.  d8888b. .d8888. 
88      .8P  Y8. .8P  Y8. 88  `8D 88'  YP 
88      88    88 88    88 88oodD' `8bo.   
88      88    88 88    88 88~~~     `Y8b. 
88booo. `8b  d8' `8b  d8' 88      db   8D 
Y88888P  `Y88P'   `Y88P'  88      `8888Y' 
                                          
"""+ reset)
            choice_one = int(input("\n1.string Loops\n2.Numberic Loops\n3.Loops Code Generator\n99.Back\n : "))
        except ValueError:
            v()
            continue
        except KeyboardInterrupt:
            p(), clear()
            continue

            
        if choice_one == 1:
                try:
                    str_loop = str(input("Enter Loop Print :"))
                except KeyboardInterrupt:
                      p(), clear()
                      continue
                try:
                    str_count = int(input("Enter Loop Count : "))
                except ValueError:
                    v()
                    continue
                except KeyboardInterrupt:
                    p(), clear()
                    continue
                
                if str_count > 1000:
                    clear()
                    print(yellow + "That's too many!" +reset)
                    continue
                
                for co in range (1, str_count + 1):
                    print(str_loop)
        elif choice_one == 2:
                try:
                    num_loop = str(input("Enter Loop Print : "))
                except KeyboardInterrupt:
                    p(), clear()
                    continue
                try:
                    num_count = int(input("Enter Loop Count : "))
                except ValueError:
                    v()
                    continue
                except KeyboardInterrupt:
                    p(), clear()
                    continue
                if num_count > 1000:
                    v()
                    continue
                for no in range (1, num_count + 1):
                    print(f"{no}.{num_loop}")
        elif choice_one == 3:
            try:
                print_loop = str(input("Enter printer Name : "))
            except KeyboardInterrupt:
                p() ,clear()
                continue
            try:
                loop_printer = str(input("Enter Loop Printer : "))
            except KeyboardInterrupt:
                p() , clear()
                continue
            try:
                count_loop = str(input("Enter Counter Name : "))
            except KeyboardInterrupt:
                p(), clear()
                continue
            try:
                loop_counter = str(input("Enter Loop Counter : "))
            except KeyboardInterrupt:
                p(), clear()
                continue
            try:
                print(f"""{print_loop} = {loop_printer}\n{count_loop} = {loop_counter}\nfor i in range(1, {count_loop} + 1):\n    print({print_loop}) """)
                num_true=input("\nDo You Want Numbric Loop Code ? (y/n) : ").lower()
            except KeyboardInterrupt:
                p(), clear()
                continue
            except ValueError:
                v()
                continue
            if num_true in ("y", "yes"):
                print(f"""{print_loop} = {loop_printer}\n{count_loop} = {loop_counter}\nfor i in range(1, {count_loop} + 1):\n    print(f"i.{print_loop}") """)
                print(yellow + "\nPlease Change 'i' In Print To \"{}\" "+ reset)
                p(), clear()
                continue
            elif num_true in ("n", "no"):
                clear()
                continue
            else:
                print(yellow + "Only (y/n) or (yes,no)"+ reset)
                p(), clear()
                return
                

        elif choice_one == 99:
            return
        else:
            soon(),p()
            continue
def science():
    os.system("python3 science.py")

menu = {
    1:loops,
    2:science
}
while True:
    try:
        clear()
        print("""
      
 .d88b.  d888888b db   db d88888b d8888b. .d8888. 
.8P  Y8. `~~88~~' 88   88 88'     88  `8D 88'  YP 
88    88    88    88ooo88 88ooooo 88oobY' `8bo.   
88    88    88    88~~~88 88~~~~~ 88`8b     `Y8b. 
`8b  d8'    88    88   88 88.     88 `88. db   8D 
 `Y88P'     YP    YP   YP Y88888P 88   YD `8888Y'                                                                                           
                                                                                                        
""")
        main = int(input("\n1.Loops\n2.Science\n99.Return to Main Menu\n0.Exit\n : "))
        if main == 0:
            break
        elif main == 99:
            clear()
            os.system("python3 meDef.py")
        menu.get(main, soon)()
    except ValueError:
        print(red +"Numbers Only" + reset)
        continue
    except KeyboardInterrupt:
        clear()
        continue
