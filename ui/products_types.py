import io

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from db.CRUD import CRUDProducts
from db.models import Type

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
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>130</y>
      <width>731</width>
      <height>381</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>80</y>
      <width>721</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>СОЗДАТЬ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>520</y>
      <width>721</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>ОБНОВИТЬ</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>40</y>
      <width>721</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>                                               ВВЕДИТЕ НАЗВАНИЕ НОВОГО ВИДА ЛЕСОПРОДУКЦИИ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>10</y>
      <width>601</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>ЧТОБЫ ДОБАВИТЬ НОВЫЙ ВИД ЛЕСОПРОДУКЦИИ, ВВЕДИТЕ НИЖЕ ЕГО НАЗВАНИЕ</string>
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


class ProductsWidget(QMainWindow):
    def __init__(self, db_session):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.db_session = db_session
        self.crud_products = CRUDProducts(Type)

        # Подключение кнопок к методам
        self.pushButton.clicked.connect(self.create_type)
        self.pushButton_2.clicked.connect(self.update_selected_type)

        # Настройка таблицы
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название"])
        self.tableWidget.cellClicked.connect(self.load_selected_type)

        # Загрузка данных в таблицу
        self.load_data()

    def load_data(self):
        """Загружает данные из базы данных в таблицу."""
        types = self.crud_products.get_all(self.db_session)
        self.tableWidget.setRowCount(len(types))
        for row_idx, type_ in enumerate(types):
            self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(type_.id)))
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(type_.title))

    def create_type(self):
        """Создает новый тип продукции."""
        title = self.lineEdit.text().strip()
        if not title:
            QMessageBox.warning(self, "Ошибка", "Название не может быть пустым.")
            return

        existing = self.crud_products.get_all(self.db_session)
        if any(t.title == title for t in existing):
            QMessageBox.warning(self, "Ошибка", "Тип продукции с таким названием уже существует.")
            return

        new_type = self.crud_products.create(self.db_session, {"title": title})
        if new_type:
            self.lineEdit.clear()
            self.load_data()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось создать тип продукции.")

    def load_selected_type(self, row, column):
        """Загружает выбранный тип продукции в строку ввода."""
        title = self.tableWidget.item(row, 1).text()
        self.lineEdit.setText(title)

    def update_selected_type(self):
        """Обновляет название выбранного типа продукции."""
        row = self.tableWidget.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите запись для обновления.")
            return

        type_id = int(self.tableWidget.item(row, 0).text())
        new_title = self.lineEdit.text().strip()
        if not new_title:
            QMessageBox.warning(self, "Ошибка", "Название не может быть пустым.")
            return

        type_obj = self.crud_products.get(self.db_session, type_id)
        if type_obj:
            self.crud_products.update(self.db_session, type_obj, {"title": new_title})
            self.load_data()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось обновить запись.")
