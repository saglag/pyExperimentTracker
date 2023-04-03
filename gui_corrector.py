"""Correct the errors found after the .ui is converted."""

def add_functions_to_class(file_path, class_name, functions_file_path):
    # Read the contents of the experiment_tracker.py file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find the line containing the class definition
    class_def_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith('class {}('.format(class_name)):
            class_def_index = i
            break

    if class_def_index is None:
        raise ValueError('Class {} not found in file {}'.format(class_name, file_path))

    # Read the contents of the functions file
    with open(functions_file_path, 'r') as f:
        functions_lines = f.readlines()

    # Find the first function definition
    function_def_index = None
    for i, line in enumerate(functions_lines):
        if line.strip().startswith('def '):
            function_def_index = i
            break

    if function_def_index is None:
        raise ValueError('No function definitions found in file {}'.format(functions_file_path))

    # Insert the functions after the class definition
    indentation = ' ' * 4
    lines.insert(class_def_index + 1, '\n')
    lines.insert(class_def_index + 2, '{}# Functions added from {}\n'.format(indentation, functions_file_path))
    lines.insert(class_def_index + 3, '\n')
    for function_line in functions_lines[function_def_index:]:
        lines.insert(class_def_index + 4, '{}{}\n'.format(indentation, function_line.rstrip()))

    # Write the modified contents back to the experiment_tracker.py file
    with open(file_path, 'w') as f:
        f.writelines(lines)





def fix_function_calls(file_path, search_replace_dict):
    # Open the file for reading and writing
    with open(file_path, 'r+') as file:
        # Read the contents of the file into a string
        file_contents = file.read()

        # Loop through the search and replace pairs in the dictionary
        for search_string, replace_string in search_replace_dict.items():
            # Replace all occurrences of the search string with the replace string
            file_contents = file_contents.replace(search_string, replace_string)

        # Move the file pointer to the beginning of the file
        file.seek(0)

        # Write the modified contents of the string to the file
        file.write(file_contents)

        # Truncate the file to the current position
        file.truncate()
 
import ast

def add_imports(file_path, new_imports):
    # Open the file and read all its lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find the index of the line containing the "from PyQt6 import ..." statement
    import_index = None
    for i, line in enumerate(lines):
        if line.startswith('from PyQt6 import '):
            import_index = i
            break
        elif line.startswith('from PyQt5 import '):
            import_index = i
            break
        
    if import_index is None:
        # The "from PyQt6 import ..." statement was not found
        print(f"Unable to find the from/import... statement in file {file_path}")
        return

    # Add the new import statements after the existing "from PyQt6 import ..." statement
    
    lines = lines[:import_index+1] + new_imports + lines[import_index+1:]

    # Write the modified lines back to the file
    with open(file_path, 'w') as f:
        f.writelines(lines)

    
def add_functions_after_line(file_path, target_code_line, functions_file_path):
    # Open the experiment_tracker.py file and read all its lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find the line number of the target code line
    target_line_num = None
    for i, line in enumerate(lines):
        if target_code_line in line:
            target_line_num = i + 1  # Add 1 to get the actual line number (since Python indexes start at 0)
            break
    
    if target_line_num is None:
        # Target code line not found
        print(f"Target code line '{target_code_line}' not found in file {file_path}")
        return

    # Open the functions_file_path file and read all its lines
    with open(functions_file_path, 'r') as f:
        function_lines = f.readlines()

    # Indent the function lines by one level
    indented_lines = ['    ' + line for line in function_lines]

    # Add the indented function lines after the target code line in the experiment_tracker.py file
    lines = lines[:target_line_num] + indented_lines + lines[target_line_num:]

    # Write the modified lines back to the experiment_tracker.py file
    with open(file_path, 'w') as f:
        f.writelines(lines)

def add_style_change():
    code_block = '''\
for i in range(self.tabWidget.count()):
    self.tabWidget.tabBar().setTabTextColor(i, QColor("white"))
self.tabWidget.setStyleSheet("QTabBar::tab:!selected { color: white; background-color: darkGray; } QTabBar::tab:selected { color: white; background-color: gray; }")\
'''
    filepath = 'experiment_tracker.py'
    with open(filepath, "r") as f:
        file_content = f.readlines()

    for i, line in enumerate(file_content):
        if "_translate = QtCore.QCoreApplication.translate" in line:
            indentation_level = len(line) - len(line.lstrip())
            new_line = line.rstrip() + "\n" + (" " * indentation_level) + code_block + "\n"
            file_content.insert(i+1, new_line)
            with open(filepath, "w") as f:
                f.writelines(file_content)
            print(f"Added code block after '_translate' at line {i+1}, indentation level: {indentation_level}")
            return i+1

    print("'_translate' not found in the file.")
    return None

def add_icon(file_path, new_imports):
    # Open the file and read all its lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find the index of the line containing the "from PyQt6 import ..." statement
    import_index = None
    for i, line in enumerate(lines):
        if line.startswith('from PyQt6 import '):
            import_index = i
            break

    if import_index is None:
        # The "from PyQt6 import ..." statement was not found
        print(f"Unable to find the 'from PyQt6 import ...' statement in file {file_path}")
        return

    # Add the new import statements after the existing "from PyQt6 import ..." statement
    
    lines = lines[:import_index+1] + new_imports + lines[import_index+1:]

    # Write the modified lines back to the file
    with open(file_path, 'w') as f:
        f.writelines(lines)



if __name__ == "__main__":
    import time
    t = time.time()
    replacements = {
                    # todayClick
                    'button_today_sim.clicked.connect(ExperimentTracker.todayClick)':'button_today_sim.clicked.connect(lambda checked: Ui_ExperimentTracker.todayClick(self, sender="sim"))',
                    'button_today_ephys.clicked.connect(ExperimentTracker.todayClick)':'button_today_ephys.clicked.connect(lambda checked: Ui_ExperimentTracker.todayClick(self, sender="ephys"))',
                    'button_today_imaging.clicked.connect(ExperimentTracker.todayClick)':'button_today_imaging.clicked.connect(lambda checked: Ui_ExperimentTracker.todayClick(self, sender="imaging"))',
                    'animal_info_today_button.clicked.connect(ExperimentTracker.todayClick)':'animal_info_today_button.clicked.connect(lambda checked: Ui_ExperimentTracker.todayClick(self, sender="animal"))',
                    
                    # nowClick
                    'button_now_sim.clicked.connect(ExperimentTracker.nowClick)': 'button_now_sim.clicked.connect(lambda checked: Ui_ExperimentTracker.nowClick(self, sender="sim"))',
                    'button_now_drug_sim.clicked.connect(ExperimentTracker.nowClick)':'button_now_drug_sim.clicked.connect(lambda checked: Ui_ExperimentTracker.nowClick(self, sender="sim drug"))',
                    'button_now_ephys.clicked.connect(ExperimentTracker.nowClick)':'button_now_ephys.clicked.connect(lambda checked: Ui_ExperimentTracker.nowClick(self, sender="ephys"))',
                    'button_now_imaging.clicked.connect(ExperimentTracker.nowClick)':'button_now_imaging.clicked.connect(lambda checked: Ui_ExperimentTracker.nowClick(self, sender="imaging"))',
                    'animal_info_now_time_button.clicked.connect(ExperimentTracker.nowClick)':'animal_info_now_time_button.clicked.connect(lambda checked: Ui_ExperimentTracker.nowClick(self, sender="animal"))',
                    'button_now_drug_imaging.clicked.connect(ExperimentTracker.nowClick)':'button_now_drug_imaging.clicked.connect(lambda checked: Ui_ExperimentTracker.nowClick(self, sender="imaging drug"))',
                    'button_now_drug_ephys.clicked.connect(ExperimentTracker.nowClick)':'button_now_drug_ephys.clicked.connect(lambda checked: Ui_ExperimentTracker.nowClick(self, sender="ephys drug"))',
                    
                    # appendInfo
                    'button_append_info_sim.clicked.connect(ExperimentTracker.appendInfo)':'button_append_info_sim.clicked.connect(lambda checked: Ui_ExperimentTracker.appendInfo(self, sender="sim"))',
                    'button_append_info_imaging.clicked.connect(ExperimentTracker.appendInfo)':'button_append_info_imaging.clicked.connect(lambda checked: Ui_ExperimentTracker.appendInfo(self, sender="imaging"))',
                    'button_append_info_ephys.clicked.connect(ExperimentTracker.appendInfo)':'button_append_info_ephys.clicked.connect(lambda checked: Ui_ExperimentTracker.appendInfo(self, sender="ephys"))',

                    # exportNotes
                    'button_export_notes_sim.clicked.connect(ExperimentTracker.exportNotes)':'button_export_notes_sim.clicked.connect(lambda checked: Ui_ExperimentTracker.exportNotes(self, sender="sim", MainWindow=ExperimentTracker))',
                    'button_export_notes_ephys.clicked.connect(ExperimentTracker.exportNotes)':'button_export_notes_ephys.clicked.connect(lambda checked: Ui_ExperimentTracker.exportNotes(self, sender="ephys", MainWindow=ExperimentTracker))',
                    'button_export_notes_imaging.clicked.connect(ExperimentTracker.exportNotes)':'button_export_notes_imaging.clicked.connect(lambda checked: Ui_ExperimentTracker.exportNotes(self, sender="imaging", MainWindow=ExperimentTracker))',
                    'animal_export_notes.clicked.connect(ExperimentTracker.exportNotes)':'animal_export_notes.clicked.connect(lambda checked: Ui_ExperimentTracker.exportNotes(self, sender="animal", MainWindow=ExperimentTracker))',
                    
                    
                    # exportInfo
                    'button_export_to_csv_sim.clicked.connect(ExperimentTracker.exportInfo)':'button_export_to_csv_sim.clicked.connect(lambda checked: Ui_ExperimentTracker.exportInfo(self, sender="sim", MainWindow=ExperimentTracker))',
                    'button_export_to_csv_ephys.clicked.connect(ExperimentTracker.exportInfo)':'button_export_to_csv_ephys.clicked.connect(lambda checked: Ui_ExperimentTracker.exportInfo(self, sender="ephys", MainWindow=ExperimentTracker))',
                    'button_export_to_csv_imaging.clicked.connect(ExperimentTracker.exportInfo)':'button_export_to_csv_imaging.clicked.connect(lambda checked: Ui_ExperimentTracker.exportInfo(self, sender="imaging", MainWindow=ExperimentTracker))',
                    'animal_export_csv.clicked.connect(ExperimentTracker.exportInfo)':'animal_export_csv.clicked.connect(lambda checked: Ui_ExperimentTracker.exportInfo(self, sender="animal", MainWindow=ExperimentTracker))',
                    
                    # pipette calculator
                    'button_pipette_calculate.clicked.connect(ExperimentTracker.calculatePipetteEntry)':'button_pipette_calculate.clicked.connect(lambda checked: Ui_ExperimentTracker.calculatePipetteEntry(self))',
                    
                    # make sure the first tab is the current index
                    'self.tabWidget.setCurrentIndex(1)':'self.tabWidget.setCurrentIndex(0)',
                    'self.tabWidget.setCurrentIndex(2)':'self.tabWidget.setCurrentIndex(0)',
                    'self.tabWidget.setCurrentIndex(3)':'self.tabWidget.setCurrentIndex(0)',
                    'self.tabWidget.setCurrentIndex(4)':'self.tabWidget.setCurrentIndex(0)',
                    
                    # delete selected rows
                    'button_clear_selection_imaging.clicked.connect(ExperimentTracker.delete_selected_rows)':'button_clear_selection_imaging.clicked.connect(lambda checked: Ui_ExperimentTracker.delete_selected_rows(self, sender="imaging", MainWindow=ExperimentTracker))',
                    'button_clear_selection_ephys.clicked.connect(ExperimentTracker.delete_selected_rows)':'button_clear_selection_ephys.clicked.connect(lambda checked: Ui_ExperimentTracker.delete_selected_rows(self, sender="ephys", MainWindow=ExperimentTracker))',
                    'button_clear_selection_sim.clicked.connect(ExperimentTracker.delete_selected_rows)':'button_clear_selection_sim.clicked.connect(lambda checked: Ui_ExperimentTracker.delete_selected_rows(self, sender="sim", MainWindow=ExperimentTracker))'
                    }
    new_imports = ["from PyQt6.QtWidgets import QFileDialog, QMessageBox\n",
                   "from PyQt6.QtCore import QDate, QTime\n",
                   "from PyQt6.QtGui import QColor, QIcon\n"]
    new_imports_qt5 = ["from PyQt5.QtWidgets import QFileDialog, QMessageBox\n",
                   "from PyQt5.QtCore import QDate, QTime\n",
                   "from PyQt5.QtGui import QColor, QIcon\n"]
    

    fix_function_calls(file_path="experiment_tracker_qt5.py", search_replace_dict= replacements)
    
    add_functions_after_line(file_path='experiment_tracker_qt5.py', target_code_line='class Ui_ExperimentTracker(object):', functions_file_path='main_fcn.py')

    add_imports(file_path='experiment_tracker_qt5.py', new_imports = new_imports_qt5)
    
    add_style_change()
    # formatting at where the modification is added needs manual fixing
    # the _translate line is doubled, and the indentation is incorrect for the added code
    
    elapsed = time.time()-t
    print('Completed in %s' % elapsed)
    