# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DungeonAttackUI.ui'
#
# Created: Fri Dec  2 12:05:21 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 765)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.labelInitialHit = QtWidgets.QLabel(self.centralWidget)
        self.labelInitialHit.setGeometry(QtCore.QRect(30, 10, 331, 23))
        self.labelInitialHit.setObjectName("labelInitialHit")
        self.lineEditHitPoints = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditHitPoints.setGeometry(QtCore.QRect(390, 10, 81, 35))
        self.lineEditHitPoints.setObjectName("lineEditHitPoints")
        self.labelMonsters = QtWidgets.QLabel(self.centralWidget)
        self.labelMonsters.setGeometry(QtCore.QRect(40, 60, 71, 16))
        self.labelMonsters.setObjectName("labelMonsters")
        self.labelAttackName = QtWidgets.QLabel(self.centralWidget)
        self.labelAttackName.setGeometry(QtCore.QRect(160, 90, 101, 23))
        self.labelAttackName.setObjectName("labelAttackName")
        self.labelAttackValue = QtWidgets.QLabel(self.centralWidget)
        self.labelAttackValue.setGeometry(QtCore.QRect(310, 90, 101, 23))
        self.labelAttackValue.setObjectName("labelAttackValue")
        self.checkBoxDragon = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBoxDragon.setGeometry(QtCore.QRect(20, 120, 103, 28))
        self.checkBoxDragon.setObjectName("checkBoxDragon")
        self.checkBoxElf = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBoxElf.setGeometry(QtCore.QRect(20, 160, 103, 28))
        self.checkBoxElf.setObjectName("checkBoxElf")
        self.checkBoxDwarf = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBoxDwarf.setGeometry(QtCore.QRect(20, 200, 103, 28))
        self.checkBoxDwarf.setObjectName("checkBoxDwarf")
        self.checkBoxNecromancer = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBoxNecromancer.setGeometry(QtCore.QRect(20, 240, 131, 28))
        self.checkBoxNecromancer.setObjectName("checkBoxNecromancer")
        self.lineEditDragonAttack = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditDragonAttack.setGeometry(QtCore.QRect(150, 120, 113, 31))
        self.lineEditDragonAttack.setObjectName("lineEditDragonAttack")
        self.lineEditElfAttack = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditElfAttack.setGeometry(QtCore.QRect(150, 160, 113, 31))
        self.lineEditElfAttack.setObjectName("lineEditElfAttack")
        self.lineEditDwarfAttack = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditDwarfAttack.setGeometry(QtCore.QRect(150, 200, 113, 31))
        self.lineEditDwarfAttack.setObjectName("lineEditDwarfAttack")
        self.lineEditNecromancerAttack = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditNecromancerAttack.setGeometry(QtCore.QRect(150, 240, 113, 31))
        self.lineEditNecromancerAttack.setObjectName("lineEditNecromancerAttack")
        self.lineEditDragonValue = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditDragonValue.setGeometry(QtCore.QRect(300, 120, 113, 31))
        self.lineEditDragonValue.setObjectName("lineEditDragonValue")
        self.lineEditElfValue = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditElfValue.setGeometry(QtCore.QRect(300, 160, 113, 31))
        self.lineEditElfValue.setObjectName("lineEditElfValue")
        self.lineEditDwarfValue = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditDwarfValue.setGeometry(QtCore.QRect(300, 200, 113, 31))
        self.lineEditDwarfValue.setObjectName("lineEditDwarfValue")
        self.lineEditNecormancerValue = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditNecormancerValue.setGeometry(QtCore.QRect(300, 240, 113, 31))
        self.lineEditNecormancerValue.setObjectName("lineEditNecormancerValue")
        self.pushButtonAttack = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonAttack.setGeometry(QtCore.QRect(170, 300, 106, 33))
        self.pushButtonAttack.setObjectName("pushButtonAttack")
        self.labelResults = QtWidgets.QLabel(self.centralWidget)
        self.labelResults.setGeometry(QtCore.QRect(20, 340, 73, 23))
        self.labelResults.setObjectName("labelResults")
        self.labelContent = QtWidgets.QLabel(self.centralWidget)
        self.labelContent.setGeometry(QtCore.QRect(20, 382, 471, 331))
        self.labelContent.setText("")
        self.labelContent.setObjectName("labelContent")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 501, 29))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelInitialHit.setText(_translate("MainWindow", "Enter your initial hit points (between 1-200):"))
        self.labelMonsters.setText(_translate("MainWindow", "Monsters"))
        self.labelAttackName.setText(_translate("MainWindow", "Attack Name"))
        self.labelAttackValue.setText(_translate("MainWindow", "Attack Value"))
        self.checkBoxDragon.setText(_translate("MainWindow", "Dragon"))
        self.checkBoxElf.setText(_translate("MainWindow", "Elf"))
        self.checkBoxDwarf.setText(_translate("MainWindow", "Dwarf"))
        self.checkBoxNecromancer.setText(_translate("MainWindow", "Necromancer"))
        self.pushButtonAttack.setText(_translate("MainWindow", "Attack!"))
        self.labelResults.setText(_translate("MainWindow", "Results:"))

