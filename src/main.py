import sys
from PyQt5.Qt import *

from main_class import Window


# 通过sys.argv获取到了命令行的参数，并用此参数来新建application
# sys.argv就是用来接收参数来执行不同的业务逻辑
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello Fred!")
window.resize(500, 500)
window.move(400, 200)

label = QLabel(window)
label.setText("Hello Sz!")
label.move(200, 200)

window.show()

# sys.exit(code)会输出程序停止执行的原因，（code=0表示正常退出）
# app.exec_()能让整个程序开始执行，并且进入到消息循环，也就是一种无限循环
# 在此无限循环中，也能监听app的各种交互和events
# 同时在结束循环时，需要将结束的原因通过sys.exit()返回
sys.exit(app.exec_())


# 一个Qt程序的编写过程
# 1. 一个应用程序对象app
# 2. 添加各种控件和控件操作
# 3. 应用程序app的执行，进入消息循环
