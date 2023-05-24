import psycopg2
import sys


from PyQt5.QtWidgets import (QApplication, QWidget,
            QTabWidget, QAbstractScrollArea,
            QVBoxLayout, QHBoxLayout,
            QTableWidget, QGroupBox,
            QTableWidgetItem, QPushButton, QMessageBox)
            
from Schedule import Schedule
from Teacher import Teacher
from Subject import Subject


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()
        self.setWindowTitle("telegram_bot_db")

        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self.schedule_tab = Schedule(self.conn)
        self.tabs.addTab(self.schedule_tab, 'Расписание')

        self.teacher_tab = Teacher(self.conn)
        self.tabs.addTab(self.teacher_tab, 'Преподаватели')

        self.subject_tab = Subject(self.conn)
        self.tabs.addTab(self.subject_tab, 'Предметы')
    
    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="lab8",
                                     user="postgres",
                                     password="A048kp46",
                                     host="localhost",
                                     port="5432")
        self.cursor = self.conn.cursor()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    sys.exit(app.exec_())