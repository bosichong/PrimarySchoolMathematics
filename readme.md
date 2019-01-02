孩子上小学一年级了，加减乘除的口算就要开始练习了，估计老师肯定会让家长出题，所以提前准备一下，利用Python开发了一套自动生成小学生口算题的小应用。而且今天是程序员节，撸200行代码庆祝一下。：）


为了让程序员老爹解放抄题的双手，让你拥有更多的时间去写代码而不用去手写几道口算题而伤神伤脑。所以有没有娃子的程序员爹爹加入一起来继续优化个开源小程序的？有什么点子，发现什么BUG，欢迎留言。

仅以此软件，献给那些热爱`Python`的程序员老爹们！

程序核心功能：

1.可以设置各算数项和结果的取值范围及多步算数符号的选择，可以生成求结果、求算数项、带括号的算式，最多支持3步算式题

2.可以简单设置文档标题，小标题。设置生成的口算题文档个数




使用方法：

1 确定本机支持python3.6.1以上版本

2 安装.docx模块,安装wxPython模块 安装方法：

`pip3 install python-docx`

`pip3 install wxpython`


3 下载程序进入主目录，终端下运行`python App.py `

4 修改运算项和结果范围里的数值,多步运算请添加修改需要的运算符号:

![输入图片说明](https://images.gitee.com/uploads/images/2019/0102/165520_883d5be6_125848.png)

![输入图片说明](https://images.gitee.com/uploads/images/2019/0102/204453_e30f38d6_125848.png)

5 添加口算题到列表中，然后生成口算题,生成的口算题文件都在docx文件目录下，打开后连接打印机就可以开印了。




程序界面截图：

![输入图片说明](https://images.gitee.com/uploads/images/2019/0102/165314_cc68e64d_125848.png "Snip20190102_1.png")


程序成生的口算题截图：

![输入图片说明](https://images.gitee.com/uploads/images/2018/1119/214154_bb529734_125848.png "001.png")

![输入图片说明](https://images.gitee.com/uploads/images/2018/1119/214206_a3081f2e_125848.png "002.png")

![输入图片说明](https://images.gitee.com/uploads/images/2018/1119/214230_b9c6e3ef_125848.png "003.png")

![输入图片说明](https://images.gitee.com/uploads/images/2018/1119/214240_e946434d_125848.png "004.png")
