def exportNotes(self,sender, MainWindow, filename=None):
    """Export the notes section."""
    if not filename:
        file_name, _ = QFileDialog.getSaveFileName(MainWindow,"Save Notes Text File","","TXT files (*.txt);; All Files (*)")
        if file_name:
            if ".txt" not in file_name:
                file_name = file_name + '.txt'
            if sender == "animal":
                notes = self.experiment_notes.toPlainText()
            elif sender == "imaging":
                notes = self.info_experiment_notes_imaging.toPlainText()
            elif sender == "ephys":
                notes = self.info_notes_ephys.toPlainText()
            elif sender == "sim":
                notes = self.info_notes_sim.toPlainText()
            if file_name:
                with open(file_name, 'w') as f:
                    f.write(notes)


def todayClick(self, sender):        
    """Get the current date."""
    today = QDate.currentDate()
    
    # change the output depending on the tab currently selected
    if sender == "animal":
        self.surgery_date.setDate(today)
    elif sender == "imaging":
        self.info_experiment_date_imaging.setDate(today)
    elif sender == "ephys":
        self.info_experiment_date_ephys.setDate(today)
    elif sender == "sim":
        self.info_experiment_date_sim.setDate(today)
    
    
def nowClick(self,sender):
    """Get the current time.""" 
    now = QTime.currentTime()
    
    # change the output depending on the tab currently selected
    if sender == 'animal':
        self.surgery_start_time.setTime(now)
    elif sender == 'imaging':
        self.info_experiment_time_imaging.setTime(now)
    elif sender == 'imaging drug':
        self.info_drug_exposure_time_start_imaging.setTime(now)
    elif sender == 'ephys':
        self.info_experiment_time_ephys.setTime(now)
    elif sender == 'ephys drug':
        self.info_drug_exposure_time_start_ephys.setTime(now)
    elif sender == 'sim':
        self.info_experiment_time_sim.setTime(now)
    elif sender == 'sim drug':
        self.info_drug_exposure_time_start_sim.setTime(now)
    

def appendInfo(self, sender):
    """Append new line to the table."""     
    def convert_spin_box_value(value):
            if value < 10:
                tmp_value = '00' + str(value)
            elif value >= 10 and value < 100:
                tmp_value = '0' + str(value)
            else:
                tmp_value = value
            return tmp_value
    # Imaging
    if sender == "imaging":
        # experiment info
        experiment_date = self.info_experiment_date_imaging.date().toString("yyyy-MM-dd") 
        experiment_time = self.info_experiment_time_imaging.time().toString("HH:mm:ss") 
        experiment_type = self.info_experiment_type_imaging.currentText() 
        cell_depth_in_microns = self.info_cell_depth_imaging.text() 
        cell_region = self.info_cell_region_imaging.currentText() 
        
        # imaging info
        isoflurane_percent = self.info_isoflurane_percent_imaging.text() 
        laser_power = self.info_laser_power_imaging.text() 
        height_in_pixels = self.info_height_in_pixels_imaging.text()
        width_in_pixels = self.info_width_in_pixels_imaging.text() 
        num_channels = self.info_num_channels_imaging.text()
        frame_rate = self.info_frame_rate_imaging.text() 
        scan_method = self.info_scan_method_imaging.currentText() 
        indicator = self.info_indicator_imaging.currentText() 
        
        # drug info
        drug_administered = self.info_drug_administered_imaging.text() 
        drug_concentration = self.info_drug_concentration_micromolar_imaging.text() 
        route_of_admin = self.info_drug_route_of_admin_imaging.text() 
        drug_start_time = self.info_drug_exposure_time_start_imaging.time().toString("HH:mm:ss")
        
        # file info, animal id, and notes
        fname = self.info_fname_imaging.text()
        fnum = self.info_fnum_imaging.value()  
        file_name = fname + '-' + str(convert_spin_box_value(fnum))         
        animal_id = self.animal_id.text() 
        notes = self.info_experiment_notes_imaging.toPlainText() 
       
        # Add row to table
        row_position = self.table_data_imaging.rowCount()
        self.table_data_imaging.insertRow(row_position)
        
        # populate the table 
        self.table_data_imaging.setItem(row_position, 0, QtWidgets.QTableWidgetItem(experiment_date))
        self.table_data_imaging.setItem(row_position, 1, QtWidgets.QTableWidgetItem(experiment_time))
        self.table_data_imaging.setItem(row_position, 2, QtWidgets.QTableWidgetItem(experiment_type))
        self.table_data_imaging.setItem(row_position, 3, QtWidgets.QTableWidgetItem(cell_depth_in_microns))
        self.table_data_imaging.setItem(row_position, 4, QtWidgets.QTableWidgetItem(cell_region))
        self.table_data_imaging.setItem(row_position, 5, QtWidgets.QTableWidgetItem(isoflurane_percent))
        self.table_data_imaging.setItem(row_position, 6, QtWidgets.QTableWidgetItem(laser_power))
        self.table_data_imaging.setItem(row_position, 7, QtWidgets.QTableWidgetItem(height_in_pixels))
        self.table_data_imaging.setItem(row_position, 8, QtWidgets.QTableWidgetItem(width_in_pixels))
        self.table_data_imaging.setItem(row_position, 9, QtWidgets.QTableWidgetItem(num_channels))
        self.table_data_imaging.setItem(row_position, 10, QtWidgets.QTableWidgetItem(scan_method))
        self.table_data_imaging.setItem(row_position, 11, QtWidgets.QTableWidgetItem(frame_rate))
        self.table_data_imaging.setItem(row_position, 12, QtWidgets.QTableWidgetItem(indicator))
        self.table_data_imaging.setItem(row_position, 13, QtWidgets.QTableWidgetItem(drug_administered))
        self.table_data_imaging.setItem(row_position, 14, QtWidgets.QTableWidgetItem(drug_concentration))
        self.table_data_imaging.setItem(row_position, 15, QtWidgets.QTableWidgetItem(route_of_admin))
        self.table_data_imaging.setItem(row_position, 16, QtWidgets.QTableWidgetItem(drug_start_time))
        self.table_data_imaging.setItem(row_position, 17, QtWidgets.QTableWidgetItem(animal_id))
        self.table_data_imaging.setItem(row_position, 18, QtWidgets.QTableWidgetItem(file_name))
        self.table_data_imaging.setItem(row_position, 19, QtWidgets.QTableWidgetItem(notes)) 
        
        # Increase the file number
        self.info_fnum_imaging.setValue(fnum + 1)            
            
    # Ephys
    elif sender == "ephys":
        # experiment info
        experiment_date = self.info_experiment_date_ephys.date().toString("yyyy-MM-dd") #0
        experiment_time = self.info_experiment_time_ephys.time().toString("HH:mm:ss") #1
        experiment_type = self.info_experiment_type_ephys.currentText() #3
        cell_depth_microns = self.info_cell_depth_ephys.text() 
        cell_region = self.info_cell_region_ephys.currentText()
        isoflurane_percent = self.info_isoflurane_percent_ephys.text() 
        
        # drug info
        drug_administered = self.info_drug_administered_ephys.text() #13
        drug_concentration = self.info_drug_concentration_micromolar_ephys.text()
        route_of_admin = self.info_drug_route_of_admin_ephys.text() 
        drug_start_time = self.info_drug_exposure_time_start_ephys.time().toString("HH:mm:ss")
        
        # patch info
        pipette_resistance = self.info_pipette_resistance_start_ephys.text()
        seal_resistance = self.info_seal_resistance_start_ephys.text()
        membrane_resistance = self.info_membrane_resistance_ephys.text()
        membrane_capacitance = self.info_membrane_capacitance_ephys.text()
        patch_region = self.info_patch_region_ephys.currentText()
        internal_solution = self.info_internal_solution_ephys.currentText()
        
        # recording info
        clamp_type = self.info_clamp_type_ephys.currentText()
        protocol = self.info_protocol_ephys.text()
        sampling_rate = self.info_sampling_rate_ephys.text()
        
        # file info, animal id, and notes
        fname = self.info_fname_ephys.text()
        fnum = self.info_fnum_ephys.value()  
        file_name = fname + '-' + str(convert_spin_box_value(fnum))           
        animal_id = self.animal_id.text() #16
        notes = self.info_notes_ephys.toPlainText() #19
        
        # Add row to table
        row_position = self.table_data_ephys.rowCount()
        self.table_data_ephys.insertRow(row_position)
        
        # populate the table 
        self.table_data_ephys.setItem(row_position, 0, QtWidgets.QTableWidgetItem(experiment_date))
        self.table_data_ephys.setItem(row_position, 1, QtWidgets.QTableWidgetItem(experiment_time))
        self.table_data_ephys.setItem(row_position, 2, QtWidgets.QTableWidgetItem(experiment_type))
        self.table_data_ephys.setItem(row_position, 3, QtWidgets.QTableWidgetItem(cell_depth_microns))
        self.table_data_ephys.setItem(row_position, 4, QtWidgets.QTableWidgetItem(cell_region))
        self.table_data_ephys.setItem(row_position, 5, QtWidgets.QTableWidgetItem(isoflurane_percent))
        self.table_data_ephys.setItem(row_position, 6, QtWidgets.QTableWidgetItem(internal_solution))
        self.table_data_ephys.setItem(row_position, 7, QtWidgets.QTableWidgetItem(clamp_type))
        self.table_data_ephys.setItem(row_position, 8, QtWidgets.QTableWidgetItem(protocol))
        self.table_data_ephys.setItem(row_position, 9, QtWidgets.QTableWidgetItem(sampling_rate))
        self.table_data_ephys.setItem(row_position, 10, QtWidgets.QTableWidgetItem(pipette_resistance))
        self.table_data_ephys.setItem(row_position, 11, QtWidgets.QTableWidgetItem(seal_resistance))
        self.table_data_ephys.setItem(row_position, 12, QtWidgets.QTableWidgetItem(membrane_resistance))
        self.table_data_ephys.setItem(row_position, 13, QtWidgets.QTableWidgetItem(membrane_capacitance))
        self.table_data_ephys.setItem(row_position, 14, QtWidgets.QTableWidgetItem(patch_region))
        self.table_data_ephys.setItem(row_position, 15, QtWidgets.QTableWidgetItem(drug_administered))
        self.table_data_ephys.setItem(row_position, 16, QtWidgets.QTableWidgetItem(drug_concentration))
        self.table_data_ephys.setItem(row_position, 17, QtWidgets.QTableWidgetItem(route_of_admin))
        self.table_data_ephys.setItem(row_position, 18, QtWidgets.QTableWidgetItem(drug_start_time))
        self.table_data_ephys.setItem(row_position, 19, QtWidgets.QTableWidgetItem(animal_id))
        self.table_data_ephys.setItem(row_position, 20, QtWidgets.QTableWidgetItem(file_name))
        self.table_data_ephys.setItem(row_position, 21, QtWidgets.QTableWidgetItem(notes))
        
        # Increase the file number
        self.info_fnum_ephys.setValue(fnum + 1)  
                          
    # Simultaneous
    elif sender == "sim":
        # experiment info
        experiment_date = self.info_experiment_date_sim.date().toString("yyyy-MM-dd") 
        experiment_time = self.info_experiment_time_sim.time().toString("HH:mm:ss") 
        experiment_type = self.info_experiment_type_sim.currentText() 
        cell_depth_in_microns = self.info_cell_depth_sim.text() 
        cell_region = self.info_cell_region_sim.currentText()
        isoflurane_percent = self.info_isoflurane_percent_sim.text() 
        
        # imaging info
        laser_power = self.info_laser_power_sim.text() 
        height_in_pixels = self.info_height_in_pixels_sim.text() 
        width_in_pixels = self.info_width_in_pixels_sim.text() 
        num_channels = self.info_num_channels_sim.text() 
        frame_rate = self.info_frame_rate_sim.text() 
        scan_method = self.info_scan_method_sim.currentText() 
        indicator = self.info_indicator_sim.currentText() 
        
        # drug info
        drug_administered = self.info_drug_administered_sim.text() 
        drug_concentration = self.info_drug_concentration_micromolar_sim.text()
        route_of_admin = self.info_drug_route_of_admin_sim.text() 
        drug_start_time = self.info_drug_exposure_time_start_sim.time().toString("HH:mm:ss")
        
        # patch info
        pipette_resistance = self.info_pipette_resistance_start_sim.text()
        seal_resistance = self.info_seal_resistance_start_sim.text()
        membrane_resistance = self.info_membrane_resistance_sim.text()
        membrane_capacitance = self.info_membrane_capacitance_sim.text()
        patch_region = self.info_patch_region_sim.currentText()
        internal_solution = self.info_internal_solution_sim.currentText()
        
        # recording info
        clamp_type = self.info_clamp_type_sim.currentText()
        protocol = self.info_protocol_sim.text()
        sampling_rate = self.info_sampling_rate_sim.text()
        
        # file info, animal id, and notes
        imaging_fname = self.info_fname_imaging_sim.text()
        imaging_fnum = self.info_fnum_imaging_sim.value() 
        ephys_fname = self.info_fname_ephys_sim.text()
        ephys_fnum = self.info_fnum_ephys_sim.value() 
        ephys_file_name = ephys_fname + '-' + str(convert_spin_box_value(ephys_fnum))
        imaging_file_name = imaging_fname + '-' + str(convert_spin_box_value(imaging_fnum))
        animal_id = self.animal_id.text() 
        notes = self.info_notes_sim.toPlainText() 
        
        # Add row to table
        row_position = self.table_data_sim.rowCount()
        self.table_data_sim.insertRow(row_position)
        
        self.table_data_sim.setItem(row_position, 0, QtWidgets.QTableWidgetItem(experiment_date))
        self.table_data_sim.setItem(row_position, 1, QtWidgets.QTableWidgetItem(experiment_time))
        self.table_data_sim.setItem(row_position, 2, QtWidgets.QTableWidgetItem(experiment_type))
        self.table_data_sim.setItem(row_position, 3, QtWidgets.QTableWidgetItem(cell_depth_in_microns))          
        self.table_data_sim.setItem(row_position, 4, QtWidgets.QTableWidgetItem(cell_region))                          
        self.table_data_sim.setItem(row_position, 5, QtWidgets.QTableWidgetItem(isoflurane_percent))
        self.table_data_sim.setItem(row_position, 6, QtWidgets.QTableWidgetItem(laser_power))                           
        self.table_data_sim.setItem(row_position, 7, QtWidgets.QTableWidgetItem(height_in_pixels))                            
        self.table_data_sim.setItem(row_position, 8, QtWidgets.QTableWidgetItem(width_in_pixels))    
        self.table_data_sim.setItem(row_position, 9, QtWidgets.QTableWidgetItem(num_channels))                            
        self.table_data_sim.setItem(row_position, 10, QtWidgets.QTableWidgetItem(scan_method))
        self.table_data_sim.setItem(row_position, 11, QtWidgets.QTableWidgetItem(frame_rate))
        self.table_data_sim.setItem(row_position, 12, QtWidgets.QTableWidgetItem(indicator))
        self.table_data_sim.setItem(row_position, 13, QtWidgets.QTableWidgetItem(internal_solution))
        self.table_data_sim.setItem(row_position, 14, QtWidgets.QTableWidgetItem(clamp_type))
        self.table_data_sim.setItem(row_position, 15, QtWidgets.QTableWidgetItem(protocol))
        self.table_data_sim.setItem(row_position, 16, QtWidgets.QTableWidgetItem(sampling_rate))
        self.table_data_sim.setItem(row_position, 17, QtWidgets.QTableWidgetItem(pipette_resistance))
        self.table_data_sim.setItem(row_position, 18, QtWidgets.QTableWidgetItem(seal_resistance))
        self.table_data_sim.setItem(row_position, 19, QtWidgets.QTableWidgetItem(membrane_resistance))
        self.table_data_sim.setItem(row_position, 20, QtWidgets.QTableWidgetItem(membrane_capacitance))
        self.table_data_sim.setItem(row_position, 21, QtWidgets.QTableWidgetItem(patch_region))
        self.table_data_sim.setItem(row_position, 22, QtWidgets.QTableWidgetItem(drug_administered))
        self.table_data_sim.setItem(row_position, 23, QtWidgets.QTableWidgetItem(drug_concentration))
        self.table_data_sim.setItem(row_position, 24, QtWidgets.QTableWidgetItem(route_of_admin))
        self.table_data_sim.setItem(row_position, 25, QtWidgets.QTableWidgetItem(drug_start_time))
        self.table_data_sim.setItem(row_position, 26, QtWidgets.QTableWidgetItem(animal_id))
        self.table_data_sim.setItem(row_position, 27, QtWidgets.QTableWidgetItem(imaging_file_name))
        self.table_data_sim.setItem(row_position, 28, QtWidgets.QTableWidgetItem(ephys_file_name))
        self.table_data_sim.setItem(row_position, 29, QtWidgets.QTableWidgetItem(notes))
        
        # Increase the file number
        self.info_fnum_imaging_sim.setValue(imaging_fnum + 1)
        self.info_fnum_ephys_sim.setValue(ephys_fnum + 1)

def exportInfo(self, sender, MainWindow, filename=None):
    """Export the table to a CSV file."""
    import pandas as pd
    # create a dictionary then store it in a dataframe
    if not filename:
        fileName = QFileDialog.getSaveFileName(MainWindow,"Save File","","CSV files (*.csv);; All Files (*)")
        file_name = fileName[0]
        if file_name:
            if ".csv" not in file_name:
                file_name = file_name + '.csv'
    if sender == "animal":
        dob = self.animal_dob.date().toString("yyyy-MM-dd") 
        species = self.animal_species.currentText()
        strain = self.animal_strain.currentText()
        sex = self.animal_sex.currentText()
        cage_number = self.animal_cage_number.text()
        animal_id = self.animal_id.text()
        surgery_date = self.surgery_date.date().toString("yyyy-MM-dd") 
        start_time = self.surgery_start_time.time().toString("HH:mm:ss") 
        brain_region = self.animal_brain_region.text()
        notes = self.animal_notes.toPlainText()
        data = {'Variable':['dob',
                            'species',
                            'strain',
                            'sex',
                            'cage_number',
                            'animal_id',
                            'surgery_date',
                            'surgery_start_time',
                            'brain_region',
                            'file_name',
                            'notes'],
                            'Value':[dob,
                                     species,
                                     strain,
                                     sex,
                                     cage_number,
                                     animal_id,
                                     surgery_date,
                                     start_time,
                                     brain_region,
                                     file_name,
                                     notes]}
    elif sender == "imaging":
       table = self.table_data_imaging
       rows = table.rowCount()
       cols = table.columnCount()
       headers = [table.horizontalHeaderItem(i).text() for i in range(cols)]
       data = []
    elif sender == "ephys":
        table = self.table_data_ephys
        rows = table.rowCount()
        cols = table.columnCount()
        headers = [table.horizontalHeaderItem(i).text() for i in range(cols)]
        data = []
    elif sender == "sim":
        table = self.table_data_sim
        rows = table.rowCount()
        cols = table.columnCount()
        headers = [table.horizontalHeaderItem(i).text() for i in range(cols)]
        data = []
    
    
    if sender != "animal":
        for row in range(rows):
            tmp = []
            for col in range(cols):
                item = table.item(row, col)
                tmp.append(item.text())
            data.append(tmp)
        df = pd.DataFrame(data, columns=headers)
        df.fillna(value=pd.np.nan, inplace=True)
        if file_name:
            df.to_csv(file_name, index=False)
    else:
        df = pd.DataFrame(data)
        df = df.transpose()
        df.fillna(value=pd.np.nan, inplace=True)
        if file_name:
            df.to_csv(file_name, index=False)

        

# do some math
def calculatePipetteEntry(self):
    """Calculate pipette position to enter the brain."""
    import math
    try:
        try:
            manipulator_angle = float(self.info_manipulator_angle_calc.text())
        except:
            manipulator_angle = 20
        try:
            cell_depth = float(self.info_cell_dept_calc.text())
        except:
            cell_depth = 150
        try:
            cell_distance_glass = float(self.info_glass_distance_calc.text())
        except:
            cell_distance_glass = 150
        try:
            x_start = int(self.info_x_start_calc.text())
        except:
            x_start = 0
        try:
            z_start = int(self.info_z_start_calc.text())
        except:
            z_start = 0  
        
        # convert from degrees to radians
        gamma_angle = math.radians(70)
        manipulator_angle = math.radians(float(manipulator_angle))
        
        # Calculate base distance of entry
        distance_from_cell = (cell_depth * math.sin(gamma_angle)) / (math.sin(manipulator_angle))
        
        # Pipette distance from glass
        pipette_distance_from_glass = distance_from_cell - cell_distance_glass
        
        # X target
        x_tar = x_start - pipette_distance_from_glass
        z_tar = z_start + cell_depth
        
        # Output the measurements
        self.info_entry_dist_from_cell_calc.setText(str(int(distance_from_cell)))
        self.info_entry_dist_from_glass_calc.setText(str(int(pipette_distance_from_glass)))
        self.info_x_tar_calc.setText(str(int(x_tar)))
        self.info_z_tar_calc.setText(str(int(z_tar)))
        
    except:
        self.cell_entry.setText("Error")

def delete_selected_rows(self, sender, MainWindow):
    msgBox = QMessageBox(
    QMessageBox.Question,
    "Delete Selected Rows",
    "Are you sure you want to delete the selected rows?",
    buttons=QMessageBox.Yes | QMessageBox.No
    )
    msgBox.setDefaultButton(QMessageBox.No)
    msgBox.exec_()
    reply = msgBox.standardButton(msgBox.clickedButton())
    if reply == QMessageBox.StandardButton.Yes:
        if sender == "imaging":
           selected_ranges = self.table_data_imaging.selectedRanges()
           for selected_range in selected_ranges:
               top_row = selected_range.topRow()
               bottom_row = selected_range.bottomRow()
               for row in range(top_row, bottom_row + 1):
                   self.table_data_imaging.removeRow(top_row) 
        elif sender == "ephys":
            selected_ranges = self.table_data_ephys.selectedRanges()
            for selected_range in selected_ranges:
                top_row = selected_range.topRow()
                bottom_row = selected_range.bottomRow()
                for row in range(top_row, bottom_row + 1):
                    self.table_data_ephys.removeRow(top_row) 
        elif sender == "sim":
            selected_ranges = self.table_data_sim.selectedRanges()
            for selected_range in selected_ranges:
                top_row = selected_range.topRow()
                bottom_row = selected_range.bottomRow()
                for row in range(top_row, bottom_row + 1):
                    self.table_data_sim.removeRow(top_row)
                    

    
         
