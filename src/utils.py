def get_click_interval():
    """获取用户输入的点击间隔（秒）"""
    while True:
        try:
            interval = float(input("请输入点击间隔（秒）："))
            if interval > 0:
                return interval
            else:
                print("请输入一个正数。")
        except ValueError:
            print("无效输入，请输入一个数字。")

def get_click_count():
    """获取用户输入的点击次数"""
    while True:
        try:
            count = int(input("请输入点击次数（输入0表示无限点击）："))
            return count
        except ValueError:
            print("无效输入，请输入一个整数。")