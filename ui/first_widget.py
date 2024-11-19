import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication

from ui.perehod import PerehodWidget

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
  <widget class="QPushButton" name="commercialPushButton">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>30</y>
     <width>241</width>
     <height>71</height>
    </rect>
   </property>
   <property name="text">
    <string>Коммерческая служба</string>
   </property>
  </widget>
  <widget class="QPushButton" name="proizvodstvoPushButton">
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
  <widget class="QPushButton" name="techPushButton">
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

        self.commercialPushButton.clicked.connect(self.createPerehodWindowCommercial)
        self.proizvodstvoPushButton.clicked.connect(self.createPerehodWindowProizvodstvo)
        self.techPushButton.clicked.connect(self.createPerehodWindowTech)

    def createPerehodWindow(self, service_type):
        """Открывает новое окно и закрывает текущее."""
        self.hide()  # Скрываем текущее окно
        self.perehod_window = PerehodWidget(service_type)
        self.perehod_window.show()

    def createPerehodWindowCommercial(self):
        self.createPerehodWindow('commercial')

    def createPerehodWindowProizvodstvo(self):
        self.createPerehodWindow('proizvodstvo')

    def createPerehodWindowTech(self):
        self.createPerehodWindow('tech')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
