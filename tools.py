import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import threading
import sys


def install_pyinstaller():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        messagebox.showinfo("安装成功", "PyInstaller 安装成功！")
    except Exception as e:
        messagebox.showerror("安装失败", str(e))


def async_install_pyinstaller():
    threading.Thread(target=install_pyinstaller).start()


def package_script():
    script_path = filedialog.askopenfilename(title="选择Python脚本", filetypes=[("Python", "*.py")])
    if not script_path:
        return
    script_dir = os.path.dirname(script_path)

    cmd = ["pyinstaller", "--onefile", "--noconsole", "--distpath", script_dir, script_path]

    try:
        subprocess.run(cmd, shell=True, check=True)
        messagebox.showinfo("完成", f"打包完成！\n输出目录: {script_dir}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("打包失败", str(e))


def create_gui():
    window = tk.Tk()
    window.title("PyInstaller打包程序")
    window.geometry("400x250")

    package_button = tk.Button(window, text="选择Python脚本并打包", command=package_script)
    package_button.pack(pady=20)

    install_button = tk.Button(window, text="安装PyInstaller", command=async_install_pyinstaller)
    install_button.pack(pady=20)

    return window


if __name__ == "__main__":
    window = create_gui()
    window.mainloop()
