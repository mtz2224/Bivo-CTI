import os
def clear():
    os.system("clear")
# colors
red = "\033[31m"
yellow = "\033[33m"
green = "\033[32m"
reset = "\033[0m"
def p():
    input(yellow +"\npress enter to continue..."+ reset)
def v():
    print("\nNumbers Only")
    p()
c = 6.5
mheight = 1000
while True:
    try:
        height =int(input("Enter Height In meter : "))
    except ValueError:
             v()
             continue
    except KeyboardInterrupt:
             p()
             continue

    temp = (height / mheight) * c
    print(green +f"result : {temp:.2f}"+ reset)
    input("Press Enter To Close ")
    break
