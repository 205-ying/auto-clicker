import time
import threading
import keyboard
import pyautogui
from utils import get_click_interval, get_click_count

clicking = False  # 全局变量，表示是否正在点击

def click_mouse(interval, count):
    """执行鼠标点击操作"""
    global clicking
    for _ in range(count):
        if not clicking:
            break  # 如果点击被停止，则跳出循环
        pyautogui.click()  # 执行一次鼠标点击
        time.sleep(interval)  # 等待指定的间隔时间

def start_clicking():
    """开始点击操作"""
    global clicking
    clicking = True
    interval = get_click_interval()  # 获取点击间隔
    count = get_click_count()  # 获取点击次数
    click_mouse(interval, count)  # 执行点击操作
    clicking = False  # 点击操作结束

def stop_clicking():
    """停止点击操作"""
    global clicking
    clicking = False

if __name__ == "__main__":
    print("按 's' 开始点击，按 'e' 停止点击。")
    keyboard.add_hotkey('s', start_clicking)  # 绑定 's' 键开始点击
    keyboard.add_hotkey('e', stop_clicking)  # 绑定 'e' 键停止点击
    keyboard.wait('esc')  # 按 'esc' 退出程序