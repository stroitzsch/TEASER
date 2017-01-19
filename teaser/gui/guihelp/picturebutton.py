# created June 2015
# by TEASER4 Development Team


from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import QAbstractButton

class PictureButton(QAbstractButton):

    def __init__(self, pixmap, parent=None):
        super(PictureButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()
