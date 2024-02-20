# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFramepQhnHR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import iconreso_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"#main {\n"
"	background-color: #222;\n"
"	border-radius: 5px;\n"
"}")
        self.main.setFrameShape(QFrame.NoFrame)
        self.main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.main)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(150, 0))
        self.menu.setMaximumSize(QSize(150, 16777215))
        self.menu.setStyleSheet(u"#menu {\n"
"	background-color: #1e1e1e;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"Line {\n"
"	height: 1px;\n"
"	background-color: #222;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 40px;\n"
"	width: 150px;\n"
"	border: none;\n"
"	color: #999;\n"
"	font-size: 12px;\n"
"	text-align: left;\n"
"	padding-left: 50px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: #fff;\n"
"	background-color: #111;\n"
"}\n"
"QPushButton:checked {\n"
"	color: #fff;\n"
"	background-color: #111;\n"
"}")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.menu)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(150, 50))
        self.logo.setMaximumSize(QSize(150, 50))
        self.logo.setStyleSheet(u"#logo {\n"
"	background-color: #181818;\n"
"	border-top-left-radius: 5px;\n"
"}\n"
"#title {\n"
"	color: #ccc;\n"
"	font-size: 16px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.logo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel(self.logo)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(45, 50))
        self.icon.setMaximumSize(QSize(45, 50))
        self.icon.setStyleSheet(u"image: url(:/icon/icons/icons8_video_playlist_48px.png);\n"
"padding-left: 11px;\n"
"padding-right: 6px;")

        self.horizontalLayout_2.addWidget(self.icon)

        self.title = QLabel(self.logo)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(110, 50))
        self.title.setMaximumSize(QSize(110, 50))
        self.title.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.title)


        self.verticalLayout_2.addWidget(self.logo)

        self.options = QFrame(self.menu)
        self.options.setObjectName(u"options")
        self.options.setMinimumSize(QSize(0, 0))
        self.options.setCursor(QCursor(Qt.PointingHandCursor))
        self.options.setStyleSheet(u"")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.options)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.video = QFrame(self.options)
        self.video.setObjectName(u"video")
        self.video.setMinimumSize(QSize(150, 50))
        self.video.setMaximumSize(QSize(150, 50))
        self.video.setFrameShape(QFrame.NoFrame)
        self.video.setFrameShadow(QFrame.Raised)
        self.videobtn = QPushButton(self.video)
        self.videobtn.setObjectName(u"videobtn")
        self.videobtn.setGeometry(QRect(0, 0, 150, 50))
        self.videobtn.setMinimumSize(QSize(150, 50))
        self.videobtn.setMaximumSize(QSize(150, 16777215))
        self.videobtn.setCheckable(True)
        self.videobtn.setChecked(True)
        self.label = QLabel(self.video)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 50, 50))
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setStyleSheet(u"image: url(:/icon/icons/icons8_video_call_20px.png);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.video)

        self.sound = QFrame(self.options)
        self.sound.setObjectName(u"sound")
        self.sound.setMinimumSize(QSize(150, 50))
        self.sound.setMaximumSize(QSize(150, 50))
        self.sound.setFrameShape(QFrame.NoFrame)
        self.sound.setFrameShadow(QFrame.Raised)
        self.musicbtn = QPushButton(self.sound)
        self.musicbtn.setObjectName(u"musicbtn")
        self.musicbtn.setGeometry(QRect(0, 0, 150, 50))
        self.musicbtn.setMinimumSize(QSize(150, 50))
        self.musicbtn.setMaximumSize(QSize(150, 50))
        self.musicbtn.setCheckable(True)
        self.label_2 = QLabel(self.sound)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 50, 50))
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setStyleSheet(u"image: url(:/icon/icons/icons8_music_20px.png);")

        self.verticalLayout_3.addWidget(self.sound)

        self.turninto = QFrame(self.options)
        self.turninto.setObjectName(u"turninto")
        self.turninto.setMinimumSize(QSize(150, 50))
        self.turninto.setMaximumSize(QSize(150, 50))
        self.turninto.setFrameShape(QFrame.NoFrame)
        self.turninto.setFrameShadow(QFrame.Raised)
        self.transformbtn = QPushButton(self.turninto)
        self.transformbtn.setObjectName(u"transformbtn")
        self.transformbtn.setGeometry(QRect(0, 0, 150, 50))
        self.transformbtn.setMinimumSize(QSize(150, 50))
        self.transformbtn.setMaximumSize(QSize(150, 50))
        self.transformbtn.setCheckable(True)
        self.label_3 = QLabel(self.turninto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 50, 50))
        self.label_3.setMinimumSize(QSize(50, 50))
        self.label_3.setMaximumSize(QSize(50, 50))
        self.label_3.setStyleSheet(u"image: url(:/icon/icons/icons8_music_video_20px.png);")

        self.verticalLayout_3.addWidget(self.turninto)


        self.verticalLayout_2.addWidget(self.options, 0, Qt.AlignTop)

        self.altmenu = QFrame(self.menu)
        self.altmenu.setObjectName(u"altmenu")
        self.altmenu.setMinimumSize(QSize(0, 0))
        self.altmenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.altmenu.setFrameShape(QFrame.NoFrame)
        self.altmenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.altmenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.altmenu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 50))
        self.frame.setMaximumSize(QSize(150, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 50, 50))
        self.label_6.setMinimumSize(QSize(50, 50))
        self.label_6.setMaximumSize(QSize(50, 50))
        self.label_6.setStyleSheet(u"image: url(:/icon/icons/icons8_time_machine_20px.png);")
        self.historybtn = QPushButton(self.frame)
        self.historybtn.setObjectName(u"historybtn")
        self.historybtn.setGeometry(QRect(0, 0, 150, 50))
        self.historybtn.setMinimumSize(QSize(150, 50))
        self.historybtn.setMaximumSize(QSize(150, 50))
        self.historybtn.setCheckable(True)
        self.historybtn.raise_()
        self.label_6.raise_()

        self.verticalLayout_4.addWidget(self.frame)

        self.about = QFrame(self.altmenu)
        self.about.setObjectName(u"about")
        self.about.setMinimumSize(QSize(150, 50))
        self.about.setMaximumSize(QSize(150, 50))
        self.about.setFrameShape(QFrame.NoFrame)
        self.about.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.about)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 50, 50))
        self.label_4.setMinimumSize(QSize(50, 50))
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setStyleSheet(u"image: url(:/icon/icons/icons8_info_squared_20px.png);")
        self.aboutbtn = QPushButton(self.about)
        self.aboutbtn.setObjectName(u"aboutbtn")
        self.aboutbtn.setGeometry(QRect(0, 0, 150, 50))
        self.aboutbtn.setMinimumSize(QSize(150, 50))
        self.aboutbtn.setMaximumSize(QSize(150, 50))
        self.aboutbtn.setCheckable(True)
        self.aboutbtn.raise_()
        self.label_4.raise_()

        self.verticalLayout_4.addWidget(self.about)

        self.settings = QFrame(self.altmenu)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(150, 50))
        self.settings.setMaximumSize(QSize(150, 50))
        self.settings.setFrameShape(QFrame.NoFrame)
        self.settings.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.settings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 50, 50))
        self.label_5.setMinimumSize(QSize(50, 50))
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setStyleSheet(u"image: url(:/icon/icons/icons8_settings_20px.png);")
        self.settingsbtn = QPushButton(self.settings)
        self.settingsbtn.setObjectName(u"settingsbtn")
        self.settingsbtn.setGeometry(QRect(0, 0, 150, 50))
        self.settingsbtn.setMinimumSize(QSize(150, 50))
        self.settingsbtn.setMaximumSize(QSize(150, 50))
        self.settingsbtn.setStyleSheet(u"border-bottom-left-radius: 5px;")
        self.settingsbtn.setCheckable(True)
        self.settingsbtn.raise_()
        self.label_5.raise_()

        self.verticalLayout_4.addWidget(self.settings)


        self.verticalLayout_2.addWidget(self.altmenu, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.menu)

        self.body = QFrame(self.main)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.NoFrame)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.body)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.window = QFrame(self.body)
        self.window.setObjectName(u"window")
        self.window.setMinimumSize(QSize(350, 50))
        self.window.setMaximumSize(QSize(350, 50))
        self.window.setStyleSheet(u"#window {\n"
"	background-color: #181818;\n"
"	border-top-right-radius: 5px;\n"
"}")
        self.window.setFrameShape(QFrame.NoFrame)
        self.window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.window)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.movewindow = QFrame(self.window)
        self.movewindow.setObjectName(u"movewindow")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movewindow.sizePolicy().hasHeightForWidth())
        self.movewindow.setSizePolicy(sizePolicy)
        self.movewindow.setFrameShape(QFrame.NoFrame)
        self.movewindow.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.movewindow)

        self.winop = QFrame(self.window)
        self.winop.setObjectName(u"winop")
        self.winop.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"#close {\n"
"	border-top-right-radius: 5px;\n"
"	image: url(:/icon/icons/icons8_Close_20px.png);\n"
"}\n"
"#close:hover {\n"
"	image: url(:/icon/icons/icons8_Close_20px_1.png);\n"
"	background-color: rgb(255, 0, 38);\n"
"}\n"
"#minimize {\n"
"	image: url(:/icon/icons/icons8_subtract_20px_1.png);\n"
"}\n"
"#minimize:hover {\n"
"	image: url(:/icon/icons/icons8_subtract_20px_2.png);\n"
"	background-color: #333;\n"
"}")
        self.winop.setFrameShape(QFrame.NoFrame)
        self.winop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.winop)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize = QPushButton(self.winop)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(50, 50))
        self.minimize.setMaximumSize(QSize(50, 50))
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.minimize)

        self.close = QPushButton(self.winop)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(50, 50))
        self.close.setMaximumSize(QSize(50, 50))
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.close)


        self.horizontalLayout_3.addWidget(self.winop, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.window)

        self.workplace = QFrame(self.body)
        self.workplace.setObjectName(u"workplace")
        self.workplace.setMinimumSize(QSize(350, 450))
        self.workplace.setMaximumSize(QSize(350, 450))
        self.workplace.setFrameShape(QFrame.NoFrame)
        self.workplace.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.workplace)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 10)
        self.stackedWidget = QStackedWidget(self.workplace)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.video_2 = QWidget()
        self.video_2.setObjectName(u"video_2")
        self.verticalLayout_7 = QVBoxLayout(self.video_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.videofr = QFrame(self.video_2)
        self.videofr.setObjectName(u"videofr")
        self.videofr.setStyleSheet(u"#videofr {\n"
"	background-color: #222;\n"
"}")
        self.videofr.setFrameShape(QFrame.NoFrame)
        self.videofr.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.videofr)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 0)
        self.searchbar = QFrame(self.videofr)
        self.searchbar.setObjectName(u"searchbar")
        self.searchbar.setMinimumSize(QSize(330, 40))
        self.searchbar.setMaximumSize(QSize(330, 40))
        self.searchbar.setStyleSheet(u"#searchtxt {\n"
"	border-radius: 5px;\n"
"	padding-left: 8px;\n"
"	padding-right: 35px;\n"
"	border: 2px solid #333;\n"
"	background-color: #191919;\n"
"	font-size: 12px;\n"
"	color: #999;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#searchtxt:focus {\n"
"	background-color: #151515;\n"
"	border: 2px solid #292929;\n"
"	color: #fff;\n"
"}\n"
"#searchbtn {\n"
"	border: none;\n"
"	color: red;\n"
"	image: url(:/icon/icons/icons8_search_20px_1.png);\n"
"}\n"
"#searchbtn:hover {\n"
"	image: url(:/icon/icons/icons8_search_20px_2.png);\n"
"}")
        self.searchbar.setFrameShape(QFrame.NoFrame)
        self.searchbar.setFrameShadow(QFrame.Raised)
        self.searchtxt = QLineEdit(self.searchbar)
        self.searchtxt.setObjectName(u"searchtxt")
        self.searchtxt.setGeometry(QRect(0, 0, 330, 40))
        self.searchtxt.setMinimumSize(QSize(330, 40))
        self.searchtxt.setMaximumSize(QSize(330, 40))
        self.searchbtn = QPushButton(self.searchbar)
        self.searchbtn.setObjectName(u"searchbtn")
        self.searchbtn.setGeometry(QRect(290, 0, 40, 40))
        self.searchbtn.setMinimumSize(QSize(40, 40))
        self.searchbtn.setMaximumSize(QSize(40, 40))
        self.searchbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.searchbar)

        self.resultbar = QFrame(self.videofr)
        self.resultbar.setObjectName(u"resultbar")
        self.resultbar.setStyleSheet(u"")
        self.resultbar.setFrameShape(QFrame.NoFrame)
        self.resultbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.resultbar)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.thumbfr = QFrame(self.resultbar)
        self.thumbfr.setObjectName(u"thumbfr")
        self.thumbfr.setMinimumSize(QSize(329, 180))
        self.thumbfr.setMaximumSize(QSize(329, 180))
        self.thumbfr.setStyleSheet(u"#thumbfr {\n"
"	border-image: url(:/icon/icons/videoback.fw.png);\n"
"	margin-left: 2px;\n"
"	border-width: 5px;\n"
"}\n"
"")
        self.thumbfr.setFrameShape(QFrame.NoFrame)
        self.thumbfr.setFrameShadow(QFrame.Raised)
        self.duration = QLabel(self.thumbfr)
        self.duration.setObjectName(u"duration")
        self.duration.setGeometry(QRect(273, 5, 51, 17))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.duration.sizePolicy().hasHeightForWidth())
        self.duration.setSizePolicy(sizePolicy1)
        self.duration.setMinimumSize(QSize(35, 17))
        self.duration.setMaximumSize(QSize(80, 15))
        self.duration.setStyleSheet(u"#duration {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 128), stop:1 rgba(0, 0, 0, 129));\n"
"	border-radius: 4px;\n"
"	color: #ccc;\n"
"	padding-bottom: 3px;\n"
"}")
        self.duration.setAlignment(Qt.AlignCenter)
        self.duration.setWordWrap(True)
        self.videotitle = QLabel(self.thumbfr)
        self.videotitle.setObjectName(u"videotitle")
        self.videotitle.setGeometry(QRect(2, 140, 327, 41))
        self.videotitle.setMinimumSize(QSize(327, 30))
        self.videotitle.setMaximumSize(QSize(327, 16777215))
        self.videotitle.setStyleSheet(u"#videotitle {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 128), stop:1 rgba(0, 0, 0, 129));\n"
"	color: #ccc;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	padding-bottom: 4px;\n"
"	font-size: 12px;\n"
"}")
        self.videotitle.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.thumbfr)

        self.optionsfr = QFrame(self.resultbar)
        self.optionsfr.setObjectName(u"optionsfr")
        self.optionsfr.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #ccc;\n"
"	padding-bottom: 2px;\n"
"}")
        self.optionsfr.setFrameShape(QFrame.NoFrame)
        self.optionsfr.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.optionsfr)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.optionsfr)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 40))
        self.label_7.setMaximumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.optionsfr)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 40))
        self.label_8.setMaximumSize(QSize(120, 40))

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.optionsfr)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(1677, 40))
        self.frame_2.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#btn720p {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#btn360p {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn720p = QPushButton(self.frame_2)
        self.btn720p.setObjectName(u"btn720p")
        self.btn720p.setEnabled(False)
        self.btn720p.setGeometry(QRect(135, 0, 75, 40))
        self.btn720p.setMinimumSize(QSize(75, 40))
        self.btn720p.setMaximumSize(QSize(75, 16777215))
        self.btn720p.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn720p.setCheckable(True)
        self.btn720p.setChecked(False)
        self.btn360p = QPushButton(self.frame_2)
        self.btn360p.setObjectName(u"btn360p")
        self.btn360p.setEnabled(False)
        self.btn360p.setGeometry(QRect(62, 0, 75, 40))
        self.btn360p.setMinimumSize(QSize(75, 40))
        self.btn360p.setMaximumSize(QSize(75, 40))
        self.btn360p.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn360p.setCheckable(True)

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.btnpath = QPushButton(self.optionsfr)
        self.btnpath.setObjectName(u"btnpath")
        self.btnpath.setEnabled(False)
        self.btnpath.setMinimumSize(QSize(0, 40))
        self.btnpath.setMaximumSize(QSize(1677, 40))
        self.btnpath.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnpath.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"\n"
"")
        self.btnpath.setCheckable(True)
        self.btnpath.setChecked(False)

        self.gridLayout.addWidget(self.btnpath, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.optionsfr, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.resultbar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#downloadbtn {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#sizebtn {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.downloadbtn = QPushButton(self.frame_3)
        self.downloadbtn.setObjectName(u"downloadbtn")
        self.downloadbtn.setEnabled(False)
        self.downloadbtn.setGeometry(QRect(230, 0, 100, 40))
        self.downloadbtn.setMinimumSize(QSize(100, 40))
        self.downloadbtn.setMaximumSize(QSize(100, 40))
        self.downloadbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sizebtn = QPushButton(self.frame_3)
        self.sizebtn.setObjectName(u"sizebtn")
        self.sizebtn.setEnabled(False)
        self.sizebtn.setGeometry(QRect(162, 0, 70, 40))
        self.sizebtn.setMinimumSize(QSize(70, 40))
        self.sizebtn.setMaximumSize(QSize(70, 40))
        self.sizebtn.setCheckable(True)
        self.sizebtn.setChecked(True)

        self.verticalLayout_9.addWidget(self.frame_3)


        self.verticalLayout_8.addWidget(self.resultbar)

        self.footer = QFrame(self.videofr)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 40))
        self.footer.setMaximumSize(QSize(16777215, 40))
        self.footer.setStyleSheet(u"")
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.footer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 0, 330, 40))
        self.progressBar.setMinimumSize(QSize(330, 40))
        self.progressBar.setMaximumSize(QSize(330, 40))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #333;\n"
"    border-radius: 5px;\n"
"	background-color: #282828;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #111;\n"
"    width: 3px;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.bartxt = QLabel(self.footer)
        self.bartxt.setObjectName(u"bartxt")
        self.bartxt.setGeometry(QRect(0, 0, 330, 40))
        self.bartxt.setMinimumSize(QSize(330, 40))
        self.bartxt.setMaximumSize(QSize(330, 40))
        self.bartxt.setStyleSheet(u"color: #ccc;\n"
"font-size: 12px;\n"
"padding-bottom: 2px;")
        self.bartxt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.footer)


        self.verticalLayout_7.addWidget(self.videofr)

        self.stackedWidget.addWidget(self.video_2)
        self.music = QWidget()
        self.music.setObjectName(u"music")
        self.videofr_2 = QFrame(self.music)
        self.videofr_2.setObjectName(u"videofr_2")
        self.videofr_2.setGeometry(QRect(0, 0, 350, 440))
        self.videofr_2.setStyleSheet(u"#videofr_2 {\n"
"	background-color: #222;\n"
"}")
        self.videofr_2.setFrameShape(QFrame.NoFrame)
        self.videofr_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.videofr_2)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 0)
        self.searchbar_2 = QFrame(self.videofr_2)
        self.searchbar_2.setObjectName(u"searchbar_2")
        self.searchbar_2.setMinimumSize(QSize(330, 40))
        self.searchbar_2.setMaximumSize(QSize(330, 40))
        self.searchbar_2.setStyleSheet(u"#searchtxt_2 {\n"
"	border-radius: 5px;\n"
"	padding-left: 8px;\n"
"	padding-right: 35px;\n"
"	border: 2px solid #333;\n"
"	background-color: #191919;\n"
"	font-size: 12px;\n"
"	color: #999;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#searchtxt_2:focus {\n"
"	background-color: #151515;\n"
"	border: 2px solid #292929;\n"
"	color: #fff;\n"
"}\n"
"#searchbtn_2 {\n"
"	border: none;\n"
"	color: red;\n"
"	image: url(:/icon/icons/icons8_search_20px_1.png);\n"
"}\n"
"#searchbtn_2:hover {\n"
"	image: url(:/icon/icons/icons8_search_20px_2.png);\n"
"}")
        self.searchbar_2.setFrameShape(QFrame.NoFrame)
        self.searchbar_2.setFrameShadow(QFrame.Raised)
        self.searchtxt_2 = QLineEdit(self.searchbar_2)
        self.searchtxt_2.setObjectName(u"searchtxt_2")
        self.searchtxt_2.setGeometry(QRect(0, 0, 330, 40))
        self.searchtxt_2.setMinimumSize(QSize(330, 40))
        self.searchtxt_2.setMaximumSize(QSize(330, 40))
        self.searchbtn_2 = QPushButton(self.searchbar_2)
        self.searchbtn_2.setObjectName(u"searchbtn_2")
        self.searchbtn_2.setGeometry(QRect(290, 0, 40, 40))
        self.searchbtn_2.setMinimumSize(QSize(40, 40))
        self.searchbtn_2.setMaximumSize(QSize(40, 40))
        self.searchbtn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.searchbar_2)

        self.resultbar_2 = QFrame(self.videofr_2)
        self.resultbar_2.setObjectName(u"resultbar_2")
        self.resultbar_2.setStyleSheet(u"")
        self.resultbar_2.setFrameShape(QFrame.NoFrame)
        self.resultbar_2.setFrameShadow(QFrame.Raised)
        self.thumbfr_2 = QFrame(self.resultbar_2)
        self.thumbfr_2.setObjectName(u"thumbfr_2")
        self.thumbfr_2.setGeometry(QRect(0, 0, 329, 180))
        self.thumbfr_2.setMinimumSize(QSize(329, 180))
        self.thumbfr_2.setMaximumSize(QSize(329, 180))
        self.thumbfr_2.setStyleSheet(u"#thumbfr_2 {\n"
"	border-image: url(:/icon/icons/videoback.fw.png);\n"
"	margin-left: 2px;\n"
"	border-width: 5px;\n"
"}\n"
"")
        self.thumbfr_2.setFrameShape(QFrame.NoFrame)
        self.thumbfr_2.setFrameShadow(QFrame.Raised)
        self.duration_2 = QLabel(self.thumbfr_2)
        self.duration_2.setObjectName(u"duration_2")
        self.duration_2.setGeometry(QRect(273, 5, 51, 17))
        sizePolicy1.setHeightForWidth(self.duration_2.sizePolicy().hasHeightForWidth())
        self.duration_2.setSizePolicy(sizePolicy1)
        self.duration_2.setMinimumSize(QSize(35, 17))
        self.duration_2.setMaximumSize(QSize(80, 15))
        self.duration_2.setStyleSheet(u"#duration_2 {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 128), stop:1 rgba(0, 0, 0, 129));\n"
"	border-radius: 4px;\n"
"	color: #ccc;\n"
"	padding-bottom: 3px;\n"
"}")
        self.duration_2.setAlignment(Qt.AlignCenter)
        self.duration_2.setWordWrap(True)
        self.videotitle_2 = QLabel(self.thumbfr_2)
        self.videotitle_2.setObjectName(u"videotitle_2")
        self.videotitle_2.setGeometry(QRect(2, 140, 327, 41))
        self.videotitle_2.setMinimumSize(QSize(327, 30))
        self.videotitle_2.setMaximumSize(QSize(327, 16777215))
        self.videotitle_2.setStyleSheet(u"#videotitle_2 {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 128), stop:1 rgba(0, 0, 0, 129));\n"
"	color: #ccc;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	padding-bottom: 4px;\n"
"	font-size: 12px;\n"
"}")
        self.videotitle_2.setWordWrap(True)
        self.optionsfr_2 = QFrame(self.resultbar_2)
        self.optionsfr_2.setObjectName(u"optionsfr_2")
        self.optionsfr_2.setGeometry(QRect(0, 190, 331, 40))
        self.optionsfr_2.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #ccc;\n"
"	padding-bottom: 2px;\n"
"}")
        self.optionsfr_2.setFrameShape(QFrame.NoFrame)
        self.optionsfr_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.optionsfr_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.optionsfr_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(1677, 40))
        self.frame_4.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#btn720p_2 {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#btn360p_2 {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btnpath_2 = QPushButton(self.frame_4)
        self.btnpath_2.setObjectName(u"btnpath_2")
        self.btnpath_2.setEnabled(False)
        self.btnpath_2.setGeometry(QRect(120, 0, 210, 40))
        self.btnpath_2.setMinimumSize(QSize(0, 40))
        self.btnpath_2.setMaximumSize(QSize(1677, 40))
        self.btnpath_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnpath_2.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"\n"
"")
        self.btnpath_2.setCheckable(True)
        self.btnpath_2.setChecked(False)
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 120, 40))
        self.label_10.setMinimumSize(QSize(120, 40))
        self.label_10.setMaximumSize(QSize(120, 40))

        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.resultbar_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 240, 330, 40))
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#downloadbtn_2 {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#sizebtn_2 {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.downloadbtn_2 = QPushButton(self.frame_5)
        self.downloadbtn_2.setObjectName(u"downloadbtn_2")
        self.downloadbtn_2.setEnabled(False)
        self.downloadbtn_2.setGeometry(QRect(230, 0, 100, 40))
        self.downloadbtn_2.setMinimumSize(QSize(100, 40))
        self.downloadbtn_2.setMaximumSize(QSize(100, 40))
        self.downloadbtn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.sizebtn_2 = QPushButton(self.frame_5)
        self.sizebtn_2.setObjectName(u"sizebtn_2")
        self.sizebtn_2.setEnabled(False)
        self.sizebtn_2.setGeometry(QRect(162, 0, 70, 40))
        self.sizebtn_2.setMinimumSize(QSize(70, 40))
        self.sizebtn_2.setMaximumSize(QSize(70, 40))
        self.sizebtn_2.setCheckable(True)
        self.sizebtn_2.setChecked(True)

        self.verticalLayout_10.addWidget(self.resultbar_2)

        self.footer_2 = QFrame(self.videofr_2)
        self.footer_2.setObjectName(u"footer_2")
        self.footer_2.setMinimumSize(QSize(0, 40))
        self.footer_2.setMaximumSize(QSize(16777215, 40))
        self.footer_2.setStyleSheet(u"")
        self.footer_2.setFrameShape(QFrame.NoFrame)
        self.footer_2.setFrameShadow(QFrame.Raised)
        self.progressBar_2 = QProgressBar(self.footer_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(0, 0, 330, 40))
        self.progressBar_2.setMinimumSize(QSize(330, 40))
        self.progressBar_2.setMaximumSize(QSize(330, 40))
        self.progressBar_2.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #333;\n"
"    border-radius: 5px;\n"
"	background-color: #282828;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #111;\n"
"    width: 3px;\n"
"}")
        self.progressBar_2.setValue(0)
        self.progressBar_2.setOrientation(Qt.Horizontal)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)
        self.bartxt_2 = QLabel(self.footer_2)
        self.bartxt_2.setObjectName(u"bartxt_2")
        self.bartxt_2.setGeometry(QRect(0, 0, 330, 40))
        self.bartxt_2.setMinimumSize(QSize(330, 40))
        self.bartxt_2.setMaximumSize(QSize(330, 40))
        self.bartxt_2.setStyleSheet(u"color: #ccc;\n"
"font-size: 12px;\n"
"padding-bottom: 2px;")
        self.bartxt_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.footer_2)

        self.stackedWidget.addWidget(self.music)
        self.transform = QWidget()
        self.transform.setObjectName(u"transform")
        self.videofr_3 = QFrame(self.transform)
        self.videofr_3.setObjectName(u"videofr_3")
        self.videofr_3.setGeometry(QRect(0, 0, 350, 440))
        self.videofr_3.setStyleSheet(u"#videofr_3 {\n"
"	background-color: #222;\n"
"}")
        self.videofr_3.setFrameShape(QFrame.NoFrame)
        self.videofr_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.videofr_3)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 0)
        self.resultbar_3 = QFrame(self.videofr_3)
        self.resultbar_3.setObjectName(u"resultbar_3")
        self.resultbar_3.setStyleSheet(u"")
        self.resultbar_3.setFrameShape(QFrame.NoFrame)
        self.resultbar_3.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.resultbar_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 220, 330, 40))
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setMaximumSize(QSize(16777215, 40))
        self.frame_7.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#downloadbtn_3 {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#sizebtn_3 {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.downloadbtn_3 = QPushButton(self.frame_7)
        self.downloadbtn_3.setObjectName(u"downloadbtn_3")
        self.downloadbtn_3.setEnabled(False)
        self.downloadbtn_3.setGeometry(QRect(230, 0, 100, 40))
        self.downloadbtn_3.setMinimumSize(QSize(100, 40))
        self.downloadbtn_3.setMaximumSize(QSize(100, 40))
        self.downloadbtn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.sizebtn_3 = QPushButton(self.frame_7)
        self.sizebtn_3.setObjectName(u"sizebtn_3")
        self.sizebtn_3.setEnabled(False)
        self.sizebtn_3.setGeometry(QRect(162, 0, 70, 40))
        self.sizebtn_3.setMinimumSize(QSize(70, 40))
        self.sizebtn_3.setMaximumSize(QSize(70, 40))
        self.sizebtn_3.setCheckable(True)
        self.sizebtn_3.setChecked(True)
        self.frame_8 = QFrame(self.resultbar_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 331, 40))
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setMaximumSize(QSize(1677, 40))
        self.frame_8.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#btn720p_2 {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#btn360p_2 {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 120, 40))
        self.label_11.setMinimumSize(QSize(120, 40))
        self.label_11.setMaximumSize(QSize(120, 40))
        self.label_11.setStyleSheet(u"color: #ccc;\n"
"font-size: 12px;\n"
"padding-bottom: 2px;")
        self.frame_6 = QFrame(self.resultbar_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 40, 331, 40))
        self.frame_6.setMinimumSize(QSize(0, 40))
        self.frame_6.setMaximumSize(QSize(1677, 40))
        self.frame_6.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#btn720p_2 {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#btn360p_2 {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.selectvideo = QPushButton(self.frame_6)
        self.selectvideo.setObjectName(u"selectvideo")
        self.selectvideo.setEnabled(True)
        self.selectvideo.setGeometry(QRect(49, 0, 281, 40))
        self.selectvideo.setMinimumSize(QSize(0, 40))
        self.selectvideo.setMaximumSize(QSize(1677, 40))
        self.selectvideo.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectvideo.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"\n"
"")
        self.selectvideo.setCheckable(True)
        self.selectvideo.setChecked(False)
        self.videophoto = QLabel(self.frame_6)
        self.videophoto.setObjectName(u"videophoto")
        self.videophoto.setGeometry(QRect(0, 0, 40, 40))
        self.videophoto.setMinimumSize(QSize(40, 40))
        self.videophoto.setMaximumSize(QSize(40, 40))
        self.videophoto.setStyleSheet(u"#videophoto {\n"
"background-color: #181818;\n"
"border-image: url(:/icon/images/videotut.jpg);\n"
"border: 2px solid #282828;\n"
"border-radius: 5px;\n"
"}")
        self.frame_9 = QFrame(self.resultbar_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 100, 331, 40))
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setMaximumSize(QSize(1677, 40))
        self.frame_9.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#btn720p_2 {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#btn360p_2 {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 191, 40))
        self.label_12.setMinimumSize(QSize(120, 40))
        self.label_12.setMaximumSize(QSize(999, 999))
        self.label_12.setStyleSheet(u"color: #ccc;\n"
"font-size: 12px;\n"
"padding-bottom: 2px;")
        self.frame_10 = QFrame(self.resultbar_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 140, 331, 40))
        self.frame_10.setMinimumSize(QSize(0, 40))
        self.frame_10.setMaximumSize(QSize(1677, 40))
        self.frame_10.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"#btn720p_2 {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#btn360p_2 {\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.selectmusic = QPushButton(self.frame_10)
        self.selectmusic.setObjectName(u"selectmusic")
        self.selectmusic.setEnabled(False)
        self.selectmusic.setGeometry(QRect(0, 0, 330, 40))
        self.selectmusic.setMinimumSize(QSize(0, 40))
        self.selectmusic.setMaximumSize(QSize(1677, 40))
        self.selectmusic.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectmusic.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"\n"
"")
        self.selectmusic.setCheckable(True)
        self.selectmusic.setChecked(False)

        self.verticalLayout_11.addWidget(self.resultbar_3)

        self.footer_3 = QFrame(self.videofr_3)
        self.footer_3.setObjectName(u"footer_3")
        self.footer_3.setMinimumSize(QSize(0, 40))
        self.footer_3.setMaximumSize(QSize(16777215, 40))
        self.footer_3.setStyleSheet(u"")
        self.footer_3.setFrameShape(QFrame.NoFrame)
        self.footer_3.setFrameShadow(QFrame.Raised)
        self.progressBar_3 = QProgressBar(self.footer_3)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setGeometry(QRect(0, 0, 330, 40))
        self.progressBar_3.setMinimumSize(QSize(330, 40))
        self.progressBar_3.setMaximumSize(QSize(330, 40))
        self.progressBar_3.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #333;\n"
"    border-radius: 5px;\n"
"	background-color: #282828;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #111;\n"
"    width: 3px;\n"
"}")
        self.progressBar_3.setValue(0)
        self.progressBar_3.setOrientation(Qt.Horizontal)
        self.progressBar_3.setTextDirection(QProgressBar.TopToBottom)
        self.bartxt_3 = QLabel(self.footer_3)
        self.bartxt_3.setObjectName(u"bartxt_3")
        self.bartxt_3.setGeometry(QRect(0, 0, 330, 40))
        self.bartxt_3.setMinimumSize(QSize(330, 40))
        self.bartxt_3.setMaximumSize(QSize(330, 40))
        self.bartxt_3.setStyleSheet(u"color: #ccc;\n"
"font-size: 12px;\n"
"padding-bottom: 2px;")
        self.bartxt_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.footer_3)

        self.footer_3.raise_()
        self.resultbar_3.raise_()
        self.stackedWidget.addWidget(self.transform)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.verticalLayout_12 = QVBoxLayout(self.history)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.history)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"#frame_11 {\n"
"	background-color: #222;\n"
"}")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(330, 40))
        self.frame_12.setMaximumSize(QSize(330, 40))
        self.frame_12.setStyleSheet(u"#abouth {\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"	color: #ccc;\n"
"} \n"
"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: rgb(255, 0, 38);\n"
"}")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.abouth = QLabel(self.frame_12)
        self.abouth.setObjectName(u"abouth")

        self.horizontalLayout_5.addWidget(self.abouth)

        self.clearh = QPushButton(self.frame_12)
        self.clearh.setObjectName(u"clearh")
        self.clearh.setEnabled(False)
        self.clearh.setMinimumSize(QSize(130, 40))
        self.clearh.setMaximumSize(QSize(130, 40))
        self.clearh.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.clearh)


        self.verticalLayout_13.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_13)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:horizontal {\n"
"	width: 0px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #222;\n"
"	width: 12px;\n"
"	margin: 3px 2px 3px 2px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: #555;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: #333;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical  {\n"
"	background: none;\n"
"	height: 26px;\n"
"    subcontrol-position: top left;\n"
"    subcontrol-origin: margin;       \n"
"	position: absolute;\n"
"}\n"
"QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	width: 0px;\n"
"    height: 0px;\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 330, 380))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 380))
        self.frame_14.setStyleSheet(u"#frame_14 {\n"
"	background-color: #222;\n"
"	padding-top: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 12px;\n"
"	color: #777;\n"
"}")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.past = QLabel(self.frame_14)
        self.past.setObjectName(u"past")
        self.past.setMinimumSize(QSize(330, 0))
        self.past.setMaximumSize(QSize(330, 16777))
        self.past.setWordWrap(True)
        self.past.setMargin(0)
        self.past.setIndent(3)

        self.verticalLayout_16.addWidget(self.past, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer)


        self.verticalLayout_15.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)


        self.verticalLayout_13.addWidget(self.frame_13)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.history)
        self.about_2 = QWidget()
        self.about_2.setObjectName(u"about_2")
        self.about_2.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.about_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.about_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"#frame_15 {\n"
"	background-color: #222;\n"
"}")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 10, 10, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"#label_9 {\n"
"	color: #444;\n"
"	font-size: 14px;\n"
"}\n"
"#label_13, #label_15, #label_17 {\n"
"	color: #666;\n"
"	font-size: 12px;\n"
"}\n"
"#label_14, #label_16, #label_18 {\n"
"	color: #ccc;\n"
"}\n"
"#label_19 {\n"
"	color: #151515;\n"
"	font-size: 10px;\n"
"}\n"
"#label_24 {\n"
"	color: #666;\n"
"	font-size: 12px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 50))
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_9, 0, Qt.AlignTop)

        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_19.addWidget(self.label_22)

        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 20))
        self.label_13.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_19.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_16)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 40))
        self.label_14.setMaximumSize(QSize(16777215, 40))
        self.label_14.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_14)

        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_19.addWidget(self.label_20)

        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_19.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_16)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 40))
        self.label_16.setMaximumSize(QSize(16777215, 40))
        self.label_16.setScaledContents(False)
        self.label_16.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_16)

        self.label_21 = QLabel(self.frame_16)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_19.addWidget(self.label_21)

        self.label_17 = QLabel(self.frame_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 20))
        self.label_17.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_19.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 40))
        self.label_18.setMaximumSize(QSize(16777215, 40))
        self.label_18.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_18)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_19.addWidget(self.label_23)

        self.label_25 = QLabel(self.frame_16)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_19.addWidget(self.label_25)

        self.label_24 = QLabel(self.frame_16)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_19.addWidget(self.label_24)

        self.label_26 = QLabel(self.frame_16)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_19.addWidget(self.label_26)

        self.pushButton = QPushButton(self.frame_16)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 40))
        self.pushButton.setMaximumSize(QSize(100, 40))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: rgb(56, 255, 69);\n"
"}\n"
"\n"
"")

        self.verticalLayout_19.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_2)

        self.label_19 = QLabel(self.frame_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 30))
        self.label_19.setMaximumSize(QSize(16777215, 30))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_19)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_17.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.about_2)
        self.settings_2 = QWidget()
        self.settings_2.setObjectName(u"settings_2")
        self.verticalLayout_20 = QVBoxLayout(self.settings_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.settings_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"#frame_17 {\n"
"	background-color: #222;\n"
"}\n"
"QLabel {\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"}\n"
"QPushButton {	\n"
"	border: 2px solid #282828;\n"
"	background-color: #181818;\n"
"	color: #ccc;\n"
"	font-size: 12px;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #111;\n"
"	color: #fff;\n"
"}")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_17)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 10, 10, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 130))
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_27 = QLabel(self.frame_18)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 0, 131, 40))
        self.label_27.setMinimumSize(QSize(0, 40))
        self.label_27.setMaximumSize(QSize(16777215, 40))
        self.tur = QPushButton(self.frame_18)
        self.tur.setObjectName(u"tur")
        self.tur.setEnabled(False)
        self.tur.setGeometry(QRect(0, 40, 330, 40))
        self.tur.setMinimumSize(QSize(330, 40))
        self.tur.setMaximumSize(QSize(330, 40))
        self.tur.setCursor(QCursor(Qt.PointingHandCursor))
        self.tur.setStyleSheet(u"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;")
        self.tur.setCheckable(True)
        self.tur.setChecked(True)
        self.eng = QPushButton(self.frame_18)
        self.eng.setObjectName(u"eng")
        self.eng.setGeometry(QRect(0, 78, 330, 40))
        self.eng.setMinimumSize(QSize(330, 40))
        self.eng.setMaximumSize(QSize(330, 40))
        self.eng.setCursor(QCursor(Qt.PointingHandCursor))
        self.eng.setStyleSheet(u"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;")
        self.eng.setCheckable(True)

        self.verticalLayout_21.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 200))
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_19)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 0, 201, 40))
        self.label_28.setMinimumSize(QSize(0, 40))
        self.label_28.setMaximumSize(QSize(16777215, 40))
        self.white = QPushButton(self.frame_19)
        self.white.setObjectName(u"white")
        self.white.setEnabled(False)
        self.white.setGeometry(QRect(0, 40, 330, 40))
        self.white.setMinimumSize(QSize(330, 40))
        self.white.setMaximumSize(QSize(330, 40))
        self.white.setCursor(QCursor(Qt.PointingHandCursor))
        self.white.setStyleSheet(u"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;")
        self.white.setCheckable(True)
        self.white.setChecked(True)
        self.blue = QPushButton(self.frame_19)
        self.blue.setObjectName(u"blue")
        self.blue.setGeometry(QRect(0, 78, 330, 40))
        self.blue.setMinimumSize(QSize(330, 40))
        self.blue.setMaximumSize(QSize(330, 40))
        self.blue.setCursor(QCursor(Qt.PointingHandCursor))
        self.blue.setStyleSheet(u"#blue:hover {\n"
"	color: rgb(0, 123, 255);\n"
"}\n"
"#blue:checked {\n"
"	color: rgb(0, 123, 255);\n"
"}")
        self.blue.setCheckable(True)
        self.red = QPushButton(self.frame_19)
        self.red.setObjectName(u"red")
        self.red.setGeometry(QRect(0, 116, 330, 40))
        self.red.setMinimumSize(QSize(330, 40))
        self.red.setMaximumSize(QSize(330, 40))
        self.red.setCursor(QCursor(Qt.PointingHandCursor))
        self.red.setStyleSheet(u"#red:hover {\n"
"	color: rgb(255, 0, 38);\n"
"}\n"
"#red:checked {\n"
"	color: rgb(255, 0, 38);\n"
"}")
        self.red.setCheckable(True)
        self.green = QPushButton(self.frame_19)
        self.green.setObjectName(u"green")
        self.green.setGeometry(QRect(0, 154, 330, 40))
        self.green.setMinimumSize(QSize(330, 40))
        self.green.setMaximumSize(QSize(330, 40))
        self.green.setCursor(QCursor(Qt.PointingHandCursor))
        self.green.setStyleSheet(u"#green {\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#green:hover {\n"
"	color: rgb(0, 255, 81);\n"
"}\n"
"#green:checked {\n"
"	color: rgb(0, 255, 81);\n"
"}\n"
"\n"
"")
        self.green.setCheckable(True)

        self.verticalLayout_21.addWidget(self.frame_19, 0, Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)


        self.verticalLayout_20.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.settings_2)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_5.addWidget(self.workplace)


        self.horizontalLayout.addWidget(self.body)


        self.verticalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"BlueTube", None))
        self.videobtn.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.label.setText("")
        self.musicbtn.setText(QCoreApplication.translate("MainWindow", u"M\u00fczik", None))
        self.label_2.setText("")
        self.transformbtn.setText(QCoreApplication.translate("MainWindow", u"D\u00f6n\u00fc\u015ft\u00fcr", None))
        self.label_3.setText("")
        self.label_6.setText("")
        self.historybtn.setText(QCoreApplication.translate("MainWindow", u"Ge\u00e7mi\u015f", None))
        self.label_4.setText("")
        self.aboutbtn.setText(QCoreApplication.translate("MainWindow", u"Hakk\u0131nda", None))
        self.label_5.setText("")
        self.settingsbtn.setText(QCoreApplication.translate("MainWindow", u"Ayarlar", None))
        self.minimize.setText("")
        self.close.setText("")
        self.searchtxt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"YouTube Linki", None))
        self.searchbtn.setText("")
        self.duration.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.videotitle.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Deneme", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dosya Konumu", None))
        self.btn720p.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn360p.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btnpath.setText(QCoreApplication.translate("MainWindow", u"/Downloads", None))
        self.downloadbtn.setText(QCoreApplication.translate("MainWindow", u"\u0130ndir", None))
        self.sizebtn.setText(QCoreApplication.translate("MainWindow", u"MB", None))
        self.progressBar.setFormat("")
        self.bartxt.setText(QCoreApplication.translate("MainWindow", u"Link Bekleniyor", None))
        self.searchtxt_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"YouTube Linki", None))
        self.searchbtn_2.setText("")
        self.duration_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.videotitle_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btnpath_2.setText(QCoreApplication.translate("MainWindow", u"/Downloads", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dosya Konumu", None))
        self.downloadbtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0130ndir", None))
        self.sizebtn_2.setText(QCoreApplication.translate("MainWindow", u"MB", None))
        self.progressBar_2.setFormat("")
        self.bartxt_2.setText(QCoreApplication.translate("MainWindow", u"Link Bekleniyor", None))
        self.downloadbtn_3.setText(QCoreApplication.translate("MainWindow", u"D\u00f6n\u00fc\u015ft\u00fcr", None))
        self.sizebtn_3.setText(QCoreApplication.translate("MainWindow", u"MB", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Video Se\u00e7", None))
        self.selectvideo.setText(QCoreApplication.translate("MainWindow", u"Video Se\u00e7in", None))
        self.videophoto.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"M\u00fczik Kaydetme Yeri Se\u00e7", None))
        self.selectmusic.setText(QCoreApplication.translate("MainWindow", u"/Downloads", None))
        self.progressBar_3.setFormat("")
        self.bartxt_3.setText(QCoreApplication.translate("MainWindow", u"Video Bekleniyor", None))
        self.abouth.setText(QCoreApplication.translate("MainWindow", u"Uygulama Ge\u00e7mi\u015fi", None))
        self.clearh.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.past.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Uygulama Hakk\u0131nda", None))
        self.label_22.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Video \u0130ndirme", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Video indirme \u00f6zelli\u011fi ile YouTube videolar\u0131n\u0131 360p ve 720p kalitesinde indirebilirsiniz.", None))
        self.label_20.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"M\u00fczik \u0130ndirme", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"M\u00fczik indirme \u00f6zelli\u011fi ile YouTube videolar\u0131n\u0131 128kbps kalitesinde ses format\u0131nda indirebilirsiniz.", None))
        self.label_21.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"D\u00f6n\u00fc\u015ft\u00fcrme", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"D\u00f6n\u00fc\u015ft\u00fcrme \u00f6zelli\u011fi ile se\u00e7ti\u011finiz herhangi bir mp4 format\u0131ndaki bir dosyay\u0131 mp3 format\u0131na \u00e7evirebilirsiniz.", None))
        self.label_23.setText("")
        self.label_25.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0130leti\u015fim: iletisimadresin@xxx", None))
        self.label_26.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Web Site", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Copyright 2023 | BlueTube", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Dil", None))
        self.tur.setText(QCoreApplication.translate("MainWindow", u"T\u00fcrk\u00e7e", None))
        self.eng.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Tema", None))
        self.white.setText(QCoreApplication.translate("MainWindow", u"Beyaz", None))
        self.blue.setText(QCoreApplication.translate("MainWindow", u"Mavi", None))
        self.red.setText(QCoreApplication.translate("MainWindow", u"K\u0131rm\u0131z\u0131", None))
        self.green.setText(QCoreApplication.translate("MainWindow", u"Ye\u015fil", None))
    # retranslateUi

