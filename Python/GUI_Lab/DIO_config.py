# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DIO_Config.ui'
#
# Created: Sat Feb 16 13:05:42 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 262)
        self.PIN_0_Box = QtGui.QGroupBox(Form)
        self.PIN_0_Box.setEnabled(True)
        self.PIN_0_Box.setGeometry(QtCore.QRect(20, 10, 371, 201))
        self.PIN_0_Box.setObjectName("PIN_0_Box")
        self.Output_Level_Box = QtGui.QGroupBox(self.PIN_0_Box)
        self.Output_Level_Box.setGeometry(QtCore.QRect(160, 30, 191, 61))
        self.Output_Level_Box.setObjectName("Output_Level_Box")
        self.High_Mode = QtGui.QRadioButton(self.Output_Level_Box)
        self.High_Mode.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.High_Mode.setObjectName("High_Mode")
        self.Low_Mode = QtGui.QRadioButton(self.Output_Level_Box)
        self.Low_Mode.setGeometry(QtCore.QRect(110, 30, 95, 20))
        self.Low_Mode.setObjectName("Low_Mode")
        self.Input_Config_Box = QtGui.QGroupBox(self.PIN_0_Box)
        self.Input_Config_Box.setGeometry(QtCore.QRect(160, 90, 191, 61))
        self.Input_Config_Box.setObjectName("Input_Config_Box")
        self.PullUp_Mode = QtGui.QRadioButton(self.Input_Config_Box)
        self.PullUp_Mode.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.PullUp_Mode.setObjectName("PullUp_Mode")
        self.High_Imp_Mode = QtGui.QRadioButton(self.Input_Config_Box)
        self.High_Imp_Mode.setGeometry(QtCore.QRect(110, 30, 95, 20))
        self.High_Imp_Mode.setObjectName("High_Imp_Mode")
        self.Pin_Name = QtGui.QLineEdit(self.PIN_0_Box)
        self.Pin_Name.setGeometry(QtCore.QRect(10, 170, 141, 22))
        self.Pin_Name.setObjectName("Pin_Name")
        self.Default_Name_Check = QtGui.QCheckBox(self.PIN_0_Box)
        self.Default_Name_Check.setGeometry(QtCore.QRect(160, 170, 131, 20))
        self.Default_Name_Check.setObjectName("Default_Name_Check")
        self.label = QtGui.QLabel(self.PIN_0_Box)
        self.label.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.label.setObjectName("label")
        self.Mode_Box = QtGui.QGroupBox(self.PIN_0_Box)
        self.Mode_Box.setGeometry(QtCore.QRect(10, 30, 141, 121))
        self.Mode_Box.setObjectName("Mode_Box")
        self.Output_Mode = QtGui.QRadioButton(self.Mode_Box)
        self.Output_Mode.setGeometry(QtCore.QRect(20, 30, 95, 21))
        self.Output_Mode.setObjectName("Output_Mode")
        self.Input_Mode = QtGui.QRadioButton(self.Mode_Box)
        self.Input_Mode.setGeometry(QtCore.QRect(20, 80, 95, 20))
        self.Input_Mode.setObjectName("Input_Mode")
        self.GenerateButton = QtGui.QPushButton(Form)
        self.GenerateButton.setGeometry(QtCore.QRect(300, 220, 93, 31))
        self.GenerateButton.setObjectName("GenerateButton")
        self.OutFile_Path = QtGui.QLineEdit(Form)
        self.OutFile_Path.setGeometry(QtCore.QRect(20, 230, 261, 22))
        self.OutFile_Path.setObjectName("OutFile_Path")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 111, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Output_Mode, QtCore.SIGNAL("clicked(bool)"), self.Input_Config_Box.setDisabled)
        QtCore.QObject.connect(self.Input_Mode, QtCore.SIGNAL("clicked(bool)"), self.Output_Level_Box.setDisabled)
        QtCore.QObject.connect(self.Input_Mode, QtCore.SIGNAL("clicked(bool)"), self.Input_Config_Box.setEnabled)
        QtCore.QObject.connect(self.Output_Mode, QtCore.SIGNAL("clicked(bool)"), self.Output_Level_Box.setEnabled)
        QtCore.QObject.connect(self.Default_Name_Check, QtCore.SIGNAL("clicked(bool)"), self.Pin_Name.clear)
        QtCore.QObject.connect(self.Default_Name_Check, QtCore.SIGNAL("clicked(bool)"), self.Pin_Name.setDisabled)
        QtCore.QObject.connect(self.GenerateButton, QtCore.SIGNAL("clicked()"), self.GenerateFun)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def GenerateFun(self):
        MFIC_h_file = self.OutFile_Path.text() + r'MFIC.h'
        DIO_config_file = self.OutFile_Path.text() + r'DIO_Config.h'
        
        Wrapper_Pin_Name = ''
        if self.Default_Name_Check.isChecked():
            Wrapper_Pin_Name = 'DIO_u8_PIN0'
        else:
            Wrapper_Pin_Name = self.Pin_Name.text()
        
        MFIC_Handler = open(MFIC_h_file,'w')
        MFIC_Handler.write('#define    '+Wrapper_Pin_Name+'     0')
        MFIC_Handler.close()
        
        DIO_Config_Handler = open(DIO_config_file,'w')
        PIN_0_InitMode = ''
        if self.Output_Mode.isChecked():
            if self.High_Mode.isChecked():
                PIN_0_InitMode = 'DIO_u8_OUTPUT_HIGH'
            else:
                PIN_0_InitMode = 'DIO_u8_OUTPUT_LOW'
        else:
            if self.PullUp_Mode.isChecked():
                PIN_0_InitMode = 'DIO_u8_INPUT_PULLUP'
            else:
                PIN_0_InitMode = 'DIO_u8_INPUT_HIGHIMP'
        DIO_Config_Handler.write('#define    DIO_u8_PIN0_INITMODE      '+PIN_0_InitMode+'\n')
        DIO_Config_Handler.close()
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "DIO_Configurator", None, QtGui.QApplication.UnicodeUTF8))
        self.PIN_0_Box.setTitle(QtGui.QApplication.translate("Form", "PIN_0", None, QtGui.QApplication.UnicodeUTF8))
        self.Output_Level_Box.setTitle(QtGui.QApplication.translate("Form", "Output Level", None, QtGui.QApplication.UnicodeUTF8))
        self.High_Mode.setText(QtGui.QApplication.translate("Form", "High", None, QtGui.QApplication.UnicodeUTF8))
        self.Low_Mode.setText(QtGui.QApplication.translate("Form", "Low", None, QtGui.QApplication.UnicodeUTF8))
        self.Input_Config_Box.setTitle(QtGui.QApplication.translate("Form", "Input Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.PullUp_Mode.setText(QtGui.QApplication.translate("Form", "Pull Up", None, QtGui.QApplication.UnicodeUTF8))
        self.High_Imp_Mode.setText(QtGui.QApplication.translate("Form", "High Imp", None, QtGui.QApplication.UnicodeUTF8))
        self.Default_Name_Check.setText(QtGui.QApplication.translate("Form", "Set Default Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Enter Pin Name", None, QtGui.QApplication.UnicodeUTF8))
        self.Mode_Box.setTitle(QtGui.QApplication.translate("Form", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.Output_Mode.setText(QtGui.QApplication.translate("Form", "Output Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.Input_Mode.setText(QtGui.QApplication.translate("Form", "Input Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.GenerateButton.setText(QtGui.QApplication.translate("Form", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Output File Path", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

