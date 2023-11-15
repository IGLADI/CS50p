import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not (
        sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png"))
        and sys.argv[2].lower().endswith(sys.argv[1].lower().split(".")[-1])
    ):
        print("Both input and output files must be JPEG or PNG images.")
        sys.exit(1)
    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2]
        with Image.open("shirt.png") as t_shirt:
            size = t_shirt.size
            with Image.open(input_image) as input_img:
                input_img = ImageOps.fit(input_img, size)
                input_img.paste(t_shirt, (0, 0), t_shirt)
                input_img.save(output_image)


if __name__ == "__main__":
    main()
