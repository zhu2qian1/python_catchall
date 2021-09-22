from typing import KeysView
from v0_Passgen import password_generator
from v0_Passgen import y_n_question
from v0_Passgen import make_str_bool


class PasswordBook:
    def __init__(self, dct: dict) -> None:
        """An alias of json for managing passwords.

        Args:
            dct (dict): a dictionary to load. must be {{{}}} (dict in dict in dict).

        Raises:
            TypeError: if dct != type(dict), TypeError will be raised.

        Returns:
            None
        """
        if type(dct) != dict:
            raise TypeError

        self.book: dict = dct
        self.sites: KeysView = self.book.keys()
        return None

    def refresh_keysview(self) -> None:
        """refresh KeysView."""
        self.sites: KeysView = self.book.keys()

    def register(self, site: str, user_id: str, password: str, forced=False) -> None:
        """register password with its user ID and site.

        Args:
            site (str): the site where the password is used
            user_id (str): the user id with which the password is used
            password (str): the password to register
            forced (bool, optional): whether the password will be saved forcibly. Defaults to False.

        Returns:
            None
        """

        ppt: str = f"The password for {user_id} in {site} already exist. Do you want to overwrite it?"

        if (not forced) and (self.is_duplicated(site, user_id)):
            if y_n_question(ppt):
                self.register(site, user_id, password, forced=True)
            else:
                print("Password is not saved.")
            return None

        try:
            self.book[site] |= {user_id: password}
        except KeyError:
            self.book.__setitem__(site, {user_id: password})

        print(f"PW registered: SITE = {site}; UID = {user_id}; PW = {password}")
        self.refresh_keysview()

    def is_duplicated(self, site: str, user_id: str) -> bool:
        # not in にしているのは2回目のチェックでKeyErrorを送出する前にリターンしたいから
        # check if {site} already exists in self.sites
        if site not in self.sites:
            return False
        # check if {user_id} in self.book[site]
        if user_id not in self.book[site]:
            return False
        return True


def input_int(prompt: str, ask_again=True) -> int:
    """Evaluate input as an integer.

    Args:
        prompt (str): the prompt.
        ask_again (bool, optional): Whether ask again when invalid answer was given. Defaults to True.

    Returns:
        int: evaluated input as an integer
    """
    while 1:
        try:
            return int(input(prompt))
        except ValueError as e:
            if ask_again:
                print("Integer must be input.")
                continue
            raise e


def load_password_book(filename: str, encoding="utf-8") -> PasswordBook:
    from json import load

    with open(filename, "r", encoding=encoding) as f:
        l: dict = load(f)
    return PasswordBook(l)


def save_password_book(
    pwbook: PasswordBook, filename: str, encoding="utf-8", ensure_ascii=False, indent=2
) -> None:
    from json import dump

    with open(filename, "w", encoding=encoding) as f:
        dump(pwbook.book, f, ensure_ascii=ensure_ascii, indent=indent)
    return None


def save_password(
    site: str,
    user_id: str,
    password: str,
    filepath: str = ".\\",
    filename: str = "passwords",
) -> None:
    filename: str = filepath + f"{filename}.json"

    json_passwords: PasswordBook = load_password_book(filename)
    json_passwords.register(site, user_id, password)
    save_password_book(json_passwords, filename)

    return None


def add_entry():
    site: str = input("Site: ")
    user_id: str = input("User ID: ")
    password: str = input("Password. Type AUTO to generate password: ")
    if password == "AUTO":
        length: int = input_int("Length of password (int): ")
        has_punc: bool = make_str_bool(input("Password has punc? T/F: "))
        password = password_generator(length, has_punc)

    save_password(site, user_id, password)


def browse():
    if input("filepath? >>> ") == "":
        filepath = ".//passwords.json"
    json_passwords: PasswordBook = load_password_book(filepath)
    while 1:
        if (stdin := input("site? >>> ")) == "q":
            break
        elif stdin not in json_passwords.sites:
            print(f"sites: {json_passwords.sites}")
        else:
            print(json_passwords.book[stdin])


def main() -> None:
    commands = {
        "add entry": add_entry,
        "browse": browse,
        "exit": exit,
        "q": quit,
    }

    while 1:
        try:
            commands[input("command? >>> ")]()
        except KeyError:
            print(f"commands: {set(commands.keys())}")


if __name__ == "__main__":
    main()
