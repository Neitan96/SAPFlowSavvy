from __future__ import annotations

import win32com.client

from .GuiComponent import GuiComponent
from .GuiScrollbar import GuiScrollbar
from .GuiComponentCollection import GuiComponentCollection
from .GuiTableColumn import GuiTableColumn
from .GuiTableRow import GuiTableRow
from .GuiContainer import GuiContainer
from .GuiUtils import GuiUtils
from .GuiCollection import GuiCollection
from .GuiVComponent import GuiVComponent
from .GuiVHViewSwitch import GuiVHViewSwitch
from .GuiOkCodeField import GuiOkCodeField
from .GuiMessageWindow import GuiMessageWindow
from .GuiLabel import GuiLabel
from .GuiRadioButton import GuiRadioButton
from .GuiTextField import GuiTextField
from .GuiCTextField import GuiCTextField
from .GuiPasswordField import GuiPasswordField
from .GuiStatusbar import GuiStatusbar
from .GuiStatusPane import GuiStatusPane
from .GuiComboBoxEntry import GuiComboBoxEntry
from .GuiComboBox import GuiComboBox
from .GuiCheckBox import GuiCheckBox
from .GuiButton import GuiButton
from .GuiBox import GuiBox
from .GuiMenu import GuiMenu
from .GuiContextMenu import GuiContextMenu
from .GuiVContainer import GuiVContainer
from .GuiMenubar import GuiMenubar
from .GuiGOSShell import GuiGOSShell
from .GuiDialogShell import GuiDialogShell
from .GuiSimpleContainer import GuiSimpleContainer
from .GuiCustomControl import GuiCustomControl
from .GuiToolbar import GuiToolbar
from .GuiTitlebar import GuiTitlebar
from .GuiUserArea import GuiUserArea
from .GuiShell import GuiShell
from .GuiStage import GuiStage
from .GuiPicture import GuiPicture
from .GuiOfficeIntegration import GuiOfficeIntegration
from .GuiNetChart import GuiNetChart
from .GuiMap import GuiMap
from .GuiHTMLViewer import GuiHTMLViewer
from .GuiGraphAdapt import GuiGraphAdapt
from .GuiEAIViewer3D import GuiEAIViewer3D
from .GuiEAIViewer2D import GuiEAIViewer2D
from .GuiColorSelector import GuiColorSelector
from .GuiCalendar import GuiCalendar
from .GuiBarChart import GuiBarChart
from .GuiApoGrid import GuiApoGrid
from .GuiAbapEditor import GuiAbapEditor
from .GuiSplitterContainer import GuiSplitterContainer
from .GuiSplit import GuiSplit
from .GuiInputFieldControl import GuiInputFieldControl
from .GuiTextedit import GuiTextedit
from .GuiToolbarControl import GuiToolbarControl
from .GuiTree import GuiTree
from .GuiChart import GuiChart
from .GuiSapChart import GuiSapChart
from .GuiComboBoxControl import GuiComboBoxControl
from .GuiGridView import GuiGridView
from .GuiContainerShell import GuiContainerShell
from .GuiTab import GuiTab
from .GuiTabStrip import GuiTabStrip
from .GuiScrollContainer import GuiScrollContainer
from .GuiFrameWindow import GuiFrameWindow
from .GuiMainWindow import GuiMainWindow
from .GuiModalWindow import GuiModalWindow
from .GuiTableControl import GuiTableControl
from .GuiSessionInfo import GuiSessionInfo
from .GuiSession import GuiSession
from .GuiConnection import GuiConnection
from .GuiApplication import GuiApplication


# noinspection PyPep8Naming
class ComponentCast:

    component: win32com.client.CDispatch

    def __init__(self, component: win32com.client.CDispatch) -> None:
        self.component = component

    def GuiComponent(self) -> GuiComponent:
        return GuiComponent(self.component)

    def GuiScrollbar(self) -> GuiScrollbar:
        return GuiScrollbar(self.component)

    def GuiComponentCollection(self) -> GuiComponentCollection:
        return GuiComponentCollection(self.component)

    def GuiTableColumn(self) -> GuiTableColumn:
        return GuiTableColumn(self.component)

    def GuiTableRow(self) -> GuiTableRow:
        return GuiTableRow(self.component)

    def GuiContainer(self) -> GuiContainer:
        return GuiContainer(self.component)

    def GuiUtils(self) -> GuiUtils:
        return GuiUtils(self.component)

    def GuiCollection(self) -> GuiCollection:
        return GuiCollection(self.component)

    def GuiVComponent(self) -> GuiVComponent:
        return GuiVComponent(self.component)

    def GuiVHViewSwitch(self) -> GuiVHViewSwitch:
        return GuiVHViewSwitch(self.component)

    def GuiOkCodeField(self) -> GuiOkCodeField:
        return GuiOkCodeField(self.component)

    def GuiMessageWindow(self) -> GuiMessageWindow:
        return GuiMessageWindow(self.component)

    def GuiLabel(self) -> GuiLabel:
        return GuiLabel(self.component)

    def GuiRadioButton(self) -> GuiRadioButton:
        return GuiRadioButton(self.component)

    def GuiTextField(self) -> GuiTextField:
        return GuiTextField(self.component)

    def GuiCTextField(self) -> GuiCTextField:
        return GuiCTextField(self.component)

    def GuiPasswordField(self) -> GuiPasswordField:
        return GuiPasswordField(self.component)

    def GuiStatusbar(self) -> GuiStatusbar:
        return GuiStatusbar(self.component)

    def GuiStatusPane(self) -> GuiStatusPane:
        return GuiStatusPane(self.component)

    def GuiComboBoxEntry(self) -> GuiComboBoxEntry:
        return GuiComboBoxEntry(self.component)

    def GuiComboBox(self) -> GuiComboBox:
        return GuiComboBox(self.component)

    def GuiCheckBox(self) -> GuiCheckBox:
        return GuiCheckBox(self.component)

    def GuiButton(self) -> GuiButton:
        return GuiButton(self.component)

    def GuiBox(self) -> GuiBox:
        return GuiBox(self.component)

    def GuiMenu(self) -> GuiMenu:
        return GuiMenu(self.component)

    def GuiContextMenu(self) -> GuiContextMenu:
        return GuiContextMenu(self.component)

    def GuiVContainer(self) -> GuiVContainer:
        return GuiVContainer(self.component)

    def GuiMenubar(self) -> GuiMenubar:
        return GuiMenubar(self.component)

    def GuiGOSShell(self) -> GuiGOSShell:
        return GuiGOSShell(self.component)

    def GuiDialogShell(self) -> GuiDialogShell:
        return GuiDialogShell(self.component)

    def GuiSimpleContainer(self) -> GuiSimpleContainer:
        return GuiSimpleContainer(self.component)

    def GuiCustomControl(self) -> GuiCustomControl:
        return GuiCustomControl(self.component)

    def GuiToolbar(self) -> GuiToolbar:
        return GuiToolbar(self.component)

    def GuiTitlebar(self) -> GuiTitlebar:
        return GuiTitlebar(self.component)

    def GuiUserArea(self) -> GuiUserArea:
        return GuiUserArea(self.component)

    def GuiShell(self) -> GuiShell:
        return GuiShell(self.component)

    def GuiStage(self) -> GuiStage:
        return GuiStage(self.component)

    def GuiPicture(self) -> GuiPicture:
        return GuiPicture(self.component)

    def GuiOfficeIntegration(self) -> GuiOfficeIntegration:
        return GuiOfficeIntegration(self.component)

    def GuiNetChart(self) -> GuiNetChart:
        return GuiNetChart(self.component)

    def GuiMap(self) -> GuiMap:
        return GuiMap(self.component)

    def GuiHTMLViewer(self) -> GuiHTMLViewer:
        return GuiHTMLViewer(self.component)

    def GuiGraphAdapt(self) -> GuiGraphAdapt:
        return GuiGraphAdapt(self.component)

    def GuiEAIViewer3D(self) -> GuiEAIViewer3D:
        return GuiEAIViewer3D(self.component)

    def GuiEAIViewer2D(self) -> GuiEAIViewer2D:
        return GuiEAIViewer2D(self.component)

    def GuiColorSelector(self) -> GuiColorSelector:
        return GuiColorSelector(self.component)

    def GuiCalendar(self) -> GuiCalendar:
        return GuiCalendar(self.component)

    def GuiBarChart(self) -> GuiBarChart:
        return GuiBarChart(self.component)

    def GuiApoGrid(self) -> GuiApoGrid:
        return GuiApoGrid(self.component)

    def GuiAbapEditor(self) -> GuiAbapEditor:
        return GuiAbapEditor(self.component)

    def GuiSplitterContainer(self) -> GuiSplitterContainer:
        return GuiSplitterContainer(self.component)

    def GuiSplit(self) -> GuiSplit:
        return GuiSplit(self.component)

    def GuiInputFieldControl(self) -> GuiInputFieldControl:
        return GuiInputFieldControl(self.component)

    def GuiTextedit(self) -> GuiTextedit:
        return GuiTextedit(self.component)

    def GuiToolbarControl(self) -> GuiToolbarControl:
        return GuiToolbarControl(self.component)

    def GuiTree(self) -> GuiTree:
        return GuiTree(self.component)

    def GuiChart(self) -> GuiChart:
        return GuiChart(self.component)

    def GuiSapChart(self) -> GuiSapChart:
        return GuiSapChart(self.component)

    def GuiComboBoxControl(self) -> GuiComboBoxControl:
        return GuiComboBoxControl(self.component)

    def GuiGridView(self) -> GuiGridView:
        return GuiGridView(self.component)

    def GuiContainerShell(self) -> GuiContainerShell:
        return GuiContainerShell(self.component)

    def GuiTab(self) -> GuiTab:
        return GuiTab(self.component)

    def GuiTabStrip(self) -> GuiTabStrip:
        return GuiTabStrip(self.component)

    def GuiScrollContainer(self) -> GuiScrollContainer:
        return GuiScrollContainer(self.component)

    def GuiFrameWindow(self) -> GuiFrameWindow:
        return GuiFrameWindow(self.component)

    def GuiMainWindow(self) -> GuiMainWindow:
        return GuiMainWindow(self.component)

    def GuiModalWindow(self) -> GuiModalWindow:
        return GuiModalWindow(self.component)

    def GuiTableControl(self) -> GuiTableControl:
        return GuiTableControl(self.component)

    def GuiSessionInfo(self) -> GuiSessionInfo:
        return GuiSessionInfo(self.component)

    def GuiSession(self) -> GuiSession:
        return GuiSession(self.component)

    def GuiConnection(self) -> GuiConnection:
        return GuiConnection(self.component)

    def GuiApplication(self) -> GuiApplication:
        return GuiApplication(self.component)

    @staticmethod
    def get_instance(sap_component: win32com.client.CDispatch):
        if sap_component is None: return None
        # noinspection PyBroadException
        try: id_comp = sap_component.TypeAsNumber
        except: return None

        # TODO Verificar id do GuiStage, GuiPicture, GuiOfficeIntegration, GuiNetChart, GuiMap,
        # TODO GuiHTMLViewer, GuiGraphAdapt, GuiEAIViewer3D, GuiEAIViewer2D, GuiCalendar,
        # TODO GuiBarChart, GuiApoGrid, GuiAbapEditor, GuiSplit, GuiInputFieldControl,
        # TODO GuiTextedit, GuiToolbarControl, GuiTree, GuiChart, GuiSapChart, GuiComboBoxControl
        # TODO GuiGridView

        if id_comp == 0:
            return GuiComponent(sap_component)

        if id_comp == 1:
            return GuiVComponent(sap_component)

        if id_comp == 2:
            return GuiVContainer(sap_component)

        if id_comp == 10:
            return GuiApplication(sap_component)

        if id_comp == 11:
            return GuiConnection(sap_component)

        if id_comp == 12:
            return GuiSession(sap_component)

        if id_comp == 20:
            return GuiFrameWindow(sap_component)

        if id_comp == 21:
            return GuiMainWindow(sap_component)

        if id_comp == 22:
            return GuiModalWindow(sap_component)

        if id_comp == 23:
            return GuiMessageWindow(sap_component)

        if id_comp == 30:
            return GuiLabel(sap_component)

        if id_comp == 31:
            return GuiTextField(sap_component)

        if id_comp == 32:
            return GuiCTextField(sap_component)

        if id_comp == 33:
            return GuiPasswordField(sap_component)

        if id_comp == 34:
            return GuiComboBox(sap_component)

        if id_comp == 35:
            return GuiOkCodeField(sap_component)

        if id_comp == 40:
            return GuiButton(sap_component)

        if id_comp == 41:
            return GuiRadioButton(sap_component)

        if id_comp == 42:
            return GuiCheckBox(sap_component)

        if id_comp == 43:
            return GuiStatusPane(sap_component)

        if id_comp == 50:
            return GuiCustomControl(sap_component)

        if id_comp == 51:
            return GuiContainerShell(sap_component)

        if id_comp == 62:
            return GuiBox(sap_component)

        if id_comp == 70:
            return GuiContainer(sap_component)

        if id_comp == 71:
            return GuiSimpleContainer(sap_component)

        if id_comp == 72:
            return GuiScrollContainer(sap_component)

        # if id == 73: return GuiListContainer(sap_object)

        if id_comp == 74:
            return GuiUserArea(sap_component)

        if id_comp == 75:
            return GuiSplitterContainer(sap_component)

        if id_comp == 80:
            return GuiTableControl(sap_component)

        if id_comp == 81:
            return GuiTableColumn(sap_component)

        if id_comp == 82:
            return GuiTableRow(sap_component)

        if id_comp == 90:
            return GuiTabStrip(sap_component)

        if id_comp == 91:
            return GuiTab(sap_component)

        if id_comp == 100:
            return GuiScrollbar(sap_component)

        if id_comp == 101:
            return GuiToolbar(sap_component)

        if id_comp == 102:
            return GuiTitlebar(sap_component)

        if id_comp == 103:
            return GuiStatusbar(sap_component)

        if id_comp == 110:
            return GuiMenu(sap_component)

        if id_comp == 111:
            return GuiMenubar(sap_component)

        if id_comp == 120:
            return GuiCollection(sap_component)

        if id_comp == 121:
            return GuiSessionInfo(sap_component)

        if id_comp == 122:
            return GuiShell(sap_component)

        if id_comp == 123:
            return GuiGOSShell(sap_component)

        # if id == 124: return GuiSplitterShell(sap_object)

        if id_comp == 125:
            return GuiDialogShell(sap_component)

        #if id == 126: return GuiDockShell(sap_object)

        if id_comp == 127:
            return GuiContextMenu(sap_component)

        if id_comp == 128:
            return GuiComponentCollection(sap_component)

        if id_comp == 129:
            return GuiVHViewSwitch(sap_component)

        return GuiComponent(sap_component)