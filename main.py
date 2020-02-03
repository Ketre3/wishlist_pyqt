from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui import Ui_MainWindow
from wishItem import WishItemWidget

import sys
import MySQLdb as mdb
import operator


DATABASE_SETTINGS = {
    'host': None,  # change this
    'user': None,  # change this
    'passwd': None,   # change this
    'db': None,  # change this
}


if not DATABASE_SETTINGS.get('host', None):
    raise Exception('Add database connection settings!')



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setup_db()
        self.connect_buttons()

        self.load_wish_list()

    def setup_db(self):
        CREATE_TABLE_Q = \
        """
        CREATE TABLE IF NOT EXISTS wishlist (
            id    INT         NOT NULL    AUTO_INCREMENT,
            name  VARCHAR(64) UNIQUE      NOT NULL,
            price FLOAT       DEFAULT 0.0,
            url   VARCHAR(64),
            notes VARCHAR(256),
            PRIMARY KEY (id)
        )
        """
        self.db = mdb.connect(**DATABASE_SETTINGS)
        self.db.query(CREATE_TABLE_Q)
        self.db.commit()

    def show_wishItem(self, nameIndex):
        INFO_Q = \
        """
        SELECT id, price, url, notes FROM wishlist
        WHERE name=%s
        """
        name = nameIndex.data()
        cur = self.db.cursor()
        cur.execute(INFO_Q, (name,))
        id, price, url, notes = cur.fetchone()
        wish_item = WishItemWidget(self, id, name, price, url, notes)
        wish_item.show()

    def load_wish_list(self):
        cur = self.db.cursor()
        cur.execute("SELECT name, SUM(price) FROM wishlist GROUP BY name")
        items = cur.fetchall()

        cur.execute("SELECT SUM(price) FROM wishlist")
        price = cur.fetchone()[0]

        self.wishListWidget.clear()
        self.wishListWidget.addItems(map(operator.itemgetter(0), items))

        self.TotalPriceLabel.setText(str(price))


    def clear_item_fields(self):
        self.nameWishItemEdit.clear()
        self.priceWishItemEdit.clear()
        self.urlWishItemEdit.clear()
        self.notesTextEdit.clear()

    def add_item(self):
        name = self.nameWishItemEdit.text()
        price = self.priceWishItemEdit.text()
        url = self.urlWishItemEdit.text()
        notes = self.notesTextEdit.toPlainText()

        INSERT_Q = \
        """
        INSERT INTO wishlist(name, price, url, notes) VALUES
        (%s, %s, %s, %s)
        """
        cursor = self.db.cursor()
        try:
            cursor.execute(INSERT_Q, (name, price, url, notes))
            self.db.commit()
        except mdb.DataError:
            QMessageBox.critical(
                self,
                "Wrong data!",
                "There's something wrong with your data, "
                "please check and try again!"
                )
        except mdb.IntegrityError:
            QMessageBox.critical(
                self,
                "Wrong data!",
                f"You already have item \"{name}\"!"
            )
        else:
            self.clear_item_fields()
            self.load_wish_list()

    def update_item(self, id, name, price, url, notes):
        UPDATE_Q = \
        """
        UPDATE wishlist SET
        name=%s,
        price=%s,
        url=%s,
        notes=%s
        WHERE id=%s
        """
        cur = self.db.cursor()
        cur.execute(UPDATE_Q, (name, price, url, notes, id))
        self.db.commit()

        self.load_wish_list()

    def delete_item(self, id):
        DELETE_Q = "DELETE FROM wishlist WHERE id=%s"

        cur = self.db.cursor()
        cur.execute(DELETE_Q, (id,))
        self.db.commit()

        self.load_wish_list()

    def connect_buttons(self):
        self.wishListWidget.doubleClicked.connect(self.show_wishItem)

        self.addWishItemButton.clicked.connect(self.add_item)
        self.resetTextButton.clicked.connect(self.clear_item_fields)
        self.updateWishListButton.clicked.connect(self.load_wish_list)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
