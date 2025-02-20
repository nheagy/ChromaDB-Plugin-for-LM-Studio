from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QSizePolicy, QComboBox, QPushButton
from PySide6.QtGui import QIntValidator, QDoubleValidator
import yaml

class DatabaseSettingsTab(QWidget):
    def __init__(self):
        super(DatabaseSettingsTab, self).__init__()

        with open('config.yaml', 'r') as f:
            config_data = yaml.safe_load(f)
            self.database_config = config_data['database']
            self.compute_device_options = config_data['Compute_Device']['available']
            self.database_creation_device = config_data['Compute_Device']['database_creation']
            self.database_query_device = config_data['Compute_Device']['database_query']
            self.search_term = config_data['database'].get('search_term', '')
            self.document_type = config_data['database'].get('document_types', '')

        v_layout = QVBoxLayout()
        h_layout_device = QHBoxLayout()
        h_layout_settings = QHBoxLayout()
        h_layout_search_term = QHBoxLayout()

        self.field_data = {}
        self.label_data = {}

        # Create Device ComboBoxes
        device_labels = [f"Create Device {self.database_creation_device}", f"Query Device {self.database_query_device}"]
        self.device_combos = [QComboBox() for _ in device_labels]

        for label_text, combo in zip(device_labels, self.device_combos):
            label = QLabel(label_text)
            combo.addItems(self.compute_device_options)
            combo.setCurrentIndex(self.compute_device_options.index(label_text.split()[-1]))
            h_layout_device.addWidget(label)
            h_layout_device.addWidget(combo)

        v_layout.addLayout(h_layout_device)

        database_settings_group = ['similarity', 'contexts']

        for setting in database_settings_group:
            current_value = self.database_config.get(setting, '')
            edit = QLineEdit()
            edit.setPlaceholderText(f"Enter new {setting}...")
            edit.setValidator(QDoubleValidator() if setting == 'similarity' else QIntValidator())
            edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            label = QLabel(f"{setting.replace('_', ' ').capitalize()}: {current_value}")
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            h_layout_settings.addWidget(label)
            h_layout_settings.addWidget(edit)
            self.field_data[setting] = edit
            self.label_data[setting] = label

        v_layout.addLayout(h_layout_settings)

        self.search_term_edit = QLineEdit()
        self.search_term_edit.setPlaceholderText("Enter new search term...")
        self.search_term_edit.setText(self.search_term)
        self.search_term_label = QLabel(f"Search Filter: {self.search_term}")
        h_layout_search_term.addWidget(self.search_term_label)
        h_layout_search_term.addWidget(self.search_term_edit)

        self.filter_button = QPushButton("Clear Filter")
        self.filter_button.clicked.connect(self.reset_search_term)
        h_layout_search_term.addWidget(self.filter_button)
        
        self.file_type_combo = QComboBox()
        file_type_items = ["All Files", "Images Only", "Documents Only"]
        self.file_type_combo.addItems(file_type_items)

        if self.document_type == 'image':
            default_index = file_type_items.index("Images Only")
        elif self.document_type == 'document':
            default_index = file_type_items.index("Documents Only")
        else:
            default_index = file_type_items.index("All Files")
        self.file_type_combo.setCurrentIndex(default_index)

        h_layout_search_term.addWidget(self.file_type_combo)

        v_layout.addLayout(h_layout_search_term)

        self.setLayout(v_layout)

    def update_config(self):
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)

        settings_changed = False

        device_map = {
            'database_creation': (self.device_combos[0], 'currentText', str, 'Create Device'),
            'database_query': (self.device_combos[1], 'currentText', str, 'Query Device')
        }

        for setting, (widget, getter, caster, label_prefix) in device_map.items():
            new_value = getattr(widget, getter)()
            if new_value != config_data['Compute_Device'].get(setting, ''):
                settings_changed = True
                config_data['Compute_Device'][setting] = caster(new_value)
                
                label = widget.parentWidget().findChildren(QLabel)[0]
                label.setText(f"{label_prefix}: {new_value}")

        database_settings = {'search_term': self.search_term_edit, **self.field_data}

        for setting, widget in database_settings.items():
            new_value = widget.text()
            if new_value and new_value != str(config_data['database'].get(setting, '')):
                settings_changed = True
                config_data['database'][setting] = float(new_value) if setting == 'similarity' else new_value
                if setting == 'search_term':
                    self.search_term_label.setText(f"Search Term: {new_value}")
                else:
                    self.label_data[setting].setText(f"{setting.replace('_', ' ').capitalize()}: {new_value}")
                widget.clear()

        file_type_map = {
            "All Files": '',
            "Images Only": 'image',
            "Documents Only": 'document'
        }

        file_type_selection = self.file_type_combo.currentText()
        document_type_value = file_type_map[file_type_selection]

        if document_type_value != config_data['database'].get('document_types', ''):
            settings_changed = True
            config_data['database']['document_types'] = document_type_value

        if settings_changed:
            with open('config.yaml', 'w', encoding='utf-8') as f:
                yaml.safe_dump(config_data, f)

        return settings_changed

    def reset_search_term(self):
        with open('config.yaml', 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)

        config_data['database']['search_term'] = ''
        
        with open('config.yaml', 'w', encoding='utf-8') as f:
            yaml.safe_dump(config_data, f)

        self.search_term_label.setText("Search Term: ")
        self.search_term_edit.clear()
