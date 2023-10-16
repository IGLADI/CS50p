filename = input("File name: ").strip().lower()
file = filename.split(".")
match file[-1]:
    case "gif" | "jpeg" | "png":
        print(f"image/{file[-1]}",)
    case "jpg":
        print(f"image/jpeg")
    case "pdf" | "zip":
        print(f"application/{file[-1]}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")