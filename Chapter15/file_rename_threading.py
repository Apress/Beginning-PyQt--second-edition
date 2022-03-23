"""Listing 15-1 to Listing 15-9
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import os, sys, time
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QProgressBar, QLineEdit, QPushButton, QTextEdit, 
    QComboBox, QFileDialog, QGridLayout)
from PyQt6.QtCore import pyqtSignal, QThread

style_sheet = """
    QProgressBar{
        background-color: #C0C6CA;
        color: #FFFFFF;
        border: 1px solid grey;
        padding: 3px;
        height: 15px;
        text-align: center;
    }

    QProgressBar::chunk{
        background: #538DB8;
        width: 5px;
        margin: 0.5px
    }
"""

# Create worker thread for running tasks like updating 
# the progress bar, renaming photos, displaying information 
# in the text edit widget.
class Worker(QThread):
    update_value_signal = pyqtSignal(int)
    update_text_edit_signal = pyqtSignal(str, str)
    clear_text_edit_signal = pyqtSignal()

    def __init__(self, dir, ext, prefix):
        super().__init__()
        self.dir = dir
        self.ext = ext
        self.prefix = prefix

    def stopRunning(self):
        """Terminate the thread."""
        self.terminate()
        self.wait()

        self.update_value_signal.emit(0)
        self.clear_text_edit_signal.emit()

    def run(self):
        """The thread begins running from here. 
        run() is only called after start()."""
        for (i, file) in enumerate(os.listdir(self.dir)):
            _, file_ext = os.path.splitext(file)
            if file_ext == self.ext:
                new_file_name = self.prefix + str(i) + self.ext
                src_path = os.path.join(self.dir, file)
                dst_path = os.path.join(self.dir, new_file_name)
                
                # os.rename(src, dst): src is original address of file to be renamed 
                # and dst is destination location with new name
                os.rename(src_path, dst_path)
                # Uncomment if process is too fast and want to see the updates
                #time.sleep(1.0) 

                self.update_value_signal.emit(i + 1)
                self.update_text_edit_signal.emit(file, new_file_name)
            else:
                pass
        # Reset the value of the progress bar
        self.update_value_signal.emit(0) 

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(600, 250)
        self.setWindowTitle("15.1 - Change File Names GUI")

        self.directory = ""
        self.combo_value = ""

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        dir_label = QLabel(
            """<p>Use Button to Choose Directory and 
            Change File Names:</p>""")
        self.dir_edit = QLineEdit()
        dir_button = QPushButton("Select Directory")
        dir_button.setToolTip("Select file directory.")
        dir_button.clicked.connect(self.chooseDirectory)

        self.change_name_edit = QLineEdit()
        self.change_name_edit.setToolTip(
            """<p>Files will be appended with numerical 
            values. For example: filename<b>01</b>.jpg</p>""")
        self.change_name_edit.setPlaceholderText("Change file names to...")

        file_exts = [".jpg", ".jpeg", ".png", ".gif", ".txt"]
        self.combo_value = file_exts[0]

        # Create combobox for selecting file extensions
        ext_combo = QComboBox()
        ext_combo.setToolTip("Only files with this extension will be changed.")
        ext_combo.addItems(file_exts)
        ext_combo.currentTextChanged.connect(self.updateComboValue)

        rename_button = QPushButton("Rename Files")
        rename_button.setToolTip("Begin renaming files in directory.")
        rename_button.clicked.connect(self.renameFiles)

        # Text edit is for displaying the file names as they are updated
        self.display_files_tedit = QTextEdit()
        self.display_files_tedit.setReadOnly(True)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        self.stop_button = QPushButton("Stop")
        self.stop_button.setEnabled(False)

        # Create layout and arrange widgets
        grid = QGridLayout()
        grid.addWidget(dir_label, 0, 0)
        grid.addWidget(self.dir_edit, 1, 0, 1, 2)
        grid.addWidget(dir_button, 1, 2)
        grid.addWidget(self.change_name_edit, 2, 0)
        grid.addWidget(ext_combo, 2, 1)
        grid.addWidget(rename_button, 2, 2)
        grid.addWidget(self.display_files_tedit, 3, 0, 1, 3)
        grid.addWidget(self.progress_bar, 4, 0, 1, 2)
        grid.addWidget(self.stop_button, 4, 2)

        self.setLayout(grid)

    def chooseDirectory(self):
        """Choose file directory."""
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        self.directory = file_dialog.getExistingDirectory(
            self, "Open Directory", "", QFileDialog.Option.ShowDirsOnly)

        if self.directory:
            self.dir_edit.setText(self.directory)

            # Set the max value of progress bar equal to max 
            # number of files in the directory
            num_of_files = len([name for name in os.listdir(self.directory)])
            self.progress_bar.setRange(0, num_of_files)

    def updateComboValue(self, text):
        """Change the combobox value. Values represent 
        the different file extensions."""
        self.combo_value = text
        print(self.combo_value)

    def renameFiles(self):
        """Create instance of worker thread to handle 
        the file renaming process."""
        prefix_text = self.change_name_edit.text()

        if self.directory != "" and prefix_text != "":
            self.worker = Worker(self.directory, self.combo_value, prefix_text)
            self.worker.clear_text_edit_signal.connect(self.display_files_tedit.clear)

            self.stop_button.setEnabled(True)
            self.stop_button.repaint()
            self.stop_button.clicked.connect(self.worker.stopRunning)
            
            self.worker.update_value_signal.connect(self.updateProgressBar)
            self.worker.update_text_edit_signal.connect(self.updateTextEdit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.start()

    def updateProgressBar(self, value):
        self.progress_bar.setValue(value)

    def updateTextEdit(self, old_text, new_text):
        self.display_files_tedit.append(
            f"[INFO] {old_text} changed to {new_text}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    sys.exit(app.exec())