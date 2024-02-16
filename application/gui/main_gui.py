import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class ImageLabel(QLabel):
    def __init__(self, text):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText(f'\n\n {text} \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 400)
        self.setAcceptDrops(True)

        mainLayout = QHBoxLayout()

        self.photoViewer = ImageLabel("Drop image here")
        self.resultViewer = ImageLabel("Result image")
        mainLayout.addWidget(self.photoViewer)
        mainLayout.addWidget(self.resultViewer)

        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_input_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_input_image(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(self.photoViewer.size())
        self.photoViewer.setPixmap(pixmap)

app = QApplication(sys.argv)
feat = App()
feat.show()
sys.exit(app.exec_())