# cloudpost说明文档
*version:`v1.0.0`*

谢谢你下载我的源码。这个项目是在我大一时发布，简陋粗糙，如有机会，欢迎指点。
### 这个项目是做什么的
轻量级api测试软件，基于pyside6和requests，尽可能少的代码和内存占用，实现用户对于接口测试的基本需求
如果你有需要，那么它可以用来应付你的作业（能帮到你请点个star~ ^_^)

### 能做什么&不能做什么
# 能做
基本的GET,POST,PUT,DELETE请求发送，左侧面板用于显示请求信息，右侧用于显示响应。
可切换HTML/JSON的输出格式，未作错误处理，点击请求无反应则是不支持此类型。
每次请求可选择是否保存至配置文件，重新启动软件默认读取最后一次保存的记录并填入url和postData。

# 不能做
错误处理，处于轻量的定位考虑。
多次，定量请求。无错误处理导致此功能排错困难。

### 会继续更新吗
会随着作者技术进步而进步的！
计划重构ui界面，并补充详细注释。tips:目前的ui是基于用户主题切换颜色的基础控件
