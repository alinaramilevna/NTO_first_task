# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orders.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 220, 751, 321))
        self.listWidget.setObjectName("listWidget")
        self.endDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.endDateEdit.setGeometry(QtCore.QRect(420, 40, 110, 24))
        self.endDateEdit.setObjectName("endDateEdit")
        self.startDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.startDateEdit.setGeometry(QtCore.QRect(300, 40, 110, 24))
        self.startDateEdit.setObjectName("startDateEdit")
        self.typeOfProductionComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.typeOfProductionComboBox.setGeometry(QtCore.QRect(40, 40, 104, 26))
        self.typeOfProductionComboBox.setObjectName("typeOfProductionComboBox")
        self.cliendComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.cliendComboBox.setGeometry(QtCore.QRect(180, 40, 104, 26))
        self.cliendComboBox.setObjectName("cliendComboBox")
        self.commentTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.commentTextEdit.setGeometry(QtCore.QRect(40, 80, 721, 79))
        self.commentTextEdit.setObjectName("commentTextEdit")
        self.countSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.countSpinBox.setGeometry(QtCore.QRect(700, 40, 48, 24))
        self.countSpinBox.setObjectName("countSpinBox")
        self.statusComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.statusComboBox.setGeometry(QtCore.QRect(550, 40, 121, 26))
        self.statusComboBox.setObjectName("statusComboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 441, 16))
        self.label.setObjectName("label")
        self.createPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.createPushButton.setGeometry(QtCore.QRect(30, 170, 381, 32))
        self.createPushButton.setObjectName("createPushButton")
        self.updatePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.updatePushButton.setGeometry(QtCore.QRect(410, 170, 381, 32))
        self.updatePushButton.setObjectName("updatePushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.statusComboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>ВЫБЕРИТЕ СТАТУС ЗАКАЗА</p><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "СОЗДАТЬ НОВЫЙ ЗАКАЗ"))
        self.createPushButton.setText(_translate("MainWindow", "СОЗДАТЬ"))
        self.updatePushButton.setText(_translate("MainWindow", "ОБНОВИТЬ"))
