import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMainWindow, qApp, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qss_file = open('style.qss').read()
        qApp.setStyleSheet(qss_file)

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        newProjectAct = QAction(QIcon('new.png'), '&New Project', self)
        newProjectAct.setShortcut('Ctrl+Shift+N')
        newProjectAct.setStatusTip('Create a New Project')
        newProjectAct.triggered.connect(self.create_new_project_action)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newProjectAct)
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

    def create_new_project_action(self):
        print("New project Action :TODO")

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()