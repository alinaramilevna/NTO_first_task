import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

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
     <string>                                ИМЯ КЛИЕНТА</string>
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
     <string>                                ФАМИЛИЯ КЛИЕНТА</string>
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
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UsersWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
