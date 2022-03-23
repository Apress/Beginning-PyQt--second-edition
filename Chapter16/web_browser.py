"""Listing 16-6
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import os, sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, 
    QWidget, QLabel, QLineEdit, QTabWidget, QToolBar, 
    QProgressBar, QStatusBar, QVBoxLayout)
from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView

style_sheet = """
    QTabWidget:pane{
        border: none
    }
"""

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create lists that will keep track of the new windows, 
        # tabs and urls
        self.window_list = []
        self.list_of_web_pages = []
        self.list_of_urls = []

        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(300, 200)
        self.setWindowTitle("16.6 – Web Browser")
        self.setWindowIcon(QIcon(os.path.join("icons", "pyqt_logo.png")))

        self.sizeMainWindow() 
        self.createToolbar()
        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        """Create the QTabWidget object and the different pages
        for the main window. Handle when a tab is closed."""
        self.tab_bar = QTabWidget()
        self.tab_bar.setTabsClosable(True) # Add close buttons to tabs
        self.tab_bar.setTabBarAutoHide(True) # Hides tab bar when less than 2 tabs
        self.tab_bar.tabCloseRequested.connect(self.closeTab)

        # Create a tab 
        self.main_tab = QWidget()
        self.tab_bar.addTab(self.main_tab, "New Tab")

        # Call method that sets up each page
        self.setUpTab(self.main_tab)
        self.setCentralWidget(self.tab_bar)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu   
        self.new_window_act = QAction("New Window", self)
        self.new_window_act.setShortcut("Ctrl+N")
        self.new_window_act.triggered.connect(self.openNewWindow)

        self.new_tab_act = QAction("New Tab", self)
        self.new_tab_act.setShortcut("Ctrl+T")
        self.new_tab_act.triggered.connect(self.openNewTab)

        self.quit_act = QAction("Quit Browser", self)
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close) 

    def createMenu(self):
        """Create the application"s menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create File menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new_window_act)
        file_menu.addAction(self.new_tab_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

    def createToolbar(self):
        """Set up the navigation toolbar."""
        tool_bar = QToolBar("Address Bar")
        tool_bar.setIconSize(QSize(30, 30))
        self.addToolBar(tool_bar)
        
        # Create toolbar actions
        back_page_button = QAction(QIcon(os.path.join("icons", "back.png")), "Back", self)
        back_page_button.triggered.connect(self.backPageButton)

        forward_page_button = QAction(QIcon(os.path.join("icons", "forward.png")), "Forward", self)
        forward_page_button.triggered.connect(self.forwardPageButton)

        refresh_button = QAction(QIcon(os.path.join("icons", "refresh.png")), "Refresh", self)
        refresh_button.triggered.connect(self.refreshButton)

        home_button = QAction(QIcon(os.path.join("icons", "home.png")), "Home", self)
        home_button.triggered.connect(self.homeButton)

        stop_button = QAction(QIcon(os.path.join("icons", "stop.png")), "Stop", self)
        stop_button.triggered.connect(self.stopButton)

        # Set up the address bar
        self.address_line = QLineEdit()
        # addAction() is used here to merely display the icon in the line edit. 
        self.address_line.addAction(QIcon("icons/search.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.address_line.setPlaceholderText("Enter website address")
        self.address_line.returnPressed.connect(self.searchForUrl)

        tool_bar.addAction(home_button)
        tool_bar.addAction(back_page_button)
        tool_bar.addAction(forward_page_button)
        tool_bar.addAction(refresh_button)
        tool_bar.addWidget(self.address_line)
        tool_bar.addAction(stop_button)

    def setUpWebView(self):
        """Create the QWebEngineView object that is used to 
        view web docs. Set up the main page, and handle 
        web_view signals."""
        web_view = QWebEngineView()
        web_view.setUrl(QUrl("https://google.com"))

        # Create page loading progress bar that is displayed in 
        # the status bar.
        self.page_load_pb = QProgressBar()
        self.page_load_label = QLabel()
        web_view.loadProgress.connect(self.updateProgressBar)

        # Display url in address bar
        web_view.urlChanged.connect(self.updateUrl)

        ok = web_view.loadFinished.connect(self.updateTabTitle)
        if ok:
            # Web page loaded
            return web_view
        else:
            print("The request timed out.")        

    def setUpTab(self, tab):
        """Create individual tabs and widgets. Add the 
        tab"s url and web view to the appropriate list. 
        Update the address bar if the user switches tabs."""
        # Create the web view that will be displayed on the page.
        self.web_page = self.setUpWebView()

        # Append new web_page and url to the appropriate lists
        self.list_of_web_pages.append(self.web_page)
        self.list_of_urls.append(self.address_line)
        self.tab_bar.setCurrentWidget(self.web_page)

        # If user switches pages, update the url in the address to 
        # reflect the current page. 
        self.tab_bar.currentChanged.connect(self.updateUrl)

        tab_v_box = QVBoxLayout()
        # Sets the left, top, right, and bottom margins to 
        # use around the layout.
        tab_v_box.setContentsMargins(0,0,0,0)
        tab_v_box.addWidget(self.web_page)
        tab.setLayout(tab_v_box)

    def openNewWindow(self):
        """Create new instance of the WebBrowser class."""
        new_window = WebBrowser()
        new_window.show()
        self.window_list.append(new_window)

    def openNewTab(self):
        """Create a new web tab."""
        new_tab = QWidget()
        self.tab_bar.addTab(new_tab, "New Tab")
        self.setUpTab(new_tab)

        # Update the tab_bar index to keep track of the new tab.
        # Load the url for the new page.
        tab_index = self.tab_bar.currentIndex()
        self.tab_bar.setCurrentIndex(tab_index + 1)
        self.list_of_web_pages[self.tab_bar.currentIndex()].load(QUrl("https://google.com"))

    def updateProgressBar(self, progress):
        """Update progress bar in status bar.
        This provides feedback to the user that page is 
        still loading."""
        if progress < 100:
            self.page_load_pb.setVisible(progress)
            self.page_load_pb.setValue(progress)
            self.page_load_label.setVisible(progress)
            self.page_load_label.setText(f"Loading Page... ({str(progress)}/100)")
            self.status_bar.addWidget(self.page_load_pb)
            self.status_bar.addWidget(self.page_load_label)
        else:
            self.status_bar.removeWidget(self.page_load_pb)
            self.status_bar.removeWidget(self.page_load_label)

    def updateTabTitle(self):
        """Update the title of the tab to reflect the 
        website."""
        tab_index = self.tab_bar.currentIndex()
        title = self.list_of_web_pages[self.tab_bar.currentIndex()].page().title()
        self.tab_bar.setTabText(tab_index, title)

    def updateUrl(self):
        """Update the url in the address to reflect the 
        current page being displayed."""
        url = self.list_of_web_pages[self.tab_bar.currentIndex()].page().url()
        formatted_url = QUrl(url).toString()
        self.list_of_urls[self.tab_bar.currentIndex()].setText(formatted_url)

    def searchForUrl(self):
        """Make a request to load a url."""
        url_text = self.list_of_urls[self.tab_bar.currentIndex()].text()

        # Append http to url
        url = QUrl(url_text)
        if url.scheme() == "":
            url.setScheme("http")

        # Request url
        if url.isValid():
            self.list_of_web_pages[self.tab_bar.currentIndex()].page().load(url)
        else:
            url.clear()

    def backPageButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].back()

    def forwardPageButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].forward()

    def refreshButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].reload()

    def homeButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].setUrl(QUrl("https://google.com"))

    def stopButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].stop()

    def closeTab(self, tab_index):
        """Slot is emitted when the close button on a tab is clicked. 
        index refers to the tab that should be removed."""
        self.list_of_web_pages.pop(tab_index)
        self.list_of_urls.pop(tab_index)

        self.tab_bar.removeTab(tab_index)

    def sizeMainWindow(self):
        """Use QApplication.primaryScreen() to access information 
        about the screen and use it to size the application window 
        when starting a new application."""
        desktop = QApplication.primaryScreen()
        size = desktop.availableGeometry()
        screen_width = size.width() 
        screen_height = size.height() 
        self.setGeometry(0, 0, screen_width, screen_height)

if __name__ == '__main__':
    app = QApplication(sys.argv)    
    app.setStyleSheet(style_sheet)
    window = WebBrowser()
    app.exec()