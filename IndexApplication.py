from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from AutomataTheoryQt import *
import sys, time

PrimaryUserInterface,_=loadUiType("BaseUserInterface.ui")

class MainApp(QMainWindow, PrimaryUserInterface):
    def __init__(self):
        QMainWindow.__init__(self)
        self.title = "RE2FA Converter by t0xic0der"
        self.setupUi(self)
		self.setWindowTitle(self.title)
        self.HandleElements()

    def HandleElements(self):
        self.textedit.setReadOnly(True)
        self.pushbutn.clicked.connect(self.compdata)

    def compdata(self):
        InputRegularExpression = self.lineedit.text()
        ReturnData = "<b>Started ToxicEngine for RE2FA conversion</b>" + "<br/><i>" + time.ctime() + "</i><br/><br/>"
        try:
            ReturnData = ReturnData + "<i>Horizontal and vertical scrolling is supported</i><br/><br/>" + RegexComputation(InputRegularExpression)
        except BaseException as ExceptionEvent:
            ReturnData = ReturnData + "<b>Failure: </b>" + str(ExceptionEvent)
        ReturnData = ReturnData + "<br/><br/>" + "<b>Stopped ToxicEngine for RE2FA conversion</b>" + "<br/>" + \
                     "<i>Follow me on https://www.github.com/t0xic0der for more such projects!</i>"
        self.textedit.setText(ReturnData)

def RegexComputation(InputRegularExpression):
    startTime = time.time()
    nfaObject = NFAfromRegex(InputRegularExpression)
    nfa = nfaObject.getNFA()
    dfaObject = DFAfromNFA(nfa)
    stopTime = time.time()
    TotalTime = stopTime - startTime
    actualData = "<b>Regular Expression: </b>" + str(InputRegularExpression) + "<br/>" + "<br/>" + \
                 "<b>Non-deterministic Finite Automata</b>" + "<br/>" + nfaObject.displayNFA() + "<br/>" + \
                 "<b>Deterministic Finite Automata</b>" + "<br/>" + dfaObject.displayDFA() + "<br/>" + \
                 "<b>Minimised Deterministic Finite Automata</b>" + "<br/>" + dfaObject.displayMinimisedDFA() + "<br/>" + \
                 "<b>Computation time: </b>" + str(TotalTime) + " seconds"
    return actualData

def main():
    app=QApplication(sys.argv)
    QFontDatabase.addApplicationFont("Roboto-Regular.ttf")
    QFontDatabase.addApplicationFont("RobotoMono-Regular.ttf")
	QFontDatabase.addApplicationFont("RobotoMono-Bold.ttf")
    QFontDatabase.addApplicationFont("RobotoMono-Italic.ttf")
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
