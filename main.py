import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QImage, QColor, QPixmap, QPainter
from PyQt5.QtCore import Qt
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Circle Creator')

        self.button_create_circle.clicked.connect(self.create_circle)

    def create_circle(self):
        diameter = random.randint(10, 100)
        image = QImage(diameter, diameter, QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        painter = QPainter()
        painter.begin(image)
        painter.setBrush(QColor(Qt.yellow))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, diameter, diameter)
        painter.end()

        label = self.label_image
        pixmap = QPixmap.fromImage(image)
        label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
