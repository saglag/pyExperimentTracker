"""Manual fixes for experiment_tracker.py."""

# add under setupUi definition:
icon_path = "icon.png"
icon = QIcon(icon_path)
ExperimentTracker.setWindowIcon(icon)

# for each textbrowser widget, add under retranslateUi definition:
self.textBrowser.setStyleSheet("background-color: black;")