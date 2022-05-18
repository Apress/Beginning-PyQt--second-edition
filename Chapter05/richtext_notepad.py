"""Listing 5-7 to Listing 5-16
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules 
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit,
    QMessageBox, QTextEdit, QFileDialog, QInputDialog, 
    QFontDialog, QColorDialog)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QTextCursor, QColor, QAction

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(400, 500)
        self.setWindowTitle("5.1 – Rich Text Notepad GUI")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.removeHighlights) # Remove highlights after editing text 
        self.setCentralWidget(self.text_edit)

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.new_act = QAction(QIcon("images/new_file.png"), "New")
        self.new_act.setShortcut("Ctrl+N")
        self.new_act.triggered.connect(self.clearText)

        self.open_act = QAction(QIcon("images/open_file.png"), "Open")
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.triggered.connect(self.openFile)

        self.save_act = QAction(QIcon("images/save_file.png"), "Save")
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.triggered.connect(self.saveToFile)

        self.quit_act = QAction(QIcon("images/exit.png"), "Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        # Create actions for Edit menu
        self.undo_act = QAction(QIcon("images/undo.png"), "Undo")
        self.undo_act.setShortcut("Ctrl+Z")
        self.undo_act.triggered.connect(self.text_edit.undo)

        self.redo_act = QAction(QIcon("images/redo.png"), "Redo")
        self.redo_act.setShortcut("Ctrl+Y")
        self.redo_act.triggered.connect(self.text_edit.redo)

        self.cut_act = QAction(QIcon("images/cut.png"), "Cut")
        self.cut_act.setShortcut("Ctrl+X")
        self.cut_act.triggered.connect(self.text_edit.cut)

        self.copy_act = QAction(QIcon("images/copy.png"), "Copy")
        self.copy_act.setShortcut("Ctrl+C")
        self.copy_act.triggered.connect(self.text_edit.copy)

        self.paste_act = QAction(QIcon("images/paste.png"), "Paste")
        self.paste_act.setShortcut("Ctrl+V")
        self.paste_act.triggered.connect(self.text_edit.paste)

        self.find_act = QAction(QIcon("images/find.png"), "Find All")
        self.find_act.setShortcut("Ctrl+F")
        self.find_act.triggered.connect(self.searchText)

        # Create actions for Tools menu
        self.font_act = QAction(QIcon("images/font.png"), "Font")
        self.font_act.setShortcut("Ctrl+T")
        self.font_act.triggered.connect(self.chooseFont)

        self.color_act = QAction(QIcon("images/color.png"), "Color")
        self.color_act.setShortcut("Ctrl+Shift+C")
        self.color_act.triggered.connect(self.chooseFontColor)

        self.highlight_act = QAction(QIcon("images/highlight.png"), "Highlight")
        self.highlight_act.setShortcut("Ctrl+Shift+H")
        self.highlight_act.triggered.connect(self.chooseFontBackgroundColor)

        # Create actions for Help menu
        self.about_act = QAction("About")
        self.about_act.triggered.connect(self.aboutDialog)

    def createMenu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create File menu and add actions 
        menu_bar = self.menuBar() # Create menu bar
        #menu_bar.setNativeMenuBar(False) # Use custom menu bar style for Mac
        file_menu=menu_bar.addMenu("File")
        file_menu.addAction(self.new_act)
        file_menu.addSeparator()
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        # Create Edit menu and add actions 
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction(self.undo_act)
        edit_menu.addAction(self.redo_act) 
        edit_menu.addSeparator()       
        edit_menu.addAction(self.cut_act) 
        edit_menu.addAction(self.copy_act) 
        edit_menu.addAction(self.paste_act) 
        edit_menu.addSeparator()
        edit_menu.addAction(self.find_act)

        # Create Tools menu and add actions 
        tool_menu = menu_bar.addMenu("Tools")
        tool_menu.addAction(self.font_act)
        tool_menu.addAction(self.color_act)
        tool_menu.addAction(self.highlight_act)

        # Create Help menu and add actions 
        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.about_act)

    def clearText(self):
        """Clear the QTextEdit field."""
        # Ask user if they want to clear text 
         # QMessageBox.question(self, title, text, buttons, default_button),buttons is a bitwise OR of QMessageBox.StandardButton values ,
         # default_button is the button that is selected by default when the dialog is shown 
        answer = QMessageBox.question(self, "Clear Text", 
            "Do you want to clear the text?", 
            QMessageBox.StandardButton.No | \
            QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            self.text_edit.clear()

    def openFile(self):
        """Open a text or html file and display its contents in
        the text edit field."""
        # Create a file dialog to select a file to open ,it returns a file name and the file type ,if the user cancels the dialog, the file name is None
        # QFileDialog.getOpenFileName(self, caption, directory, filter); filter is a string of file types that can be selected, e.g. "Text Files (*.txt)"
        # caption is the title of the dialog, directory is the directory that the dialog will open in, and filter is the file types that can be selected

        file_name, file_type= QFileDialog.getOpenFileName(
            self, "Open File", "", 
            "HTML Files (*.html);;Text Files (*.txt)") 
        # print(file_name)
        # print(type(file_name))
        # print("file types : ", file_type)

        if file_name: # If a file name is returned 
            with open(file_name, "r") as f:
                notepad_text = f.read() # Read the contents of the file into a string
            self.text_edit.setText(notepad_text) # set the text edit field to the contents of the file

    def saveToFile(self):
        """If the save button is clicked, display dialog asking 
        user if they want to save the text in the text edit 
        field to a text file.""" 
        #QFileDialog.getSaveFileName(self, caption, directory, filter, initial_filter, options) 
        # Create a file dialog to select a file to save to ,it returns a file name and the file type ,if the user cancels the dialog, the file name is None
        #captio is the title of the dialog, directory is the directory that the dialog opens in, filter is a string of file types that can be selected, e.g. "Text Files (*.txt)"
        #initial_filter is the file type that is selected by default when the dialog is shown, options is a bitwise OR of QFileDialog.Option values 

        file_name, file_type = QFileDialog.getSaveFileName(self, "Save File",
            "","HTML Files (*.html);;Text Files (*.txt)")
        print(file_name)
        print(type(file_name))
        print("file types : ", file_type)
        try:

            if file_name.endswith(".txt"):
                notepad_text = self.text_edit.toPlainText()
                with open(file_name, "w") as f:            
                    f.write(notepad_text)
            elif file_name.endswith(".html"):
                notepad_richtext = self.text_edit.toHtml()
                with open(file_name, "w") as f:            
                    f.write(notepad_richtext)
            else:
                QMessageBox.information(
                    self, "Not Saved", "only text or html file saved.", 
                    QMessageBox.StandardButton.Ok)
        except Exception as e:
            print(e)
            QMessageBox.information(
                self, "Not Saved", "Text not saved.", 
                QMessageBox.StandardButton.Ok)

    def searchText(self):
        """Search for text."""
        # Display input dialog to ask user for text to find
        # QInputDialog.getText(self, title, label, echo_mode, text, options)
        # title is the title of the dialog,
        # label is the text that is displayed in the dialog, 
        # echo_mode is the mode that the text is displayed in, 
        # text is the text that is displayed in the dialog by default, 
        # options is a bitwise OR of QInputDialog.InputDialogOption values
        # text, ok = QInputDialog.getText(self, "Search Text", "Text:", QLineEdit.Normal, "", QInputDialog.StandardButtons.Ok)
        find_text, ok = QInputDialog.getText(
            self, "Search Text", "Find:",QLineEdit.Normal,"type..")

        if ok:
            extra_selections = []
            # Set the cursor in the text edit field to the beginning
            self.text_edit.moveCursor(QTextCursor.MoveOperation.Start)
            color = QColor(Qt.GlobalColor.gray)

            while(self.text_edit.find(find_text)):
                # Use ExtraSelection() to mark the text you are
                # searching for as gray 
                selection = QTextEdit.ExtraSelection()  
                selection.format.setBackground(color)

                # Set the cursor of the selection                 
                selection.cursor = self.text_edit.textCursor()
                extra_selections.append(selection)

            # Highlight all selections in the QTextEdit widget
            self.text_edit.setExtraSelections(extra_selections)

    def removeHighlights(self):
        """Reset extra selections after editing text."""
        #reset highlights editing text
        extra_selections = []
        self.text_edit.setExtraSelections(extra_selections)

            
    def chooseFont(self):
        
        current = self.text_edit.currentFont() # get the current font and font size
        """Select a font from the QFontDialog."""
        opt = QFontDialog.FontDialogOption.DontUseNativeDialog # QFontDialog.FontDialogOption is a bitwise OR of QFontDialog.FontDialogOption values
        font, ok = QFontDialog.getFont(current, self, 
            options=opt) # QFontDialog.getFont(current, parent, options) returns a tuple of a font and a boolean indicating whether the user clicked OK or Cancel
        if ok:
            self.text_edit.setCurrentFont(font)  # set the font of the text edit field to the font returned by the dialog
                
    def chooseFontColor(self):
        """Select a font from the QColorDialog."""
        color = QColorDialog.getColor() # QColorDialog.getColor() returns a QColor object that represents the color selected by the user
        if color.isValid():
            self.text_edit.setTextColor(color) # set the text color of the text edit field to the color returned by the dialog

    def chooseFontBackgroundColor(self):
        """Select a color for text's background."""
        color = QColorDialog.getColor() # QColorDialog.getColor() returns a QColor object that represents the color selected by the user
        if color.isValid():
            self.text_edit.setTextBackgroundColor(color)

    def aboutDialog(self):
        """Display the About dialog."""
        # QMessageBox.about(self, title, text) displays a message box with the title and text specified
        QMessageBox.about(self, "About Notepad", 
            """<p>Beginner's Practical Guide to PyQt</p>
            <p>Project 5.1 - Notepad GUI</p>""")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())