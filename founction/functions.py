# -*- coding:utf-8 -*-
import os
from tkinter import messagebox, END
from tkinter.filedialog import askopenfilenames, askdirectory
import pyminizip


# 选择文件夹中的文件，将其信息显示在Treeview中
def SelectFiles(tree, mw):
    mw.iconify()  # 最小化界面主窗口
    fnames = askopenfilenames()
    for i in range(0, len(fnames)):
        basename = os.path.basename(fnames[i])
        size = os.path.getsize(fnames[i])
        # 格式化输出
        if 0 < size < 1024 * 1024:
            size = "%(size).1f" % {'size': size / 1024} + " KB"
        elif size < 1024 * 1024 * 1024:
            size = "%(size).2f" % {'size': size / (1024 * 1024)} + " MB"
        else:
            size = "%(size).2f" % {'size': size / (1024 * 1024 * 1024)} + " GB"
        tree.insert("", "end", values=[basename, size, fnames[i]])


# 删除Treeview中选中的记录，可以单条，可以多条
def DeleteFilesFromTreeview(tree):
    selected_files = tree.selection()
    if selected_files == 0:
        return
    for i in range(0, len(selected_files)):
        tree.delete(selected_files[i])


# 浏览选择压缩文件的目的地址
def SelectDestinationDir(entry):
    entry.delete(0, END)
    pathname = askdirectory()
    # 目的文件夹 + 系统分隔符 + 默认文件名（用户可编辑）
    entry.insert(0, os.path.normpath(pathname) + os.path.sep + "default.zip")


def ZipFileBegin(tree, settings):
    children = tree.get_children()
    srcFileList = list()
    for c in children:
        srcFileList.append(tree.item(c)["values"][2])
    dstFilePath = settings[0].get()
    key = settings[2].get()
    keyAgain = settings[3].get()
    if keyAgain != key:
        messagebox.showerror('Σ(っ °Д °;)っ', '密码不一致，请重新输入！')
        return
    zipLevelStr = settings[1].get()
    # 选择压缩等级， 默认为正常压缩 3
    if zipLevelStr == "0-不压缩":
        zipLevel = 0
    elif zipLevelStr == "1-快速压缩":
        zipLevel = 3
    elif zipLevelStr == "2-正常压缩":
        zipLevel = 6
    else:
        zipLevel = 9
    messagebox.showinfo("￣へ￣", "压缩已经开始，请耐心等待...")
    pyminizip.compress_multiple(srcFileList, [], dstFilePath, key, zipLevel)
    srcFileSize = 0
    for file in srcFileList:
        srcFileSize += os.path.getsize(file)
    dstFileSize = os.path.getsize(dstFilePath)
    zipRate = "%(rate).4f" % {'rate': (dstFileSize / srcFileSize) * 100} + "%"
    messagebox.showinfo("o(*￣▽￣*)ブ",
                        "压缩成功！！！\n压缩前文件大小: %s B\n压缩后文件大小: %s B\n压缩率为: %s"
                        % (srcFileSize, dstFileSize, zipRate))


# 点击取消按钮返回主界面
def CancelZip(mainwindow):
    mainwindow.deiconify()
