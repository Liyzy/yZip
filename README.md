## tkinter控件使用图片问题
`_tkinter.TclError: couldn't recognize data in image file "xxx"`
参考[The Tkinter PhotoImage Class](http://effbot.org/tkinterbook/photoimage.htm)，PhotoImage for images in PGM, PPM, GIF and PNG formats. The latter is supported starting with Tk 8.6.想要使用其他类型的图片需要使用PIL(Python Imaging Library)处理。
首先安装Pillow
`pip install Pillow`
然后
```python
from PIL import Image, ImageTk
image = Image.open("you image path")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo # keep a reference!
label.pack()
```
## 设置窗口标题
```python
root.title("yZip 1.0.0") # 窗口标题
```

## 设置窗口居中显示
```python
# maxsize()获得当前显示器分辨率
nScreenWid, nScreenHei = root.maxsize()  
# 窗口应有大小，若使用winfo_width()则返回当前窗口大小，如果还未调用mainloop(),则返回0
nCurWid = root.winfo_reqwidth()  
nCurHeight = root.winfo_reqheight()
# {}x{}设置窗口初始大小，如果没有这个设置，窗口会随着组件大小的变化而变化;{}+{}表示窗口距离屏幕左上角的位置
root.geometry("{}x{}+{}+{}".format(nCurWid, nCurHeight, 
              (nScreenWid - nCurWid)//2, (nScreenHei - nCurHeight)//2))
```
## 设置窗口背景颜色
```python
root.configure(background='RoyalBlue')  # 窗口背景颜色
```
## 设置窗口置顶
```py
root.wm_attributes('-topmost', 1)
```
## 禁止窗口最大化
```python
root = Tk()
root.resizable(False, False)
```
## 创建下拉菜单Combobox
```python
# 下拉选择菜单
ziptype = StringVar()  # 窗体自带的文本，新建一个值
typeChoices = Combobox(frame2, width=12, textvariable=ziptype)
typeChoices['values'] = ('zip', '7z', 'tar')  # 设置下拉列表的值
typeChoices.grid(row=3, column=1, sticky=NW)
typeChoices.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
```
## 创建输入框Entry
```python
sv1 = StringVar()  # 可以使用sv1.get()获得输入框的内容，当在初始化时定义了textvariable=sv1

entryKey = Entry(frame3, width=20, bg="white", fg="black",
                 show='*', state=DISABLED, textvariable=sv1,  # 初始状态设为不可用
                 validate="focusout",  # validate密码格式验证在该输入框失去焦点后
                 invalidcommand=invalid,  # 密码格式不正确即validatecommand返回False时调用invalid
                 validatecommand=(self.top.register(validateKey), '%P'))  # 密码格式验证函数，这里只需验证第一个输入框即可
entryKey.grid(row=5, column=1, padx=10)
```
## 创建复选框Checkbutton
```python
check = IntVar()

def testCheckButton():
    print("var is " + str(check.get()))

c = Checkbutton(frame2, text="输入密码：", font="YaHei, 10",
                variable=check, command=testCheckButton)
c.grid(row=5, column=0, sticky=NW)
'''
check变量具有值0或者1
可以用check.get()获得check的值，即Checkbutton的状态（0为未勾选，1为勾选）
当初始时设置了variable=check
'''
```
## 事件绑定
```python
import tkinter
# 一般情况下的事件绑定
def handler():
    '''事件处理函数'''
    print ("handler")
 
 
if __name__=='__main__':
    root = tkinter.Tk()
    btn = tkinter.Button(text=u'按钮', command=handler)
    btn.pack()
    root.mainloop()
```
```python
import tkinter
# handler()函数需要参数的情况下使用lambda
def handler(a, b, c):
    '''事件处理函数'''
    print ("handler", a, b, c)
 
 
if __name__=='__main__':
    root = tkinter.Tk()
    btn = tkinter.Button(text=u'按钮', command=lambda : handler(a=1, b=2, c=3))
    btn.pack()
    root.mainloop()
```
## 创建消息框messagebox
```python
import tkinter
import tkinter.messagebox 

tkinter.messagebox.showinfo('提示', '明天有雨')       # 提示信息
tkinter.messagebox.showwarning('警告','木马文件')     # 警告信息
tkinter.messagebox.showerror('错误','密码不匹配')     # 错误信息
tkinter.messagebox.askokcancel('询问','继续?')           # 是否继续某操作
tkinter.messagebox.asktrycancel('询问','再次尝试?')      # 是否再次尝试某操作
tkinter.messagebox.askquestion('问题','你喜欢音乐么？')   # 询问一个 是/否 问题
tkinter.messagebox.askyesno('问题','你喜欢音乐么？')      # 询问一个 是/否 问题
```
## 画布工具Canvas
```python
canvas = tk.Canvas(root, bg='gray', height=200, width=100)
 
image_file = tk.PhotoImage(file='tkinter.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
 
x0, y0, x1, y1 = 20, 20, 40, 40
# 从坐标(20,20)到(40,40)画一条直线。
line = canvas.create_line(x0, y0, x1, y1)   
 
# 从0度到180度画一个扇形
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
 
# 创建一个矩形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)

# 创建一个填充色为red的圆
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
 
canvas.pack()
```
## 列表Treeview
```python
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
# 插入
def SelectFiles(treeview):
    fnames = askopenfilenames()
    for i in range(0, len(fnames)):
        basename = os.path.basename(fnames[i])
        size = os.path.getsize(fnames[i])
        treeview.insert("", "end", values=[basename, size, fnames[i]])
# 删除选中条目
def DeleteFilesFromTreeview(treeview):
    selected_files = treeview.selection()
    for i in range(0, len(selected_files)):
        treeview.delete(selected_files[i])
# 得到所有的条目值
children = treeview.get_children()
for c in children:
    print(treeview.item(c)["values"][0])  # 要得到第二列值则改为treeview.item(c)["values"][1]
```
## 字符串类型的一串数字格式化输出
```python
# 格式化输出
if 0 < size < 1024 * 1024:
    size = "%(size).1f" % {'size': size / 1024} + "KB"
elif size < 1024 * 1024 * 1024:
    size = "%(size).2f" % {'size': size / (1024 * 1024)} + "MB"
else:
    size = "%(size).2f" % {'size': size / (1024 * 1024 * 1024)} + "GB"
```
## 窗口隐藏（或最小化）与显示
```python
# 隐藏窗口
mainwindow.withdraw()    
# 显示窗口
mainwindow.update()
mainwindow.deiconify()
# 最小化窗口
mainwindow.iconify()
# 显示窗口
mainwindow.deiconify()
```