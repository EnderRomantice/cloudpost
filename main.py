import os
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow
from cloudpost.service.resService import makeRes
from cloudpost.view.cloudDemo import Ui_MainWindow
from cloudpost.service.loadConfig import readStartConfig, loadsConfig


class Main(QMainWindow):
    def __init__(self):

        super(Main, self).__init__()  #代表调用Main的父类构造方法，self确保父类能访问到Main
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        readStartConfig(self)

        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.resCount = 0

        #链接start
        self.ui.startButton.clicked.connect(self.request)
    # 请求主方法

    def request(self):

        #初始化请求参数
        reqMethod = self.ui.reqMethod.currentText()  #确定方法

        codeUse = self.ui.codeUse.currentText()

        outUse = self.ui.outUse.currentText()

        logSave = self.ui.logSave.currentText()

        url = codeUse + self.ui.urlInput.text()

        postData = self.ui.postInput.text()

        response = makeRes( reqMethod, url=url, params=postData, out=outUse)

        status = str(response["statusCode"]) + ' error QAQ' if response["statusCode"] != 200 else str(response["statusCode"]) + ' OK ^_^'

        resOutPut = response["res"]

        self.resCount += 1

        self.ui.leftOut.append(f"请求记录{self.resCount}\n\n请求时间:{self.now}\n\n响应状态:{status}\n\nurl:\n{url}\n\n请求头:\n{response["resHeaders"]}\n______________________________________________________________________")

        self.ui.rightOut.setPlainText(resOutPut)
        if logSave == "SAVE":
            loadsConfig(self.ui.urlInput.text(), postData)

if __name__ == "__main__":
    print("当前工作目录:", os.getcwd())

    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
