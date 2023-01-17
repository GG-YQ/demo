# 1 常用库
## 1.1 基本库
- os：文件、目录、路径、系统环境处理
- sys：命令行参数List，第一个元素是程序本身路径；退出程序，正常退出时exit(0)；获取Python解释程序的版本信息；返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值；操作系统平台名称。sys.path是python的搜索模块的路径集，是一个list。
- subprocess：执行系统命令 
- json 和 pickle： 用于序列化的两个模块。json，用于字符串 和 python数据类型间进行转换；pickle，用于python特有的类型 和 python的数据类型间进行转换。
- shutil：压缩包zip、tar；类似于高级API，主要强大之处在于其对文件的复制与删除操作；
- time、datetime：时间和日期处理；
- re：正则
- random：随机
- TuShare：开源财经数据接口包
- numpy、scicy、pandas、matplotlib / seaborn（推荐）、Statsmodels：数据包
- - numpy：矩阵运算、随机数
- - SciPy：构建于NumPy之上的科学计算工具集，不是完整的包含NumPy、Matplotlib的SciPy技术栈；它专为科学和工程设计，包括统计,优化,整合,线性代数模块,傅里叶变换,信号和图像处理,常微分方程求解器等等。如：数值计算的算法、一些功能函数，可以方便的处理数据。
- - pandas：数据整理
- - matplotlib / seaborn：数据可视化，推荐后者
- - Statsmodels：统计计量
- xlrd、xlwt：专门用于xlsx文件的读写
## PDF识别
- pdfminer：提取文本
- tabula：提取表格不太规范
- pdfplumber：提取表格且规范
## 文本分析
- 中文分词jieba、自然语言处理nltk：nltk处理语言数据，为像WordNet这样的词汇资源提供了简便易用的界面。具有为文本分类(classification)、文本标记(tokenization)、词干提取(stemming)、词性标记(tagging)、语义分析(parsing)和语义推理(semantic reasoning)准备的文本处理库。
其他：Pattern、TextBlob
## 机器学习
- 百度搜索pandas→进入pandas官网→点击documentation进入对应标签页面→选择pandas Ecosystem标签→pandas生态环境→第一个标签是Statsmodels库，选择该标签
StatsModels：基本统计库，提供包括描述性统计、评估和推断等操作在内的统计模型。
Scikit-learn：用于机器学习，建立在Scipy之上。
PyTorch：简洁的深度学习算法包。Sklearn和PyTorch的文档教程有公式原理、参考论文，利于学习。
Tenseflow： sklearn是机器学习算法包，pytorch和TensorFlow是深度学习算法包。sklearn有很多数据处理方法，目前在使用tf或者pytorch的过程中都会结合sklearn进行数据处理。在工业界用tf的比较多，学术界基本都是pytorch，入门的话，肯定pytorch简单好用，如果只是服务端部署，建议pytorch，移动端部署tflite还是支持的比较好一些。sklearn做机器学习，pytorch搞实验室研究，tf搞部署。
mxnet：类似tensorflow进行框架部署，但社区生态上处于劣势。
Keras：用Python编写的神经网络的高阶API，支持TensorFlow、CNTK和Theano，Keras可以最快的开发速度将想法转化为实际成果。
XGBoost：高效、灵活、移植的分布式梯度提升库，使用机器学习算法中的梯度提升框架。XGBoost 提供了并行树提升方法，代码还可以在主流分布式环境（Hadoop、SGE、MPI）下运行，借助分布式技术XGBoost可以处理十亿量级的数据。