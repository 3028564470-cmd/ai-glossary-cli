from datetime import datetime
def add_record():
    content = input("今天学习了什么？").strip()

    if content == "":
        print("学习内容不能为空。")
        return

    while True:
        hours_text = input("今天学习了多少小时？").strip()

        try:
            hours = float(hours_text)

            if hours <= 0:
                print("学习时长必须大于 0。")
                continue

            break

        except ValueError:
            print("请输入数字，例如 2 或 1.5。")

    date = datetime.now().strftime("%Y-%m-%d")
    record = f"{date} | {hours} 小时 | {content}"

    with open("study_records.txt", "a", encoding="utf-8") as file:
        file.write(record + "\n")

    print("学习记录已保存！")


def view_records():
    try:
        with open("study_records.txt", "r", encoding="utf-8") as file:
            records = file.readlines()

        if len(records) == 0:
            print("目前还没有学习记录。")
            return

        print("\n你的学习记录：")
        for index, record in enumerate(records, start=1):
            print(f"{index}. {record.strip()}")

    except FileNotFoundError:
        print("目前还没有学习记录，请先添加一条。")
def show_total_hours():
    try:
        with open("study_records.txt", "r", encoding="utf-8") as file:
            records = file.readlines()
        total_hours = 0.0
        for record in records:
            if "|" not in record:
                continue
            hours_part = record.split("|")[1].strip()
            hours = float(hours_part.replace("小时", ""))
            total_hours += hours
        print(f"\n你总共学习了 {total_hours} 小时。")

    except FileNotFoundError:
        print("目前还没有学习记录，请先添加一条。")


print("欢迎使用 AI 学习记录工具！")

while True:
    print("\n1. 添加学习记录")
    print("2. 查看学习记录")
    print("3. 学习时长统计")
    print("4. 退出")
    choice = input("请选择功能（1/2/3/4）：").strip()

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        show_total_hours()
    elif choice == "4":
        print("学习加油，再见！")
        break
    else:
        print("输入无效，请输入 1、2、3 或 4。")