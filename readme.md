# 简介

这是一个简单的scrapy的爬虫
在大神winter删除所有答案之前，备份winter目前为止[2015年05月31日]在知乎的所有答案
[原因请戳-->](http://weibo.com/1196343093/Ck4wP32Bq)
[winter的项目地址](https://github.com/wintercn/dog-fucked-zhihu)

本项目作为一个简单的scrapy练手项目，只需要改部分内容，即可爬取知乎任何用户的所有答案
如果您也在用scrapy欢迎交流指正：D

#环境 & Usage

* python 2.7
* pip [安装和介绍](https://pypi.python.org/pypi/pip#downloads)
* scrapy 0.24 [安装和使用](https://scrapy-chs.readthedocs.org/zh_CN/0.24/intro/install.html)
* mongoDB 3.0.2 [安装和使用](http://docs.mongodb.org/manual/) | [中文版](http://docs.mongodb.org/manual/)
* pymongo 3.0.2 [安装和使用](https://pypi.python.org/pypi/pymongo/3.0.2)
* robomongo [mongo可视化工具下载](http://robomongo.org/download.html)

# 目前实现的功能
命令行下使用`scrapy list`可以看到三个爬虫
* q_test: 爬取[winter答题首页](http://www.zhihu.com/people/winter-25/answers)的所有题目和题目链接
* question: 进一步跟踪下一页的链接，爬取winter所哟回答过的题目及其链接并存储到数据库
* answer: 从数据库取出所有链接，进入详情页面，爬题目的详细描述、winter答题的详细内容

# todo
* 题目描述太长的话，会被知乎折叠一部分，本项目目前并不能取到【显示更多】里的描述
* 处理富文本：比如内容中的图片、a链接
* winter专栏还没爬
* winter原项目的【取消所有点赞，批量替换所有答案】功能，没作者权限做不了，后续可以这样玩自己
