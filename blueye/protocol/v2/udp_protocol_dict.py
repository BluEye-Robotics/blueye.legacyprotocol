# -*- coding: utf-8 -*-
# This file is autogenerated. Please do not edit
from collections import OrderedDict
_json_hash = "90413634076faf22ba2be2ff7a309c42"
_generator_hash = "ddae73db6077927655e12907e1a638e0"
protocol_data = [OrderedDict({'version': '1', 'messages': [OrderedDict({'name': 'telemetry', 'message_type': '1', 'fields': [OrderedDict({'description': 'Protocol version', 'dtype': '<u1', 'field_name': 'version', 'unit': '', 'init': '1'}), OrderedDict({'description': '', 'dtype': '<u1', 'field_name': 'command_type', 'unit': '', 'init': '1'}), OrderedDict({'description': '', 'dtype': '<u4', 'field_name': 'time', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<f8', 'field_name': 'rt_clock', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u8', 'field_name': 'error_flags', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u8', 'field_name': 'debug_flags', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<f8', 'field_name': 'user_lat', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<f8', 'field_name': 'user_lon', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i8', 'field_name': 'total_space', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i8', 'field_name': 'free_space', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'camera_record_time', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'temp_bottom', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'temp_water', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'temp_top', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'temp_cpu', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u1', 'field_name': 'lights_upper', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u1', 'field_name': 'lights_lower', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'dive_time', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'control_mode', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'pressure_top', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i4', 'field_name': 'depth', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i4', 'field_name': 'depth_reference', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<f4', 'field_name': 'heading_reference', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<f4', 'field_name': 'roll', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<f4', 'field_name': 'pitch', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<f4', 'field_name': 'yaw', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'imucal_samples', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_temp', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_voltage', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i4', 'field_name': 'battery_current', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i4', 'field_name': 'battery_average_current', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u1', 'field_name': 'battery_state_of_charge_rel', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_remaining_capacity', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_full_charge_capacity', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_run_time_to_empty', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_avg_time_to_empty', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_avg_time_to_full', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_at_rate_time_to_full', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_at_rate_time_to_empty', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_charging_current', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_charging_voltage', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_status', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_cell_voltage_1', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_cell_voltage_2', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_cell_voltage_3', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_cell_voltage_4', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'battery_cell_temperature_1', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'battery_cell_temperature_2', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'battery_cell_temperature_3', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<i2', 'field_name': 'battery_cell_temperature_4', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u1', 'field_name': 'battery_max_error', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u1', 'field_name': 'battery_state_of_charge_abs', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_cycle_count', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_design_capacity', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_manufacture_date', 'unit': ''}), OrderedDict({'description': '', 'dtype': '<u2', 'field_name': 'battery_serial_number', 'unit': ''})]})]}), OrderedDict({'version': '2', 'messages': [OrderedDict({'name': 'telemetry', 'message_type': '1', 'fields': [OrderedDict({'description': 'Protocol version', 'dtype': '<u1', 'field_name': 'version', 'unit': '', 'init': '2'}), OrderedDict({'description': 'Command type', 'dtype': '<u1', 'field_name': 'command_type', 'unit': '', 'init': '1'}), OrderedDict({'description': 'Time', 'dtype': '<u4', 'field_name': 'time', 'unit': 'ms'}), OrderedDict({'description': 'Real-time clock', 'dtype': '<f8', 'field_name': 'rt_clock', 'unit': 's'}), OrderedDict({'description': 'Error flags (bitmask)', 'dtype': '<u8', 'field_name': 'error_flags', 'unit': '', 'flags': [OrderedDict({'value': '0x00000001', 'name': 'ERR_PMU_COMM_ACK', 'component': 'pmu', 'description': 'Did not receive ack from pmu'}), OrderedDict({'value': '0x00000002', 'name': 'ERR_PMU_COMM_STREAM', 'component': 'pmu', 'description': 'Pmu streaming timeout'}), OrderedDict({'value': '0x00000004', 'name': 'ERR_DEPTH_READ', 'component': 'sensor_depth', 'description': 'Failed to read depth sensor'}), OrderedDict({'value': '0x00000008', 'name': 'ERR_DEPTH_SPIKE', 'component': 'sensor_depth', 'description': 'Depth read spike detected'}), OrderedDict({'value': '0x00000010', 'name': 'ERR_INNER_PRESSURE_READ', 'component': 'sensor_inner_pressure', 'description': 'Failed to read inner pressure sensor'}), OrderedDict({'value': '0x00000020', 'name': 'ERR_INNER_PRESSURE_SPIKE', 'component': 'sensor_inner_pressure', 'description': 'Inner pressure read spike detected'}), OrderedDict({'value': '0x00000040', 'name': 'ERR_COMPASS_CALIBRATION', 'component': 'compass', 'description': 'Invalid compass calibration'}), OrderedDict({'value': '0x00000080', 'name': 'ERR_TILT_CALIBRATION', 'component': 'tilt', 'description': 'Invalid tilt calibration'}), OrderedDict({'value': '0x00000100', 'name': 'ERR_GP1_READ', 'component': 'guest_port', 'description': 'Guest port 1 read error'}), OrderedDict({'value': '0x00000200', 'name': 'ERR_GP2_READ', 'component': 'guest_port', 'description': 'Guest port 2 read error'}), OrderedDict({'value': '0x00000400', 'name': 'ERR_GP3_READ', 'component': 'guest_port', 'description': 'Guest port 3 read error'}), OrderedDict({'value': '0x00000800', 'name': 'ERR_GP1_NOT_FLASHED', 'component': 'guest_port', 'description': 'Guest port 1 not flashed'}), OrderedDict({'value': '0x00001000', 'name': 'ERR_GP2_NOT_FLASHED', 'component': 'guest_port', 'description': 'Guest port 2 not flashed'}), OrderedDict({'value': '0x00002000', 'name': 'ERR_GP3_NOT_FLASHED', 'component': 'guest_port', 'description': 'Guest port 3 not flashed'}), OrderedDict({'value': '0x00004000', 'name': 'ERR_GP1_UNKNOWN_DEVICE', 'component': 'guest_port', 'description': 'Unknown device on guest port 1'}), OrderedDict({'value': '0x00008000', 'name': 'ERR_GP2_UNKNOWN_DEVICE', 'component': 'guest_port', 'description': 'Unknown device on guest port 2'}), OrderedDict({'value': '0x00010000', 'name': 'ERR_GP3_UNKNOWN_DEVICE', 'component': 'guest_port', 'description': 'Unknown device on guest port 3'}), OrderedDict({'value': '0x00020000', 'name': 'ERR_GP1_DEVICE_CONNECTION', 'component': 'guest_port', 'description': 'Guest port 1 connection error'}), OrderedDict({'value': '0x00040000', 'name': 'ERR_GP2_DEVICE_CONNECTION', 'component': 'guest_port', 'description': 'Guest port 2 connection error'}), OrderedDict({'value': '0x00080000', 'name': 'ERR_GP3_DEVICE_CONNECTION', 'component': 'guest_port', 'description': 'Guest port 3 connection error'}), OrderedDict({'value': '0x00100000', 'name': 'ERR_GP1_DEVICE', 'component': 'guest_port', 'description': 'Guest port 1 device error'}), OrderedDict({'value': '0x00200000', 'name': 'ERR_GP2_DEVICE', 'component': 'guest_port', 'description': 'Guest port 2 device error'}), OrderedDict({'value': '0x00400000', 'name': 'ERR_GP3_DEVICE', 'component': 'guest_port', 'description': 'Guest port 3 device error'}), OrderedDict({'value': '0x00800000', 'name': 'ERR_DRONE_SERIAL_NOT_SET', 'component': 'drone_info', 'description': 'Drone serial number not set'}), OrderedDict({'value': '0x01000000', 'name': 'ERR_DRONE_SERIAL', 'component': 'drone_info', 'description': 'Drone serial number error'}), OrderedDict({'value': '0x02000000', 'name': 'ERR_MB_EEPROM_READ', 'component': 'mb_eeeprom', 'description': 'MB eeprom read error'}), OrderedDict({'value': '0x04000000', 'name': 'ERR_BB_EEPROM_READ', 'component': 'drone_info', 'description': 'BB eeprom read error'}), OrderedDict({'value': '0x08000000', 'name': 'ERR_MB_EEPROM_NOT_FLASHED', 'component': 'drone_info', 'description': 'MB eeprom not flashed'}), OrderedDict({'value': '0x10000000', 'name': 'ERR_BB_EEPROM_NOT_FLASHED', 'component': 'drone_info', 'description': 'BB eeprom not flashed'}), OrderedDict({'value': '0x20000000', 'name': 'ERR_MAIN_CAMERA_CONNECTION', 'component': 'main_camera', 'description': 'Main camera is unreachable'}), OrderedDict({'value': '0x40000000', 'name': 'ERR_MAIN_CAMERA_FIRMWARE', 'component': 'main_camera', 'description': 'Main camera has wrong firmware'}), OrderedDict({'value': '0x80000000', 'name': 'ERR_GUESTPORT_CAMERA_CONNECTION', 'component': 'guestport_camera', 'description': 'Guestport camera is unreachable'}), OrderedDict({'value': '0x100000000', 'name': 'ERR_GUESTPORT_CAMERA_FIRMWARE', 'component': 'guestport_camera', 'description': 'Guestport camera has wrong firmware'}), OrderedDict({'value': '0x200000000', 'name': 'ERR_MB_SERIAL', 'component': 'drone_info', 'description': 'MB serial number error'}), OrderedDict({'value': '0x400000000', 'name': 'ERR_BB_SERIAL', 'component': 'drone_info', 'description': 'BB serial number error'}), OrderedDict({'value': '0x800000000', 'name': 'ERR_DS_SERIAL', 'component': 'drone_info', 'description': 'DS serial number error'}), OrderedDict({'value': '0x1000000000', 'name': 'ERR_GP_CURRENT_READ', 'component': 'guest_port', 'description': 'Error reading GP current'}), OrderedDict({'value': '0x2000000000', 'name': 'ERR_GP_CURRENT', 'component': 'guest_port', 'description': 'Max GP current exceeded'}), OrderedDict({'value': '0x4000000000', 'name': 'ERR_GP1_BAT_CURRENT', 'component': 'guest_port', 'description': 'Max battery current exceeded on GP1'}), OrderedDict({'value': '0x8000000000', 'name': 'ERR_GP2_BAT_CURRENT', 'component': 'guest_port', 'description': 'Max battery current exceeded on GP2'}), OrderedDict({'value': '0x10000000000', 'name': 'ERR_GP3_BAT_CURRENT', 'component': 'guest_port', 'description': 'Max battery current exceeded on GP3'}), OrderedDict({'value': '0x20000000000', 'name': 'ERR_GP_20V_CURRENT', 'component': 'guest_port', 'description': 'Max 20V current exceeded on GP'})]}), OrderedDict({'description': 'Debug flags (bitmask)', 'dtype': '<u8', 'field_name': 'debug_flags', 'unit': ''}), OrderedDict({'description': 'Latitude', 'dtype': '<f8', 'field_name': 'user_lat', 'unit': 'dec °'}), OrderedDict({'description': 'Longitude', 'dtype': '<f8', 'field_name': 'user_lon', 'unit': 'dec °'}), OrderedDict({'description': 'Total space on data partition', 'dtype': '<i8', 'field_name': 'total_space', 'unit': 'bytes'}), OrderedDict({'description': 'Free space on data partition', 'dtype': '<i8', 'field_name': 'free_space', 'unit': 'bytes'}), OrderedDict({'description': 'Record time (-1 if not recording)', 'dtype': '<i2', 'field_name': 'camera_record_time', 'unit': 's'}), OrderedDict({'description': 'Bottom temperature', 'dtype': '<i2', 'field_name': 'temp_bottom', 'unit': '0.1°C'}), OrderedDict({'description': 'Water temperature', 'dtype': '<i2', 'field_name': 'temp_water', 'unit': '0.1°C'}), OrderedDict({'description': 'Top canister temperature', 'dtype': '<i2', 'field_name': 'temp_top', 'unit': '0.1°C'}), OrderedDict({'description': 'cpu temperature', 'dtype': '<i2', 'field_name': 'temp_cpu', 'unit': '0.1°C'}), OrderedDict({'description': 'Humidity in top canister', 'dtype': '<i2', 'field_name': 'humidity_top', 'unit': '0.1%'}), OrderedDict({'description': 'Humidity in bottom canister', 'dtype': '<i2', 'field_name': 'humidity_bottom', 'unit': '0.1%'}), OrderedDict({'description': 'Status upper lights (0..255)', 'dtype': '<u1', 'field_name': 'lights_upper', 'unit': ''}), OrderedDict({'description': 'Status lower lights (0..255)', 'dtype': '<u1', 'field_name': 'lights_lower', 'unit': ''}), OrderedDict({'description': 'Dive time (-1 if not diving)', 'dtype': '<i2', 'field_name': 'dive_time', 'unit': 's'}), OrderedDict({'description': 'Control mode', 'dtype': '<i2', 'field_name': 'control_mode', 'unit': ''}), OrderedDict({'description': 'Pressure in top canister', 'dtype': '<u2', 'field_name': 'pressure_top', 'unit': 'mbar'}), OrderedDict({'description': 'Depth', 'dtype': '<i4', 'field_name': 'depth', 'unit': 'mm'}), OrderedDict({'description': 'Depth reference', 'dtype': '<i4', 'field_name': 'reference_depth', 'unit': 'mm'}), OrderedDict({'description': 'Heading reference', 'dtype': '<f4', 'field_name': 'reference_heading', 'unit': ''}), OrderedDict({'description': 'Surge reference', 'dtype': '<f4', 'field_name': 'reference_surge', 'unit': ''}), OrderedDict({'description': 'Sway reference', 'dtype': '<f4', 'field_name': 'reference_sway', 'unit': ''}), OrderedDict({'description': 'Heave reference', 'dtype': '<f4', 'field_name': 'reference_heave', 'unit': ''}), OrderedDict({'description': 'Yaw reference', 'dtype': '<f4', 'field_name': 'reference_yaw', 'unit': ''}), OrderedDict({'description': 'Surge control force', 'dtype': '<f4', 'field_name': 'control_force_surge', 'unit': ''}), OrderedDict({'description': 'Sway control force', 'dtype': '<f4', 'field_name': 'control_force_sway', 'unit': ''}), OrderedDict({'description': 'Heave control force', 'dtype': '<f4', 'field_name': 'control_force_heave', 'unit': ''}), OrderedDict({'description': 'Yaw control force', 'dtype': '<f4', 'field_name': 'control_force_yaw', 'unit': ''}), OrderedDict({'description': 'Roll', 'dtype': '<f4', 'field_name': 'roll', 'unit': ''}), OrderedDict({'description': 'Pitch', 'dtype': '<f4', 'field_name': 'pitch', 'unit': ''}), OrderedDict({'description': 'Yaw', 'dtype': '<f4', 'field_name': 'yaw', 'unit': ''}), OrderedDict({'description': 'Numer of IMU calibration samples (-1 if not calibrating)', 'dtype': '<i2', 'field_name': 'imucal_samples', 'unit': ''}), OrderedDict({'description': 'Battery temperature', 'dtype': '<u2', 'field_name': 'battery_temp', 'unit': '0.1°C'}), OrderedDict({'description': 'Battery voltage', 'dtype': '<u2', 'field_name': 'battery_voltage', 'unit': 'mV'}), OrderedDict({'description': 'Battery current', 'dtype': '<i4', 'field_name': 'battery_current', 'unit': 'mA'}), OrderedDict({'description': 'Battery average current', 'dtype': '<i4', 'field_name': 'battery_average_current', 'unit': 'mA'}), OrderedDict({'description': 'Battery relative state of charge', 'dtype': '<u1', 'field_name': 'battery_state_of_charge_rel', 'unit': '%'}), OrderedDict({'description': 'Remaining battery capacity', 'dtype': '<u2', 'field_name': 'battery_remaining_capacity', 'unit': 'mAh'}), OrderedDict({'description': 'Full charge battery capacity', 'dtype': '<u2', 'field_name': 'battery_full_charge_capacity', 'unit': 'mAh'}), OrderedDict({'description': 'Battery run time to empty', 'dtype': '<u2', 'field_name': 'battery_run_time_to_empty', 'unit': 'min'}), OrderedDict({'description': 'Battery average time to empty', 'dtype': '<u2', 'field_name': 'battery_avg_time_to_empty', 'unit': 'min'}), OrderedDict({'description': 'Battery average time to full', 'dtype': '<u2', 'field_name': 'battery_avg_time_to_full', 'unit': 'min'}), OrderedDict({'description': 'Battery at rate time to full', 'dtype': '<u2', 'field_name': 'battery_at_rate_time_to_full', 'unit': 'min'}), OrderedDict({'description': 'Battery at rate time to empty', 'dtype': '<u2', 'field_name': 'battery_at_rate_time_to_empty', 'unit': 'min'}), OrderedDict({'description': 'Battery charging current', 'dtype': '<u2', 'field_name': 'battery_charging_current', 'unit': 'mA'}), OrderedDict({'description': 'Battery charging voltage', 'dtype': '<u2', 'field_name': 'battery_charging_voltage', 'unit': 'mV'}), OrderedDict({'description': 'Battery status', 'dtype': '<u2', 'field_name': 'battery_status', 'unit': ''}), OrderedDict({'description': 'Battery cell voltage 1', 'dtype': '<u2', 'field_name': 'battery_cell_voltage_1', 'unit': 'mV'}), OrderedDict({'description': 'Battery cell voltage 2', 'dtype': '<u2', 'field_name': 'battery_cell_voltage_2', 'unit': 'mV'}), OrderedDict({'description': 'Battery cell voltage 3', 'dtype': '<u2', 'field_name': 'battery_cell_voltage_3', 'unit': 'mV'}), OrderedDict({'description': 'Battery cell voltage 4', 'dtype': '<u2', 'field_name': 'battery_cell_voltage_4', 'unit': 'mV'}), OrderedDict({'description': 'Battery cell temperature 1', 'dtype': '<i2', 'field_name': 'battery_cell_temperature_1', 'unit': '0.1°C'}), OrderedDict({'description': 'Battery cell temperature 2', 'dtype': '<i2', 'field_name': 'battery_cell_temperature_2', 'unit': '0.1°C'}), OrderedDict({'description': 'Battery cell temperature 3', 'dtype': '<i2', 'field_name': 'battery_cell_temperature_3', 'unit': '0.1°C'}), OrderedDict({'description': 'Battery cell temperature 4', 'dtype': '<i2', 'field_name': 'battery_cell_temperature_4', 'unit': '0.1°C'}), OrderedDict({'description': 'Battery max error', 'dtype': '<u1', 'field_name': 'battery_max_error', 'unit': ''}), OrderedDict({'description': 'Battery absolute state of charge', 'dtype': '<u1', 'field_name': 'battery_state_of_charge_abs', 'unit': ''}), OrderedDict({'description': 'Battery cycle count', 'dtype': '<u2', 'field_name': 'battery_cycle_count', 'unit': ''}), OrderedDict({'description': 'Battery design capacity', 'dtype': '<u2', 'field_name': 'battery_design_capacity', 'unit': ''}), OrderedDict({'description': 'Battery manufacture date', 'dtype': '<u4', 'field_name': 'battery_manufacture_date', 'unit': ''}), OrderedDict({'description': 'Battery serial number', 'dtype': '<u2', 'field_name': 'battery_serial_number', 'unit': ''})]}), OrderedDict({'name': 'compasscalibration', 'message_type': '2', 'fields': [OrderedDict({'description': 'Protocol version', 'dtype': '<u1', 'field_name': 'version', 'unit': '', 'init': '2'}), OrderedDict({'description': 'Command type', 'dtype': '<u1', 'field_name': 'command_type', 'unit': '', 'init': '2'}), OrderedDict({'description': 'Active Status', 'dtype': '<i1', 'field_name': 'active_status', 'unit': ''}), OrderedDict({'description': 'Progress x up', 'dtype': '<u1', 'field_name': 'progress_x_up', 'unit': ''}), OrderedDict({'description': 'Progress x down', 'dtype': '<u1', 'field_name': 'progress_x_down', 'unit': ''}), OrderedDict({'description': 'Progress y up', 'dtype': '<u1', 'field_name': 'progress_y_up', 'unit': ''}), OrderedDict({'description': 'Progress y down', 'dtype': '<u1', 'field_name': 'progress_y_down', 'unit': ''}), OrderedDict({'description': 'Progress z up', 'dtype': '<u1', 'field_name': 'progress_z_up', 'unit': ''}), OrderedDict({'description': 'Progress z down', 'dtype': '<u1', 'field_name': 'progress_z_down', 'unit': ''}), OrderedDict({'description': 'Progress thruster', 'dtype': '<u1', 'field_name': 'progress_thruster', 'unit': ''})]}), OrderedDict({'name': 'thicknessgauge', 'message_type': '3', 'fields': [OrderedDict({'description': 'Protocol version', 'dtype': '<u1', 'field_name': 'version', 'unit': '', 'init': '2'}), OrderedDict({'description': 'Command type', 'dtype': '<u1', 'field_name': 'command_type', 'unit': '', 'init': '3'}), OrderedDict({'description': 'Thickness', 'dtype': '<f8', 'field_name': 'thickness_measurement', 'unit': 'm'}), OrderedDict({'description': 'Echo count', 'dtype': '<u1', 'field_name': 'echo_count', 'unit': ''}), OrderedDict({'description': 'Sound velocity', 'dtype': '<i2', 'field_name': 'sound_velocity', 'unit': 'm/s'}), OrderedDict({'description': 'Valid measurement', 'dtype': '<u1', 'field_name': 'valid_measurement', 'unit': ''})]})]})]

