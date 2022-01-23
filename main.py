# GUI Created by: PyQt5 UI code generator 5.15.2
#Quick program to start matching carOrdinal to cars for Forza Horizon 5.
#Haven't found an existing list yet, figured I'd start the fun task myself.
#
from PyQt5 import QtCore, QtGui, QtWidgets
from forzatelemetry import Telemetry
import threading
import json

index = 0
year = 'Year'
make = 'Make'
model = 'Model'
carOrdinal = '0'
file_name = 'carlist.json'

def indexNext():
    global index, car_list
    index +=1
    while car_list[index]['Ordinal'] != "wtfbbq":
        index += 1

def SkipCar():
    global index
    indexNext()

def SaveCar():
    global car_list
    car_list[index]['Ordinal'] = telem.getCarOrdinal()
    open_file = open(file_name, "w")
    json.dump(car_list, open_file)
    open_file.close()
    indexNext()
            
#to be looped in a background thread to constantly update all window boxes
def UpdateBoxes():
    global car_list, index, year, make, model, carOrdinal
    while True:
        for a, b, c, d in car_list: #b= Year c=Make d=Model a=carOrdinal
            year = car_list[index][b]
            make = car_list[index][c]
            model = car_list[index][d]
        ui.lineEdit.setText(f"{year} {make} {model}")
        ui.lineOrdinal.setText(str(telem.getCarOrdinal()))
        ui.lineTimeStamp.setText(str(telem.getTimeStampMS('formatted')))
        ui.lineCurrentIndex.setText(str(index))
        if telem.getCarOrdinal() == 0:
            ui.btnSavecarOrdinal.setEnabled(False)
        else:
            ui.btnSavecarOrdinal.setEnabled(True)

#load json file and returns as dictionary, creates backup file as precaution
def LoadFile(file_name):
    with open(file_name, 'r') as json_file: 
        backup = 'carlist.backup.json' 
        open_file = open(backup, "w")
        car_list = json.load(json_file)
        json.dump(car_list, open_file) 
        open_file.close()
        return car_list

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 252)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelOrdinal = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelOrdinal.setObjectName("labelOrdinal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelOrdinal)
        self.lineOrdinal = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineOrdinal.setAlignment(QtCore.Qt.AlignCenter)
        self.lineOrdinal.setReadOnly(True)
        self.lineOrdinal.setObjectName("lineOrdinal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineOrdinal)
        self.labelTImeStamp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelTImeStamp.setObjectName("labelTImeStamp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTImeStamp)
        self.lineTimeStamp = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineTimeStamp.setAlignment(QtCore.Qt.AlignCenter)
        self.lineTimeStamp.setReadOnly(True)
        self.lineTimeStamp.setObjectName("lineTimeStamp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineTimeStamp)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelCurrentIndex = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCurrentIndex.setObjectName("labelCurrentIndex")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelCurrentIndex)
        self.lineCurrentIndex = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineCurrentIndex.setAlignment(QtCore.Qt.AlignCenter)
        self.lineCurrentIndex.setObjectName("lineCurrentIndex")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineCurrentIndex)
        self.horizontalLayout_4.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSavecarOrdinal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSavecarOrdinal.setObjectName("btnSavecarOrdinal")
        self.horizontalLayout.addWidget(self.btnSavecarOrdinal)
        self.btnSkipCar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSkipCar.setObjectName("btnSkipCar")
        self.horizontalLayout.addWidget(self.btnSkipCar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnSavecarOrdinal.clicked.connect(SaveCar)   #Save Current Ordinal
        self.btnSkipCar.clicked.connect(SkipCar)          #Skip current Car

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Car Ordinal Updater"))
        self.lineEdit.setText(_translate("MainWindow", "YEAR MAKE MODEL"))
        self.labelOrdinal.setText(_translate("MainWindow", "carOrdinal"))
        self.labelTImeStamp.setText(_translate("MainWindow", "Time Stamp"))
        self.labelCurrentIndex.setText(_translate("MainWindow", "Current Index"))
        self.lineCurrentIndex.setText(_translate("MainWindow", "0"))
        self.btnSavecarOrdinal.setText(_translate("MainWindow", "Save Car Ordinal"))
        self.btnSkipCar.setText(_translate("MainWindow", "Skip Car"))


if __name__ == "__main__":
    import sys
    #load json file to dictionary
    car_list = LoadFile(file_name) 

    #start telemetry server listening
    telem = Telemetry()
    telem.startServer(5300)
    telem.dataRefresh()

    #load window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #start thread loop for constant telemtry updates
    telem.dataLoop()

    #start background thread loop to keep gui updated
    threadBackgroundUpdates = threading.Thread(target=UpdateBoxes, daemon=True)
    threadBackgroundUpdates.start()

    #set index to first car that isn't set
    indexNext() 


    sys.exit(app.exec_())
