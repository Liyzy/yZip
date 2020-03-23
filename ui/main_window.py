from tkinter import *
from tkinter import messagebox

from ui.setting_window import ZipSettingWindow

# 主窗口大小
WID_WIDTH, WID_HEIGHT = 850, 500


def NewFile(window):
    NewZipSettingWindow(window)


def OpenFile():
    print("打开文件")


def About():
    messagebox.showinfo("*^____^*", "这是由李辉完成的python项目，界面设置由tkinter完成，带密码压缩功能由pyminizip完成。")


# 创建新建压缩文件窗口
def NewZipSettingWindow(window):
    zw = ZipSettingWindow(window)
    zw.show()


############
## 主窗口 ##
############
class MainWindow:
    def __init__(self, rt):
        # 禁止窗口最大化
        rt.resizable(False, False)

        # 窗口标题
        rt.title("yZip 1.8.11")

        # 窗口背景颜色
        rt.configure(background='RoyalBlue')

        # 按钮上使用图片
        image_open_file = PhotoImage(file=r"D:\Program Files\python\PycharmProjects\yZip\source\img\open.gif")
        image_new_zip_file = PhotoImage(file=r"D:\Program Files\python\PycharmProjects\yZip\source\img\zipfile.gif")

        # 新建与打开按钮
        button_openfile = Button(rt)
        button_openfile.config(text="打开压缩文件",
                               bg='white', fg='black',  # fg是前面的字体的颜色，bg是背景的颜色
                               activeforeground='black', activebackground='LightSkyBlue',  # 当按钮被点击时所使用的颜色
                               cursor='hand2',  # button上光标样式
                               anchor='s',  # 控制按钮上内容的位置。使用n, ne, e, se, s, sw, w, nw, or center这些值之一。默认值是center
                               image=image_open_file, compound="top")
        button_openfile.image = image_open_file  # keep a reference
        button_openfile.pack(padx=185, side=LEFT)
        x = button_openfile.winfo_reqwidth()

        button_new_zipfile = Button(rt)
        button_new_zipfile.config(text="新建压缩文件",
                                  bg='white', fg='black',
                                  activeforeground='black', activebackground='LightSkyBlue',
                                  cursor='hand2',  # button上光标样式
                                  anchor='s',
                                  image=image_new_zip_file, compound="top", command=lambda: NewZipSettingWindow(rt))
        button_new_zipfile.image = image_new_zip_file  # keep a reference
        button_new_zipfile.pack(side=LEFT)

        # 窗口置顶
        rt.wm_attributes('-topmost', 1)

        # 菜单选项
        menu = Menu(rt)
        rt.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="文件", menu=filemenu)
        filemenu.add_command(label="新建", command=lambda: NewFile(rt))
        filemenu.add_command(label="打开文件", command=OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=rt.quit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="帮助", menu=helpmenu)
        helpmenu.add_command(label="关于", command=About)

        # 设置窗口居中显示
        # maxsize()获得当前显示器分辨率
        nScreenWid, nScreenHei = rt.maxsize()
        # {}x{}设置窗口初始大小，如果没有这个设置，窗口会随着组件大小的变化而变化;{}+{}表示窗口距离屏幕左上角的位置
        rt.geometry("{}x{}+{}+{}".format(WID_WIDTH, WID_HEIGHT,
                                         (nScreenWid - WID_WIDTH) // 2, (nScreenHei - WID_HEIGHT) // 2))
