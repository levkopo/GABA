# Form implementation generated from reading ui file '.\interface\qt_design\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 359)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setToolTipDuration(0)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/waba/waba_title.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.groupBox_6)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/settings_brightness.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(30)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_3.addWidget(self.spinBox)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_3.setAccelerated(False)
        self.spinBox_3.setProperty("showGroupSeparator", False)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_2.addWidget(self.spinBox_3)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_2.setMaximum(30)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox_2)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.groupBox_3)
        self.doubleSpinBox.setMaximum(2.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_8.addWidget(self.doubleSpinBox)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.groupBox_7)
        self.listWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget_2.setDefaultDropAction(QtCore.Qt.DropAction.MoveAction)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidget_2.setMovement(QtWidgets.QListView.Movement.Snap)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.gridLayout_3.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_7, 0, 0, 2, 2)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_4, 0, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.listWidget.setDefaultDropAction(QtCore.Qt.DropAction.MoveAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidget.setMovement(QtWidgets.QListView.Movement.Snap)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_4.addWidget(self.listWidget, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout.addWidget(self.groupBox_5, 2, 5, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout.addWidget(self.groupBox_4, 1, 5, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 0, 4, 1, 2)
        self.graphWidget = PlotWidget(parent=self.tab_2)
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout.addWidget(self.graphWidget, 1, 4, 2, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 0, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(parent=self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_4 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_4.setEnabled(False)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(parent=self.menu_4)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(parent=self.menu_4)
        self.menu_6.setToolTipsVisible(True)
        self.menu_6.setObjectName("menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/github_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_3.setIcon(icon1)
        self.action_3.setObjectName("action_3")
        self.action_YouTube = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/youtube_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_YouTube.setIcon(icon2)
        self.action_YouTube.setObjectName("action_YouTube")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/waba/logo2_release.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_5.setIcon(icon3)
        self.action_5.setObjectName("action_5")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setCheckable(True)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setCheckable(True)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtGui.QAction(parent=MainWindow)
        self.action_7.setCheckable(True)
        self.action_7.setObjectName("action_7")
        self.action_PyQt6 = QtGui.QAction(parent=MainWindow)
        self.action_PyQt6.setObjectName("action_PyQt6")
        self.action_9 = QtGui.QAction(parent=MainWindow)
        self.action_9.setCheckable(True)
        self.action_9.setChecked(True)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtGui.QAction(parent=MainWindow)
        self.action_10.setCheckable(True)
        self.action_10.setChecked(True)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtGui.QAction(parent=MainWindow)
        self.action_11.setCheckable(True)
        self.action_11.setChecked(True)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtGui.QAction(parent=MainWindow)
        self.action_12.setCheckable(True)
        self.action_12.setChecked(True)
        self.action_12.setObjectName("action_12")
        self.action_13 = QtGui.QAction(parent=MainWindow)
        self.action_13.setCheckable(True)
        self.action_13.setObjectName("action_13")
        self.action_14 = QtGui.QAction(parent=MainWindow)
        self.action_14.setCheckable(True)
        self.action_14.setObjectName("action_14")
        self.action_15 = QtGui.QAction(parent=MainWindow)
        self.action_15.setCheckable(True)
        self.action_15.setObjectName("action_15")
        self.action_17 = QtGui.QAction(parent=MainWindow)
        self.action_17.setObjectName("action_17")
        self.action_18 = QtGui.QAction(parent=MainWindow)
        self.action_18.setObjectName("action_18")
        self.action_19 = QtGui.QAction(parent=MainWindow)
        self.action_19.setObjectName("action_19")
        self.action_20 = QtGui.QAction(parent=MainWindow)
        self.action_20.setObjectName("action_20")
        self.action_22 = QtGui.QAction(parent=MainWindow)
        self.action_22.setObjectName("action_22")
        self.action_23 = QtGui.QAction(parent=MainWindow)
        self.action_23.setObjectName("action_23")
        self.action_25 = QtGui.QAction(parent=MainWindow)
        self.action_25.setObjectName("action_25")
        self.action_26 = QtGui.QAction(parent=MainWindow)
        self.action_26.setObjectName("action_26")
        self.menu_3.addAction(self.action_4)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_26)
        self.menu.addAction(self.action_25)
        self.menu.addAction(self.action_23)
        self.menu_2.addAction(self.action_YouTube)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_PyQt6)
        self.menu_5.addAction(self.action_13)
        self.menu_5.addAction(self.action_14)
        self.menu_5.addAction(self.action_15)
        self.menu_6.addAction(self.action_17)
        self.menu_6.addAction(self.action_18)
        self.menu_6.addAction(self.action_20)
        self.menu_6.addAction(self.action_19)
        self.menu_6.addSeparator()
        self.menu_6.addAction(self.action_22)
        self.menu_4.addAction(self.menu_5.menuAction())
        self.menu_4.addAction(self.menu_6.menuAction())
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_9)
        self.menu_4.addAction(self.action_10)
        self.menu_4.addAction(self.action_11)
        self.menu_4.addAction(self.action_12)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.label_4.setBuddy(self.spinBox)
        self.label_3.setBuddy(self.spinBox_3)
        self.label_5.setBuddy(self.spinBox_2)
        self.label_7.setBuddy(self.comboBox_2)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Обновлять раз в"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Не обновлять"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Не обновлять"))
        self.comboBox.setItemText(1, _translate("MainWindow", "30 секунд"))
        self.comboBox.setItemText(2, _translate("MainWindow", "1 минуту"))
        self.comboBox.setItemText(3, _translate("MainWindow", "5 минут"))
        self.comboBox.setItemText(4, _translate("MainWindow", "10 минут"))
        self.comboBox.setItemText(5, _translate("MainWindow", "15 минут"))
        self.comboBox.setItemText(6, _translate("MainWindow", "30 минут"))
        self.comboBox.setItemText(7, _translate("MainWindow", "1 час"))
        self.comboBox.setItemText(8, _translate("MainWindow", "2 часа"))
        self.pushButton_3.setText(_translate("MainWindow", "Обновить сейчас"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Дополнительное"))
        self.label_4.setText(_translate("MainWindow", "Шаг таймера"))
        self.spinBox.setSuffix(_translate("MainWindow", " секунд"))
        self.groupBox.setTitle(_translate("MainWindow", "Снимок"))
        self.label_3.setText(_translate("MainWindow", "Количество снимков"))
        self.label_5.setText(_translate("MainWindow", "Выдержка"))
        self.spinBox_2.setSuffix(_translate("MainWindow", " секунд"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Сглаживание"))
        self.label_7.setText(_translate("MainWindow", "Метод сглаживания"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "default"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "logarithmic"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "smart"))
        self.label_8.setText(_translate("MainWindow", "Интервал"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Главная"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Свободны"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Asus (amogus)"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "Dexp D30 (sus)"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "Телевизор бабушки"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.comboBox_4.setItemText(0, _translate("MainWindow", "[1] internal_camera"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "[2] GoPro mini"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Распределение"))
        self.groupBox_5.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Авто-калибровка"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Asus {e6f07b5f-ee97-4a90-b076-33f57bf4eaa7}"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Sus {amogus}"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Калибровка"))
        self.pushButton.setText(_translate("MainWindow", "Обновить"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">v0.4_EXP | made with 💕</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Применить"))
        self.menu.setTitle(_translate("MainWindow", "Окно"))
        self.menu_3.setTitle(_translate("MainWindow", "Сворачивать в трей"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.menu_4.setTitle(_translate("MainWindow", "Уведомления"))
        self.menu_5.setTitle(_translate("MainWindow", "Изменения яркости"))
        self.menu_6.setTitle(_translate("MainWindow", "Вид уведомлений"))
        self.action_2.setText(_translate("MainWindow", "Свои темы и переводы"))
        self.action_3.setText(_translate("MainWindow", "Страница на GitHub"))
        self.action_YouTube.setText(_translate("MainWindow", "Гайд на YouTube"))
        self.action_5.setText(_translate("MainWindow", "О приложении"))
        self.action_4.setText(_translate("MainWindow", "Вместо закрытия"))
        self.action_6.setText(_translate("MainWindow", "Вместо сворачивания"))
        self.action_7.setText(_translate("MainWindow", "Никогда"))
        self.action_PyQt6.setText(_translate("MainWindow", "О PyQt6"))
        self.action_9.setText(_translate("MainWindow", "Подсказки"))
        self.action_10.setText(_translate("MainWindow", "Предупреждения"))
        self.action_11.setText(_translate("MainWindow", "Ошибки"))
        self.action_12.setText(_translate("MainWindow", "Обновления"))
        self.action_13.setText(_translate("MainWindow", "Не уведомлять"))
        self.action_14.setText(_translate("MainWindow", "При ручном запуске"))
        self.action_15.setText(_translate("MainWindow", "Каждый раз"))
        self.action_17.setText(_translate("MainWindow", "По умолчанию"))
        self.action_17.setToolTip(_translate("MainWindow", "<html><head/><body><p>Оставить выбор за приложением</p><p><span style=\" font-style:italic;\">Например: Предупреждения будут показываться диалоговыми окнами, а найденое обновление для приложения - в панели уведомлений</span></p></body></html>"))
        self.action_18.setText(_translate("MainWindow", "В панель уведомлений"))
        self.action_18.setToolTip(_translate("MainWindow", "<html><head/><body><p>Все уведомления переберутся в панель уведомлений (если такая имеется)</p><p><span style=\" font-weight:600;\">Предупреждения будут автоматически приниматься!</span></p></body></html>"))
        self.action_19.setText(_translate("MainWindow", "В угол экрана (beta)"))
        self.action_19.setToolTip(_translate("MainWindow", "<html><head/><body><p>(<span style=\" font-weight:600;\">BETA</span>) Все уведомления переберутся в угол экрана</p></body></html>"))
        self.action_20.setText(_translate("MainWindow", "Диалоговым окном"))
        self.action_20.setToolTip(_translate("MainWindow", "<html><head/><body><p>Все уведомления будут вызывать системное диалоговое окно</p><p><span style=\" font-style:italic;\">Может немного раздражать</span></p></body></html>"))
        self.action_22.setText(_translate("MainWindow", "Больше настроек..."))
        self.action_23.setText(_translate("MainWindow", "Закрыть"))
        self.action_25.setText(_translate("MainWindow", "Свернуть в трей"))
        self.action_26.setText(_translate("MainWindow", "Свернуть в панель приложений"))
from pyqtgraph import PlotWidget
