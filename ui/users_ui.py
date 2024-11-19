import io

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from db.CRUD import CRUDUser
from db.models import User

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>120</y>
      <width>761</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>СОХРАНИТЬ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>90</y>
      <width>761</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>ЗАГРУЗИТЬ</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>751</width>
      <height>381</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>10</y>
      <width>491</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>ЧТОБЫ ДОБАВИТЬ КЛИЕНТА, ВВЕДИТЕ ЕГО ИМЯ И ФАМИЛИЮ </string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>40</y>
      <width>331</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>введите имя клиента</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>412</x>
      <y>40</y>
      <width>361</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>введите фамилию клиента</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>24</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class UsersWidget(QMainWindow):
    def __init__(self, db_session):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.db_session = db_session
        self.crud_user = CRUDUser(User)

        self.pushButton.clicked.connect(self.save_changes)
        self.pushButton_2.clicked.connect(self.load_data)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Имя", "Фамилия"])

        self.load_data()

    def load_data(self):
        self.create_user()
        users = self.crud_user.get_all(self.db_session)

        self.tableWidget.setRowCount(len(users))
        for row_idx, user in enumerate(users):
            self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(user.id)))
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(user.name))
            self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(user.surname))

    def save_changes(self):
        """
        Сохраняет изменения из таблицы в базу данных.
        """
        for row in range(self.tableWidget.rowCount()):
            user_id = self.tableWidget.item(row, 0).text()
            name = self.tableWidget.item(row, 1).text()
            surname = self.tableWidget.item(row, 2).text()

            user = self.crud_user.get(self.db_session, int(user_id))
            if user:
                self.crud_user.update(self.db_session, user, {"name": name, "surname": surname})
            else:
                self.crud_user.create(self.db_session, {"id": user_id, "name": name, "surname": surname})

    def create_user(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        if name != 'введите имя клиента' and surname != 'введите фамилию клиента':
            self.crud_user.create(self.db_session, {'name': name, 'surname': surname})
