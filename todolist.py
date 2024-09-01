import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 300)

        self.tasks = []

        self.layout = QVBoxLayout()

        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.remove_button = QPushButton("Remove Task")
        self.complete_button = QPushButton("Complete Task")
        self.task_list = QListWidget()

        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.complete_button)
        self.layout.addWidget(self.task_list)

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)
        self.complete_button.clicked.connect(self.complete_task)

        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.input_field.clear()

    def remove_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.tasks.remove(selected_item.text())
            self.task_list.takeItem(self.task_list.row(selected_item))
        else:
            QMessageBox.warning(self, "Warning", "Select a task to remove")

    def complete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_index = self.task_list.row(selected_item)
            self.task_list.item(task_index).setText(f"[Completed] {selected_item.text()}")
        else:
            QMessageBox.warning(self, "Warning", "Select a task to mark as complete")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
