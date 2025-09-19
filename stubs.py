from time import sleep
def printslowcolor(text):
    for char in text:
        print(char, end='', flush=True)
        sleep(0.05)