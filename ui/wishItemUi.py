# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wishItem.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(426, 522)
        self.nameLabel = QtWidgets.QLabel(Form)
        self.nameLabel.setGeometry(QtCore.QRect(20, 50, 54, 17))
        self.nameLabel.setObjectName("nameLabel")
        self.priceLabel = QtWidgets.QLabel(Form)
        self.priceLabel.setGeometry(QtCore.QRect(20, 100, 54, 17))
        self.priceLabel.setObjectName("priceLabel")
        self.urlLabel = QtWidgets.QLabel(Form)
        self.urlLabel.setGeometry(QtCore.QRect(20, 160, 54, 17))
        self.urlLabel.setObjectName("urlLabel")
        self.nameWishItemEdit = QtWidgets.QLineEdit(Form)
        self.nameWishItemEdit.setGeometry(QtCore.QRect(70, 50, 311, 25))
        self.nameWishItemEdit.setReadOnly(True)
        self.nameWishItemEdit.setObjectName("nameWishItemEdit")
        self.urlWishItemEdit = QtWidgets.QLineEdit(Form)
        self.urlWishItemEdit.setGeometry(QtCore.QRect(70, 160, 311, 25))
        self.urlWishItemEdit.setReadOnly(True)
        self.urlWishItemEdit.setObjectName("urlWishItemEdit")
        self.priceWishItemEdit = QtWidgets.QLineEdit(Form)
        self.priceWishItemEdit.setGeometry(QtCore.QRect(70, 100, 311, 25))
        self.priceWishItemEdit.setReadOnly(True)
        self.priceWishItemEdit.setObjectName("priceWishItemEdit")
        self.notesEdit = QtWidgets.QTextEdit(Form)
        self.notesEdit.setGeometry(QtCore.QRect(70, 220, 311, 111))
        self.notesEdit.setReadOnly(True)
        self.notesEdit.setObjectName("notesEdit")
        self.notesLabel = QtWidgets.QLabel(Form)
        self.notesLabel.setGeometry(QtCore.QRect(20, 270, 54, 17))
        self.notesLabel.setObjectName("notesLabel")
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setGeometry(QtCore.QRect(40, 380, 141, 101))
        self.deleteButton.setObjectName("deleteButton")
        self.changeUpdateButton = QtWidgets.QPushButton(Form)
        self.changeUpdateButton.setGeometry(QtCore.QRect(240, 380, 141, 101))
        self.changeUpdateButton.setObjectName("changeUpdateButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nameLabel.setText(_translate("Form", "Name:"))
        self.priceLabel.setText(_translate("Form", "Price:"))
        self.urlLabel.setText(_translate("Form", "Url:"))
        self.notesLabel.setText(_translate("Form", "Notes:"))
        self.deleteButton.setText(_translate("Form", "Delete"))
        self.changeUpdateButton.setText(_translate("Form", "Change"))
