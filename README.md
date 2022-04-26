# NLPQA_Test
这个只是测试代码，功能性与稳定性还不满足工程要求。
测试代码依赖Jie（结巴）中文分词系统与HanLP汉语言包，两者在GitHub上的托管如下所示，两者的具体部署详见各自的托管网址，此处不再累述。另外HanLP是Java代码实现的，测试代码使用了JPype-3来实现Python3对Jar包的调用。

使用时首先将库解压到需要引用的目录中，例如D:\workspace\HanLP\hanlp-1.2.8-release(Windows)  /opt/HanLP(Linux)

测试代码比较了Jieba中文分词与HanLP汉语言包的分词、词性标注与关键词的功能。此外还测试了HanLP的文本推荐功能。

## ref
Jieba：https://github.com/fxsjy/jieba<br> 
HanLP: https://github.com/hankcs/HanLP<br>
目前Java版本的代码在分支[1.x](https://github.com/hankcs/HanLP/tree/1.x)中维护
JPype3: https://github.com/tcalmant/jpype-py3/<br>
