# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taotao.ui'
#
# Created: Fri Oct 16 23:48:13 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.result_group = QtGui.QGroupBox(self.centralwidget)
        self.result_group.setObjectName("result_group")
        self.horizontalLayout = QtGui.QHBoxLayout(self.result_group)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data_view = QtGui.QTableView(self.result_group)
        self.data_view.setObjectName("data_view")
        self.horizontalLayout.addWidget(self.data_view)
        self.gridLayout_2.addWidget(self.result_group, 1, 0, 1, 1)
        self.query_group = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query_group.sizePolicy().hasHeightForWidth())
        self.query_group.setSizePolicy(sizePolicy)
        self.query_group.setObjectName("query_group")
        self.gridLayout = QtGui.QGridLayout(self.query_group)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.query_group)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.keyword = QtGui.QLineEdit(self.query_group)
        self.keyword.setObjectName("keyword")
        self.gridLayout.addWidget(self.keyword, 0, 2, 1, 4)
        self.label_4 = QtGui.QLabel(self.query_group)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.start_price = QtGui.QDoubleSpinBox(self.query_group)
        self.start_price.setObjectName("start_price")
        self.gridLayout.addWidget(self.start_price, 2, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.query_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 3, 1, 1)
        self.end_price = QtGui.QDoubleSpinBox(self.query_group)
        self.end_price.setObjectName("end_price")
        self.gridLayout.addWidget(self.end_price, 2, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.query_group)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 5, 1, 1)
        self.start_credit = QtGui.QComboBox(self.query_group)
        self.start_credit.setObjectName("start_credit")
        self.gridLayout.addWidget(self.start_credit, 2, 6, 1, 1)
        self.label_8 = QtGui.QLabel(self.query_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 7, 1, 1)
        self.end_credit = QtGui.QComboBox(self.query_group)
        self.end_credit.setObjectName("end_credit")
        self.gridLayout.addWidget(self.end_credit, 2, 8, 1, 1)
        self.sort = QtGui.QComboBox(self.query_group)
        self.sort.setObjectName("sort")
        self.gridLayout.addWidget(self.sort, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.query_group)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 6, 1, 1)
        self.cat = QtGui.QComboBox(self.query_group)
        self.cat.setObjectName("cat")
        self.gridLayout.addWidget(self.cat, 0, 8, 1, 2)
        self.is_guarantee = QtGui.QCheckBox(self.query_group)
        self.is_guarantee.setObjectName("is_guarantee")
        self.gridLayout.addWidget(self.is_guarantee, 2, 9, 1, 1)
        self.label_9 = QtGui.QLabel(self.query_group)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 4, 1, 1)
        self.page_size = QtGui.QSpinBox(self.query_group)
        self.page_size.setObjectName("page_size")
        self.gridLayout.addWidget(self.page_size, 1, 5, 1, 1)
        self.area = QtGui.QComboBox(self.query_group)
        self.area.setObjectName("area")
        self.gridLayout.addWidget(self.area, 1, 8, 1, 1)
        self.label_6 = QtGui.QLabel(self.query_group)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 6, 1, 1)
        self.label_3 = QtGui.QLabel(self.query_group)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.submitButton = QtGui.QPushButton(self.query_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setObjectName("submitButton")
        self.gridLayout.addWidget(self.submitButton, 0, 11, 3, 1)
        self.auto_send = QtGui.QCheckBox(self.query_group)
        self.auto_send.setObjectName("auto_send")
        self.gridLayout.addWidget(self.auto_send, 1, 9, 1, 1)
        self.gridLayout_2.addWidget(self.query_group, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "taotao 淘宝购物伴侣", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "关键字：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "价格范围：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "商家信用：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "商品分类：", None, QtGui.QApplication.UnicodeUTF8))
        self.is_guarantee.setText(QtGui.QApplication.translate("MainWindow", "消保商家", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "最大记录数：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "商家所在地：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "排序方式：", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("MainWindow", "查询结果", None, QtGui.QApplication.UnicodeUTF8))
        self.auto_send.setText(QtGui.QApplication.translate("MainWindow", "自动发货", None, QtGui.QApplication.UnicodeUTF8))

import taotao_rc_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

