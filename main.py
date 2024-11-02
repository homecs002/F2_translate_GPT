import tkinter as tk
import pyperclip
import keyboard
import sys
import ctypes
import pyautogui

sys.path.append("..")
sys.path.append(".")

from GPT_models.zhipu import call_zhipu_api

def on_f2_press():
    # 模拟Ctrl+C操作以复制选中文本
    pyautogui.hotkey('ctrl', 'c')
    
    # 从剪贴板获取文本
    selected_text = pyperclip.paste()
    print(f'翻译的文本：{selected_text}')
    # 调用GPT API
    generated_content = call_zhipu_api(selected_text)
    
    # 显示内容
    show_floating_window(generated_content)

def show_floating_window(content):
    # 定义POINT结构
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    pt = POINT()
    # 获取鼠标位置
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))

    # 创建悬浮窗口
    root = tk.Tk()
    root.title("GPT Output")
    
    # 设置窗口位置和置顶
    root.geometry(f"+{pt.x}+{pt.y}")
    root.attributes("-topmost", True)

    label = tk.Label(root, text=content, wraplength=300)
    label.pack()
    root.mainloop()

# keyboard.add_hotkey('f2', on_f2_press)

# # 运行主循环
# keyboard.wait('esc')

if __name__ == "__main__":
    print("已经启动！")

    while (1):
        if keyboard.is_pressed('f2'):
            on_f2_press()
            keyboard.wait('f2', suppress=False)
        # keyboard.add_hotkey('f2', on_f2_press)