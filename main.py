import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt, QDateTime

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        exitAction = QAction(QIcon('images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        exitAction1 = QAction(QIcon('images/edit.png'), 'Edit', self)
        exitAction2 = QAction(QIcon('images/print.png'), 'Print', self)
        exitAction3 = QAction(QIcon('images/save.png'), 'Save', self)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu.addAction(exitAction1)
        filemenu.addAction(exitAction2)
        filemenu.addAction(exitAction3)

        menubar.addMenu('&Edit')
        menubar.addMenu('&Source')
        menubar.addMenu('&Help')

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        toolbar1 = self.addToolBar('Edit')
        toolbar1.addAction(exitAction1)

        toolbar2 = self.addToolBar('Print')
        toolbar2.addAction(exitAction2)

        toolbar3 = self.addToolBar('Save')
        toolbar3.addAction(exitAction3)

        now = QDate.currentDate()
        print(now.toString('d.M.yy'))
        print(now.toString('dd.MM.yyyy'))
        print(now.toString('ddd.MMMM.yyyy'))
        print(now.toString(Qt.ISODate))
        print(now.toString(Qt.DefaultLocaleLongDate))

        datetime = QDateTime.currentDateTime()
        print(datetime.toString('d.M.yy hh:mm:ss'))
        print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
        print(datetime.toString(Qt.DefaultLocaleLongDate))
        print(datetime.toString(Qt.DefaultLocaleShortDate))

        self.statusBar().showMessage(datetime.toString(Qt.DefaultLocaleShortDate))

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        btn.move(50, 100)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('images/web.png'))
        self.setGeometry(300, 300, 1000, 800)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())