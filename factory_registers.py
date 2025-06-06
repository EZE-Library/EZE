"""
Register EZE widgets to use without import.
"""

from kivy.factory import Factory

register = Factory.register
register("EZESegmentedButton", module="eze.uix.segmentedbutton")
register("EZESegmentedButtonItem", module="eze.uix.segmentedbutton")
register("EZEScrollView", module="eze.uix.scrollview")
register("EZERecycleView", module="eze.uix.recycleview")
register("EZEResponsiveLayout", module="eze.uix.responsivelayout")
register("EZESegmentedControl", module="eze.uix.segmentedcontrol")
register("EZESegmentedControlItem", module="eze.uix.segmentedcontrol")
register("EZESliverAppbar", module="eze.uix.sliverappbar")
register("EZESliverAppbarContent", module="eze.uix.sliverappbar")
register("EZESliverAppbarHeader", module="eze.uix.sliverappbar")
register("EZENavigationRailItem", module="eze.uix.navigationrail")
register("EZENavigationRail", module="eze.uix.navigationrail")
register("EZENavigationRailFabButton", module="eze.uix.navigationrail")
register("EZENavigationRailMenuButton", module="eze.uix.navigationrail")
register("EZESwiper", module="eze.uix.swiper")
register("EZECarousel", module="eze.uix.carousel")
register("EZEWidget", module="eze.uix.widget")
register("EZEFloatLayout", module="eze.uix.floatlayout")
register("EZEAnchorLayout", module="eze.uix.anchorlayout")
register("EZEScreen", module="eze.uix.screen")
register("EZEScreenManager", module="eze.uix.screenmanager")
register("EZERecycleGridLayout", module="eze.uix.recyclegridlayout")
register("EZEBoxLayout", module="eze.uix.boxlayout")
register("EZERelativeLayout", module="eze.uix.relativelayout")
register("EZEGridLayout", module="eze.uix.gridlayout")
register("EZEStackLayout", module="eze.uix.stacklayout")
register("EZEExpansionPanel", module="eze.uix.expansionpanel")
register("EZEExpansionPanelOneLine", module="eze.uix.expansionpanel")
register("EZEExpansionPanelTwoLine", module="eze.uix.expansionpanel")
register("EZEExpansionPanelThreeLine", module="eze.uix.expansionpanel")
register("FitImage", module="eze.uix.fitimage")
register("EZEBackdrop", module="eze.uix.backdrop")
register("EZEBanner", module="eze.uix.banner")
register("EZETooltip", module="eze.uix.tooltip")
register("EZEBottomSheet", module="eze.uix.bottomsheet")
register("EZEBottomNavigation", module="eze.uix.bottomnavigation")
register("EZEBottomNavigationItem", module="eze.uix.bottomnavigation")
register("EZEToggleButton", module="eze.uix.behaviors.toggle_behavior")
register("EZEFloatingActionButtonSpeedDial", module="eze.uix.button")
register("EZEIconButton", module="eze.uix.button")
register("EZERoundImageButton", module="eze.uix.button")
register("EZEFlatButton", module="eze.uix.button")
register("EZERaisedButton", module="eze.uix.button")
register("EZEFloatingActionButton", module="eze.uix.button")
register("EZERectangleFlatButton", module="eze.uix.button")
register("EZETextButton", module="eze..uix.button")
register("EZECustomRoundIconButton", module="eze.uix.button")
register("EZERoundFlatButton", module="eze.uix.button")
register("EZEFillRoundFlatButton", module="eze.uix.button")
register("EZERectangleFlatIconButton", module="eze.uix.button")
register("EZERoundFlatIconButton", module="eze.uix.button")
register("EZEFillRoundFlatIconButton", module="eze.uix.button")
register("EZECard", module="eze.uix.card")
register("EZESeparator", module="eze.uix.card")
register("EZESelectionList", module="eze.uix.selection")
register("EZEChip", module="eze.uix.chip")
register("EZESmartTile", module="eze.uix.imagelist")
register("EZELabel", module="eze.uix.label")
register("EZEIcon", module="eze.uix.label")
register("EZEList", module="eze.uix.list")
register("ILeftBody", module="eze.uix.list")
register("ILeftBodyTouch", module="eze.uix.list")
register("IRightBody", module="eze.uix.list")
register("IRightBodyTouch", module="eze.uix.list")
register("OneLineListItem", module="eze.uix.list")
register("TwoLineListItem", module="eze.uix.list")
register("ThreeLineListItem", module="eze.uix.list")
register("OneLineAvatarListItem", module="eze.uix.list")
register("TwoLineAvatarListItem", module="eze.uix.list")
register("ThreeLineAvatarListItem", module="eze.uix.list")
register("OneLineIconListItem", module="eze.uix.list")
register("TwoLineIconListItem", module="eze.uix.list")
register("ThreeLineIconListItem", module="eze.uix.list")
register("OneLineRightIconListItem", module="eze.uix.list")
register("TwoLineRightIconListItem", module="eze.uix.list")
register("ThreeLineRightIconListItem", module="eze.uix.list")
register("OneLineAvatarIconListItem", module="eze.uix.list")
register("TwoLineAvatarIconListItem", module="eze.uix.list")
register("ThreeLineAvatarIconListItem", module="eze.uix.list")
register("HoverBehavior", module="eze.uix.behaviors.hover_behavior")
register("FocusBehavior", module="eze.uix.behaviors.focus_behavior")
register("MagicBehavior", module="eze.uix.behaviors.magic_behavior")
register("EZENavigationDrawer", module="eze.uix.navigationdrawer")
register("EZENavigationLayout", module="eze.uix.navigationdrawer")
register("EZENavigationDrawerMenu", module="eze.uix.navigationdrawer")
register("EZENavigationDrawerHeader", module="eze.uix.navigationdrawer")
register("EZENavigationDrawerItem", module="eze.uix.navigationdrawer")
register("EZENavigationDrawerLabel", module="eze.uix.navigationdrawer")
register("EZENavigationDrawerDivider", module="eze.uix.navigationdrawer")
register("EZEProgressBar", module="eze.uix.progressbar")
register("EZEScrollViewRefreshLayout", module="eze.uix.refreshlayout")
register("EZECheckbox", module="eze.uix.selectioncontrol")
register("EZESwitch", module="eze.uix.selectioncontrol")
register("EZESlider", module="eze.uix.slider")
register("EZESpinner", module="eze.uix.spinner")
register("EZETabs", module="eze.uix.tab")
register("EZETextField", module="eze.uix.textfield")
register("EZETextFieldRect", module="eze.uix.textfield")
register("EZETopAppBar", module="eze.uix.toolbar")
register("EZEBottomAppBar", module="eze.uix.toolbar")
register("EZEDropDownItem", module="eze.uix.dropdownitem")
register("EZECircularLayout", module="eze.uix.circularlayout")
register("EZEHeroFrom", module="eze.uix.hero")
register("EZEHeroTo", module="eze.uix.hero")
