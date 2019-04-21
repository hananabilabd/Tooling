#from PyQt4.uic import loadUiType
from PyQt4 import  QtGui ,uic,QtCore
from PyQt4.QtGui import *
import module_make
import sys, os
import image_rc
#from  gui2 import Ui_MainWindow
#Ui_MainWindow, QMainWindow = loadUiType('module_make.ui')
#class Main(QMainWindow,Ui_MainWindow):
class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__()
        image_rc.qInitResources()
        uic.loadUi(self.resource_path('gui.ui'), self)
        #self.setupUi(self)
        #image_rc.qInitResources()
        _fromUtf8 = QtCore.QString.fromUtf8
        pixmap = QPixmap(_fromUtf8(":/newPrefix/mohsen.jpg")) # load image from binary (from the image_rc)
        self.label.setPixmap(pixmap)
        self.pushButton.clicked.connect(self.browse)


    def resource_path(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    def browse(self):

        self.path = QtGui.QFileDialog.getExistingDirectory(self, "Select Folder", "")

        module_make.main(  self.path +r'\\',self.lineEdit.text())
        #print()



            # self.pushButton_20.clicked.connect( self.start_thread0 )
        # self.pushButton_20.setStyleSheet( "background-color: green" ) ## This is to change Button Color

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())



