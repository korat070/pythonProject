import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt, QDateTime

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = None
        self.todoVbox = None
        self.todoList = [
            {'id': 0, 'todo': '할일1', 'done': False},
            {'id': 1, 'todo': '할일2', 'done': False},
            {'id': 2, 'todo': '할일2', 'done': True}
        ]
        self.initUI()


    def renderTodos(self):

        self.todoVbox = QVBoxLayout()

        for todo in self.todoList:

            edtTodo = QLineEdit()
            edtTodo.setText(todo['todo'])

            btnDeleteTodo = QPushButton('삭제')
            btnDeleteTodo.clicked.connect(self.handleDelete)
            btnDeleteTodo.setObjectName(str(todo['id']))
            btnDeleteTodo.objectName()

            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.addWidget(edtTodo)
            hbox.addWidget(btnDeleteTodo)

            self.todoVbox.addLayout(hbox)

        self.todoVbox.update()
    def initUI(self):

        self.todo = QLineEdit()
        createTodo = QPushButton('생성')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.todo)
        hbox.addWidget(createTodo)
        hbox.addStretch(1)

        createTodo.clicked.connect(self.handleCreateTodo)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(hbox)
        self.vbox.addStretch(1)
        self.renderTodos()
        self.vbox.addLayout(self.todoVbox)
        self.setLayout(self.vbox)
        self.setWindowTitle('Todo List')
        self.setWindowIcon(QIcon('images/web.png'))
        self.setGeometry(300, 300, 1000, 800)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handleCreateTodo(self):
        print(self)

    def handleDelete(self):
        btn = self.sender()
        btn.objectName()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())