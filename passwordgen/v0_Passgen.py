def password_generator(length: int = 12, has_punc: bool = True) -> str:
    """generate password."""
    from random import choices
    from string import digits, ascii_letters

    letters: str = digits + ascii_letters
    if has_punc:
        from string import punctuation

        letters += punctuation

    return "".join(choices(letters, k=length))


def y_n_question(prompt: str) -> bool:
    """keep asking a closed question until getting an answer of "y" or "n".\n
    return True if the answer is "y", otherwise return False."""
    while 1:
        if (ans := input(prompt + " y/n >>> ")) in ("y", "Y"):
            return True
        elif ans in ("n", "N"):
            return False
        else:
            print("Invalid answer. Answer with 'y' or 'n'.")


def make_str_bool(string: str) -> bool:
    """make string into boolean value."""
    falses: list = ["0", "false", "False", "f", "F", ""]

    if string in falses:
        return False
    return True


def save_password(
    site: str,
    user_id: str,
    password: str,
    filepath: str = ".\\",
    filename: str = "passwords",
) -> None:
    """save the given $password with its $site and $user_id to the $filepath as a json file named $filename."""
    from json import load, dump

    # load json
    with open(filepath + f"{filename}.json", "r", encoding="utf-8") as f:
        password_dict: dict = load(f)

    # TODO check if the site exists
    # site_already_exists: bool = False
    # try:
    #     if password_dict[site]:
    #         site_already_exists = True
    # except KeyError:
    #     pass

    # chcek if the data is already saved
    try:
        if password_dict[site][user_id]:
            # ask whether to overwrite or not
            prompt: str = f"There is already a password for {user_id} at {site}.\nDo you want to overwrite it?"
            if not y_n_question(prompt):
                # when replied with 'y', do nothing and the finally block will come into play.
                # otherwise, return None and abort this function.
                print("The password is not saved.")
                return None
            print(f"Password saved: at {site}; UID = {user_id}; PW = {password}")

    except KeyError:
        print(f"Password saved: at {site}; UID = {user_id}; PW = {password}")
        password_dict[site] = {user_id: password}

    finally:
        with open(filepath + f"{filename}.json", "w", encoding="utf-8") as f:
            dump(password_dict, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    from sys import argv

    stdin = list(argv)
    try:
        if stdin[3] == "AUTO":
            stdin[3] = password_generator(int(stdin[4]), make_str_bool(stdin[5]))
        save_password(stdin[1], stdin[2], stdin[3])

    except IndexError:
        print(
            "IndexError; Not enough arguments.",
            "Usage: py Passgen.py ${1:Site_name} ${2:UID} ${3:password} ${4:length} ${5:has_punc}",
            'Tips: Putting "AUTO" into the 3rd argument allows auto generation of password.',
        )
