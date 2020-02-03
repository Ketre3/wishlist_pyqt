from PyQt5.QtWidgets import QMessageBox, QDialog
from ui import Ui_WishItem
import MySQLdb as mdb


class WishItemWidget(QDialog, Ui_WishItem):
    def __init__(self, parent, id, name, price, url, notes):
        super().__init__(parent)
        self.setupUi(self)
        self.id = id
        self.parent = parent
        self.is_updating = False
        self.add_info(name, price, url, notes)
        self.connect_buttons()

    def add_info(self, name, price, url, notes):
        self.nameWishItemEdit.setText(name)
        self.priceWishItemEdit.setText(str(price))
        self.urlWishItemEdit.setText(url)
        self.notesEdit.setText(notes)

    def change_update(self):
        if not self.is_updating:
            # open for update
            self.nameWishItemEdit.setReadOnly(False)
            self.priceWishItemEdit.setReadOnly(False)
            self.urlWishItemEdit.setReadOnly(False)
            self.notesEdit.setReadOnly(False)

            self.changeUpdateButton.setText("Update")
            self.is_updating = True
        else:
            name = self.nameWishItemEdit.text()
            price = self.priceWishItemEdit.text()
            url = self.urlWishItemEdit.text()
            notes = self.notesEdit.toPlainText()
            try:
                self.parent.update_item(self.id, name, price, url, notes)
            except mdb.IntegrityError:
                QMessageBox.critical(
                    self,
                    "Wrong data!",
                    f"You already have item \"{name}\"!\n"
                    "Change name and try again."
                )
            else:
                QMessageBox.information(
                    self,
                    "Updated!",
                    "Item has been updated!"
                )

                self.close()

    def delete(self):
        self.parent.delete_item(self.id)
        QMessageBox.information(
                self,
                "Deleted!",
                "Item has been deleted!"
        )
        self.close()

    def connect_buttons(self):
        self.changeUpdateButton.clicked.connect(self.change_update)
        self.deleteButton.clicked.connect(self.delete)
