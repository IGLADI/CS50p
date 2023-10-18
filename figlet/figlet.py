from pyfiglet import Figlet
import sys
import random
# import time

if not (len(sys.argv) == 1 or len(sys.argv) == 3) or (len(sys.argv) == 3 and sys.argv[1] != "-f"):
    print("Invalid usage")
    exit(5)

figlet = Figlet()
if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        figlet.setFont(font=sys.argv[2])

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)

if len(sys.argv) == 1 or len(sys.argv) == 3:
    text = input("Input: ")
    print(figlet.renderText(text))
    # for i in range(100):
    #     f = random.choice(figlet.getFonts())
    #     figlet.setFont(font=f)
    #     time.sleep(0.5)
    #     print(f)
    #     print(figlet.renderText(text))
    
def print_usage():
    print("Usage: python3 figlet.py [-f FONT]")