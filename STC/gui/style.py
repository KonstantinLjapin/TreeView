""" Определяет параметры внешнего вида приложения """

from os import path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from STC.config.config import CONFIG


class StyleFactory:
    """ Фабрика для стиля приложения """

    # pylint: disable = too-few-public-methods
    def __init__(self, app: QApplication):
        self.style = self.setAppStyle(app)

    @staticmethod
    def setAppStyle(app: QApplication):
        """ Возвращает экземпляр класса определенного стиля """
        style = CONFIG.color_style.color_style_current
        match style:
            case 'DarkGray':
                return StyleQDarkGrayStyle(app=app)
            case 'Fusion':
                return StyleFusion(app=app)
            case 'Windows':
                return StyleWindows(app=app)
            case 'Standard':
                return StyleStandart(app=app)


# pylint: disable=too-many-instance-attributes
class StyleClass:
    """ Родительский класс """
    color = 'black'

    def __init__(self, app: QApplication):
        self.app = app
        self.initStyle()
        self.fonts()
        self.icons()
        CONFIG.style = self

    def initStyle(self):
        """Текстовые стили """
        self.main_style_str = ""
        self.bar_btn_style_str = ""
        self.bar_title_style_str = ""
        self.app.setStyleSheet(self.main_style_str)

    def fonts(self):
        """ Параметры шрифтов """
        self.font = CONFIG.fonts.font
        self.font_size = CONFIG.fonts.font_size
        self.font_size_big = CONFIG.fonts.font_size_big
        self.font_size_toolbar = CONFIG.fonts.font_size_toolbar
        _id = QFontDatabase.addApplicationFont("Montserrat/Montserrat-Medium.ttf")
        self.app.setFont(QFont(self.font, self.font_size))

    def icons(self) -> None:
        """ Параметры иконок """
        match self.__class__.color:
            case 'white':
                self.icon_folder = CONFIG.icons.icons_white
                self.toolbar_text_color = 'rgb(255, 255, 255)'
                self.btn_stylesheet_active_table = \
                    "background-color: #D1DBCB; color: black; Text-align:left"
                self.btn_stylesheet_table = \
                    "background-color: #323232; color: #eff0f1; Text-align:left"
                self.splash_screen_text_color = Qt.white
            case 'black':
                self.icon_folder = CONFIG.icons.icons_black
                self.toolbar_text_color = 'rgb(0, 0, 0)'
                self.btn_stylesheet_active_table = "Text-align:left"
                self.btn_stylesheet_table = "Text-align:left"
                self.splash_screen_text_color = Qt.black

        self.arrow_down = QIcon(
            path.join(self.icon_folder, 'arrow_down [#338].png'))
        self.arrow_left = QIcon(
            path.join(self.icon_folder, 'arrow_left [#334].png'))
        self.arrow_left_2 = QIcon(
            path.join(self.icon_folder, 'arrow_left_2 [#334].png'))
        self.arrow_repeat = QIcon(
            path.join(self.icon_folder, 'arrow_repeat [#236].png'))
        self.arrow_repeat_red = QIcon(
            path.join(self.icon_folder, 'arrow_repeat_red [#236].png'))
        self.arrow_right = QIcon(
            path.join(self.icon_folder, 'arrow_right [#333].png'))
        self.arrow_up = QIcon(
            path.join(self.icon_folder, 'arrow_up [#337].png'))
        self.close = QIcon(
            path.join(self.icon_folder, 'close [#1511].png'))
        self.done_mini = QIcon(
            path.join(self.icon_folder, 'done_mini [#1484].png'))
        self.exit_full_screen = QIcon(
            path.join(self.icon_folder, 'exit_full_screen [#905].png'))
        self.file_arrow_down = QIcon(
            path.join(self.icon_folder, 'file_arrow_down [#1717].png'))
        self.file_arrow_down_norm = QIcon(
            path.join(self.icon_folder, 'file_arrow_down_norm [#1717].png'))
        self.file_arrow_down_serv = QIcon(
            path.join(self.icon_folder, 'file_arrow_down_serv [#1717].png'))
        self.file_arrow_down_full = QIcon(
            path.join(self.icon_folder, 'file_arrow_down_full [#1717].png'))
        self.file_plus = QIcon(
            path.join(self.icon_folder, 'file_plus [#1682].png'))
        self.filter = QIcon(
            path.join(self.icon_folder, 'filter [#1384].png'))
        self.full_screen = QIcon(
            path.join(self.icon_folder, 'full_screen [#904].png'))
        self.network_3_round = QIcon(
            path.join(self.icon_folder, 'network_3_round [#1084].png'))
        self.option_bar_settings = QIcon(
            path.join(self.icon_folder, 'option_bar_settings [#1399].png'))
        self.search_left = QIcon(
            path.join(self.icon_folder, 'search_left [#1504].png'))
        self.underline = QIcon(
            path.join(self.icon_folder, 'underline [#1437].png'))


class StyleQDarkGrayStyle(StyleClass):
    """ Темная тема """
    color = 'white'

    def initStyle(self):
        """ Параметры темы """
        self.main_style_str = """
                            QToolTip
                                {
                                     border: 1px solid black;
                                     background-color: #D1DBCB;
                                     padding: 1px;
                                     border-radius: 3px;
                                     opacity: 100;
                                }

                            QWidget
                                {
                                    color: #b1b1b1;
                                    background-color: #323232;
                                    selection-background-color:#323232;
                                    selection-color: black;
                                    background-clip: border;
                                    border-image: none;
                                    border: 0px transparent black;
                                    outline: 0;
                                }

                                QWidget:item:hover
                                    {
                                        background-color: #D1DBCB;
                                        color: black;
                                    }

                                QWidget:item:selected
                                    {
                                        background-color: #D1DBCB;
                                        border: 0px
                                    }

                            QCheckBox
                                {
                                    spacing: 5px;
                                    outline: none;
                                    color: #eff0f1;
                                    margin-bottom: 2px;
                                }

                                QCheckBox:disabled
                                    {
                                        color: #76797C;
                                    }

                                QCheckBox::indicator,QGroupBox::indicator
                                    {
                                        width: 18px;
                                        height: 18px;
                                    }

                                QGroupBox::indicator
                                    {
                                        margin-left: 2px;
                                    }

                                QCheckBox::indicator:unchecked
                                    {
                                        image: url('img/checkbox_unchecked.png');
                                    }

                                QCheckBox::indicator:unchecked:hover,
                                QCheckBox::indicator:unchecked:focus,
                                QCheckBox::indicator:unchecked:pressed,
                                QGroupBox::indicator:unchecked:hover,
                                QGroupBox::indicator:unchecked:focus,
                                QGroupBox::indicator:unchecked:pressed
                                    {
                                      border: none;
                                        image: url('img/checkbox_unchecked_focus.png');
                                    }

                                QCheckBox::indicator:checked
                                    {
                                        image: url('img/checkbox_checked.png');
                                    }

                                QCheckBox::indicator:checked:hover,
                                QCheckBox::indicator:checked:focus,
                                QCheckBox::indicator:checked:pressed,
                                QGroupBox::indicator:checked:hover,
                                QGroupBox::indicator:checked:focus,
                                QGroupBox::indicator:checked:pressed
                                    {
                                        border: none;
                                        image: url('img/checkbox_checked_focus.png');
                                    }


                                QCheckBox::indicator:indeterminate
                                    {
                                        image: url('img/checkbox_indeterminate.png');
                                    }

                                QCheckBox::indicator:indeterminate:focus,
                                QCheckBox::indicator:indeterminate:hover,
                                QCheckBox::indicator:indeterminate:pressed
                                    {
                                        image: url('img/checkbox_indeterminate_focus.png');
                                    }

                                QCheckBox::indicator:checked:disabled,
                                QGroupBox::indicator:checked:disabled
                                    {
                                        image: url('img/checkbox_checked_disabled.png');
                                    }

                                QCheckBox::indicator:unchecked:disabled,
                                QGroupBox::indicator:unchecked:disabled
                                    {
                                        image: url('img/checkbox_unchecked_disabled.png');
                                    }

                            QRadioButton
                                {
                                    spacing: 5px;
                                    outline: none;
                                    color: #eff0f1;
                                    margin-bottom: 2px;
                                }

                                QRadioButton:disabled
                                    {
                                        color: #76797C;
                                    }

                                QRadioButton::indicator
                                    {
                                        width: 21px;
                                        height: 21px;
                                    }

                                QRadioButton::indicator:unchecked
                                    {
                                        image: url('img/radio_unchecked.png');
                                    }


                                QRadioButton::indicator:unchecked:hover,
                                QRadioButton::indicator:unchecked:focus,
                                QRadioButton::indicator:unchecked:pressed
                                    {
                                        border: none;
                                        outline: none;
                                        image: url('img/radio_unchecked_focus.png');
                                    }

                                QRadioButton::indicator:checked
                                    {
                                        border: none;
                                        outline: none;
                                        image: url('img/radio_checked.png');
                                    }

                                QRadioButton::indicator:checked:hover,
                                QRadioButton::indicator:checked:focus,
                                QRadioButton::indicator:checked:pressed
                                    {
                                        border: none;
                                        outline: none;
                                        image: url('img/radio_checked_focus.png');
                                    }

                                QRadioButton::indicator:checked:disabled
                                    {
                                        outline: none;
                                        image: url('img/radio_checked_disabled.png');
                                    }

                                QRadioButton::indicator:unchecked:disabled
                                    {
                                        image: url('img/radio_unchecked_disabled.png');
                                    }

                            QMenuBar
                                {
                                    background-color: #323232;
                                    color: #D1DBCB;
                                }

                                QMenuBar::item
                                    {
                                        background-color: #323232;
                                        background: transparent;
                                        /* padding: 2px 20px 2px 20px; */
                                    }

                                QMenuBar::item:selected
                                    {
                                        background: transparent;
                                        /* border: 1px solid #76797C; */
                                    }

                                QMenuBar::item:pressed
                                    {
                                        border: 0px solid #76797C;
                                        background-color: #D1DBCB;
                                        color: #000;
                                        margin-bottom:-1px;
                                        padding-bottom:1px;
                                    }

                                QMenu
                                    {
                                        background-color: #323232;
                                        /* border: 1px solid #76797C; */
                                        color: #eff0f1;
                                        /*margin: 2px; */
                                    }

                                QMenu::icon
                                    {
                                        /*margin: 5px;*/
                                    }

                                QMenu::item
                                    {
                                        padding: 2px 30px 2px 30px;
                                        /*margin-left: 5px;*/
                                        border: 1px solid transparent; /* reserve space for selection border */
                                    }

                                QMenu::item:selected
                                    {
                                        color: #000000;
                                    }

                                QMenu::separator {
                                        height: 2px;
                                        background: #D1DBCB;
                                        margin-left: 10px;
                                        margin-right: 5px;
                                    }

                                QMenu::indicator {
                                        width: 18px;
                                        height: 18px;
                                    }

                                /* non-exclusive indicator = check box style indicator
                                   (see QActionGroup::setExclusive) */
                                QMenu::indicator:non-exclusive:unchecked {
                                        image: url('img/checkbox_unchecked.png');
                                    }

                                QMenu::indicator:non-exclusive:unchecked:selected {
                                        image: url('img/checkbox_unchecked_disabled.png');
                                    }

                                QMenu::indicator:non-exclusive:checked {
                                        image: url('img/checkbox_checked.png');
                                    }

                                QMenu::indicator:non-exclusive:checked:selected {
                                        image: url('img/checkbox_checked_disabled.png');
                                    }

                                /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
                                QMenu::indicator:exclusive:unchecked {
                                        image: url('img/radio_unchecked.png');
                                    }

                                QMenu::indicator:exclusive:unchecked:selected {
                                        image: url('img/radio_unchecked_disabled.png');
                                    }

                                QMenu::indicator:exclusive:checked {
                                        image: url('img/radio_checked.png');
                                    }

                                QMenu::indicator:exclusive:checked:selected {
                                        image: url('img/radio_checked_disabled.png');
                                    }

                                QMenu::right-arrow {
                                        margin: 5px;
                                        image: url('img/right_arrow.png')
                                    }


                                QWidget:disabled
                                    {
                                        color: #454545;
                                        background-color: #323232;
                                    }

                            QAbstractItemView
                                {
                                    alternate-background-color: #323232;
                                    color: #eff0f1;
                                    border: 1px solid 3A3939;
                                    border-radius: 2px;
                                }

                                QWidget:focus, QMenuBar:focus,QToolBar:focus,QScrollAreaViewer:focus
                                    {
                                        /* border: 2px solid #D1DBCB; */
                                    }

                                QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus
                                    {
                                        border: none;
                                    }

                            QLineEdit
                                {
                                    background-color: #1e1e1e;
                                    selection-background-color: #D1DBCB;
                                    selection-color: black;
                                    padding: 5px;
                                    border-style: solid;
                                    border: 1px solid #76797C;
                                    border-radius: 2px;
                                    color: #eff0f1;
                                }

                             QGroupBox {
                                    border:1px solid #76797C;
                                    border-radius: 2px;
                                    margin-top: 20px;
                                }

                                QGroupBox::title {
                                        subcontrol-origin: margin;
                                        subcontrol-position: top center;
                                        padding-left: 10px;
                                        padding-right: 10px;
                                        padding-top: 10px;
                                    }

                            QAbstractScrollArea
                                {
                                    border-radius: 0px;
                                    border: 0px solid #76797C;
                                    background-color: transparent;
                                }

                            QScrollBar:horizontal
                                {
                                    height: 15px;
                                    margin: 3px 15px 3px 15px;
                                    border: 1px transparent #2A2929;
                                    border-radius: 4px;
                                    background-color: #2A2929;
                                }

                                QScrollBar::handle:horizontal
                                    {
                                        background-color: #605F5F;
                                        min-width: 5px;
                                        border-radius: 4px;
                                    }

                                QScrollBar::add-line:horizontal
                                    {
                                        margin: 0px 3px 0px 3px;
                                        border-image: url('img/right_arrow_disabled.png');
                                        width: 10px;
                                        height: 10px;
                                        subcontrol-position: right;
                                        subcontrol-origin: margin;
                                    }

                                QScrollBar::sub-line:horizontal
                                    {
                                        margin: 0px 3px 0px 3px;
                                        border-image: url('img/left_arrow_disabled.png');
                                        height: 10px;
                                        width: 10px;
                                        subcontrol-position: left;
                                        subcontrol-origin: margin;
                                    }

                                QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
                                    {
                                        border-image: url('img/right_arrow.png');
                                        height: 10px;
                                        width: 10px;
                                        subcontrol-position: right;
                                        subcontrol-origin: margin;
                                    }


                                QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
                                    {
                                        border-image: url('img/left_arrow.png');
                                        height: 10px;
                                        width: 10px;
                                        subcontrol-position: left;
                                        subcontrol-origin: margin;
                                    }

                                QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
                                    {
                                        background: none;
                                    }


                                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
                                    {
                                        background: none;
                                    }

                                QScrollBar:vertical
                                    {
                                        background-color: #2A2929;
                                        width: 15px;
                                        margin: 15px 3px 15px 3px;
                                        border: 1px transparent #2A2929;
                                        border-radius: 4px;
                                    }

                                QScrollBar::handle:vertical
                                    {
                                        background-color: #605F5F;
                                        min-height: 5px;
                                        border-radius: 4px;
                                    }

                                QScrollBar::sub-line:vertical
                                    {
                                        margin: 3px 0px 3px 0px;
                                        border-image: url('img/up_arrow_disabled.png');
                                        height: 10px;
                                        width: 10px;
                                        subcontrol-position: top;
                                        subcontrol-origin: margin;
                                    }

                                QScrollBar::add-line:vertical
                                    {
                                        margin: 3px 0px 3px 0px;
                                        border-image: url('img/down_arrow_disabled.png');
                                        height: 10px;
                                        width: 10px;
                                        subcontrol-position: bottom;
                                        subcontrol-origin: margin;
                                    }

                                QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
                                    {

                                        border-image: url('img/up_arrow.png');
                                        height: 10px;
                                        width: 10px;
                                        subcontrol-position: top;
                                        subcontrol-origin: margin;
                                    }


                                QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
                                    {
                                        border-image: url('img/down_arrow.png');
                                        height: 10px;
                                        width: 10px;
                                        subcontrol-position: bottom;
                                        subcontrol-origin: margin;
                                    }

                                QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
                                    {
                                        background: none;
                                    }


                                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                                    {
                                        background: none;
                                    }

                            QTextEdit
                                {
                                    background-color: #1e1e1e;
                                    color: #eff0f1;
                                    border: 1px solid #76797C;
                                }

                            QPlainTextEdit
                                {
                                    background-color: #1e1e1e;;
                                    color: #eff0f1;
                                    border-radius: 2px;
                                    border: 1px solid #76797C;
                                }

                            QPlainTextEdit:hover
                                {
                                    background: #D1DBCB;
                                        color: black;
                                }

                            QHeaderView::section
                                {
                                    background-color: #76797C;
                                    color: #eff0f1;
                                    padding: 5px;
                                    border: 1px solid #76797C;
                                }

                            QSizeGrip {
                                    image: url('img/sizegrip.png');
                                    width: 12px;
                                    height: 12px;
                                }

                            QMainWindow::separator
                                {
                                    background-color: #323232;
                                    color: white;
                                    padding-left: 4px;
                                    spacing: 2px;
                                    border: 1px dashed #76797C;
                                }

                                QMainWindow::separator:hover
                                    {

                                        background-color: #787876;
                                        color: white;
                                        padding-left: 4px;
                                        border: 1px solid #76797C;
                                        spacing: 2px;
                                    }


                                QMenu::separator
                                    {
                                        height: 1px;
                                        background-color: #76797C;
                                        color: white;
                                        padding-left: 4px;
                                        margin-left: 10px;
                                        margin-right: 5px;
                                    }

                            QFrame
                                {
                                    border-radius: 0px;
                                    /*border: 1px solid #76797C;*/
                                }


                                QFrame[frameShape="0"]
                                    {
                                        border-radius: 0px;
                                        border: 0px transparent #76797C;
                                    }

                            QStackedWidget
                                {
                                    border: 1px transparent black;
                                }

                            QToolBar {
                                    border: 0px transparent #393838;
                                    background: 0px solid #323232;
                                    font-weight: bold;
                                }

                                QToolBar::handle:horizontal {
                                        image: url('img/Hmovetoolbar.png');
                                    }
                                QToolBar::handle:vertical {
                                        image: url('img/Vmovetoolbar.png');
                                    }
                                QToolBar::separator:horizontal {
                                        image: url('img/Hsepartoolbar.png');
                                    }
                                QToolBar::separator:vertical {
                                        image: url('img/Vsepartoolbar.png');
                                    }
                                QToolButton#qt_toolbar_ext_button {
                                        background: #58595a
                                    }

                            QPushButton
                                {
                                    color: #eff0f1;
                                    background-color: #323232;
                                    border-width: 1px;
                                    border-color: #76797C;
                                    border-style: solid;
                                    padding: 5px;
                                    border-radius: 0px;
                                    outline: none;
                                }

                                QPushButton:disabled
                                    {
                                        background-color: #323232;
                                        border-width: 1px;
                                        border-color: #454545;
                                        border-style: solid;
                                        padding-top: 5px;
                                        padding-bottom: 5px;
                                        padding-left: 10px;
                                        padding-right: 10px;
                                        border-radius: 2px;
                                        color: #454545;
                                    }

                                QPushButton:focus {
                                        background-color: #D1DBCB;
                                        color: black;
                                    }

                                QPushButton:pressed
                                    {
                                        color: black;
                                        background-color: #D1DBCB;
                                        padding-top: -15px;
                                        padding-bottom: -17px;
                                    }

                                QPushButton:checked{
                                        background-color: #76797C;
                                        border-color: #6A6969;
                                    }

                            QComboBox
                                {
                                    selection-background-color: #D1DBCB;
                                    background-color: #31363B;
                                    border-style: solid;
                                    border: 1px solid #76797C;
                                    border-radius: 2px;
                                    padding: 5px;
                                    min-width: 75px;
                                }

                                QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QAbstractView:hover,QTreeView:hover
                                    {
                                        border: 1px solid #D1DBCB;
                                    }



                                QComboBox:on
                                    {
                                        padding-top: 0px;
                                        padding-left: 4px;
                                        selection-background-color: #4a4a4a;
                                    }

                                QComboBox QAbstractItemView
                                    {
                                        background-color: #1e1e1e;
                                        border-radius: 2px;
                                        border: 1px solid #76797C;
                                        selection-background-color: #D1DBCB;
                                    }

                                QComboBox::drop-down
                                    {
                                        subcontrol-origin: padding;
                                        subcontrol-position: top right;
                                        width: 15px;

                                        border-left-width: 0px;
                                        border-left-color: darkgray;
                                        border-left-style: solid;
                                        border-top-right-radius: 3px;
                                        border-bottom-right-radius: 3px;
                                    }

                                QComboBox::down-arrow
                                    {
                                        image: url('img/down_arrow_disabled.png');
                                    }

                                QComboBox::down-arrow:on, QComboBox::down-arrow:hover,
                                QComboBox::down-arrow:focus
                                    {
                                        image: url('img/down_arrow.png');
                                    }

                            QAbstractSpinBox {
                                    padding: 2px;
                                    margin: 2px;
                                    background-color: #1e1e1e;
                                    color: #eff0f1;
                                    border-radius: 0px;
                                    min-width: 75px;
                                    selection-background-color: #D1DBCB;
                                    selection-color: black;
                                }

                                QAbstractSpinBox:up-button
                                    {
                                        background-color: transparent;
                                        subcontrol-origin: border;
                                        subcontrol-position: center right;
                                    }

                                QAbstractSpinBox:down-button
                                    {
                                        background-color: transparent;
                                        subcontrol-origin: border;
                                        subcontrol-position: center left;
                                    }

                                QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {
                                        image: url('img/up_arrow_disabled.png');
                                        width: 10px;
                                        height: 10px;
                                    }
                                QAbstractSpinBox::up-arrow:hover
                                    {
                                        image: url('img/up_arrow.png');
                                    }


                                QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off
                                    {
                                        image: url('img/down_arrow_disabled.png');
                                        width: 10px;
                                        height: 10px;
                                    }
                                QAbstractSpinBox::down-arrow:hover
                                    {
                                        image: url('img/down_arrow.png');
                                    }

                            QLabel
                                {
                                    border: 0px solid black;
                                    margin-left: 2px;
                                    margin-right: 2px;
                                    color: #D1DBCB;
                                }

                            QTabWidget{
                                    border: 0px transparent black;
                                }

                                QTabWidget::pane {
                                        border: 1px solid #76797C;
                                        padding: 5px;
                                        margin: 0px;
                                    }

                                QTabWidget::tab-bar {
                                        left: 5px; /* move to the right by 5px */
                                    }

                            QTabBar
                                {
                                    qproperty-drawBase: 0;
                                    border-radius: 3px;
                                }

                                QTabBar::focus
                                    {
                                        border: 0px transparent black;
                                        color: black;
                                    }

                                QTabBar::hover
                                    {
                                        border: 0px transparent black;
                                        color: black;
                                    }

                                QTabBar::close-button  {
                                        image: url('img/close.png');
                                        background: transparent;
                                    }

                                QTabBar::close-button:hover
                                    {
                                        image: url('img/close-hover.png');
                                        background: transparent;
                                    }

                                QTabBar::close-button:pressed {
                                        image: url('img/close-pressed.png');
                                        background: transparent;
                                    }

                                /* TOP TABS */
                                QTabBar::tab:top {
                                        color: #eff0f1;
                                        border: 1px solid #76797C;
                                        border-bottom: 1px transparent black;
                                        background-color: #323232;
                                        padding: 5px;
                                        min-width: 50px;
                                        border-top-left-radius: 2px;
                                        border-top-right-radius: 2px;
                                    }

                                QTabBar::tab:top:!selected
                                    {
                                        color: #eff0f1;
                                        background-color: #54575B;
                                        border: 1px solid #76797C;
                                        border-bottom: 1px transparent black;
                                        border-top-left-radius: 2px;
                                        border-top-right-radius: 2px;
                                    }

                                QTabBar::tab:top:!selected:hover {
                                        background-color: #D1DBCB;
                                        color: black;
                                    }

                                /* BOTTOM TABS */
                                QTabBar::tab:bottom {
                                        color: #eff0f1;
                                        border: 1px solid #76797C;
                                        border-top: 1px transparent black;
                                        background-color: #323232;
                                        padding: 5px;
                                        border-bottom-left-radius: 2px;
                                        border-bottom-right-radius: 2px;
                                        min-width: 50px;
                                    }

                                QTabBar::tab:bottom:!selected
                                    {
                                        color: #eff0f1;
                                        background-color: #54575B;
                                        border: 1px solid #76797C;
                                        border-top: 1px transparent black;
                                        border-bottom-left-radius: 2px;
                                        border-bottom-right-radius: 2px;
                                    }

                                QTabBar::tab:bottom:!selected:hover {
                                        background-color: #D1DBCB;
                                        color: black;
                                    }

                                /* LEFT TABS */
                                QTabBar::tab:left {
                                        color: #eff0f1;
                                        border: 1px solid #76797C;
                                        border-left: 1px transparent black;
                                        background-color: #323232;
                                        padding: 5px;
                                        border-top-right-radius: 2px;
                                        border-bottom-right-radius: 2px;
                                        min-height: 50px;
                                    }

                                QTabBar::tab:left:!selected
                                    {
                                        color: #eff0f1;
                                        background-color: #54575B;
                                        border: 1px solid #76797C;
                                        border-left: 1px transparent black;
                                        border-top-right-radius: 2px;
                                        border-bottom-right-radius: 2px;
                                    }

                                QTabBar::tab:left:!selected:hover {
                                        background-color: #D1DBCB;
                                        color: black;
                                    }


                                /* RIGHT TABS */
                                QTabBar::tab:right {
                                        color: #eff0f1;
                                        border: 1px solid #76797C;
                                        border-right: 1px transparent black;
                                        background-color: #323232;
                                        padding: 5px;
                                        border-top-left-radius: 2px;
                                        border-bottom-left-radius: 2px;
                                        min-height: 50px;
                                    }

                                QTabBar::tab:right:!selected
                                    {
                                        color: #eff0f1;
                                        background-color: #54575B;
                                        border: 1px solid #76797C;
                                        border-right: 1px transparent black;
                                        border-top-left-radius: 2px;
                                        border-bottom-left-radius: 2px;
                                    }

                                QTabBar::tab:right:!selected:hover {
                                        background-color: #D1DBCB;
                                        color: black;
                                    }

                                QTabBar QToolButton::right-arrow:enabled {
                                         image: url('img/right_arrow.png');
                                     }

                                 QTabBar QToolButton::left-arrow:enabled {
                                         image: url('img/left_arrow.png');
                                     }

                                QTabBar QToolButton::right-arrow:disabled {
                                         image: url('img/right_arrow_disabled.png');
                                     }

                                 QTabBar QToolButton::left-arrow:disabled {
                                         image: url('img/left_arrow_disabled.png');
                                     }

                            QDockWidget {
                                    background: #323232;
                                    border: 1px solid #403F3F;
                                    titlebar-close-icon: url('img/close.png');
                                    titlebar-normal-icon: url('img/undock.png');
                                }

                                QDockWidget::close-button, QDockWidget::float-button {
                                        border: 1px solid transparent;
                                        border-radius: 2px;
                                        background: transparent;
                                    }

                                QDockWidget::close-button:hover, QDockWidget::float-button:hover {
                                        background: rgba(255, 255, 255, 10);
                                    }

                                QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
                                        padding: 1px -1px -1px 1px;
                                        background: rgba(255, 255, 255, 10);
                                    }

                                QTreeView, QListView
                                    {
                                        border: 1px solid #76797C;
                                        background-color: #1e1e1e;
                                    }

                                QTreeView:branch:selected, QTreeView:branch:hover
                                    {
                                        background: url(img/transparent.png);
                                    }

                                QTreeView::branch:has-siblings:!adjoins-item {
                                        border-image: url('img/transparent.png');
                                    }

                                QTreeView::branch:has-siblings:adjoins-item {
                                        border-image: url('img/transparent.png');
                                    }

                                QTreeView::branch:!has-children:!has-siblings:adjoins-item {
                                        border-image: url('img/transparent.png');
                                    }

                                QTreeView::branch:has-children:!has-siblings:closed,
                                QTreeView::branch:closed:has-children:has-siblings {
                                        image: url('img/branch_closed.png');
                                    }

                                QTreeView::branch:open:has-children:!has-siblings,
                                QTreeView::branch:open:has-children:has-siblings  {
                                        image: url('img/branch_open.png');
                                    }

                                QTreeView::branch:has-children:!has-siblings:closed:hover,
                                QTreeView::branch:closed:has-children:has-siblings:hover {
                                    image: url('img/branch_closed-on.png');
                                    }

                                QTreeView::branch:open:has-children:!has-siblings:hover,
                                QTreeView::branch:open:has-children:has-siblings:hover  {
                                    image: url('img/branch_open-on.png');
                                    }

                                QListView::item:!selected:hover, QTreeView::item:!selected:hover {
                                        background: #848383;
                                        outline: 0;
                                        color: #eff0f1;
                                    }

                                QTreeView::item {}

                                QListView::item:selected:hover, QTreeView::item:selected:hover {
                                        background: #D1DBCB;
                                    }

                                QSlider::groove:horizontal {
                                        border: 1px solid #565a5e;
                                        height: 4px;
                                        background: #565a5e;
                                        margin: 0px;
                                        border-radius: 2px;
                                    }

                                QSlider::handle:horizontal {
                                        background: #D1DBCB;
                                        border: 1px solid #999999;
                                        width: 10px;
                                        height: 10px;
                                        margin: -5px 0;
                                    }

                                QSlider::add-page:qlineargradient {
                                        background: #595858;
                                        border-top-right-radius: 5px;
                                        border-bottom-right-radius: 5px;
                                        border-top-left-radius: 0px;
                                        border-bottom-left-radius: 0px;
                                    }

                                QSlider::sub-page::qlineargradient:horizontal {
                                        background:  #D1DBCB;
                                        border-top-right-radius: 0px;
                                        border-bottom-right-radius: 0px;
                                        border-top-left-radius: 5px;
                                        border-bottom-left-radius: 5px;
                                    }

                                QSlider::groove:vertical {
                                        border: 1px solid #565a5e;
                                        width: 4px;
                                        background: #565a5e;
                                        margin: 0px;
                                        border-radius: 3px;
                                    }

                                QSlider::handle:vertical {
                                        background: #D1DBCB;
                                        border: 1px solid #999999;
                                        width: 10px;
                                        height: 10px;
                                        margin: 0 -5px;
                                    }

                            QToolButton {
                                    color: #D1DBCB;
                                    background-color: transparent;
                                    border: 0px transparent #76797C;
                                    border-radius: 0px;
                                    padding: 1px;
                                    margin-right: 5px;
                                }

                                QToolButton[popupMode="1"] { /* only for MenuButtonPopup */
                                     padding-right: 20px; /* make way for the popup button */
                                     border: 1px #76797C;
                                     border-radius: 0px;
                                    }

                                QToolButton[popupMode="2"] { /* only for InstantPopup */
                                     padding-right: 10px; /* make way for the popup button */
                                     border: 0px #76797C;
                                    }


                                QToolButton:hover, QToolButton::menu-button:hover {
                                        background-color: transparent;
                                        border: 1px solid #D1DBCB;
                                        padding: 2px;
                                    }

                                QToolButton:checked, QToolButton:pressed,
                                        QToolButton::menu-button:pressed {
                                                color: black;
                                                background-color: #D1DBCB;
                                                border: 0px solid #D1DBCB;
                                                padding: 2px;
                                            }

                                /* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */
                                QToolButton::menu-indicator {
                                        image: url('img/down_arrow.png');
                                        top: -7px; left: -2px; /* shift it a bit */
                                    }

                                /* the subcontrols below are used only in the MenuButtonPopup mode */
                                QToolButton::menu-button {
                                        border: 1px transparent #76797C;
                                        border-top-right-radius: 6px;
                                        border-bottom-right-radius: 6px;
                                        /* 16px width + 4px for border = 20px allocated above */
                                        width: 16px;
                                        outline: none;
                                    }

                                QToolButton::menu-arrow {
                                        image: url('img/down_arrow.png');
                                    }

                                QToolButton::menu-arrow:open {
                                        border: 1px solid #76797C;
                                    }

                                QPushButton::menu-indicator  {
                                        subcontrol-origin: padding;
                                        subcontrol-position: bottom right;
                                        left: 8px;
                                    }

                            QTableView
                                {
                                    border: 1px solid #76797C;
                                    gridline-color: #323232;
                                    background-color: #1e1e1e;
                                }

                            QTableView, QHeaderView
                                {
                                    border-radius: 0px;
                                }

                                QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed {
                                        background: #D1DBCB;
                                        color: black;
                                    }

                                QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active {
                                        background: #D1DBCB;
                                        color: black;
                                    }

                                QHeaderView
                                    {
                                        background-color: #323232;
                                        border: 1px transparent;
                                        border-radius: 0px;
                                        margin: 0px;
                                        padding: 0px;

                                    }

                                QHeaderView::section  {
                                        background-color: #323232;
                                        color: #eff0f1;
                                        padding: 5px;
                                        border: 1px solid #76797C;
                                        border-radius: 0px;
                                        text-align: center;
                                    }

                                QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one
                                    {
                                        border-top: 1px solid #76797C;
                                    }

                                QHeaderView::section::vertical
                                    {
                                        border-top: transparent;
                                    }

                                QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one
                                    {
                                        border-left: 1px solid #76797C;
                                    }

                                QHeaderView::section::horizontal
                                    {
                                        border-left: transparent;
                                    }


                                QHeaderView::section:checked
                                     {
                                        color: white;
                                        background-color: #848383;
                                     }

                                 /* style the sort indicator */
                                QHeaderView::down-arrow {
                                        image: url('img/down_arrow.png');
                                    }

                                QHeaderView::up-arrow {
                                        image: url('img/up_arrow.png');
                                    }


                                QTableCornerButton::section {
                                        background-color: #323232;
                                        border: 1px transparent #76797C;
                                        border-radius: 0px;
                                    }

                            QToolBox  {
                                    padding: 5px;
                                    border: 1px transparent black;
                                }

                                QToolBox::tab {
                                        color: #eff0f1;
                                        background-color: #323232;
                                        border: 1px solid #76797C;
                                        border-bottom: 1px transparent #323232;
                                        border-top-left-radius: 5px;
                                        border-top-right-radius: 5px;
                                    }

                                QToolBox::tab:selected { /* italicize selected tabs */
                                        font: italic;
                                        background-color: #323232;
                                        border-color: #D1DBCB;
                                     }

                                QStatusBar::item {
                                        border: 0px transparent dark;
                                        margin: 0px;
                                        border: 0px;
                                     }


                                QFrame[height="3"], QFrame[width="3"] {
                                        background-color: #76797C;
                                    }


                                QSplitter::handle {
                                        border: 1px dashed #76797C;
                                    }

                                QSplitter::handle:hover {
                                        background-color: #787876;
                                        border: 1px solid #76797C;
                                    }

                                QSplitter::handle:horizontal {
                                        width: 1px;
                                    }

                                QSplitter::handle:vertical {
                                        height: 1px;
                                    }

                            QProgressBar {
                                    border: 1px solid #76797C;
                                    border-radius: 5px;
                                    text-align: center;
                                }

                                QProgressBar::chunk {
                                        background-color: #D1DBCB;
                                    }

                            QDateEdit
                                {
                                    selection-background-color: #D1DBCB;
                                    border-style: solid;
                                    border: 1px solid #CEE343;
                                    border-radius: 2px;
                                    padding: 1px;
                                    min-width: 75px;
                                }

                                QDateEdit:on
                                    {
                                        padding-top: 3px;
                                        padding-left: 4px;
                                        selection-background-color: #4a4a4a;
                                    }

                                QDateEdit QAbstractItemView
                                    {
                                        background-color: #1e1e1e;
                                        border-radius: 2px;
                                        border: 1px solid #3375A3;
                                        selection-background-color: #D1DBCB;
                                    }

                                QDateEdit::drop-down
                                    {
                                        subcontrol-origin: padding;
                                        subcontrol-position: top right;
                                        width: 15px;
                                        border-left-width: 0px;
                                        border-left-color: darkgray;
                                        border-left-style: solid;
                                        border-top-right-radius: 3px;
                                        border-bottom-right-radius: 3px;
                                    }

                                QDateEdit::down-arrow
                                    {
                                        image: url('img/down_arrow_disabled.png');
                                    }

                                QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover,
                                QDateEdit::down-arrow:focus
                                    {
                                        image: url('img/down_arrow.png');
                                    }
                                SentenceFrame {
                                    background-color: #1e1e1e;
                                    }
                                SentenceFrame:hover
                                    {
                                        background: #D1DBCB;
                                            color: black;
                                    }
                                SentenceTextEdit
                                    {
                                    border: 1px solid #323232;
                                    }
                        """
        self.bar_btn_style_str = """
                        QPushButton
                        {
                            color: #eff0f1;
                            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e1e1e, stop: 1 #323232);
                            border-width: 0px;
                            border-color: #323232;
                            border-style: solid;
                            padding: 0px;
                            border-radius: 0px;
                            outline: none;
                            text-align: bottom;
                        }

                        QPushButton:disabled
                            {
                                background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e1e1e, stop: 1 #323232);
                                border-width: 0px;
                                border-color: #323232;
                                border-style: solid;
                                padding-top: 0px;
                                padding-bottom: 0px;
                                padding-left: 0px;
                                padding-right: 0px;
                                border-radius: 0px;
                                color: #454545;
                            }

                        QPushButton:focus {
                                background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e1e1e, stop: 1 #323232);
                                color: black;
                            }

                        QPushButton:pressed
                            {
                                color: black;
                                background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e1e1e, stop: 1 #323232);
                                padding-top: -15px;
                                padding-bottom: -17px;
                            }

                        QPushButton:checked{
                                background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e1e1e, stop: 1 #323232);
                                border-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e1e1e, stop: 1 #323232);
                            }"""
        self.bar_title_style_str = """
                            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e1e1e, stop: 1 #323232);
                            border-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e1e1e, stop: 1 #323232);
                            color: #D1DBCB;
                            border: 0px solid black;
                                margin-left: 0px;
                                margin-right: 0px;
                                color: #D1DBCB;
                                """
        self.app.setStyleSheet(self.main_style_str)


class StyleFusion(StyleClass):
    """ Одна из стандартных светлых тем """

    def initStyle(self):
        """ Параметры темы """
        self.main_style_str = ""
        self.bar_btn_style_str = """
                                    QPushButton
                                        {
                                            border-width: 0px;
                                            border-color: #323232;
                                            border-style: solid;
                                            padding: 0px;
                                            border-radius: 0px;
                                            outline: none;
                                            text-align: bottom;
                                        }
                                    QPushButton:disabled
                                        {
                                            border-width: 0px;
                                            border-style: solid;
                                            padding-top: 0px;
                                            padding-bottom: 0px;
                                            padding-left: 0px;
                                            padding-right: 0px;
                                            border-radius: 0px;
                                            color: #454545;
                                        }
                                    QPushButton:pressed
                                        {
                                            padding-top: -15px;
                                            padding-bottom: -17px;
                                        }
                                    """
        self.bar_title_style_str = ""
        self.app.setStyle('Fusion')


class StyleWindows(StyleClass):
    """ Еще одна из стандартных светлых тем """

    def initStyle(self):
        """ Параметры темы """
        self.main_style_str = ""
        self.bar_btn_style_str = """
                                    QPushButton
                                        {
                                            border-width: 0px;
                                            border-color: #323232;
                                            border-style: solid;
                                            padding: 0px;
                                            border-radius: 0px;
                                            outline: none;
                                            text-align: bottom;
                                        }
                                    QPushButton:disabled
                                        {
                                            border-width: 0px;
                                            border-style: solid;
                                            padding-top: 0px;
                                            padding-bottom: 0px;
                                            padding-left: 0px;
                                            padding-right: 0px;
                                            border-radius: 0px;
                                            color: #454545;
                                        }
                                    QPushButton:pressed
                                        {
                                            padding-top: -15px;
                                            padding-bottom: -17px;
                                        }
                                    """
        self.bar_title_style_str = ""
        self.app.setStyle('Windows')


class StyleStandart(StyleClass):
    """ Базовая тема Qt5 """

    def initStyle(self):
        """ Параметры темы """
        self.main_style_str = ""
        self.bar_btn_style_str = """
                                    QPushButton
                                        {
                                            border-width: 0px;
                                            border-color: #323232;
                                            border-style: solid;
                                            padding: 0px;
                                            border-radius: 0px;
                                            outline: none;
                                            text-align: bottom;
                                        }
                                    QPushButton:disabled
                                        {
                                            border-width: 0px;
                                            border-style: solid;
                                            padding-top: 0px;
                                            padding-bottom: 0px;
                                            padding-left: 0px;
                                            padding-right: 0px;
                                            border-radius: 0px;
                                            color: #454545;
                                        }
                                    QPushButton:pressed
                                        {
                                            padding-top: -15px;
                                            padding-bottom: -17px;
                                        }
                                    """
        self.bar_title_style_str = ""
