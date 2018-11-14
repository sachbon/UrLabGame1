import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()

    w.setGeometry(100, 100, 300, 200)
    w.setWindowTitle('PYQt5 lessons')

    label1 = QtWidgets.QLabel(w)
    label1.setText('Hello World')
    label1.move(130,20)
    label2 = QtWidgets.QLabel(w)
    #label2.setPixmap(QtGui.QPixmap('name of file in brakets'))
    label2.move(120,90)

    w.show()
    sys.exit(app.exec_())

window()
