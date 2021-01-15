from file_cards_system import cards_tool

# 当前文件cards_main.py 是总控中心,负责调用各个功能业务函数
# 当前的文件不去实现具体的功能, 主要用来负责调用函数,
# 并提供当前整个项目程序的入口
# 1.导入工具包 ( 导入模块)
# 当下次启动名片管理系统时,把文件中的数据读取加载到名片列表中

cards_tool.load_file_to_cards()
# 对于重复次数不确定的代码, 使用死循环, 但是死循环中必须要有break退出
while True:
    # 2.使用工具包中的工具  模块名.变量名 / 模块名.函数名()
    cards_tool.show_menu()
    # 3.通过键盘获取用户的输入选择    4.根据用户的输入选择进行判断
    option = input("请输入您的选择:")
    # 5.如果用户输入 "1", 用户需要新建名片
    if option == "1":
        cards_tool.new_card()
    # 6.如果用户输入 "2", 用户需要显示全部
    elif option == "2":
        cards_tool.show_all()
    # 7.如果用户输入 "3", 用户需要查询名片
    elif option == "3":
        cards_tool.search_card()
    # 8.如果用户输入 "0", 用户需要退出名片系统
    elif option == "0":
        print("用户需要退出名片系统")
        # 当名片管理系统退出时, 把名片列表中的数据保存文件中
        cards_tool.save_data_to_file()
        print("欢迎使用名片管理系统, 大哥常来玩啊!")
        break
    # 9.如果用户输入的其它字符串, 提示用户输入有误, 请重新输
    else:
        print("您的输入有误,请核对后按照菜单提示重新输入!!!")
