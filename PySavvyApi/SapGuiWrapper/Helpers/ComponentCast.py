from __future__ import annotations

import win32com.client


# noinspection PyPep8Naming
class ComponentCast:

    component: win32com.client.CDispatch
    
    def __init__(self, component: win32com.client.CDispatch) -> None:
        self.component = component

    def GuiComponent(self) -> GuiComponent:
        from ..Objects.GuiComponent import GuiComponent
        return GuiComponent(self.component)

    def GuiScrollbar(self) -> GuiScrollbar:
        from ..Objects.GuiScrollbar import GuiScrollbar
        return GuiScrollbar(self.component)

    def GuiComponentCollection(self) -> GuiComponentCollection:
        from ..Objects.GuiComponentCollection import GuiComponentCollection
        return GuiComponentCollection(self.component)

    def GuiTableColumn(self) -> GuiTableColumn:
        from ..Objects.GuiTableColumn import GuiTableColumn
        return GuiTableColumn(self.component)

    def GuiTableRow(self) -> GuiTableRow:
        from ..Objects.GuiTableRow import GuiTableRow
        return GuiTableRow(self.component)

    def GuiContainer(self) -> GuiContainer:
        from ..Objects.GuiContainer import GuiContainer
        return GuiContainer(self.component)

    def GuiUtils(self) -> GuiUtils:
        from ..Objects.GuiUtils import GuiUtils
        return GuiUtils(self.component)

    def GuiCollection(self) -> GuiCollection:
        from ..Objects.GuiCollection import GuiCollection
        return GuiCollection(self.component)

    def GuiVComponent(self) -> GuiVComponent:
        from ..Objects.GuiVComponent import GuiVComponent
        return GuiVComponent(self.component)
    
    def GuiVHViewSwitch(self) -> GuiVHViewSwitch:
        from ..Objects.GuiVHViewSwitch import GuiVHViewSwitch
        return GuiVHViewSwitch(self.component)
    
    def GuiOkCodeField(self) -> GuiOkCodeField:
        from ..Objects.GuiOkCodeField import GuiOkCodeField
        return GuiOkCodeField(self.component)

    def GuiMessageWindow(self) -> GuiMessageWindow:
        from ..Objects.GuiMessageWindow import GuiMessageWindow
        return GuiMessageWindow(self.component)

    def GuiLabel(self) -> GuiLabel:
        from ..Objects.GuiLabel import GuiLabel
        return GuiLabel(self.component)

    def GuiRadioButton(self) -> GuiRadioButton:
        from ..Objects.GuiRadioButton import GuiRadioButton
        return GuiRadioButton(self.component)

    def GuiTextField(self) -> GuiTextField:
        from ..Objects.GuiTextField import GuiTextField
        return GuiTextField(self.component)

    def GuiCTextField(self) -> GuiCTextField:
        from ..Objects.GuiCTextField import GuiCTextField
        return GuiCTextField(self.component)

    def GuiPasswordField(self) -> GuiPasswordField:
        from ..Objects.GuiPasswordField import GuiPasswordField
        return GuiPasswordField(self.component)

    def GuiStatusbar(self) -> GuiStatusbar:
        from ..Objects.GuiStatusbar import GuiStatusbar
        return GuiStatusbar(self.component)

    def GuiStatusPane(self) -> GuiStatusPane:
        from ..Objects.GuiStatusPane import GuiStatusPane
        return GuiStatusPane(self.component)

    def GuiComboBoxEntry(self) -> GuiComboBoxEntry:
        from ..Objects.GuiComboBoxEntry import GuiComboBoxEntry
        return GuiComboBoxEntry(self.component)

    def GuiComboBox(self) -> GuiComboBox:
        from ..Objects.GuiComboBox import GuiComboBox
        return GuiComboBox(self.component)

    def GuiCheckBox(self) -> GuiCheckBox:
        from ..Objects.GuiCheckBox import GuiCheckBox
        return GuiCheckBox(self.component)

    def GuiButton(self) -> GuiButton:
        from ..Objects.GuiButton import GuiButton
        return GuiButton(self.component)

    def GuiBox(self) -> GuiBox:
        from ..Objects.GuiBox import GuiBox
        return GuiBox(self.component)

    def GuiMenu(self) -> GuiMenu:
        from ..Objects.GuiMenu import GuiMenu
        return GuiMenu(self.component)

    def GuiContextMenu(self) -> GuiContextMenu:
        from ..Objects.GuiContextMenu import GuiContextMenu
        return GuiContextMenu(self.component)

    def GuiVContainer(self) -> GuiVContainer:
        from ..Objects.GuiVContainer import GuiVContainer
        return GuiVContainer(self.component)

    def GuiMenubar(self) -> GuiMenubar:
        from ..Objects.GuiMenubar import GuiMenubar
        return GuiMenubar(self.component)

    def GuiGOSShell(self) -> GuiGOSShell:
        from ..Objects.GuiGOSShell import GuiGOSShell
        return GuiGOSShell(self.component)

    def GuiDialogShell(self) -> GuiDialogShell:
        from ..Objects.GuiDialogShell import GuiDialogShell
        return GuiDialogShell(self.component)

    def GuiSimpleContainer(self) -> GuiSimpleContainer:
        from ..Objects.GuiSimpleContainer import GuiSimpleContainer
        return GuiSimpleContainer(self.component)

    def GuiCustomControl(self) -> GuiCustomControl:
        from ..Objects.GuiCustomControl import GuiCustomControl
        return GuiCustomControl(self.component)

    def GuiToolbar(self) -> GuiToolbar:
        from ..Objects.GuiToolbar import GuiToolbar
        return GuiToolbar(self.component)

    def GuiTitlebar(self) -> GuiTitlebar:
        from ..Objects.GuiTitlebar import GuiTitlebar
        return GuiTitlebar(self.component)

    def GuiUserArea(self) -> GuiUserArea:
        from ..Objects.GuiUserArea import GuiUserArea
        return GuiUserArea(self.component)

    def GuiShell(self) -> GuiShell:
        from ..Objects.GuiShell import GuiShell
        return GuiShell(self.component)

    def GuiStage(self) -> GuiStage:
        from ..Objects.GuiStage import GuiStage
        return GuiStage(self.component)

    def GuiPicture(self) -> GuiPicture:
        from ..Objects.GuiPicture import GuiPicture
        return GuiPicture(self.component)

    def GuiOfficeIntegration(self) -> GuiOfficeIntegration:
        from ..Objects.GuiOfficeIntegration import GuiOfficeIntegration
        return GuiOfficeIntegration(self.component)

    def GuiNetChart(self) -> GuiNetChart:
        from ..Objects.GuiNetChart import GuiNetChart
        return GuiNetChart(self.component)

    def GuiMap(self) -> GuiMap:
        from ..Objects.GuiMap import GuiMap
        return GuiMap(self.component)

    def GuiHTMLViewer(self) -> GuiHTMLViewer:
        from ..Objects.GuiHTMLViewer import GuiHTMLViewer
        return GuiHTMLViewer(self.component)

    def GuiGraphAdapt(self) -> GuiGraphAdapt:
        from ..Objects.GuiGraphAdapt import GuiGraphAdapt
        return GuiGraphAdapt(self.component)

    def GuiEAIViewer3D(self) -> GuiEAIViewer3D:
        from ..Objects.GuiEAIViewer3D import GuiEAIViewer3D
        return GuiEAIViewer3D(self.component)

    def GuiEAIViewer2D(self) -> GuiEAIViewer2D:
        from ..Objects.GuiEAIViewer2D import GuiEAIViewer2D
        return GuiEAIViewer2D(self.component)

    def GuiColorSelector(self) -> GuiColorSelector:
        from ..Objects.GuiColorSelector import GuiColorSelector
        return GuiColorSelector(self.component)

    def GuiCalendar(self) -> GuiCalendar:
        from ..Objects.GuiCalendar import GuiCalendar
        return GuiCalendar(self.component)

    def GuiBarChart(self) -> GuiBarChart:
        from ..Objects.GuiBarChart import GuiBarChart
        return GuiBarChart(self.component)

    def GuiApoGrid(self) -> GuiApoGrid:
        from ..Objects.GuiApoGrid import GuiApoGrid
        return GuiApoGrid(self.component)

    def GuiAbapEditor(self) -> GuiAbapEditor:
        from ..Objects.GuiAbapEditor import GuiAbapEditor
        return GuiAbapEditor(self.component)

    def GuiSplitterContainer(self) -> GuiSplitterContainer:
        from ..Objects.GuiSplitterContainer import GuiSplitterContainer
        return GuiSplitterContainer(self.component)

    def GuiSplit(self) -> GuiSplit:
        from ..Objects.GuiSplit import GuiSplit
        return GuiSplit(self.component)

    def GuiInputFieldControl(self) -> GuiInputFieldControl:
        from ..Objects.GuiInputFieldControl import GuiInputFieldControl
        return GuiInputFieldControl(self.component)

    def GuiTextedit(self) -> GuiTextedit:
        from ..Objects.GuiTextedit import GuiTextedit
        return GuiTextedit(self.component)

    def GuiToolbarControl(self) -> GuiToolbarControl:
        from ..Objects.GuiToolbarControl import GuiToolbarControl
        return GuiToolbarControl(self.component)

    def GuiTree(self) -> GuiTree:
        from ..Objects.GuiTree import GuiTree
        return GuiTree(self.component)

    def GuiChart(self) -> GuiChart:
        from ..Objects.GuiChart import GuiChart
        return GuiChart(self.component)

    def GuiSapChart(self) -> GuiSapChart:
        from ..Objects.GuiSapChart import GuiSapChart
        return GuiSapChart(self.component)

    def GuiComboBoxControl(self) -> GuiComboBoxControl:
        from ..Objects.GuiComboBoxControl import GuiComboBoxControl
        return GuiComboBoxControl(self.component)

    def GuiGridView(self) -> GuiGridView:
        from ..Objects.GuiGridView import GuiGridView
        return GuiGridView(self.component)

    def GuiContainerShell(self) -> GuiContainerShell:
        from ..Objects.GuiContainerShell import GuiContainerShell
        return GuiContainerShell(self.component)

    def GuiTab(self) -> GuiTab:
        from ..Objects.GuiTab import GuiTab
        return GuiTab(self.component)

    def GuiTabStrip(self) -> GuiTabStrip:
        from ..Objects.GuiTabStrip import GuiTabStrip
        return GuiTabStrip(self.component)

    def GuiScrollContainer(self) -> GuiScrollContainer:
        from ..Objects.GuiScrollContainer import GuiScrollContainer
        return GuiScrollContainer(self.component)

    def GuiFrameWindow(self) -> GuiFrameWindow:
        from ..Objects.GuiFrameWindow import GuiFrameWindow
        return GuiFrameWindow(self.component)

    def GuiMainWindow(self) -> GuiMainWindow:
        from ..Objects.GuiMainWindow import GuiMainWindow
        return GuiMainWindow(self.component)

    def GuiModalWindow(self) -> GuiModalWindow:
        from ..Objects.GuiModalWindow import GuiModalWindow
        return GuiModalWindow(self.component)

    def GuiTableControl(self) -> GuiTableControl:
        from ..Objects.GuiTableControl import GuiTableControl
        return GuiTableControl(self.component)

    def GuiSessionInfo(self) -> GuiSessionInfo:
        from ..Objects.GuiSessionInfo import GuiSessionInfo
        return GuiSessionInfo(self.component)

    def GuiSession(self) -> GuiSession:
        from ..Objects.GuiSession import GuiSession
        return GuiSession(self.component)

    def GuiConnection(self) -> GuiConnection:
        from ..Objects.GuiConnection import GuiConnection
        return GuiConnection(self.component)

    def GuiApplication(self) -> GuiApplication:
        from ..Objects.GuiApplication import GuiApplication
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
            from ..Objects.GuiComponent import GuiComponent
            return GuiComponent(sap_component)

        if id_comp == 1:
            from ..Objects.GuiVComponent import GuiVComponent
            return GuiVComponent(sap_component)
        
        if id_comp == 2:
            from ..Objects.GuiVContainer import GuiVContainer
            return GuiVContainer(sap_component)

        if id_comp == 10:
            from ..Objects.GuiApplication import GuiApplication
            return GuiApplication(sap_component)

        if id_comp == 11:
            from ..Objects.GuiConnection import GuiConnection
            return GuiConnection(sap_component)

        if id_comp == 12:
            from ..Objects.GuiSession import GuiSession
            return GuiSession(sap_component)

        if id_comp == 20:
            from ..Objects.GuiFrameWindow import GuiFrameWindow
            return GuiFrameWindow(sap_component)

        if id_comp == 21:
            from ..Objects.GuiMainWindow import GuiMainWindow
            return GuiMainWindow(sap_component)

        if id_comp == 22:
            from ..Objects.GuiModalWindow import GuiModalWindow
            return GuiModalWindow(sap_component)

        if id_comp == 23:
            from ..Objects.GuiMessageWindow import GuiMessageWindow
            return GuiMessageWindow(sap_component)

        if id_comp == 30:
            from ..Objects.GuiLabel import GuiLabel
            return GuiLabel(sap_component)

        if id_comp == 31:
            from ..Objects.GuiTextField import GuiTextField
            return GuiTextField(sap_component)

        if id_comp == 32:
            from ..Objects.GuiCTextField import GuiCTextField
            return GuiCTextField(sap_component)

        if id_comp == 33:
            from ..Objects.GuiPasswordField import GuiPasswordField
            return GuiPasswordField(sap_component)

        if id_comp == 34:
            from ..Objects.GuiComboBox import GuiComboBox
            return GuiComboBox(sap_component)

        if id_comp == 35:
            from ..Objects.GuiOkCodeField import GuiOkCodeField
            return GuiOkCodeField(sap_component)

        if id_comp == 40:
            from ..Objects.GuiButton import GuiButton
            return GuiButton(sap_component)

        if id_comp == 41:
            from ..Objects.GuiRadioButton import GuiRadioButton
            return GuiRadioButton(sap_component)

        if id_comp == 42:
            from ..Objects.GuiCheckBox import GuiCheckBox
            return GuiCheckBox(sap_component)

        if id_comp == 43:
            from ..Objects.GuiStatusPane import GuiStatusPane
            return GuiStatusPane(sap_component)

        if id_comp == 50:
            from ..Objects.GuiCustomControl import GuiCustomControl
            return GuiCustomControl(sap_component)

        if id_comp == 51:
            from ..Objects.GuiContainerShell import GuiContainerShell
            return GuiContainerShell(sap_component)

        if id_comp == 62:
            from ..Objects.GuiBox import GuiBox
            return GuiBox(sap_component)

        if id_comp == 70:
            from ..Objects.GuiContainer import GuiContainer
            return GuiContainer(sap_component)

        if id_comp == 71:
            from ..Objects.GuiSimpleContainer import GuiSimpleContainer
            return GuiSimpleContainer(sap_component)

        if id_comp == 72:
            from ..Objects.GuiScrollContainer import GuiScrollContainer
            return GuiScrollContainer(sap_component)

        # if id == 73: return GuiListContainer(sap_object)

        if id_comp == 74:
            from ..Objects.GuiUserArea import GuiUserArea
            return GuiUserArea(sap_component)

        if id_comp == 75:
            from ..Objects.GuiSplitterContainer import GuiSplitterContainer
            return GuiSplitterContainer(sap_component)

        if id_comp == 80:
            from ..Objects.GuiTableControl import GuiTableControl
            return GuiTableControl(sap_component)

        if id_comp == 81:
            from ..Objects.GuiTableColumn import GuiTableColumn
            return GuiTableColumn(sap_component)

        if id_comp == 82:
            from ..Objects.GuiTableRow import GuiTableRow
            return GuiTableRow(sap_component)

        if id_comp == 90:
            from ..Objects.GuiTabStrip import GuiTabStrip
            return GuiTabStrip(sap_component)

        if id_comp == 91:
            from ..Objects.GuiTab import GuiTab
            return GuiTab(sap_component)

        if id_comp == 100:
            from ..Objects.GuiScrollbar import GuiScrollbar
            return GuiScrollbar(sap_component)

        if id_comp == 101:
            from ..Objects.GuiToolbar import GuiToolbar
            return GuiToolbar(sap_component)

        if id_comp == 102:
            from ..Objects.GuiTitlebar import GuiTitlebar
            return GuiTitlebar(sap_component)

        if id_comp == 103:
            from ..Objects.GuiStatusbar import GuiStatusbar
            return GuiStatusbar(sap_component)

        if id_comp == 110:
            from ..Objects.GuiMenu import GuiMenu
            return GuiMenu(sap_component)

        if id_comp == 111:
            from ..Objects.GuiMenubar import GuiMenubar
            return GuiMenubar(sap_component)

        if id_comp == 120:
            from ..Objects.GuiCollection import GuiCollection
            return GuiCollection(sap_component)

        if id_comp == 121:
            from ..Objects.GuiSessionInfo import GuiSessionInfo
            return GuiSessionInfo(sap_component)

        if id_comp == 122:
            from ..Objects.GuiShell import GuiShell
            return GuiShell(sap_component)

        if id_comp == 123:
            from ..Objects.GuiGOSShell import GuiGOSShell
            return GuiGOSShell(sap_component)

        # if id == 124: return GuiSplitterShell(sap_object)

        if id_comp == 125:
            from ..Objects.GuiDialogShell import GuiDialogShell
            return GuiDialogShell(sap_component)

        #if id == 126: return GuiDockShell(sap_object)

        if id_comp == 127:
            from ..Objects.GuiContextMenu import GuiContextMenu
            return GuiContextMenu(sap_component)

        if id_comp == 128:
            from ..Objects.GuiComponentCollection import GuiComponentCollection
            return GuiComponentCollection(sap_component)

        if id_comp == 129:
            from ..Objects.GuiVHViewSwitch import GuiVHViewSwitch
            return GuiVHViewSwitch(sap_component)

        from ..Objects.GuiComponent import GuiComponent
        return GuiComponent(sap_component)