# 当前文件cards_tool.py文件, 主要用来实现各个业务功能函数的,
# 当前文件中不会去调用函数, 仅仅是封装了实现业务功能的函数
# 实现封装: 菜单显示  新建名片 显示全部名片  查询名片 修改名片  删除名片 返回上一级

import os

# 名片管理系统中的数据结构
# 一个名片信息就是一个人物的详细信息, 使用字典来保存
# 多个名片信息就用多个字典来保存
# 多个字典都保存到列表中, 因为列表提供了非常丰富的增删改查操作
# 定义全局变量 名片列表 (空列表)
#   [{},{},{},{}]
cards_list = [
    # { "name": "小明", "phone": "10086", "qq": "12345", "email": "xm@qq.com"},
    # { "name": "小红", "phone": "10080", "qq": "23456", "email": "xh@qq.com"},
    # { "name": "小张", "phone": "10090", "qq": "54321", "email": "xz@qq.com"},
    # { "name": "小王", "phone": "10070", "qq": "55521", "email": "xw@qq.com"}
]


# 1.定义 显示菜单功能函数
def show_menu():
    """
    当前函数show_menu实现了 显示菜单功能
    :return:
    """
    print()
    print()
    print("*" * 50)
    print("欢迎使用 [名片管理系统] v1.0")
    print()
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print()
    print("0. 退出系统")
    print("*" * 50)


# 2.定义 新建名片功能函数
def new_card():
    """
    当前函数new_card 实现了新建名片功能
    :return:
    """
    # pass 就是一个占位符, 作用: 起到完善语法结构的作用
    # pass
    print("[功能] 新建名片")
    # ①.通过键盘获取用户的输入信息
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入QQ号:")
    email_str = input("请输入邮箱:")
    # ②.将获取的输入信息保存到字典中
    new_dict = {
        'name': name_str,
        'phone': phone_str,
        'qq': qq_str,
        'email': email_str
    }
    # ③.将新建的字典保存到名片列表中
    cards_list.append(new_dict)
    # ④.打印新建 新建名片成功
    print("新建姓名是:%s 的名片成功!!!" % name_str)
    # print("名片列表cards_list:", cards_list)


# 3.定义 显示全部功能函数
def show_all():
    """
    当前函数show_all实现了 显示全部的功能
    :return:
    """
    # ... 与 pass相同,  就是一个占位符, 作用: 起到完善语法结构的作用
    # ...
    # TODO (张三 2020/04/08)当前函数show_all显示全部的功能 待完成
    print("[功能] 显示全部名片")
    # 0.判断名片列表是否有数据, 如果没有数据,提示用户新建名片, 代码不再向下执行,让函数提前终止执行
    if len(cards_list) <= 0:
        print("当前名片列表中没有数据, 请新建名片!")
        # 代码不再向下执行,让函数提前终止执行
        return
    # ①.按照格式打印表头的信息
    print("-" * 50)  # 如果大家的windows系统显示对不起, 将后面三个 显示宽度10改为8
    print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10), sep="\t\t")
    print("-" * 50)
    # ②.按照格式打印表格中的数据(名片列表中的信息)
    for item in cards_list:
        # 临时变量item获取的是列表中的一个一个字典
        # print(item)
        # 那就可以通过字典的键 获取对应的value值
        print(item.get('name').ljust(10), item.get('phone').ljust(10),
              item.get('qq').ljust(10), item.get('email').ljust(10), sep="\t\t")


# 4.定义 查询名片功能函数
def search_card():
    """
    当前函数search_card 实现了 查询名片功能
    :return:
    """
    # pass
    # TODO (张三 2020/04/08)当前函数 search_card  查询名片功能 还没有完成, 需要完成
    print("[功能] 查询名片")
    # ①.先获取用户要查询的姓名
    find_name = input("请输入你要查询的姓名:")
    # ②.拿着要查询的姓名到名片列表中查找
    for item in cards_list:
        # 临时变量item获取的是列表中的一个一个字典
        # print(item )
        # 那就可以通过字典的键 获取对应的value值
        # ③.如果找到指定姓名的信息, 按照格式打印表头, 再打印表格中的数据, 已经找到了,就不需要继续向下查找了
        if item.get('name') == find_name:
            print("已经找到姓名是:%s 的信息了" % find_name)
            # 打印表头
            print("-" * 50)
            print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10), sep="\t\t")
            print("-" * 50)
            # 打印表格中的数据
            print(item.get('name').ljust(10), item.get('phone').ljust(10),
                  item.get('qq').ljust(10), item.get('email').ljust(10), sep="\t\t")
            print("-" * 50)
            # 当查询到指定姓名的名片后, 需要对当前的名片进行操作, 对名片的操作选择封装成函数
            # print("item:",item)
            deal_card(item)  # item是当前要操作的字典
            # 已经找到了, 就不需要继续向下查找了
            break
    # ④.如果整个名片列表都遍历完了,也没有找到要查询的姓名,要给用户一个提示
    else:
        print("没有找到姓名是:%s 的信息, 请核对后重新输入!!!" % find_name)


# 5.定义对名片的操作函数
def deal_card(find_dict):  # find_dict 是形参,是当前查询到的字典, 需要操作的字典
    """
    当前函数deal_card实现了对查询到的名片进行操作, 包括:修改, 删除,返回上一级
    :return:
    """
    # print("find_dict:", find_dict)

    # ①.先获取用户对查询到的名片操作选择
    action = input("请输入对名片的操作选择[1.修改  2.删除  0.返回上一级]:")
    # ②.根据用户的输入选择进行条件判断

    # ③.如果用户输入 "1", 用户需要修改名片
    if action == "1":
        print("[功能] 修改名片")
        # i.获取用户修改后的姓名,电话,QQ号,邮箱, 保存到变量中
        # modify_name  = input("请输入修改后的姓名:")
        # modify_phone = input("请输入修改后的电话:")
        # modify_qq    = input("请输入修改后的QQ号:")
        # modify_email = input("请输入修改后的邮箱:")
        # # ii.将获取的信息更新到当前字典的键对应的value值
        # find_dict['name']  = modify_name
        # find_dict['phone'] = modify_phone
        # find_dict['qq']    = modify_qq
        # find_dict['email'] = modify_email
        # 简化代码
        # find_dict['name']  = input("请输入修改后的姓名:")
        # find_dict['phone'] = input("请输入修改后的电话:")
        # find_dict['qq']    = input("请输入修改后的QQ号:")
        # find_dict['email'] = input("请输入修改后的邮箱:")

        # 高级操作部分
        find_dict['name'] = input_card_info("请输入修改后的姓名[不修改直接回车]:", find_dict.get('name'))
        find_dict['phone'] = input_card_info("请输入修改后的电话[不修改直接回车]:", find_dict.get('phone'))
        find_dict['qq'] = input_card_info("请输入修改后的QQ号[不修改直接回车]:", find_dict.get('qq'))
        find_dict['email'] = input_card_info("请输入修改后的邮箱[不修改直接回车]:", find_dict.get('email'))
        # iii. 修改名片成功
        print("修改名片成功!!!")
    # ④.如果用户输入 "2", 用户需要删除名片
    elif action == "2":
        print("[功能] 删除名片")
        # i.使用名片列表的remove()方法删除, 删除当前查询到人物的字典
        cards_list.remove(find_dict)
        # ii.打印删除名片成功
        print("删除名片成功!")
        print("删除姓名是:%s的名片成功了" % find_dict['name'])
    # ⑤.如果用户输入 "0", 用户需要返回上一级
    elif action == "0":
        print("[功能] 返回上一级")
        # 让函数体提前终止运行使用
        return
    # ⑥.如果用户输入其它字符, 提示输入有误
    else:
        print("您的输入有误,请按照提示重新输入!!!")


# 6.定义函数  对input()函数的功能扩展
def input_card_info(msg, value):
    """
    实现_input()函数的功能扩展
    :param msg: 提示输入信息
    :param value: 字典的默认值
    :return:  按照判断的结果返回
    """
    # 当前的函数需要获取用户的输入信息
    info = input(msg)
    # 如果用户没有输入信息,把传递过来的 字典的默认值 直接返回
    if len(info) == 0:
        # print("当前用户没有输入信息--->>>%s<<<---" % info)
        return value
    # 如果用户有输入信息, 将输入的信息返回
    else:
        # print("当前用户有输入信息--->>>%s<<<---" % info)
        return info


# 7.定义函数  当名片管理系统退出时,把名片列表中的数据保存文件中( 文件是可以永久保存数据的)
def save_data_to_file():
    """
    当前函数实现了 把名片列表中的数据保存到文件中
    :return:
    """
    # ①.打开文件
    file = open("cards_data.txt", "w", encoding="utf-8")
    # ②.操作文件
    # 把名片列表中的数据保存到文件中
    # write只能写入字符串类型, 需要数据类型转换
    file.write(str(cards_list))
    # ③.关闭文件
    file.close()


# 8.定义函数  当下次启动名片管理系统时,把文件中的数据读取加载到名片列表中
def load_file_to_cards():
    """
    当前函数实现了, 把文件中的数据读取加载到名片列表中
    :return:
    """
    # (1).判断cards_data.txt 是否存在, 如果存在则可以读取
    if os.path.exists("cards_data.txt"):
        # ①.打开文件
        file = open("cards_data.txt", "r", encoding="utf-8")
        # ②.操作文件 (读取文件内容)
        text = file.read()
        # print(text)
        # print(type(text))
        # ③.关闭文件
        file.close()
        # ④.将读取的文件内容给全局变量(名片列表)
        # 注意: 在函数中修改全局变量, 需要global关键字声明
        global cards_list
        # 读取的文件的内容是字符串,需要把字符串两边的引号去除
        cards_list = eval(text)
    # (2).如果不存在cards_data.txt文件, 提示新建
    else:
        print("文件cards_data.txt不存在, 请新建文件!!!")
