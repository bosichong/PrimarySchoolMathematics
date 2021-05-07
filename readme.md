孩子上小学一年级了，加减乘除的口算就要开始练习了，估计老师肯定会让家长出题，所以提前准备一下，利用Python开发了一套自动生成小学生口算题的小应用。而且今天是程序员节，撸200行代码庆祝一下。：）

为了让程序员老爹解放抄题的双手，让你拥有更多的时间去写代码而不用去手写几道口算题而伤神伤脑。所以有没有娃子的程序员爹爹加入一起来继续优化个开源小程序的？有什么点子，发现什么BUG，欢迎留言。

仅以此软件，献给那些热爱`Python`的程序员老爹们！

程序核心功能：

1.可以设置各算数项和结果的取值范围及多步算数符号的选择，可以生成求结果、求算数项、带括号的算式，最多支持3步算式题

2.可以简单设置文档标题，小标题。设置生成的口算题文档个数

pip安装：

    pip install PrimarySchoolMath

运行：

终端进入python3的交互界面：

    import PrimarySchoolMath

如果提示缺少相关依赖包，请安装一下依赖：

    pip install python-docx==0.8.10
    pip install wxPython==4.1.1


Git克隆或是下载压缩包：

下载程序进入程序主目录，安装程序相关依赖，在程序根目录下运行终端：

    pip install -r requirements.txt


3 程序主目录终端下运行`python App.py`,Mac下边如果遇到无法启动请试试：`pythonw App.py`

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
