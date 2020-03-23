from tkinter import *
from tkinter.ttk import Treeview, Combobox
from founction.functions import *

# 压缩设置窗口大小
SETTING_WID_WIDTH, SETTING_WID_HEIGHT = 800, 700


##############
## 设置窗口 ##
##############

class ZipSettingWindow:
    def __init__(self, mainwin):
        super().__init__()
        self.master = mainwin
        self.top = Toplevel(mainwin)
        self.top.title("新建压缩文件")
        self.top.attributes('-topmost', 1)
        nScreenWid, nScreenHei = self.top.maxsize()
        self.top.geometry("{}x{}+{}+{}".format(SETTING_WID_WIDTH, SETTING_WID_HEIGHT,
                                               (nScreenWid - 800) // 2, (nScreenHei - 700) // 2))
        self.top.resizable(width=False, height=False)

    # 选择文件部分
    def SelectFilePart(self):
        # 标签一：添加文件到压缩文件
        Label(self.top, text="添加文件到压缩文件",
              font=("YaHei", 10, "bold"), bg="black", fg="white").grid(row=0, column=0, sticky=W)
        # 生成文件选择表格的容器
        frame1 = Frame(self.top)
        frame1.grid(row=1, column=0, sticky='w')  # sticky='w'指定了组件在单元格中靠左对齐
        # 滚动条
        scrollBar = Scrollbar(frame1)
        scrollBar.pack(side=RIGHT, fill=Y)
        # 文件选择表格
        columns = ("文件名", "文件大小", "文件夹路径")
        treeview = Treeview(frame1, height=18, show="headings",
                            columns=columns, yscrollcommand=scrollBar.set)
        # 设置每列宽度和对齐方式
        treeview.column("文件名", width=200, anchor='center')
        treeview.column("文件大小", width=200, anchor='center')
        treeview.column("文件夹路径", width=380, anchor='center')
        # 设置每列表头标题文本
        treeview.heading("文件名", text="文件名")
        treeview.heading("文件大小", text="文件大小")
        treeview.heading("文件夹路径", text="文件夹路径")
        treeview.pack()
        # Treeview组件与垂直滚动条结合
        scrollBar.config(command=treeview.yview)
        # 添加与删除按钮
        deleteButton = Button(frame1, text="删除",
                              bg='white', fg='black', width='10', activeforeground='black',
                              activebackground='LightSkyBlue',
                              cursor='hand2', anchor='s', compound="center",
                              command=lambda: DeleteFilesFromTreeview(treeview))
        deleteButton.pack(side=RIGHT, padx=5)
        addButton = Button(frame1, text="添加",
                           bg='white', fg='black', width='10',
                           activeforeground='black', activebackground='LightSkyBlue',
                           cursor='hand2', anchor='s', compound="center",
                           command=lambda: SelectFiles(treeview, self.master))
        addButton.pack(side=RIGHT)
        return treeview

    def SettingPart(self):
        # 生成压缩设置的容器
        frame2 = Frame(self.top)
        frame2.grid(row=2, column=0, sticky='w')  # sticky='w'指定了组件在单元格中靠左对齐
        # 标签二：压缩文件设置
        Label(frame2, text="压缩文件设置",
              font=("YaHei", 10, "bold"), bg="black", fg="white").grid(row=1, column=0)
        # 输入压缩后文件路径
        Label(frame2, text="文件名", font="YaHei, 10").grid(row=2, column=0)
        entry1 = Entry(frame2, width=80, bg="white", fg="black")
        entry1.insert(0, os.path.abspath(os.sep)+"default.zip")   # 设置默认的压缩后路径
        entry1.grid(row=2, column=1)
        # 浏览选择压缩后文件路径按钮
        selectDestDirButton = Button(frame2, text="浏览...",
                                     bg='white', fg='black', width='10',
                                     activeforeground='black', activebackground='LightSkyBlue',
                                     cursor='hand2', anchor='s', compound="center",
                                     command=lambda: SelectDestinationDir(entry1))
        selectDestDirButton.grid(row=2, column=2, padx=44)
        # 压缩文件保存类型
        Label(frame2, text="保存类型", font="YaHei, 10").grid(row=3, column=0)
        # 保存类型下拉选择菜单
        zipType = StringVar()  # 窗体自带的文本，新建一个值
        typeChoices = Combobox(frame2, width=12, textvariable=zipType)
        typeChoices['values'] = ('zip', '7z', 'tar')  # 设置下拉列表的值
        typeChoices.grid(row=3, column=1, sticky=NW)
        typeChoices.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        # 压缩级别
        Label(frame2, text="压缩级别", font="YaHei, 10").grid(row=4, column=0)
        zipLevel = StringVar()
        zipLevelChoices = Combobox(frame2, width=12, textvariable=zipLevel)
        zipLevelChoices['values'] = ("0-不压缩", "1-快速压缩", "2-正常压缩", "3-最大压缩")  # 设置下拉列表的值
        zipLevelChoices.grid(row=4, column=1, sticky=NW, pady=5)
        zipLevelChoices.current(2)  # 默认为正常压缩
        # 输入密码
        frame3 = Frame(self.top)
        frame3.grid(row=5, column=0, sticky='w')

        # 当勾选“显示密码”时，明文展示密码
        def ShowKey():
            if keyCheck.get() == 1:
                keyLabel.config(text=sv1.get())
                entryAgainKey.config(state=DISABLED)
            else:
                keyLabel.config(text="")
                entryKey.config(show='*')
                entryAgainKey.config(state=NORMAL)

        # 当勾选“输入密码”时允许输入密码
        def EntryKey():
            if check.get() == 1:
                entryKey.config(state=NORMAL)
                entryAgainKey.config(state=NORMAL)
                showKeyCheckButton.config(state=NORMAL, command=ShowKey)
            else:
                entryKey.config(state=DISABLED)
                entryAgainKey.config(state=DISABLED)
                showKeyCheckButton.config(state=DISABLED)

        # 密码输入验证，密码要求为ASCII码(十六进制20-7E)，即ASCII中可显示字符部份
        def validateKey(key):
            # 如果之前有非法字符，则在再次验证时把输入密码有误的信息去掉
            keyLabel.config(text="")
            pattern = re.compile('[\u0020-\u007E]*')
            match = pattern.fullmatch(key)
            if match is None:
                return False
            return True

        # 密码格式不正确后的处理
        def invalid():
            # 之前如果有不一致提示，则在下次验证时把错误信息去掉
            keyLabel.config(text="")
            # 清空输入框
            entryKey.delete(0, END)
            entryAgainKey.delete(0, END)
            # 错误提示文本
            keyLabel.config(text="密码含有非法字符")

        # # 密码不一致后的处理
        # def KeyInvalid():
        #     # 清空确认密码框
        #     entryAgainKey.delete(0, END)
        #     # 错误提示文本
        #     keyLabel.config(text="密码不一致，请重新输入")
        #
        # # 密码一致性检验
        # def validateKeyAgain():
        #     if len(sv2.get()) != 0 and sv2.get() != sv1.get():
        #         return False
        #     else:
        #         return True

        check = IntVar()
        entryKeyCheckButton = Checkbutton(
            frame3, text="输入密码", font="YaHei, 10",
            variable=check)
        entryKeyCheckButton.grid(row=5, column=0, sticky=NW)
        # 创建密码输入框和确认密码框
        sv1 = StringVar()
        sv2 = StringVar()
        entryKey = Entry(frame3, width=20, bg="white", fg="black",
                         show='*', state=DISABLED, textvariable=sv1,  # 初始状态设为不可用
                         validate="focusout",  # validate密码格式验证在该输入框失去焦点后
                         invalidcommand=invalid,  # 密码格式不正确即validatecommand返回False时调用invalid
                         validatecommand=(self.top.register(validateKey), '%P'))  # 密码格式验证函数，这里只需验证第一个输入框即可
        entryKey.grid(row=5, column=1, padx=10)
        Label(frame3, text="再次输入密码", font="YaHei, 10").grid(row=5, column=2)
        entryAgainKey = Entry(frame3, width=20, bg="white", fg="black",
                              show='*', state=DISABLED, textvariable=sv2)
        entryAgainKey.grid(row=5, column=3)
        entryKeyCheckButton.config(command=EntryKey)
        # 创建“显示密码”复选框
        keyCheck = IntVar()
        showKeyCheckButton = Checkbutton(frame3, text="显示密码", font="YaHei, 10",
                                         variable=keyCheck, state=DISABLED)
        showKeyCheckButton.grid(row=5, column=4)
        # 创建密码Label(无奈之举，Entry的show的配置如果在开始设为'*'，后面就改不了文本明文显示了，找了很多资料，没有这一项设置)
        keyLabel = Label(frame3, font="YaHei, 10", fg="red")
        keyLabel.grid(row=5, column=5)
        Label(frame3, text="    ").grid(row=6)
        # 压缩目的路径，压缩等级， 密码
        return [entry1, zipLevelChoices, entryKey, entryAgainKey]

    def BeginPart(self, tree, settings):
        frame = Frame(self.top)
        frame.grid(row=7, column=0, sticky='w')
        # 标签三：开始压缩
        Label(frame, text="开始压缩",
              font=("YaHei", 10, "bold"), bg="black", fg="white").grid(row=7, column=0, sticky='w')
        beginButton = Button(frame, text="开始",
                             bg='white', fg='black', width=10,
                             activeforeground='black', activebackground='LightSkyBlue',
                             cursor='hand2', anchor='s', compound="center",
                             command=lambda: ZipFileBegin(tree, settings))
        beginButton.grid(row=8, column=1, padx=160)
        cancelButton = Button(frame, text="取消",
                              bg='white', fg='black', width=10,
                              activeforeground='black', activebackground='LightSkyBlue',
                              cursor='hand2', anchor='s', compound="center",
                              command=CancelZip(self.master))
        cancelButton.grid(row=8, column=2)
        Label(self.top, text="   ").grid(row=9)  # 获得一个空行
        Label(self.top, text="copyright@lihui BY-NC-SA", font=("YaHei", 12, "bold")).grid(row=10, column=0, padx=250)

    def show(self):
        tree = self.SelectFilePart()
        settings = self.SettingPart()
        self.BeginPart(tree, settings)
