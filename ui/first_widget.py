import sys
import io

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>369</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>30</y>
     <width>241</width>
     <height>71</height>
    </rect>
   </property>
   <property name="text">
    <string>Коммерческая слубжа</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton_2">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>110</y>
     <width>241</width>
     <height>71</height>
    </rect>
   </property>
   <property name="text">
    <string>Служба производства</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton_3">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>190</y>
     <width>241</width>
     <height>71</height>
    </rect>
   </property>
   <property name="text">
    <string>Служба технолога</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

'''


class StartWidget(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
