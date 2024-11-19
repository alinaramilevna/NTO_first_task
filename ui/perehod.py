import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication

template = '''
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>482</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="usersPushButton">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>20</y>
     <width>221</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>Работа с клиентами</string>
   </property>
  </widget>
  <widget class="QPushButton" name="ordersPushButton">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>90</y>
     <width>221</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>Работа с заказами</string>
   </property>
  </widget>
  <widget class="QPushButton" name="productionPushButton">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>160</y>
     <width>221</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>Работа с видами продукции</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class PerehodWidget(QWidget):
    def __init__(self, service: str):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        if service == 'commercial':
            pass
        elif service == 'proizvodstvo':
            pass
        elif service == 'tech':
            pass

    def usersPushButton(self):
        pass

    def ordersPushButton(self):
        pass

    def productsPushButton(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PerehodWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
