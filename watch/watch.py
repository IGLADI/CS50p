import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'<iframe[^>]*src=["\'](https?://(?:www\.)?youtube\.com/embed/[\w-]+)["\']', s):
        video_id = re.search(r'https?://(?:www\.)?youtube\.com/embed/([\w-]+)', match.group(1)).group(1)
        youtu_be_url = f'https://youtu.be/{video_id}'
        return youtu_be_url
    else:
        return None


if __name__ == "__main__":
    main()