- [git](#git)
- [WPS](#wps)
- [SQL](#sql)
- [SAS](#sas)

# git
```
#用vs打开项目文件夹，进入项目目录：所有git命令都要在项目空间下进行，如果需要新建或进入其他目录则需要执行下面的代码
$ mkdir git-tutorial
$ cd git-tutorial

#第一次通过git去使用GitHub需要全局设置：--global针对系统上所有仓库有效；-e针对当前仓库有效
$ git config --global user.name "xxxx" 
$ git config --global user.email "xxxx@xxx"
$ git config --global --list //查看操作是否完成
$ ssh-keygen -t rsa -C "xxxx@xxx" //邮箱和上述邮箱一致，一直回车可略过密码等设置
#找到id_rsa.pub，复制内容，添加到github的ssh keys
$ ssh -T git@github.com //选择yes，验证是否成功
$ git remote add origin https://github.com/GG-YQ/xxx.git

#初始化：
$ git init

#提交到库：
$ git add xxxx.xxx
$ git commit -m "first commit or some note"
$ git push -u origin master

#克隆：切换到目标文件目录，pull下载远程代码并合并；clone拷贝仓库到本地让自己能够查看修改
$ git clone git@github.com:github-book/git-tutorial.git
$ git pull origin master

#其他：diff在commit前查看区别；status查看状态；log查看日志；
$ git diff
$ git status
$ git log
$ git branch b1
$ git checkout b1

#git忽略文件设置：模板参考<https://github.com/github/gitignore>；忽略规则参考<https://www.cnblogs.com/kevingrace/p/5690241.html>
1. 创建.gitignore文件
在版本管理的根目录下（与.Git文件夹同级）创建一个 .gitignore，命令为：touch .gitignore
2. 直接用vscode打开编辑，写入要忽略的文件或文件夹并保存
.gitignore
.vscode/
**/__pycache__
3. 强制添加一个被.gitignore忽略了的文件xxxx.xxx到Git
$ git add -f xxxx.xxx
4. 检查哪个规则忽略了文件xxxx.xxx
$ git check-ignore -v xxxx.xxx
5. 未生效原因排查
.gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。解决方法就是先把本地缓存删除（改变成未track状态），然后再提交：
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
```
#在git bash命令行git commit -m "messages"可以正常commit，但是使用vscode工具栏commit一直卡住：vs code升级后，原来提交代码时，是在vscode里直接填写message的，升级之后没有了，会直接对代码进行提交，这样的话导致服务器拒绝。
解决办法：在设置里改回旧版本的提交方式。file>>preferences>>settings，取消勾选“use editer as commit input”。


# WPS
1. 显示格式TEXT()函数
=text(A1,”h小时mm分”)
=text(A1,”yyyy年mm月dd日”)
=text(A1,”aaaa”) #长星期格式”aaaa”，短星期格式”aaa”
=text(A1,”000”) #填入多位数序列
2. 日期格式yyyy-mm-dd转yyyy/m/d
- 使用text()
- 选中，分列-默认分隔符号选择tab-列数据类型选择日期-完成
3. 条件格式
选定区域-条件格式-公式-录入公式-格式设置
4. 显示分位和单位
自定义格式：0!.0,
5. 条件匹配
- 条件匹配单值、多值、最大值、最小值
- 单条件匹配单值：index+match
- 多条件匹配单值：将多条件通过&转化为单条件，然后使用index+match
- 单条件匹配多值：idnex+small+if
- 多条件匹配数字：averageifs()、sumifs()、sumproduct()
6. 维度转换
- 一维转二维：法一，透视表；法二，全量行标签进行条件匹配。
- 二维转一维：透视表
7. 切片器

# SQL
1. Hive SQL
- Null：sum、count会忽略null、count(1)不会，或者嵌套nvl
- Union all
- 堆叠变二维：自身join求笛卡尔积，然后where或on过滤
- 窗口函数：sum()over()、row_number()over()
- 日期处理date_format()、date_add()、date_sub()、last_day()
- 时间戳和其他格式转换
- 多类聚合：grouping sets、rollup
- 空值：判断is null、=’\\N’；和’’空字符串不一样，空字符串需要用=’’判断；和’ ’空格也不一样；处理，nvl、nullif、coalesce()
- 随机选择num个：row_number()over(order by rand()) as rn where rn<=num
- 拆分：split、explode
- 字符串处理：concat()、concat_ws()、substr()、trim、rtrim、ltrim、Lpad()、Rpad()
- 格式转换：cast()
- 日期提取小时2位字符：.z_hour
2. Nosql
- 图表示

# SAS
数据导入：Excel只能用proc，不能用data步导入。
```
PROC IMPORT
DATAFILE="filename" | DATATABLE="tablename" (Not used for Microsoft Excel files)
<DBMS=data-source-identifier>
<OUT=libref.SAS data-set-name> <SAS data-set-option(s)>
<REPLACE;>
<file-format-specific-statements>;
```
- 必选参数只有一个，即DATAFILE|DATATABLE，其中DATAFILE可以用别名file代替，DATATABLE可以用别名table代替。
- DBMS=data-source-identifier：导入的数据的类型
- SAS data-set-option(s)： SAS data set的选项，比如可以使用where data set option.
- OUT=<libref.>SAS data-set：数据集的名子
- REPLACE：如果数据集已经存在，是否替换。
- <file-format-specific-statements>：文件格式说明，比如，对于Excel文档，GETNAMES=YES | NO可以规定是否使用文档中的第一行来产生SAS 变量，SHEET=sheet-name来指定文档中sheet的名子，每个语句是以逗号作为分割符。