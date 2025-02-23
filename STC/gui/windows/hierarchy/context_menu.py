""" Контекстное меню для иерархического древа """

from PyQt5.QtWidgets import QAction
from PyQt5.Qt import QColor
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QKeySequence
from STC.gui.windows.ancestors.context_menu import ContextMenu


class ContextMenuForTree(ContextMenu):
    """ Контекстное меню для иерархического древа """

    def __init__(self, obj, kttp_list: list[str], kind_list: list[str]) -> None:
        super().__init__(obj)
        self.addAction(self.actionUpdateDate())
        self.addAction(self.actionCopy())
        self.addAction(self.actionUpdTree())
        self.addAction(self.actionCreateMk())
        self.addMenuKttp(kttp_list=kttp_list)
        self.addMenuKind(kind_list=kind_list)
        self.addMenuColor()

    def actionUpdateDate(self) -> QAction:
        """ Изменяет дату последнего обновления
            спецификации на текущую """

        action = QAction(self.object)
        action.setText('Обновить дату последнего изменения')
        action.triggered.connect(self.object.tree_view.updDateCheck)
        action.triggered.connect(self.object.redrawTreeView)
        return action

    def actionCopy(self) -> QAction:
        """ Копирует значение ячейки
            (ctrl + c работает) """

        action = QAction(self.object)
        action.setText('Копировать')
        action.triggered.connect(self.object.copyText)
        return action

    def actionUpdTree(self) -> QAction:
        """ Вызов окна редактирования документов
            изделия активной строки """

        action = QAction(self.object)
        action.setText('Документы')
        action.triggered.connect(self.object.showWindowNewDocument.emit)
        return action

    def actionCreateMk(self) -> QAction:
        """ Вызов окна создания маршрутной карты """

        action = QAction(self.object)
        action.setText('Создать МК')
        action.triggered.connect(self.object.showWindowCreateMk.emit)
        return action

    def addMenuKttp(self, kttp_list: list[str]) -> None:
        """ Вызов подменю изменения карт типового технологического процесса """

        self.kttp_menu = self.addMenu('КТТП')
        self.addMenuKttpAdd(kttp_list)
        self.addMenuKttpDel()

    def addMenuKttpAdd(self, kttp_list: list[str]) -> None:
        """ Вызов подменю списка КТТП для привязки
            технологического процесса к изделию """

        kttp_menu_add = self.kttp_menu.addMenu('Привязать КТТП')
        for kttp_name in sorted(kttp_list):
            action = QAction(self.object)
            action.setText(f'{kttp_name}')
            action.triggered.connect(self.object.tree_view.model.addKttp)
            action.triggered.connect(self.object.redrawTreeView)
            kttp_menu_add.addAction(action)

    def addMenuKttpDel(self) -> None:
        """ Вызов подменю списка КТТП для аннулирования связи
            технологического процесса и определенного изделия """

        kttp_menu_del = self.kttp_menu.addMenu('Отвязать КТТП')
        documents = self.object.tree_view.selected_product.getDocumentByType(
            class_name='ТД',
            subtype_name='Карта типового (группового) технологического процесса',
            org_code='2',
            only_relevant=True,
            only_text=False)
        for document in documents:
            action = QAction(self.object)
            action.setText(f'{document.deno} {document.name}')
            action.triggered.connect(self.object.tree_view.model.delKttp)
            action.triggered.connect(self.object.redrawTreeView)
            kttp_menu_del.addAction(action)

    def addMenuKind(self, kind_list: list[str]) -> None:
        """ Вызов подменю из списка видов изделия """

        kind_menu = self.addMenu('Выбрать вид изделия')
        for kind_name in sorted(kind_list):
            action = QAction(self.object)
            action.setText(f'{kind_name}')
            action.triggered.connect(self.object.setKind)
            action.triggered.connect(self.object.redrawTreeView)
            kind_menu.addAction(action)

    def addMenuColor(self) -> None:
        """ Вызов подменю выбора цвета для
            строки иерархической таблицы """

        color_menu = self.addMenu('Изменить цвет')
        colors = {'red': {'color': QColor(200, 0, 0, 200),
                          'shortcut': 'Shift+R'},
                  'green': {'color': QColor(0, 200, 0, 200),
                            'shortcut': 'Shift+G'},
                  'blue': {'color': QColor(0, 0, 200, 200),
                           'shortcut': 'Shift+B'},
                  'basic': {'color': QColor(0, 0, 0, 0),
                            'shortcut': 'Shift+T'}}
        for color_dict in colors.values():
            pixmap = QPixmap(16, 16)
            pixmap.fill(color_dict['color'])
            action = QAction(self.object)
            action.setShortcut(QKeySequence(color_dict['shortcut']))
            action.setIcon(QIcon(pixmap))
            action.triggered.connect(self.object.setColor)
            color_menu.addAction(action)
