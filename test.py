import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QCheckBox, QPlainTextEdit, QLineEdit


class Main(QWidget):
    def init(self):
        super().init()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.txt = QPlainTextEdit('Ваш заказ:\n', self)
        self.txt.move(10, 120)
        self.txt.setEnabled(False)

        self.cb1 = QCheckBox('Чизбургер', self)
        self.cb1.move(10, 10)

        self.cb2 = QCheckBox('Гамбургер', self)
        self.cb2.move(10, 30)

        self.cb3 = QCheckBox('Кока-кола', self)
        self.cb3.move(10, 50)

        self.cb4 = QCheckBox('Нагетсы', self)
        self.cb4.move(10, 70)

        self.btn = QPushButton('Заказать', self)
        self.btn.adjustSize()
        self.btn.move(10, 90)
        self.btn.clicked.connect(self.zakaz)

    def zakaz(self):
        self.txt.setPlainText('')
        if self.cb1.isChecked():
            self.txt.setPlainText(self.txt.toPlainText() + 'Чизбургер' + '\n')
        if self.cb2.isChecked():
            self.txt.setPlainText(self.txt.toPlainText() + 'Гамбургер' + '\n')
        if self.cb3.isChecked():
            self.txt.setPlainText(self.txt.toPlainText() + 'Кока-кола' + '\n')
        if self.cb4.isChecked():
            self.txt.setPlainText(self.txt.toPlainText() + 'Нагетсы' + '\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
