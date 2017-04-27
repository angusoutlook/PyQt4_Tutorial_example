#encoding utf-8

import sys
from PyQt4 import QtCore,QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()


    def initUI(self):

        textEdit=QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction=QtGui.QAction(QtGui.QIcon('exit24.png'),'&Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.statusBar()
        self.statusBar().showMessage('Ready')

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Statusbar')

        menubar=self.menuBar()
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.show()



def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ =='__main__':
    main()

