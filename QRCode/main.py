import qrcode


def remove_http(arg: str) -> str:
    """remove https:// or http:// prefix from a string."""
    arg = arg.removeprefix("https://")
    arg = arg.removeprefix("http://")
    return arg


def convert_slashes(arg: str) -> str:
    """convert slashes in a string into a space."""
    arg = arg.replace("/", " ")
    arg = arg.replace("\\", " ")
    return arg


def trim(arg: str, max_len: int = 40) -> str:
    """trim a lengthy string if its length exceeded max_len which is by default 40."""
    if arg.__len__().__gt__(max_len):
        arg = arg[:max_len]
    return arg


def main():
    text = input("Enter a string to be converted into QR-Code.\n>>> ")
    text = remove_http(text)
    img = qrcode.make(text)

    text = convert_slashes(text)
    text = trim(text)
    img.save(f".\\{text}.png")


if __name__ == "__main__":
    main()
