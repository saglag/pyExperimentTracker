# pyExperimentTracker
A simple custom GUI for tracking electrophysiology and imaging experiments. GUI was built using Qt Designer and converted to a python file that was modified to add custom button functionality and exporting CSV/TXT files.

## Installation:
- Code has been written to minimize dependencies as much as possible while maintaining compatibility with my personal workflow. 
  - PyQt5 or PyQt6 
  - Pandas (for table extraction and exporting)
- Create custom Anaconda environment using the appropriate python version:

```
conda create env -n pyExperimentTracker python=3.7
conda activate pyExperimentTracker
conda install pyqt5
conda install pandas
conda install -c conda-forge pyinstaller
```
- UI conversion
```
cd C:\path\to\directory
# Make a backup copy of the ui file
copy experiment_tracker_win7.ui experiment_tracker_win7_copy.ui

# Convert the ui file to a python file
pyuic5 experiment_tracker_win7.ui -x -o experiment_tracker_win7.py
# IMPORTANT: if the order isn't correct, it will delete the contents of the .ui file

# Modify GUI to add button functionality (make changes to file_name specified in script if necessary)
python3.7 gui_corrector.py

# Convert the resources file to a python file
pyrcc5 resources.qrc -o resources_rc.py

# Compile the application
pyinstaller --icon=images\icon.png --onedir --name "Experiment Tracker" experiment_tracker_win7.py

```

- ~~Standalone applications are not provided in the various subfolders, due to Github size limits.~~
- Portable applications are built using a one directory conversion via pyinstaller via a command line interface 
  - Windows 7 and instructions are found in the cli_fcns.txt file. 
- Version-specific applications can be created via pyinstaller, if necessary.
- experiment_tracker.py requires PyQt6, experiment_tracker_win.py requires PyQt5. .ui files provided and can be modified as necessary.

## Previews:
### Windows 7 Interface
![Screenshot from 2023-04-10 10-08-37](https://user-images.githubusercontent.com/32366041/230917883-37b58ec5-fb1d-45d0-9887-ce19ee7e812b.png)
