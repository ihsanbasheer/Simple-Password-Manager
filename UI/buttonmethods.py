import sqlite3
from PyQt5.QtWidgets import  QMessageBox, QTableWidgetItem


class Buttons(object): # Functions of Buttons
    
    def button_features(self):
        self.loginbutton.clicked.connect(self.loginmain)
        self.addbutton.clicked.connect(self.add_entry)
        self.updatebutton.clicked.connect(self.update_entry)
        self.removebutton.clicked.connect(self.remove_entry)
        self.refreshbutton.clicked.connect(self.refresh_table)
        
    def loginmain(self):
        l_username = self.userinputlogin.text()
        l_password = self.passinputlogin.text()
        
        if l_username == self.MASTERLOGIN and l_password == self.MASTERPASS:
            self.stackedWidget.setCurrentWidget(self.mainpage)
        else:
            QMessageBox.warning(self.loginpage, 'ACCESS DENIED', 'Incorrect username or password')  
              
    def populate_table(self):
        connect = sqlite3.connect("login_info.db")
        d = connect.cursor()
        d.execute('SELECT * FROM login')
        data = d.fetchall()

        for row, (username, password) in enumerate(data):
            self.tableview.insertRow(row)
            self.tableview.setItem(row, 0, QTableWidgetItem(username))
            self.tableview.setItem(row, 1, QTableWidgetItem(password))

    def clear_table(self): 
        self.tableview.clearContents()
        self.tableview.setRowCount(0)
        
    def add_entry(self):
        username = self.userinput.text()
        password = self.passinput.text()

        if not username or not password:
            return

        connect = sqlite3.connect("login_info.db")
        d = connect.cursor()
        d.execute('SELECT * FROM login WHERE username = ?', (username,))
        existing_user = d.fetchone()

        if existing_user:
            QMessageBox.warning(self.tableview, 'Duplicate Username', 'Username already exists. Please choose a different username.')
        else:
            d.execute('INSERT INTO login VALUES (?, ?)', (username, password))
            connect.commit()

            row_position = self.tableview.rowCount()
            self.tableview.insertRow(row_position)
            self.tableview.setItem(row_position, 0, QTableWidgetItem(username))
            self.tableview.setItem(row_position, 1, QTableWidgetItem(password))

    def update_entry(self):
        username = self.userinput.text()
        password = self.passinput.text()
        row_position = self.find_row_position(username)

        self.tableview.setItem(row_position, 1, QTableWidgetItem(password))

        if username and password:
            connect = sqlite3.connect("login_info.db")
            d = connect.cursor()
            d.execute('UPDATE login SET pass = ? WHERE username = ?', (password, username))
            connect.commit()

    def remove_entry(self):
        username = self.userinput.text()
        row_position = self.find_row_position(username)

        if row_position != -1:
            self.tableview.removeRow(row_position)

            connect = sqlite3.connect("login_info.db")
            d = connect.cursor()
            d.execute('DELETE FROM login WHERE username = ?', (username,))
            connect.commit()

    def refresh_table(self):
        self.clear_table()
        self.populate_table()

    def find_row_position(self, username):
        for row in range(self.tableview.rowCount()):
            item = self.tableview.item(row, 0)
            if item is not None and item.text() == username:
                return row
        return -1