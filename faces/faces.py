def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")

def main():
    text = input("")
    text = convert(text)
    print(text)

main()