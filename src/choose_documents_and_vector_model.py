import subprocess
import os
import yaml
from pathlib import Path
from PySide6.QtWidgets import QFileDialog, QDialog, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout

def choose_documents_directory():
    allowed_extensions = ['.pdf', '.docx', '.epub', '.txt', '.enex', '.eml', '.msg', '.csv', '.xls', '.xlsx', '.rtf', '.odt',
                          '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tif', '.tiff', '.html', '.htm', '.md', '.doc']
    current_dir = Path(__file__).parent.resolve()
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    file_paths, _ = file_dialog.getOpenFileNames(None, "Choose Documents and Images for Database", str(current_dir))

    if file_paths:
        incompatible_files = []
        compatible_files = []

        for file_path in file_paths:
            extension = Path(file_path).suffix.lower()
            if extension in allowed_extensions:
                if extension in ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tif', '.tiff']:
                    target_folder = current_dir / "Images_for_DB"
                else:
                    target_folder = current_dir / "Docs_for_DB"

                # Check and unlink existing symlink if necessary
                symlink_target = target_folder / Path(file_path).name
                if symlink_target.exists():
                    symlink_target.unlink()

                # Create new symlink
                symlink_target.symlink_to(file_path)
            else:
                incompatible_files.append(Path(file_path).name)

        if incompatible_files:
            dialog = QDialog()
            dialog.setWindowTitle("Incompatible Files Detected")
            layout = QVBoxLayout()

            text_edit = QTextEdit()
            text_edit.setReadOnly(True)
            text_edit.setText("One or more files selected are not compatible to be put into the database.  Click 'Ok' to only add compatible documents or 'cancel' to back out::\n\n" + "\n".join(incompatible_files))
            layout.addWidget(text_edit)

            button_box = QHBoxLayout()
            ok_button = QPushButton("OK")
            cancel_button = QPushButton("Cancel")
            button_box.addWidget(ok_button)
            button_box.addWidget(cancel_button)
            layout.addLayout(button_box)

            dialog.setLayout(layout)

            ok_button.clicked.connect(dialog.accept)
            cancel_button.clicked.connect(dialog.reject)

            user_choice = dialog.exec()

            if user_choice == QDialog.Rejected:
                return

def load_config():
    with open(Path("config.yaml"), 'r') as stream:
        return yaml.safe_load(stream)

def select_embedding_model_directory():
    initial_dir = Path('Embedding_Models') if Path('Embedding_Models').exists() else Path.home()
    chosen_directory = QFileDialog.getExistingDirectory(None, "Select Embedding Model Directory", str(initial_dir))
    
    if chosen_directory:
        config_file_path = Path("config.yaml")
        if config_file_path.exists():
            try:
                with open(config_file_path, 'r') as file:
                    config_data = yaml.safe_load(file)
            except Exception as e:
                config_data = {}

        config_data["EMBEDDING_MODEL_NAME"] = chosen_directory

        with open(config_file_path, 'w') as file:
            yaml.dump(config_data, file)

        print(f"Selected directory: {chosen_directory}")