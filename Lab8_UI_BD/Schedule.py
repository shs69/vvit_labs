import psycopg2
from PyQt5.QtWidgets import (QApplication, QWidget,
                QTabWidget, QAbstractScrollArea,
                QVBoxLayout, QHBoxLayout,
                QTableWidget, QGroupBox,
                QTableWidgetItem, QPushButton, QMessageBox)

class Schedule(QWidget):
    def __init__(self, database):
        super(Schedule, self).__init__()
        self.conn = database
        self.cursor = self.conn.cursor()

        self.week = 'нечётная'
        self.days_tables = []
        self.vboxes = []
        self.days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']
        self.gboxes = []
        for i in self.days:
            self.gboxes.append(QGroupBox(i))

        self._create_schedule_tab()
    

    def _create_schedule_tab(self):
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)

        for i in range(len(self.gboxes) // 2):
            self.hbox1.addWidget(self.gboxes[i])
        for i in range(len(self.gboxes) // 2, len(self.gboxes)):
            self.hbox2.addWidget(self.gboxes[i])

        self._create_days_tables()

        self.change_week_button = QPushButton("Включить нечетную неделю")
        self.hbox3.addWidget(self.change_week_button)
        self.change_week_button.clicked.connect(self._change_week)

        self.update_schedule_button = QPushButton("Обновить")
        self.hbox3.addWidget(self.update_schedule_button)
        self.update_schedule_button.clicked.connect(self._update_days_tables)

        self.setLayout(self.vbox)

    def _change_week(self):
        if self.week == 'нечётная':
            self.week = 'чётная'
            self.change_week_button.setText('Включить четную неделю')
        else:
            self.week = 'нечётная'
            self.change_week_button.setText('Включить нечетную неделю')
        self._update_days_tables()

    def _create_days_tables(self):
        for i in range(len(self.days)):
            self.days_tables.append(QTableWidget())
            self.days_tables[i].setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
            self.days_tables[i].setColumnCount(5)
            self.days_tables[i].setHorizontalHeaderLabels(["Предмет", "Преподаватель", "Кабинет", "Начало", ""])

            self.vboxes.append(QVBoxLayout())
            self.vboxes[i].addWidget(self.days_tables[i])
            self.gboxes[i].setLayout(self.vboxes[i])
        self._update_days_tables()

    def _update_days_tables(self):
        for day in range(len(self.days)):
            self.cursor.execute("SELECT tt.subject, te.full_name, tt.room_numb, tt.start_time, tt.id\
                                FROM timetable AS tt JOIN teacher AS te ON te.subject=tt.subject\
                                WHERE day=%s and week=%s ORDER BY tt.id", [str(self.days[day]), str(self.week)])
            records = list(self.cursor.fetchall())
            self.days_tables[day].setRowCount(len(records) + 1)

            for i, r in enumerate(records):
                r = list(r)
                changeButton = QPushButton("Изменить")

                self.days_tables[day].setItem(i, 0, QTableWidgetItem(str(r[0])))
                self.days_tables[day].setItem(i, 1, QTableWidgetItem(str(r[1])))
                self.days_tables[day].setItem(i, 2, QTableWidgetItem(str(r[2])))
                self.days_tables[day].setItem(i, 3, QTableWidgetItem(str(r[3])))

                self.days_tables[day].setCellWidget(i, 4, changeButton)
                changeButton.clicked.connect(lambda ch, num=i, day=day, id=r[4]: self._change_day_from_table(num, day, id))

            self.days_tables[day].setItem(len(records), 0, QTableWidgetItem(''))
            self.days_tables[day].setItem(len(records), 1, QTableWidgetItem(''))
            self.days_tables[day].setItem(len(records), 2, QTableWidgetItem(''))
            self.days_tables[day].setItem(len(records), 3, QTableWidgetItem(''))
            changeButton = QPushButton("Добавить")
            self.days_tables[day].setCellWidget(len(records), 4, changeButton)
            changeButton.clicked.connect(lambda ch, day=day, elem=len(records): self._add_record(day, elem))

            self.days_tables[day].resizeRowsToContents()

    def _change_day_from_table(self, rowNum, day, id):
        row = list()
        for i in range(self.days_tables[day].columnCount() - 1):
            try:
                row.append(self.days_tables[day].item(rowNum, i).text())
            except:
                row.append(None)
        try:
            if row.count('') == self.days_tables[day].columnCount() - 1:
                self.cursor.execute(f"DELETE FROM timetable WHERE id={id}")
            else:
                self.cursor.execute(f"UPDATE timetable SET subject='{row[0]}', start_time='{row[3]}', \
                                     room_numb={row[2]}, week={self.week} WHERE id={id}")
            self.conn.commit()
        except BaseException as E:
            QMessageBox.about(self, "Error", str(E))
            print(E)
            self.conn.rollback()
        finally:
            self._update_days_tables()

    def _add_record(self, day, row):
        data = [self.days_tables[day].item(row, 0).text(),
                self.days_tables[day].item(row, 1).text(),
                self.days_tables[day].item(row, 2).text(),
                self.days_tables[day].item(row, 3).text()]
        try:
            self.cursor.execute(f"INSERT INTO timetable (subject, day, room_numb, start_time, week)\
                            VALUES ('{data[0]}', '{self.days[day]}','{data[2]}', '{data[3]}', '{str(self.week)}')")
            self.cursor.execute(f"insert into teacher (full_name, subject) values ('{data[1]}', '{data[0]}')")
            self.cursor.execute(f"insert into subject (name) values ('{data[0]}')")
            self.conn.commit()
        except BaseException as E:
            QMessageBox.about(self, "Error", str(E))
            print(E)
            self.conn.rollback()
        finally:
            self._update_days_tables()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    conn = psycopg2.connect(database="lab8",
                                     user="postgres",
                                     password="A048kp46",
                                     host="localhost",
                                     port="5432")
    cursor = conn.cursor()
    win = Schedule(conn)
    win.showMaximized()
    sys.exit(app.exec_())

