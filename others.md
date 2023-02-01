- [VSCode](#vscode)
- [git](#git)
- [WPS](#wps)
- [SQL](#sql)
- [SAS](#sas)

# VSCode
- 代码目录下生成的".vscode"文件夹只对阅读代码有影响而对编译器无影响，并且这个文件夹产生的数据极大，远超出github仓库允许的容量(100M)，一般不push。
- 自动格式化需设置忽略排序：可能会产生import依赖问题

# git
- 基本用法
    - 用vs打开项目文件夹，进入项目目录：所有git命令都要在项目空间下进行，如果需要新建或进入其他目录则需要执行下面的代码
        ```
        $ pwd  //查询当前目录  
        $ mkdir git-tutorial  
        $ cd git-tutorial  
        ```  
    - 远程库的连接和解除
        ```
        //第一次通过git去使用GitHub需要全局设置：--global针对系统上所有仓库有效；-e针对当前仓库有效
        $ git config --global user.name "xxxx" 
        $ git config --global user.email "xxxx@xxx"
        $ git config --global --list //查看操作是否完成
        $ ssh-keygen -t rsa -C "xxxx@xxx" //邮箱和上述邮箱一致，一直回车可略过密码等设置，找到id_rsa.pub，复制内容，添加到github的ssh keys
        $ ssh -T git@github.com //选择yes，验证是否成功
        //建立连接：Git支持多种协议，包括https，但ssh协议速度最快
        $ git remote add origin git@github.com:username/reponame.git
        不推荐 $ git remote add origin https://github.com/username/reponame.git
        //远程库的查询和删除：先用git remote -v查看远程库信息；然后用git remote rm根据名字删除，比如删除origin，即解除远程关联。
        $ git remote -v  
        $ git remote rm name
        ```  
    - 初始化
        ```$ git init```
    - 提交到库：rm删除文件、add添加文件到暂存区；commit通过暂存区的指针将暂存区的快照提交到本地git库；push同步到远程库，第一次推送master分支时加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。
        ```
        $ git rm <file>
        $ git add xxxx.xxx
        $ git commit -m "first commit or some note"
        $ git push -u origin master
        ```  
    - 远程库其他操作
        ```
        //切换到目标文件目录，clone拷贝仓库到本地让自己能够查看修改：有无仓库权限均可，适用本地为空
        $ git clone git@github.com:username/reponame.git
        //切换到目标文件目录，pull下载远程代码并合并：必须有权限
        $ git pull origin master
        //本地推送分支：使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交
        $ git push origin branch-name
        //在本地创建和远程分支对应的分支：本地和远程分支的名称最好一致
        $ git checkout -b branch-name origin/branch-name
        //建立本地分支和远程分支的关联：
        $ git branch --set-upstream branch-name origin/branch-name
        ```  
    - git忽略文件设置：[模板参考](https://github.com/github/gitignore)；[忽略规则参考](https://www.cnblogs.com/kevingrace/p/5690241.html)
        ```
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
        5. 未生效原因排查：.gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。解决方法就是先把本地缓存删除（改变成未track状态），然后再提交
        git rm -r --cached .
        git add .
        git commit -m 'update .gitignore'
        ```  
- 分支管理
    - 版本恢复
        ```$ git reset --hard <commit_id>```
    - 回退到上一个版本：
        ```$ git reset --hard HEAD^```
    - 回退到commit_id以xxxx开头的版本
        ```$ git reset --hard xxxx```
    - git log可以查看提交历史，以便确定要回退到的左侧版本，HEAD指向当前版本
        ```
        $ git log
        $ git log --pretty=oneline
        $ git log --graph --pretty=oneline --abbrev-commit
        ```
    - 用git reflog查看历史命令，以便确定右侧版本
        ```$ git reflog```
    - 创建并切换到分支bname
        ```
        $ git checkout -b <bname>  
        $ git switch -c <bname>
        ```
    - 创建新分支newbname
        ```$ git branch <newbname>```
    - 切换到分支bname
        ```
        $ git checkout <bname>
        $ git switch <bname>
        ```
    - 查看当前分支：git branch命令会列出所有分支，当前分支前面会标一个*号
        ```$ git branch```
    - 合并某分支到当前分支：通常，合并分支时，如果可能，Git会用Fast forward模式，但这种模式下，删除分支后，会丢掉分支信息。如果要强制禁用Fast forward模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。
        ```
        $ git merge <name>
        $ git merge --no-ff -m "merge with no-ff" dev
        ```
    - 删除分支：如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除
        ```
        $ git branch -d <name>
        $ git branch -D <name>
        ```
    - bug分支：修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；当手头工作没有完成时，先把工作现场```$ git stash```一下，然后去修复bug，修复后，再```$ git stash pop```，回到工作现场；在master分支上修复的bug，想要合并到当前dev分支，可以用```$ git cherry-pick <commit>```命令，把bug提交的修改“复制”到当前分支，避免重复劳动。

- 标签：tag是一个有意义的名字，跟某个commit绑在一起
    - 新建一个标签：默认为HEAD，也可以指定一个commit id；-a指定标签名，-m指定说明文字
        ```
        $ git tag <tagname> <commit id>
        $ git tag -a <tagname> -m "blablabla..." <commit id>
        ```
    - 查看所有标签
        ```$ git tag```
    - 推送一个本地标签
        ```$ git push origin <tagname>```
    - 推送全部未推送过的本地标签
        ```$ git push origin --tags```
    - 删除一个本地标签
        ```$ git tag -d <tagname>```
    - 删除一个远程标签
        ```$ git push origin :refs/tags/<tagname>```

- FQ
    - 在git bash命令行git commit -m "messages"可以正常commit，但是使用vscode工具栏commit一直卡住：vs code升级后，原来提交代码时，是在vscode里直接填写message的，升级之后没有了，会直接对代码进行提交，这样的话导致服务器拒绝。
        ```
        解决办法：在设置里改回旧版本的提交方式。file>>preferences>>settings，取消勾选“use editer as commit input”。
        ```
    - 其他：diff在commit前查看区别；status查看工作目录和暂存区域状态
        ```
        $ git diff
        $ git status
        ```  

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
- file-format-specific-statements：文件格式说明，比如，对于Excel文档，GETNAMES=YES | NO可以规定是否使用文档中的第一行来产生SAS 变量，SHEET=sheet-name来指定文档中sheet的名子，每个语句是以逗号作为分割符。