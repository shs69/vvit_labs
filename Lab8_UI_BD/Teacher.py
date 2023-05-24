import psycopg2
from PyQt5.QtWidgets import (QApplication, QWidget,
                QTabWidget, QAbstractScrollArea,
                QVBoxLayout, QHBoxLayout,
                QTableWidget, QGroupBox,
                QTableWidgetItem, QPushButton, QMessageBox)


class Teacher(QWidget):
    def __init__(self, database):
        super(Teacher, self).__init__()
        self.conn = database
        self.cursor = self.conn.cursor()

        self._create_teacher_tab()
    
    def _create_teacher_tab(self):
        self.gbox = QGroupBox("Преподаватели")

        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)

        self.hbox1.addWidget(self.gbox)

        self._create_teacher_table()

        self.update_teacher_button = QPushButton("Обновить")
        self.hbox2.addWidget(self.update_teacher_button)
        self.update_teacher_button.clicked.connect(self._update_teacher_table)

        self.setLayout(self.vbox)
    
    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(3)
        self.teacher_table.setHorizontalHeaderLabels(["Имя", "Предмет", ""])

        self.vbox_table = QVBoxLayout()
        self.vbox_table.addWidget(self.teacher_table)
        self.gbox.setLayout(self.vbox_table)

        self._update_teacher_table()

    def _update_teacher_table(self):


        self.cursor.execute("SELECT full_name, subject, id FROM teacher ORDER BY full_name")
        records = list(self.cursor.fetchall())
        self.teacher_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            changeButton = QPushButton("Изменить")

            self.teacher_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem(i, 1, QTableWidgetItem(str(r[1])))

            self.teacher_table.setCellWidget(i, 2, changeButton)
            changeButton.clicked.connect(lambda ch, num=i, id=r[2]: self._change_teacher(num, id))

        self.teacher_table.setItem(len(records), 0, QTableWidgetItem(''))
        self.teacher_table.setItem(len(records), 1, QTableWidgetItem(''))
        changeButton = QPushButton("Добавить")
        self.teacher_table.setCellWidget(len(records), 2, changeButton)
        changeButton.clicked.connect(lambda ch, row=len(records): self._add_record(row))

        self.teacher_table.resizeRowsToContents()
    
    def _change_teacher(self, rowNum, id):
        row = list()
        for i in range(self.teacher_table.columnCount() - 1):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            if row.count('') == self.teacher_table.columnCount() - 1:
                self.cursor.execute(f"DELETE FROM teacher WHERE id={id}")
            else:
                self.cursor.execute(f"UPDATE teacher SET full_name='{row[0]}', subject='{row[1]}'\
                                    WHERE id={id}")
            self.conn.commit()
        except BaseException as E:
            QMessageBox.about(self, "Error", str(E))
            self.conn.rollback()
        finally:
            self._update_teacher_table()

    def _add_record(self, row):
        data = [self.teacher_table.item(row, 0).text(),
                self.teacher_table.item(row, 1).text()]
        try:
            self.cursor.execute(f"INSERT INTO teacher (full_name, subject)\
                                VALUES ('{data[0]}', '{data[1]}')")
            self.conn.commit()
        except BaseException as E:
            QMessageBox.about(self, "Error", str(E))
            self.conn.rollback()
        finally:
            self._update_teacher_table()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    conn = psycopg2.connect(database="lab8",
                                     user="postgres",
                                     password="A048kp46",
                                     host="localhost",
                                     port="5432")
    cursor = conn.cursor()
    win = Teacher(conn)
    win.showMaximized()
    sys.exit(app.exec_())



    # Чистый код 