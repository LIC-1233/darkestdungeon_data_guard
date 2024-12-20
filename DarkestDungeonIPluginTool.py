import logging
from typing import Sequence

import mobase
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QWidget

logger = logging.getLogger()


class DarkestDungeonIPluginTool(mobase.IPluginTool):
    def __init__(self):
        super(DarkestDungeonIPluginTool, self).__init__()
        self.__organizer = None
        self.__parentWidget: QWidget
        pass

    def init(self, organizer: mobase.IOrganizer):
        self.__organizer = organizer
        return True

    def setParentWidget(self, parent: QWidget):
        self.__parentWidget: QWidget = parent

    def requirements(self) -> list[mobase.IPluginRequirement]:
        return [mobase.PluginRequirementFactory.gameDependency("Darkest Dungeon")]

    def display(self) -> None:
        self.__parentWidget.show()
        QMessageBox.critical(
            self.__parentWidget,
            "display",
            "暗黑地牢数据完整性检测暗黑地牢mod文件数据完整性",
        )
        pass

    def displayName(self) -> str:
        return "暗黑地牢数据完整性检测"

    def icon(self) -> QIcon:
        return QIcon()

    def tooltip(self) -> str:
        return "检测暗黑地牢mod文件数据完整性"

    def author(self) -> str:
        return "LIC"

    def description(self) -> str:
        return "检测暗黑地牢mod文件数据完整性"

    def name(self) -> str:
        return "暗黑地牢数据完整性检测"

    def settings(self) -> Sequence[mobase.PluginSetting]:
        return [mobase.PluginSetting("key", "value", "default")]

    def version(self) -> mobase.VersionInfo:
        return mobase.VersionInfo(0, 0, 1)


def createPlugin():
    return DarkestDungeonIPluginTool()
