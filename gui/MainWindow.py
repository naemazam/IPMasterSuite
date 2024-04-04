
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QScrollArea, QApplication
from gui.Ip import Ip
from gui.Subnetting import Subnetting
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(Ip(), "Address calculator")
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(Subnetting())
        self.tab_widget.addTab(self.scroll_area, "Subnetting")

        self.setCentralWidget(self.tab_widget)
        self.setWindowTitle("IP address tools")
        self.setFixedSize(420, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
