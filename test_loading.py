import time

for i in range(5):
    print("loading" + "." * i, end="\r")
    time.sleep(0.5)
