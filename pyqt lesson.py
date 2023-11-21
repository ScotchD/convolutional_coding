from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Программа")
        self.setGeometry(300, 250, 350, 200)

        self.lbl = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Кнопка")
        self.btn.move(100, 150)
        self.btn.setFixedWidth(130)
        self.btn.clicked.connect(self.command)

    def command(self):
        self.lbl.setText("Вторая надпись")
        self.lbl.move(100, 50)
        self.lbl.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()