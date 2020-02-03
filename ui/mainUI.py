# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wishListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.wishListWidget.setGeometry(QtCore.QRect(20, 10, 411, 501))
        self.wishListWidget.setObjectName("wishListWidget")
        self.newWishItemBox = QtWidgets.QGroupBox(self.centralwidget)
        self.newWishItemBox.setGeometry(QtCore.QRect(450, 10, 321, 491))
        self.newWishItemBox.setObjectName("newWishItemBox")
        self.addWishItemButton = QtWidgets.QPushButton(self.newWishItemBox)
        self.addWishItemButton.setGeometry(QtCore.QRect(170, 410, 141, 61))
        self.addWishItemButton.setObjectName("addWishItemButton")
        self.nameLabel = QtWidgets.QLabel(self.newWishItemBox)
        self.nameLabel.setGeometry(QtCore.QRect(30, 50, 41, 21))
        self.nameLabel.setObjectName("nameLabel")
        self.priceLabel = QtWidgets.QLabel(self.newWishItemBox)
        self.priceLabel.setGeometry(QtCore.QRect(30, 100, 54, 17))
        self.priceLabel.setObjectName("priceLabel")
        self.nameWishItemEdit = QtWidgets.QLineEdit(self.newWishItemBox)
        self.nameWishItemEdit.setGeometry(QtCore.QRect(70, 50, 239, 25))
        self.nameWishItemEdit.setObjectName("nameWishItemEdit")
        self.priceWishItemEdit = QtWidgets.QLineEdit(self.newWishItemBox)
        self.priceWishItemEdit.setGeometry(QtCore.QRect(70, 100, 239, 25))
        self.priceWishItemEdit.setObjectName("priceWishItemEdit")
        self.urlLabel = QtWidgets.QLabel(self.newWishItemBox)
        self.urlLabel.setGeometry(QtCore.QRect(30, 150, 31, 17))
        self.urlLabel.setObjectName("urlLabel")
        self.noteLabel = QtWidgets.QLabel(self.newWishItemBox)
        self.noteLabel.setGeometry(QtCore.QRect(20, 280, 54, 17))
        self.noteLabel.setObjectName("noteLabel")
        self.urlWishItemEdit = QtWidgets.QLineEdit(self.newWishItemBox)
        self.urlWishItemEdit.setGeometry(QtCore.QRect(70, 150, 239, 25))
        self.urlWishItemEdit.setObjectName("urlWishItemEdit")
        self.notesTextEdit = QtWidgets.QTextEdit(self.newWishItemBox)
        self.notesTextEdit.setGeometry(QtCore.QRect(70, 210, 241, 161))
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.resetTextButton = QtWidgets.QPushButton(self.newWishItemBox)
        self.resetTextButton.setGeometry(QtCore.QRect(10, 410, 141, 61))
        self.resetTextButton.setObjectName("resetTextButton")
        self.updateWishListButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateWishListButton.setGeometry(QtCore.QRect(80, 520, 131, 31))
        self.updateWishListButton.setObjectName("updateWishListButton")
        self.totalLiteralLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLiteralLabel.setGeometry(QtCore.QRect(240, 520, 71, 31))
        self.totalLiteralLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalLiteralLabel.setObjectName("totalLiteralLabel")
        self.TotalPriceLabel = QtWidgets.QLabel(self.centralwidget)
        self.TotalPriceLabel.setGeometry(QtCore.QRect(300, 520, 71, 31))
        self.TotalPriceLabel.setObjectName("TotalPriceLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.newWishItemBox.setTitle(_translate("MainWindow", "New Item!"))
        self.addWishItemButton.setText(_translate("MainWindow", "Add to wishlist"))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.priceLabel.setText(_translate("MainWindow", "Price:"))
        self.urlLabel.setText(_translate("MainWindow", "Url:"))
        self.noteLabel.setText(_translate("MainWindow", "Notes:"))
        self.resetTextButton.setText(_translate("MainWindow", "Reset"))
        self.updateWishListButton.setText(_translate("MainWindow", "Update list"))
        self.totalLiteralLabel.setText(_translate("MainWindow", "Total:"))
        self.TotalPriceLabel.setText(_translate("MainWindow", "0"))
