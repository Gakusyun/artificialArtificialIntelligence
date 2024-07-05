import json


def ihys(str) -> str:
    str = str.replace("你好", "主人好")
    return str


def personal_pronoun(str) -> str:
    str = str.replace("我", "主人").replace("你", "")
    return str


def yiwfjv(str) -> str:
    str = str.replace("吗", "").replace("？", "")
    return str


def main():
    str = input(">>")
    str = ihys(str)
    str = personal_pronoun(str)
    str = yiwfjv(str)
    print(str)


if __name__ == "__main__":

    while True:
        main()
