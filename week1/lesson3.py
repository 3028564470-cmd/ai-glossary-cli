ai_glossary = {
    "大模型": "能理解和生成文本、图片、代码等内容的模型。",
    "提示词": "给大模型的任务说明或问题。",
    "向量数据库": "用于存储和检索文本向量的数据库。",
    "RAG": "先从资料中检索信息，再让大模型回答问题的方法。",
    "Agent": "能调用工具、分步骤完成任务的 AI 程序。",
    "Python": "一种语法简洁、适合 AI 开发的编程语言。",
    "API": "应用程序编程接口，允许不同软件之间进行交互。"
}

def explain_term(term):
    if term in ai_glossary:
        print(f"\n{term}：{ai_glossary[term]}\n")
    elif term == "":
        print("\n请输入一个有效的 AI 术语。\n")
    elif term == "全部":
        print("目前收录的术语:")
        for item in ai_glossary:
            print(item)
    else:
        print(f"\n暂时没有找到“{term}”的解释。\n")

print("欢迎使用 AI 术语小词典！")
print("输入“退出”可以结束程序。")

while True:
    input_term = input("请输入想查询的术语：").strip()

    if input_term == "退出":
        print("学习加油，再见！")
        break

    explain_term(input_term)