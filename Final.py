import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from svertcod_gl import Ui_MainWindow
from svertcod_inf import Ui_Form

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def openinf():
    global Form
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

ui.commandLinkButton.clicked.connect(openinf)

sys.exit(app.exec_())