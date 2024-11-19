import io
import sys

from PyQt5 import uic
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem

from db.CRUD import CRUDOrder
from db.CRUD import CRUDProducts
from db.CRUD import CRUDUser
from db.models import Order, Type, User

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
   <widget class="QListWidget" name="listWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>220</y>
      <width>751</width>
      <height>321</height>
     </rect>
    </property>
   </widget>
   <widget class="QDateEdit" name="endDateEdit">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>40</y>
      <width>110</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
   <widget class="QDateEdit" name="startDateEdit">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>40</y>
      <width>110</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
   <widget class="QComboBox" name="typeOfProductionComboBox">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>40</y>
      <width>104</width>
      <height>26</height>
     </rect>
    </property>
   </widget>
   <widget class="QComboBox" name="cliendComboBox">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>40</y>
      <width>104</width>
      <height>26</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="commentTextEdit">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>80</y>
      <width>721</width>
      <height>79</height>
     </rect>
    </property>
   </widget>
   <widget class="QSpinBox" name="countSpinBox">
    <property name="geometry">
     <rect>
      <x>700</x>
      <y>40</y>
      <width>48</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
   <widget class="QComboBox" name="statusComboBox">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>40</y>
      <width>121</width>
      <height>26</height>
     </rect>
    </property>
    <property name="toolTip">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;ВЫБЕРИТЕ СТАТУС ЗАКАЗА&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>10</y>
      <width>441</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>СОЗДАТЬ НОВЫЙ ЗАКАЗ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="createPushButton">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>170</y>
      <width>381</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>СОЗДАТЬ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="updatePushButton">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>170</y>
      <width>381</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>ОБНОВИТЬ</string>
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


class OrdersWidget(QMainWindow):
    def __init__(self, db_session):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.db_session = db_session

        self.crud_order = CRUDOrder(Order)
        self.crud_products = CRUDProducts(Type)
        self.crud_customers = CRUDUser(User)

        self.createPushButton.clicked.connect(self.create_order)
        self.updatePushButton.clicked.connect(self.update_order)

        self.countSpinBox.setMinimum(0)
        self.countSpinBox.setMaximum(2147483647)

        self.load_data()
        self.initComboBoxes()

    def load_data(self):
        """Загружаем данные для списка заказов"""
        with self.db_session() as session:
            orders = self.crud_order.get_all(session)
            self.listWidget.clear()
            for order in orders:
                item_text = (f"Статус: {order.status}, Дата регистрации: {order.time_registration}, "
                             f"Дата выпуска: {order.time_ready}, Клиент: {order.user}, "
                             f"Вид продукции: {order.type}, Количество: {order.count}, "
                             f"Комментарий: {order.comment}")

                list_item = QListWidgetItem(item_text)

                if order.status == 'Согласован клиентом':
                    list_item.setForeground(QBrush(QColor('orange')))
                elif order.status == 'Принят в производство':
                    list_item.setForeground(QBrush(QColor('yellow')))
                elif order.status == 'Выполнен':
                    list_item.setForeground(QBrush(QColor('green')))

                self.listWidget.addItem(list_item)

    def initComboBoxes(self):
        """Инициализируем комбобоксы"""
        types_of_products = self.crud_products.get_all(self.db_session)

        self.typeOfProductionComboBox.clear()
        self.typeOfProductionComboBox.addItem("<Не выбрано>")
        self.typeOfProductionComboBox.addItems([product.title for product in types_of_products])

        customers = self.crud_customers.get_all(self.db_session)

        self.cliendComboBox.clear()
        self.cliendComboBox.addItem("<Не выбрано>")
        self.cliendComboBox.addItems([' '.join([customer.name, customer.surname]) for customer in customers])

        self.statusComboBox.clear()
        self.statusComboBox.addItem("<Не выбрано>")
        self.statusComboBox.addItems(['Черновик', 'Согласован клиентом', 'Принят в производство', 'Выполнен'])

    def create_order(self):
        """Создание нового заказа"""
        # Получаем данные из UI элементов
        client = self.cliendComboBox.currentText()
        product_type = self.typeOfProductionComboBox.currentText()

        start_date = self.startDateEdit.date().toString('yyyy-MM-dd')
        end_date = self.endDateEdit.date().toString('yyyy-MM-dd')

        if self.startDateEdit.date() >= self.endDateEdit.date():
            return

        quantity = self.countSpinBox.value()
        comment = self.commentTextEdit.toPlainText()
        status = self.statusComboBox.currentText() if client != '<Не выбрано>' and product_type != '<Не выбрано>' and quantity != 0 else 'Черновик'

        order_data = {
            'time_registration': start_date,
            'time_ready': end_date,
            'count': quantity,
            'comment': comment,
            'status': status,
            'user': client,
            'type': product_type
        }

        with self.db_session() as session:
            self.crud_order.create(session, order_data)
            self.load_data()  # Обновляем данные на UI

    def update_order(self):
        """Обновление существующего заказа"""
        selected_item = self.listWidget.currentItem()
        if selected_item:
            order_id = int(selected_item.text().split(":")[1].strip())
            order_data = {
                'status': self.statusComboBox.currentText(),
                'quantity': self.countSpinBox.value(),
                'comment': self.commentTextEdit.toPlainText(),
            }

            with self.db_session() as session:
                updated_order = self.crud_order.update(session, order_id, order_data)
                self.load_data()  # Обновляем список заказов


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OrdersWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
