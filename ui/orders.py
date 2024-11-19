import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OrdersWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
