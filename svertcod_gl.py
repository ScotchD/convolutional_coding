from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(650, 20, 61, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(110, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(240, 20, 42, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(260, 60, 42, 31))
        self.spinBox_2.setObjectName("spinBox_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 180, 281, 87))
        self.textEdit_2.setTabChangesFocus(False)
        self.textEdit_2.setReadOnly(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 350, 281, 87))
        self.textEdit_3.setTabChangesFocus(False)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(30, 450, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 480, 281, 87))
        self.textEdit_4.setTabChangesFocus(False)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(490, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(410, 150, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(410, 180, 281, 87))
        self.textEdit_5.setTabChangesFocus(False)
        self.textEdit_5.setReadOnly(False)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(410, 350, 281, 87))
        self.textEdit_6.setTabChangesFocus(False)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(410, 320, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(410, 450, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setScaledContents(False)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(410, 480, 281, 87))
        self.textEdit_7.setTabChangesFocus(False)
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName("textEdit_7")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(520, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setUnderline(True)
        self.commandLinkButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("123")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 280, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttons()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Количество регистров"))
        self.label_2.setText(_translate("MainWindow", "Количество сумматоров"))
        self.label_3.setText(_translate("MainWindow", "Перечень регистров для сумматоров"))
        self.label_4.setText(_translate("MainWindow", "Кодирование"))
        self.label_5.setText(_translate("MainWindow", "Текст"))
        self.label_6.setText(_translate("MainWindow", "Информационное слово"))
        self.label_7.setText(_translate("MainWindow", "Кодовое слово"))
        self.label_8.setText(_translate("MainWindow", "Декодирование"))
        self.label_9.setText(_translate("MainWindow", "Кодовое слово"))
        self.label_10.setText(_translate("MainWindow", "Информационное слово"))
        self.label_11.setText(_translate("MainWindow", "Текст"))
        self.commandLinkButton.setText(_translate("MainWindow", "Информация"))
        self.pushButton.setText(_translate("MainWindow", "Кодировать"))
        self.pushButton_2.setText(_translate("MainWindow", "Декодировать"))

    def buttons(self):
        self.pushButton.clicked.connect(lambda: self.codir(self.spinBox.text(), self.spinBox_2.text(), self.textEdit.toPlainText(), self.textEdit_2.toPlainText()))
        self.pushButton_2.clicked.connect(lambda: self.decodir(self.spinBox.text(), self.spinBox_2.text(), self.textEdit.toPlainText(), self.textEdit_5.toPlainText()))

    def codir(self, spinBox, spinBox_2, textEdit, textEdit_2):
        ch1 = self.textEdit.toPlainText()
        p1 = False
        if ch1 == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Пустое поле для перечня регистров")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            p1 = True


        ch2 = self.textEdit.toPlainText()
        p2 = False
        if p1 == False:
            for i in range(len(ch2)):
                if ch2[i].isalpha():
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Неверные символы")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec_()
                    p2 = True
                    break

        ch3 = self.textEdit.toPlainText()
        ch3 = ch3.split("\n")
        p3 = False
        if len(ch3) != int(self.spinBox_2.text()) and p1 == False and p2 == False:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Указано не то количество сумматоров, которое заявлено")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            p3 = True

        ch4 = self.textEdit.toPlainText()
        ch4 = ch4.split("\n")
        p4 = False
        if p1 == False and p2 == False and p3 == False:
            for i in range(len(ch4)):
                ch4[i] = ch4[i].split()
            p4_1 = False
            for i in range(len(ch4)):
                for j in range(len(ch4[i])):
                    ch4[i][j] = int(ch4[i][j])
                    if ch4[i][j] < 0 or ch4[i][j] > int(self.spinBox.text()):
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Выход за пределы регистров")
                        error.setIcon(QMessageBox.Warning)
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec_()
                        p4 = True
                        p4_1 = True
                        break
                if p4_1:
                    break

        ch4_1 = self.textEdit.toPlainText().split("\n")
        for i in range(len(ch4_1)):
            ch4_1[i] = ch4_1[i].split()
        p4_1 = False
        for i in range(len(ch4_1)):
            p4_2 = False
            for j in range(len(ch4_1[i])):
                if ch4_1[i].count(ch4_1[i][j]) > 1 and p1 == False and p2 == False and p3 == False and p4 == False:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Указано больше одного сумматора на один регистр")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec_()
                    p4_1 = True
                    p4_2 = True
                    break
            if p4_2:
                break

        ch5 = self.textEdit_2.toPlainText()
        p5 = False
        if ch5 == "" and p1 == False and p2 == False and p3 == False and p4 == False and p4_1 == False:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Пустое поле для текста")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            p5 = True

        if p1 == False and p2 == False and p3 == False and p4 == False and p4_1 == False and p5 == False:
            def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
                bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
                return bits.zfill(8 * ((len(bits) + 7) // 8))

            def summator(x, y):
                for i in range(len(SR)):
                    rs = []
                    for j in range(len(SR[i])):
                        rs.append(y[SR[i][j]])
                    # print("rs: ", rs)
                    l = 0
                    for k in range(len(rs)):
                        if rs[k] == 1:
                            l += 1
                    if l % 2 == 0:
                        l = 0
                    else:
                        l = 1
                    # print("l: ", l)
                    x.append(l)
                    # print("rez: ", x)

            kreg = int(spinBox)
            reg = [0] * kreg

            sumat = int(spinBox_2)
            SR = textEdit
            SR = SR.split("\n")
            for i in range(len(SR)):
                SR[i] = SR[i].split()
            for i in range(len(SR)):
                for j in range(len(SR[i])):
                    SR[i][j] = int(SR[i][j]) - 1

            infsl = textEdit_2
            pr1 = False
            for i in range(len(infsl)):
                if infsl[i] != "0":
                    if infsl[i] != "1":
                        pr1 = True
                        break
            if pr1:
                infsl = text_to_bits(infsl)
            self.textEdit_3.setText(infsl)

            rez = []
            while len(infsl) != 0 or kreg != 0:
                if len(infsl) != 0:
                    reg.insert(0, int(infsl[0]))
                    del reg[-1]
                    infsl = infsl.replace(infsl[0], '', 1)
                    summator(rez, reg)
                else:
                    reg.insert(0, 0)
                    del reg[-1]
                    summator(rez, reg)
                    kreg -= 1

            REZ = ""
            for i in range(len(rez)):
                REZ += str(rez[i])
            self.textEdit_4.setText(REZ)

    def decodir(self, spinBox, spinBox_2, textEdit, textEdit_5):
        ch1 = self.textEdit.toPlainText()
        p1 = False
        if ch1 == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Пустое поле для перечня регистров")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            p1 = True

        ch2 = self.textEdit.toPlainText()
        p2 = False
        if p1 == False:
            for i in range(len(ch2)):
                if ch2[i].isalpha():
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Неверные символы")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec_()
                    p2 = True
                    break

        ch3 = self.textEdit.toPlainText()
        ch3 = ch3.split("\n")
        p3 = False
        if len(ch3) != int(self.spinBox_2.text()) and p1 == False and p2 == False:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Указано не то количество сумматоров, которое заявлено")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            p3 = True

        ch4 = self.textEdit.toPlainText()
        ch4 = ch4.split("\n")
        p4 = False
        if p1 == False and p2 == False and p3 == False:
            for i in range(len(ch4)):
                ch4[i] = ch4[i].split()
            p4_1 = False
            for i in range(len(ch4)):
                for j in range(len(ch4[i])):
                    ch4[i][j] = int(ch4[i][j])
                    if ch4[i][j] < 0 or ch4[i][j] > int(self.spinBox.text()):
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Выход за пределы регистров")
                        error.setIcon(QMessageBox.Warning)
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec_()
                        p4 = True
                        p4_1 = True
                        break
                if p4_1:
                    break

        ch4_1 = self.textEdit.toPlainText().split("\n")
        for i in range(len(ch4_1)):
            ch4_1[i] = ch4_1[i].split()
        p4_1 = False
        for i in range(len(ch4_1)):
            p4_2 = False
            for j in range(len(ch4_1[i])):
                if ch4_1[i].count(ch4_1[i][j]) > 1 and p1 == False and p2 == False and p3 == False and p4 == False:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Указано больше одного сумматора на один регистр")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec_()
                    p4_1 = True
                    p4_2 = True
                    break
            if p4_2:
                break

        ch5 = self.textEdit_5.toPlainText()
        p5 = False
        if ch5 == "" and p1 == False and p2 == False and p3 == False and p4 == False and p4_1 == False:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Пустое поле для кодового слова")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            p5 = True

        ch6 = self.textEdit_5.toPlainText()
        p6 = False
        if p1 == False and p2 == False and p3 == False and p4 == False and p4_1 == False and p5 == False:
            for i in range(len(ch6)):
                if ch6[i] != "1":
                    if ch6[i] != "0":
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Некорректное кодовое слово")
                        error.setIcon(QMessageBox.Warning)
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec_()
                        p6 = True
                        break

        if p1 == False and p2 == False and p3 == False and p4 == False and p4_1 == False and p5 == False and p6 == False:
            def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
                n = int(bits, 2)
                return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

            def summator(x, y):
                for i in range(len(SR)):
                    rs = []
                    for j in range(len(SR[i])):
                        rs.append(y[SR[i][j]])
                    # print("rs: ", rs)
                    l = 0
                    for k in range(len(rs)):
                        if rs[k] == 1:
                            l += 1
                    if l % 2 == 0:
                        l = 0
                    else:
                        l = 1
                    # print("l: ", l)
                    x.append(l)
                    # print("rez: ", x)
            try:
                REZ = textEdit_5

                kreg = int(spinBox)
                kreg1 = kreg
                reg = [0] * kreg

                sumat = int(spinBox_2)
                SR = textEdit
                SR = SR.split("\n")
                for i in range(len(SR)):
                    SR[i] = SR[i].split()
                for i in range(len(SR)):
                    for j in range(len(SR[i])):
                        SR[i][j] = int(SR[i][j]) - 1

                INFSL = []
                while len(REZ) != 0:
                    ck = ""
                    for i in range(sumat):
                        ck += REZ[0]
                        REZ = REZ.replace(REZ[0], "", 1)
                    # print("ck: ", ck)
                    # print("REZ: ", REZ)

                    reg1 = []
                    for i in range(len(reg)):
                        reg1.append(reg[i])
                    reg1.insert(0, 0)
                    del reg1[-1]
                    # print("reg1: ", reg1)
                    rez1 = []
                    summator(rez1, reg1)

                    REZ1 = ""
                    for i in range(len(rez1)):
                        REZ1 += str(rez1[i])
                    # print("REZ1: ", REZ1)

                    reg2 = []
                    for i in range(len(reg)):
                        reg2.append(reg[i])
                    reg2.insert(0, 1)
                    del reg2[-1]
                    # print("reg2: ", reg2)
                    rez2 = []
                    summator(rez2, reg2)

                    REZ2 = ""
                    for i in range(len(rez2)):
                        REZ2 += str(rez2[i])
                    # print("REZ2: ", REZ2)

                    if REZ1 == ck and REZ2 != ck:
                        INFSL.append(0)
                        reg = []
                        for i in range(len(reg1)):
                            reg.append(reg1[i])
                        # print("reg: ", reg)
                    elif REZ1 != ck and REZ2 == ck:
                        INFSL.append(1)
                        reg = []
                        for i in range(len(reg2)):
                            reg.append(reg2[i])
                        # print("reg: ", reg)
                    elif len(REZ) == 0:
                        INFSL.append(0)
                    elif REZ1 == ck and REZ2 == ck:
                        reg4 = []
                        for i in range(len(reg2)):
                            reg4.append(reg2[i])
                        reg.insert(0, 0)
                        del reg[-1]

                        ck = ""
                        for i in range(sumat):
                            ck += REZ[i]
                        # print("ck: ", ck)

                        reg1 = []
                        for i in range(len(reg)):
                            reg1.append(reg[i])
                        reg1.insert(0, 0)
                        del reg1[-1]
                        # print("reg1: ", reg1)
                        rez1 = []
                        summator(rez1, reg1)

                        REZ1 = ""
                        for i in range(len(rez1)):
                            REZ1 += str(rez1[i])
                        # print("REZ1: ", REZ1)

                        reg2 = []
                        for i in range(len(reg)):
                            reg2.append(reg[i])
                        reg2.insert(0, 1)
                        del reg2[-1]
                        # print("reg2: ", reg2)
                        rez2 = []
                        summator(rez2, reg2)

                        REZ2 = ""
                        for i in range(len(rez2)):
                            REZ2 += str(rez2[i])
                        # print("REZ2: ", REZ2)

                        if REZ1 == ck or REZ2 == ck:
                            INFSL.append(0)
                            # print("INFSL: ", INFSL)
                            # print("reg: ", reg)
                            # print("REZ: ", REZ)
                        else:
                            reg = []
                            for i in range(len(reg4)):
                                reg.append(reg4[i])
                            INFSL.append(1)
                            # print("INFSL: ", INFSL)
                            # print("reg: ", reg)
                            # print("REZ: ", REZ)

                    # print("INFSL: ", INFSL)

                IS = ""
                for i in range(len(INFSL)):
                    IS += str(INFSL[i])
                IS = IS[:-kreg1]
                self.textEdit_6.setText(IS)
                self.textEdit_7.setText(text_from_bits(IS))
            except ValueError:
                self.textEdit_7.setText("")

                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Данное кодовое слово не декодируется")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
            except IndexError:
                self.textEdit_6.setText("")
                self.textEdit_7.setText("")

                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Данное кодовое слово не декодируется")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()