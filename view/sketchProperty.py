# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sketchProperty.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SketchProperty(object):
    def setupUi(self, SketchProperty):
        SketchProperty.setObjectName("SketchProperty")
        SketchProperty.resize(311, 390)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SketchProperty.sizePolicy().hasHeightForWidth())
        SketchProperty.setSizePolicy(sizePolicy)
        SketchProperty.setMinimumSize(QtCore.QSize(270, 325))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SketchProperty)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.TextLabelID = QtWidgets.QLabel(SketchProperty)
        self.TextLabelID.setObjectName("TextLabelID")
        self.horizontalLayout_6.addWidget(self.TextLabelID)
        self.LineEditID = QtWidgets.QLineEdit(SketchProperty)
        self.LineEditID.setReadOnly(True)
        self.LineEditID.setObjectName("LineEditID")
        self.horizontalLayout_6.addWidget(self.LineEditID)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.GroupBoxGP = QtWidgets.QGroupBox(SketchProperty)
        self.GroupBoxGP.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupBoxGP.sizePolicy().hasHeightForWidth())
        self.GroupBoxGP.setSizePolicy(sizePolicy)
        self.GroupBoxGP.setObjectName("GroupBoxGP")
        self.GroupBoxGPLayout = QtWidgets.QGridLayout(self.GroupBoxGP)
        self.GroupBoxGPLayout.setObjectName("GroupBoxGPLayout")
        self.TextLabelPoint1 = QtWidgets.QLabel(self.GroupBoxGP)
        self.TextLabelPoint1.setObjectName("TextLabelPoint1")
        self.GroupBoxGPLayout.addWidget(self.TextLabelPoint1, 0, 0, 1, 1)
        self.LineEditPoint1 = QtWidgets.QLineEdit(self.GroupBoxGP)
        self.LineEditPoint1.setObjectName("LineEditPoint1")
        self.GroupBoxGPLayout.addWidget(self.LineEditPoint1, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.GroupBoxGP)
        self.GroupBoxPlot = QtWidgets.QGroupBox(SketchProperty)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupBoxPlot.sizePolicy().hasHeightForWidth())
        self.GroupBoxPlot.setSizePolicy(sizePolicy)
        self.GroupBoxPlot.setObjectName("GroupBoxPlot")
        self.GroupBoxPlotLayout = QtWidgets.QGridLayout(self.GroupBoxPlot)
        self.GroupBoxPlotLayout.setObjectName("GroupBoxPlotLayout")
        self.line = QtWidgets.QFrame(self.GroupBoxPlot)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.GroupBoxPlotLayout.addWidget(self.line, 1, 0, 1, 1)
        self.doubleSpinBoxAnimationValue = QtWidgets.QDoubleSpinBox(self.GroupBoxPlot)
        self.doubleSpinBoxAnimationValue.setDecimals(1)
        self.doubleSpinBoxAnimationValue.setMaximum(1.0)
        self.doubleSpinBoxAnimationValue.setSingleStep(0.1)
        self.doubleSpinBoxAnimationValue.setProperty("value", 1.0)
        self.doubleSpinBoxAnimationValue.setObjectName("doubleSpinBoxAnimationValue")
        self.GroupBoxPlotLayout.addWidget(self.doubleSpinBoxAnimationValue, 2, 0, 1, 1)
        self.PushButtonAnimate = QtWidgets.QPushButton(self.GroupBoxPlot)
        self.PushButtonAnimate.setObjectName("PushButtonAnimate")
        self.GroupBoxPlotLayout.addWidget(self.PushButtonAnimate, 2, 1, 1, 1)
        self.PushButtonPlot = QtWidgets.QPushButton(self.GroupBoxPlot)
        self.PushButtonPlot.setObjectName("PushButtonPlot")
        self.GroupBoxPlotLayout.addWidget(self.PushButtonPlot, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.GroupBoxPlot)
        self.label.setObjectName("label")
        self.GroupBoxPlotLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.GroupBoxPlot)
        self.GroupBoxAttributes = QtWidgets.QGroupBox(SketchProperty)
        self.GroupBoxAttributes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GroupBoxAttributes.setObjectName("GroupBoxAttributes")
        self.GroupBoxAttributesLayout = QtWidgets.QGridLayout(self.GroupBoxAttributes)
        self.GroupBoxAttributesLayout.setObjectName("GroupBoxAttributesLayout")
        self.TextLabelColor = QtWidgets.QLabel(self.GroupBoxAttributes)
        self.TextLabelColor.setObjectName("TextLabelColor")
        self.GroupBoxAttributesLayout.addWidget(self.TextLabelColor, 0, 0, 1, 1)
        self.PushButtonColor = QtWidgets.QPushButton(self.GroupBoxAttributes)
        self.PushButtonColor.setObjectName("PushButtonColor")
        self.GroupBoxAttributesLayout.addWidget(self.PushButtonColor, 0, 1, 1, 1)
        self.TextLabelStyle = QtWidgets.QLabel(self.GroupBoxAttributes)
        self.TextLabelStyle.setObjectName("TextLabelStyle")
        self.GroupBoxAttributesLayout.addWidget(self.TextLabelStyle, 1, 0, 1, 1)
        self.ComboBoxStyle = QtWidgets.QComboBox(self.GroupBoxAttributes)
        self.ComboBoxStyle.setObjectName("ComboBoxStyle")
        self.ComboBoxStyle.addItem("")
        self.ComboBoxStyle.addItem("")
        self.ComboBoxStyle.addItem("")
        self.ComboBoxStyle.addItem("")
        self.GroupBoxAttributesLayout.addWidget(self.ComboBoxStyle, 1, 1, 1, 1)
        self.TextLabelWidth = QtWidgets.QLabel(self.GroupBoxAttributes)
        self.TextLabelWidth.setObjectName("TextLabelWidth")
        self.GroupBoxAttributesLayout.addWidget(self.TextLabelWidth, 2, 0, 1, 1)
        self.ComboBoxWidth = QtWidgets.QComboBox(self.GroupBoxAttributes)
        self.ComboBoxWidth.setObjectName("ComboBoxWidth")
        self.ComboBoxWidth.addItem("")
        self.ComboBoxWidth.addItem("")
        self.ComboBoxWidth.addItem("")
        self.ComboBoxWidth.addItem("")
        self.ComboBoxWidth.addItem("")
        self.ComboBoxWidth.addItem("")
        self.ComboBoxWidth.addItem("")
        self.ComboBoxWidth.addItem("")
        self.ComboBoxWidth.addItem("")
        self.GroupBoxAttributesLayout.addWidget(self.ComboBoxWidth, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.GroupBoxAttributes)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.PushButtonOK = QtWidgets.QPushButton(SketchProperty)
        self.PushButtonOK.setObjectName("PushButtonOK")
        self.horizontalLayout_7.addWidget(self.PushButtonOK)
        self.PushButtonCancel = QtWidgets.QPushButton(SketchProperty)
        self.PushButtonCancel.setObjectName("PushButtonCancel")
        self.horizontalLayout_7.addWidget(self.PushButtonCancel)
        self.PushButtonApply = QtWidgets.QPushButton(SketchProperty)
        self.PushButtonApply.setObjectName("PushButtonApply")
        self.horizontalLayout_7.addWidget(self.PushButtonApply)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.retranslateUi(SketchProperty)
        QtCore.QMetaObject.connectSlotsByName(SketchProperty)

    def retranslateUi(self, SketchProperty):
        _translate = QtCore.QCoreApplication.translate
        SketchProperty.setWindowTitle(_translate("SketchProperty", "Form"))
        self.TextLabelID.setText(_translate("SketchProperty", "ID"))
        self.GroupBoxGP.setTitle(_translate("SketchProperty", "Geometry Properties"))
        self.TextLabelPoint1.setText(_translate("SketchProperty", "Point"))
        self.GroupBoxPlot.setTitle(_translate("SketchProperty", "Plot/Animation"))
        self.PushButtonAnimate.setText(_translate("SketchProperty", "Animation"))
        self.PushButtonPlot.setText(_translate("SketchProperty", "Plot"))
        self.label.setText(_translate("SketchProperty", "Basis Function"))
        self.GroupBoxAttributes.setTitle(_translate("SketchProperty", "Attributes"))
        self.TextLabelColor.setText(_translate("SketchProperty", "Color"))
        self.PushButtonColor.setText(_translate("SketchProperty", "Color"))
        self.TextLabelStyle.setText(_translate("SketchProperty", "Style"))
        self.ComboBoxStyle.setItemText(0, _translate("SketchProperty", "SOLID"))
        self.ComboBoxStyle.setItemText(1, _translate("SketchProperty", "DASH"))
        self.ComboBoxStyle.setItemText(2, _translate("SketchProperty", "DOT"))
        self.ComboBoxStyle.setItemText(3, _translate("SketchProperty", "DOTDASH"))
        self.TextLabelWidth.setText(_translate("SketchProperty", "Width"))
        self.ComboBoxWidth.setItemText(0, _translate("SketchProperty", "1.0"))
        self.ComboBoxWidth.setItemText(1, _translate("SketchProperty", "2.0"))
        self.ComboBoxWidth.setItemText(2, _translate("SketchProperty", "3.0"))
        self.ComboBoxWidth.setItemText(3, _translate("SketchProperty", "4.0"))
        self.ComboBoxWidth.setItemText(4, _translate("SketchProperty", "5.0"))
        self.ComboBoxWidth.setItemText(5, _translate("SketchProperty", "6.0"))
        self.ComboBoxWidth.setItemText(6, _translate("SketchProperty", "7.0"))
        self.ComboBoxWidth.setItemText(7, _translate("SketchProperty", "8.0"))
        self.ComboBoxWidth.setItemText(8, _translate("SketchProperty", "9.0"))
        self.PushButtonOK.setText(_translate("SketchProperty", "Ok"))
        self.PushButtonCancel.setText(_translate("SketchProperty", "Cancel"))
        self.PushButtonApply.setText(_translate("SketchProperty", "Apply"))
