import json, os


class Robot:
    name = "奴婢"
    relation = "智能助理"
    your_name = "主人"
    r18 = False

    def refresh(self, data):
        self.name = data["name"]
        self.relation = data["relation"]
        self.r18 = data["r18"]
        self.your_name = data["your_name"]

    def about(self):
        if self.r18:
            print(
                "我是"
                + self.name
                + ", 是"
                + self.your_name
                + "的"
                + self.relation
                + "。是永远的18岁哦！"
            )
        else:
            print(
                "我叫"
                + self.name
                + ", 是"
                + self.your_name
                + "的"
                + self.relation
                + "。人家还没成年呢！"
            )


def help():
    print("输入help查看帮助")
    print("输入about查看关于")
    print("输入setting修改设置")
    print("输入reload重新加载设置")
    print("输入exit退出")


def get_settings():
    name = input("请输入智能助理的名称：")
    relation = input("请输入" + name + "是你的什么:")
    your_name = input("请输入" + name + "称呼你为：")
    return {"name": name, "relation": relation, "r18": False, "your_name": your_name}


def r18on(robot):
    robot.r18 = True
    settings = {
        "name": robot.name,
        "relation": robot.relation,
        "r18": True,
        "your_name": robot.your_name,
    }
    with open("./settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False)
        f.close()


def r18off(robot):
    robot.r18 = False
    settings = {
        "name": robot.name,
        "relation": robot.relation,
        "r18": False,
        "your_name": robot.your_name,
    }
    with open("./settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False)
        f.close()


def setting(robot):
    settings = get_settings()
    robot.refresh(settings)
    with open("./settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False)
        f.close()


def reload(robot):
    with open("settings.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
        robot.refresh(data)


def check(text, robot):
    if text == "about":
        robot.about()
        return 1
    elif text == "help":
        help()
        return 1
    elif text == "r18on":
        r18on(robot)
        return 1
    elif text == "r18off":
        r18off(robot)
        return 1
    elif text == "setting":
        setting(robot)
        return 1
    elif text == "reload":
        reload(robot)
        return 1
    elif text == "exit":
        return -1
    else:
        return 0


def change(text, robot):
    text = text.replace("你好", "robot.your_name" + "好")
    text = text.replace("吗", "").replace("？", "！")
    if text.find(robot.name) == -1:
        text = text.replace("我", "robot.your_name").replace("你", "robot.name")
    else:
        text = (
            text.replace("我", "robot.name")
            .replace("你", "")
            .replace(robot.name, "robot.your_name")
            .replace(robot.your_name, "robot.name")
        )
    text = text.replace("robot.name", robot.name).replace(
        "robot.your_name", robot.your_name
    )
    return text


def main():
    robot = Robot()
    if os.path.isfile("./settings.json"):
        with open("settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()
            robot.refresh(data)
    else:
        settings = get_settings()
        with open("./settings.json", "w", encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False)
            f.close()
        robot.refresh(settings)
    while True:
        text = input(">>")
        flag = check(text, robot)
        if flag == -1:
            break
        elif flag == 1:
            continue
        text = change(text, robot)
        if not robot.r18:
            for word in ["做爱", "性奴", "自慰", "高潮", "撸管", "肏", "doi"]:
                if text.find(word) != -1:
                    print(robot.name + ": 这话我绝对不会说！")
                    is_r18 = True
            if is_r18:
                is_r18 = False
                continue
        print(robot.name + ": " + text)


if __name__ == "__main__":
    main()
