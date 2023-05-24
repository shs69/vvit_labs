import psycopg2
from PyQt5.QtWidgets import (QApplication, QWidget,
                QTabWidget, QAbstractScrollArea,
                QVBoxLayout, QHBoxLayout,
                QTableWidget, QGroupBox,
                QTableWidgetItem, QPushButton, QMessageBox)

class Subject(QWidget):
    def __init__(self, database):
        super(Subject, self).__init__()
        self.conn = database
        self.cursor = self.conn.cursor()

        self._create_subject_tab()
    
    def _create_subject_tab(self):
        self.gbox = QGroupBox("Предметы")

        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)

        self.hbox1.addWidget(self.gbox)

        self._create_subject_table()

        self.update_subject_button = QPushButton("Обновить")
        self.hbox2.addWidget(self.update_subject_button)
        self.update_subject_button.clicked.connect(self._update_subject_table)

        self.setLayout(self.vbox)
    
    def _create_subject_table(self):
        self.subject_table = QTableWidget()
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subject_table.setColumnCount(2)
        self.subject_table.setHorizontalHeaderLabels(["Название", ""])

        self.vbox_table = QVBoxLayout()
        self.vbox_table.addWidget(self.subject_table)
        self.gbox.setLayout(self.vbox_table)

        self._update_subject_table()

    def _update_subject_table(self):
        self.cursor.execute("SELECT name, id \
                             FROM subject ORDER BY name")
        records = list(self.cursor.fetchall())
        self.subject_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            changeButton = QPushButton("Изменить")

            self.subject_table.setItem(i, 0, QTableWidgetItem(str(r[0])))

            self.subject_table.setCellWidget(i, 1, changeButton)
            changeButton.clicked.connect(lambda ch, num=i, id=r[1]: self._change_subject(num, id))

        self.subject_table.setItem(len(records), 0, QTableWidgetItem(''))
        changeButton = QPushButton("Добавить")
        self.subject_table.setCellWidget(len(records), 1, changeButton)
        changeButton.clicked.connect(lambda ch, row=len(records): self._add_record(row))

        self.subject_table.resizeRowsToContents()
    
    def _change_subject(self, rowNum, id):
        row = list()
        for i in range(self.subject_table.columnCount() - 1):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            if row.count('') == self.subject_table.columnCount() - 1:
                self.cursor.execute(f"DELETE FROM subject WHERE id={id}")
            else:
                self.cursor.execute(f"UPDATE subject SET name='{row[0]}'\
                                    WHERE id={id}")
            self.conn.commit()
        except BaseException as E:
            QMessageBox.about(self, "Error", str(E))
            self.conn.rollback()
        finally:
            self._update_subject_table()

    def _add_record(self, row):
        try:
            self.cursor.execute(f"INSERT INTO subject (name)\
                                VALUES ('{self.subject_table.item(row, 0).text()}')")
            self.conn.commit()
        except BaseException as E:
            QMessageBox.about(self, "Error", str(E))
            self.conn.rollback()
        finally:
            self._update_subject_table()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    conn = psycopg2.connect(database="lab8",
                                     user="postgres",
                                     password="A048kp46",
                                     host="localhost",
                                     port="5432")
    cursor = conn.cursor()
    win = Subject(conn)
    win.showMaximized()
    sys.exit(app.exec_())