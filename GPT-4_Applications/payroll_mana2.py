import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QAction

class CSVFileViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('급여 관리 장부')
        self.setGeometry(100, 100, 800, 600)

        self.file_path = None
        self.table_widget = QTableWidget()

        self.btn_open = QPushButton('Open CSV', self)
        self.btn_open.clicked.connect(self.openFile)

        layout = QVBoxLayout()
        layout.addWidget(self.btn_open)
        layout.addWidget(self.table_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Create the "Quit" action and add it to the menu bar
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        self.menuBar().addAction(quit_action)

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_path:
            self.file_path = file_path
            self.displayCSVContents()

    def displayCSVContents(self):
        if not self.file_path:
            return

        with open(self.file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)

            if not rows:
                return

            num_rows = len(rows)
            num_columns = len(rows[0])

            self.table_widget.setRowCount(num_rows)
            self.table_widget.setColumnCount(num_columns)

            for row_idx, row in enumerate(rows):
                for col_idx, cell_value in enumerate(row):
                    item = QTableWidgetItem(cell_value)
                    self.table_widget.setItem(row_idx, col_idx, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CSVFileViewer()
    window.show()
    sys.exit(app.exec_())
