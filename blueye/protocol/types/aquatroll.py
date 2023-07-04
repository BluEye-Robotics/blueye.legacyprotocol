# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.protobuf import timestamp_pb2 as gp_timestamp  # type: ignore


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'AquaTrollType',
        'AquaTrollDevice',
        'AquaTrollQuality',
        'AquaTrollParameter',
        'AquaTrollUnit',
        'AquaTrollSensor',
        'AquaTrollParameterBlock',
        'AquaTrollSensorMetadata',
        'AquaTrollSensorMetadataArray',
        'AquaTrollProbeMetadata',
        'AquaTrollSensorParameters',
        'AquaTrollSensorParametersArray',
    },
)


class AquaTrollType(proto.Enum):
    r"""-

    Aqua Troll Type IDs
    """
    AQUA_TROLL_TYPE_UNSPECIFIED = 0
    AQUA_TROLL_TYPE_SHORT = 1
    AQUA_TROLL_TYPE_UNSIGNED_SHORT = 2
    AQUA_TROLL_TYPE_LONG = 3
    AQUA_TROLL_TYPE_UNSIGNED_LONG = 4
    AQUA_TROLL_TYPE_FLOAT = 5
    AQUA_TROLL_TYPE_DOUBLE = 6
    AQUA_TROLL_TYPE_CHARACTER = 7
    AQUA_TROLL_TYPE_STRING = 8
    AQUA_TROLL_TYPE_TIME = 9


class AquaTrollDevice(proto.Enum):
    r"""-

    Aqua Troll Device IDs
    """
    AQUA_TROLL_DEVICE_UNSPECIFIED = 0
    AQUA_TROLL_DEVICE_LEVEL_TROLL_500 = 1
    AQUA_TROLL_DEVICE_LEVEL_TROLL_700 = 2
    AQUA_TROLL_DEVICE_BAROTROLL_500 = 3
    AQUA_TROLL_DEVICE_LEVEL_TROLL_300 = 4
    AQUA_TROLL_DEVICE_AQUA_TROLL_200 = 5
    AQUA_TROLL_DEVICE_AQUA_TROLL_600 = 7
    AQUA_TROLL_DEVICE_AQUA_TROLL_100 = 10
    AQUA_TROLL_DEVICE_FLOW_TROLL_500 = 11
    AQUA_TROLL_DEVICE_RDO_PRO = 12
    AQUA_TROLL_DEVICE_RUGGED_TROLL_200 = 16
    AQUA_TROLL_DEVICE_RUGGED_BAROTROLL = 17
    AQUA_TROLL_DEVICE_AQUA_TROLL_400 = 18
    AQUA_TROLL_DEVICE_RDO_TITAN = 19
    AQUA_TROLL_DEVICE_SMARTROLL = 21
    AQUA_TROLL_DEVICE_AQUA_TROLL_600_VENTED = 26
    AQUA_TROLL_DEVICE_LEVEL_TROLL_400 = 30
    AQUA_TROLL_DEVICE_RDO_PRO_X = 31
    AQUA_TROLL_DEVICE_AQUA_TROLL_500 = 33
    AQUA_TROLL_DEVICE_AQUA_TROLL_500_VENTED = 34


class AquaTrollQuality(proto.Enum):
    r"""protolint:disable ENUM_FIELD_NAMES_ZERO_VALUE_END_WITH"""
    AQUA_TROLL_QUALITY_NORMAL = 0
    AQUA_TROLL_QUALITY_USER_CAL_EXPIRED = 1
    AQUA_TROLL_QUALITY_FACTORY_CAL_EXPIRED = 2
    AQUA_TROLL_QUALITY_ERROR = 3
    AQUA_TROLL_QUALITY_WARM_UP = 4
    AQUA_TROLL_QUALITY_SENSOR_WARNING = 5
    AQUA_TROLL_QUALITY_CALIBRATING = 6
    AQUA_TROLL_QUALITY_OFF_LINE = 7


class AquaTrollParameter(proto.Enum):
    r"""-

    Aqua Troll Parameter IDs
    """
    AQUA_TROLL_PARAMETER_UNSPECIFIED = 0
    AQUA_TROLL_PARAMETER_TEMPERATURE = 1
    AQUA_TROLL_PARAMETER_PRESSURE = 2
    AQUA_TROLL_PARAMETER_DEPTH = 3
    AQUA_TROLL_PARAMETER_LEVEL_DEPTH_TO_WATER = 4
    AQUA_TROLL_PARAMETER_LEVEL_SURFACE_ELEVATION = 5
    AQUA_TROLL_PARAMETER_LATITUDE = 6
    AQUA_TROLL_PARAMETER_LONGITUDE = 7
    AQUA_TROLL_PARAMETER_ELEVATION = 8
    AQUA_TROLL_PARAMETER_ACTUAL_CONDUCTIVITY = 9
    AQUA_TROLL_PARAMETER_SPECIFIC_CONDUCTIVITY = 10
    AQUA_TROLL_PARAMETER_RESISTIVITY = 11
    AQUA_TROLL_PARAMETER_SALINITY = 12
    AQUA_TROLL_PARAMETER_TOTAL_DISSOLVED_SOLIDS = 13
    AQUA_TROLL_PARAMETER_DENSITY_OF_WATER = 14
    AQUA_TROLL_PARAMETER_SPECIFIC_GRAVITY = 15
    AQUA_TROLL_PARAMETER_BAROMETRIC_PRESSURE = 16
    AQUA_TROLL_PARAMETER_PH = 17
    AQUA_TROLL_PARAMETER_PH_MV = 18
    AQUA_TROLL_PARAMETER_ORP = 19
    AQUA_TROLL_PARAMETER_DISSOLVED_OXYGEN_CONCENTRATION = 20
    AQUA_TROLL_PARAMETER_DISSOLVED_OXYGEN_SATURATION = 21
    AQUA_TROLL_PARAMETER_NITRATE = 22
    AQUA_TROLL_PARAMETER_AMMONIUM = 23
    AQUA_TROLL_PARAMETER_CHLORIDE = 24
    AQUA_TROLL_PARAMETER_TURBIDITY = 25
    AQUA_TROLL_PARAMETER_BATTERY_VOLTAGE = 26
    AQUA_TROLL_PARAMETER_HEAD = 27
    AQUA_TROLL_PARAMETER_FLOW = 28
    AQUA_TROLL_PARAMETER_TOTAL_FLOW = 29
    AQUA_TROLL_PARAMETER_OXYGEN_PARTIAL_PRESSURE = 30
    AQUA_TROLL_PARAMETER_TOTAL_SUSPENDED_SOLIDS = 31
    AQUA_TROLL_PARAMETER_EXTERNAL_VOLTAGE = 32
    AQUA_TROLL_PARAMETER_BATTERY_CAPACITY_REMAINING = 33
    AQUA_TROLL_PARAMETER_RHODAMINE_WT_CONCENTRATION = 34
    AQUA_TROLL_PARAMETER_RHODAMINE_WT_FLUORESCENCE_INTENSITY = 35
    AQUA_TROLL_PARAMETER_CHLORIDE_CL_MV = 36
    AQUA_TROLL_PARAMETER_NITRATE_AS_NITROGEN_NO3_N_CONCENTRATION = 37
    AQUA_TROLL_PARAMETER_NITRATE_NO3_MV = 38
    AQUA_TROLL_PARAMETER_AMMONIUM_AS_NITROGEN_NH4_PLUS_N_CONCENTRATION = 39
    AQUA_TROLL_PARAMETER_AMMONIUM_NH4_MV = 40
    AQUA_TROLL_PARAMETER_AMMONIA_AS_NITROGEN_NH3_N_CONCENTRATION = 41
    AQUA_TROLL_PARAMETER_TOTAL_AMMONIA_AS_NITROGEN_NH3_N_CONCENTRATION = 42
    AQUA_TROLL_PARAMETER_EH = 48
    AQUA_TROLL_PARAMETER_VELOCITY = 49
    AQUA_TROLL_PARAMETER_CHLOROPHYLL_A_CONCENTRATION = 50
    AQUA_TROLL_PARAMETER_CHLOROPHYLL_A_FLUORESCENCE_INTENSITY = 51
    AQUA_TROLL_PARAMETER_BLUE_GREEN_ALGAE_PHYCOCYANIN_CONCENTRATION = 54
    AQUA_TROLL_PARAMETER_BLUE_GREEN_ALGAE_PHYCOCYANIN_FLUORESCENCE_INTENSITY = 55
    AQUA_TROLL_PARAMETER_BLUE_GREEN_ALGAE_PHYCOERYTHRIN_CONCENTRATION = 58
    AQUA_TROLL_PARAMETER_BLUE_GREEN_ALGAE_PHYCOERYTHRIN_FLUORESCENCE_INTENSITY = 59
    AQUA_TROLL_PARAMETER_FLUORESCEIN_WT_CONCENTRATION = 67
    AQUA_TROLL_PARAMETER_FLUORESCEIN_WT_FLUORESCENCE_INTENSITY = 68
    AQUA_TROLL_PARAMETER_FLUORESCENT_DISSOLVED_ORGANIC_MATTER_CONCENTRATION = 69
    AQUA_TROLL_PARAMETER_FLUORESCENT_DISSOLVED_ORGANIC_MATTER_FLUORESCENCE_INTENSITY = 70
    AQUA_TROLL_PARAMETER_CRUDE_OIL_CONCENTRATION = 80
    AQUA_TROLL_PARAMETER_CRUDE_OIL_FLUORESCENCE_INTENSITY = 81
    AQUA_TROLL_PARAMETER_COLORED_DISSOLVED_ORGANIC_MATTER_CONCENTRATION = 87


class AquaTrollUnit(proto.Enum):
    r"""-

    Aqua Troll Unit IDs
    """
    AQUA_TROLL_UNIT_UNSPECIFIED = 0
    AQUA_TROLL_UNIT_TEMP_CELSIUS = 1
    AQUA_TROLL_UNIT_TEMP_FARENHEIT = 2
    AQUA_TROLL_UNIT_TEMP_KELVIN = 3
    AQUA_TROLL_UNIT_POUNDS_PER_SQUARE_INCH = 17
    AQUA_TROLL_UNIT_PASCALS = 18
    AQUA_TROLL_UNIT_KILOPASCALS = 19
    AQUA_TROLL_UNIT_BARS = 20
    AQUA_TROLL_UNIT_MILLIBARS = 21
    AQUA_TROLL_UNIT_MILLIMETERS_OF_MERCURY = 22
    AQUA_TROLL_UNIT_INCHES_OF_MERCURY = 23
    AQUA_TROLL_UNIT_CENTIMETERS_OF_WATER = 24
    AQUA_TROLL_UNIT_INCHES_OF_WATER = 25
    AQUA_TROLL_UNIT_TORR = 26
    AQUA_TROLL_UNIT_STANDARD_ATMOSPHERE = 27
    AQUA_TROLL_UNIT_MILLIMETERS = 33
    AQUA_TROLL_UNIT_CENTIMETERS = 34
    AQUA_TROLL_UNIT_METERS = 35
    AQUA_TROLL_UNIT_KILOMETER = 36
    AQUA_TROLL_UNIT_INCHES = 37
    AQUA_TROLL_UNIT_FEET = 38
    AQUA_TROLL_UNIT_DEGREES = 49
    AQUA_TROLL_UNIT_MINUTES = 50
    AQUA_TROLL_UNIT_SECONDS = 51
    AQUA_TROLL_UNIT_MICROSIEMENS_PER_CENTIMETER = 65
    AQUA_TROLL_UNIT_MILLISIEMENS_PER_CENTIMETER = 66
    AQUA_TROLL_UNIT_OHM_CENTIMETERS = 81
    AQUA_TROLL_UNIT_PRACTICAL_SALINITY_UNITS = 97
    AQUA_TROLL_UNIT_PARTS_PER_THOUSAND_SALINITY = 98
    AQUA_TROLL_UNIT_PARTS_PER_MILLION = 113
    AQUA_TROLL_UNIT_PARTS_PER_THOUSAND = 114
    AQUA_TROLL_UNIT_PARTS_PER_MILLION_NITROGEN = 115
    AQUA_TROLL_UNIT_PARTS_PER_MILLION_CHLORIDE = 116
    AQUA_TROLL_UNIT_MILLIGRAMS_PER_LITER = 117
    AQUA_TROLL_UNIT_MICROGRAMS_PER_LITER = 118
    AQUA_TROLL_UNIT_MICROMOLES_PER_LITER_DEPRECATED = 119
    AQUA_TROLL_UNIT_GRAMS_PER_LITER = 120
    AQUA_TROLL_UNIT_PARTS_PER_BILLION = 121
    AQUA_TROLL_UNIT_GRAMS_PER_CUBIC_CENTIMETER = 129
    AQUA_TROLL_UNIT_PH = 145
    AQUA_TROLL_UNIT_MICRO_VOLTS = 161
    AQUA_TROLL_UNIT_MILLI_VOLTS = 162
    AQUA_TROLL_UNIT_VOLTS = 163
    AQUA_TROLL_UNIT_PERCENT_SATURATION = 177
    AQUA_TROLL_UNIT_FORMAZIN_NEPHELOMETRIC_UNITS = 193
    AQUA_TROLL_UNIT_NEPHELOMETRIC_TURBIDITY_UNITS = 194
    AQUA_TROLL_UNIT_FORMAZIN_TURBIDITY_UNITS = 195
    AQUA_TROLL_UNIT_CUBIC_FEET_PER_SECOND = 209
    AQUA_TROLL_UNIT_CUBIC_FEET_PER_MINUTE = 210
    AQUA_TROLL_UNIT_CUBIC_FEET_PER_HOUR = 211
    AQUA_TROLL_UNIT_CUBIC_FEET_PER_DAY = 212
    AQUA_TROLL_UNIT_GALLONS_PER_SECOND = 213
    AQUA_TROLL_UNIT_GALLONS_PER_MINUTE = 214
    AQUA_TROLL_UNIT_GALLONS_PER_HOUR = 215
    AQUA_TROLL_UNIT_MILLIONS_OF_GALLONS_PER_DAY = 216
    AQUA_TROLL_UNIT_CUBIC_METERS_PER_SECOND = 217
    AQUA_TROLL_UNIT_CUBIC_METERS_PER_MINUTE = 218
    AQUA_TROLL_UNIT_CUBIC_METERS_PER_HOUR = 219
    AQUA_TROLL_UNIT_CUBIC_METERS_PER_DAY = 220
    AQUA_TROLL_UNIT_LITERS_PER_SECOND = 221
    AQUA_TROLL_UNIT_MILLIONS_OF_LITERS_PER_DAY = 222
    AQUA_TROLL_UNIT_MILLILITERS_PER_MINUTE = 223
    AQUA_TROLL_UNIT_THOUSANDS_OF_LITERS_PER_DAY = 224
    AQUA_TROLL_UNIT_CUBIC_FEET = 225
    AQUA_TROLL_UNIT_GALLONS = 226
    AQUA_TROLL_UNIT_MILLIONS_OF_GALLONS = 227
    AQUA_TROLL_UNIT_CUBIC_METERS = 228
    AQUA_TROLL_UNIT_LITERS = 229
    AQUA_TROLL_UNIT_ACRE_FEET = 230
    AQUA_TROLL_UNIT_MILLILITERS = 231
    AQUA_TROLL_UNIT_MILLIONS_OF_LITERS = 232
    AQUA_TROLL_UNIT_THOUSANDS_OF_LITERS = 233
    AQUA_TROLL_UNIT_ACRE_INCHES = 234
    AQUA_TROLL_UNIT_PERCENT = 241
    AQUA_TROLL_UNIT_RELATIVE_FLUORESCENCE_UNITS = 257
    AQUA_TROLL_UNIT_MILLILITERS_PER_SECOND = 273
    AQUA_TROLL_UNIT_MILLILITERS_PER_HOUR = 274
    AQUA_TROLL_UNIT_LITERS_PER_MINUTE = 275
    AQUA_TROLL_UNIT_LITERS_PER_HOUR = 276
    AQUA_TROLL_UNIT_MICROAMPS = 289
    AQUA_TROLL_UNIT_MILLIAMPS = 290
    AQUA_TROLL_UNIT_AMPS = 291
    AQUA_TROLL_UNIT_FEET_PER_SECOND = 305
    AQUA_TROLL_UNIT_METERS_PER_SECOND = 306


class AquaTrollSensor(proto.Enum):
    r"""-

    Aqua Troll Sensor IDs
    """
    AQUA_TROLL_SENSOR_UNSPECIFIED = 0
    AQUA_TROLL_SENSOR_TEMPERATURE = 1
    AQUA_TROLL_SENSOR_S5_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 2
    AQUA_TROLL_SENSOR_S15_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 3
    AQUA_TROLL_SENSOR_S30_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 4
    AQUA_TROLL_SENSOR_S100_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 5
    AQUA_TROLL_SENSOR_S300_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 6
    AQUA_TROLL_SENSOR_S500_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 7
    AQUA_TROLL_SENSOR_S1000_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 8
    AQUA_TROLL_SENSOR_S30_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 9
    AQUA_TROLL_SENSOR_S100_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 10
    AQUA_TROLL_SENSOR_S300_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 11
    AQUA_TROLL_SENSOR_S500_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_AND_TEMPERATURE = 12
    AQUA_TROLL_SENSOR_S30_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_TEMPERATURE = 13
    AQUA_TROLL_SENSOR_S5_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 14
    AQUA_TROLL_SENSOR_S15_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 15
    AQUA_TROLL_SENSOR_S30_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 16
    AQUA_TROLL_SENSOR_S100_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 17
    AQUA_TROLL_SENSOR_S300_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 18
    AQUA_TROLL_SENSOR_S500_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 19
    AQUA_TROLL_SENSOR_NOT_USED = 20
    AQUA_TROLL_SENSOR_S30_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 21
    AQUA_TROLL_SENSOR_S100_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 22
    AQUA_TROLL_SENSOR_S300_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 23
    AQUA_TROLL_SENSOR_S500_PSI_FULL_SCALE_ABSOLUTE_PRESSURE_WITH_LEVEL_TEMPERATURE_AND_CONDUCTIVITY = 24
    AQUA_TROLL_SENSOR_S165_PSI_FULL_SCALE_ABSOLUTE_PRESSURE = 25
    AQUA_TROLL_SENSOR_PH_ANALOG_SENSOR = 26
    AQUA_TROLL_SENSOR_PH_ORP_ANALOG_SENSOR = 27
    AQUA_TROLL_SENSOR_DISSOLVED_OXYGEN_CLARK_CELL_ANALOG_SENSOR = 28
    AQUA_TROLL_SENSOR_NITRATE_ANALOG_SENSOR = 29
    AQUA_TROLL_SENSOR_AMMONIUM_ANALOG_SENSOR = 30
    AQUA_TROLL_SENSOR_CHLORIDE_ANALOG_SENSOR = 31
    AQUA_TROLL_SENSOR_S100_FOOT_FULL_SCALE_LEVEL_WITH_ABSOLUTE_PRESSURE_AND_TEMPERATURE = 32
    AQUA_TROLL_SENSOR_S250_FOOT_FULL_SCALE_LEVEL_WITH_ABSOLUTE_PRESSURE_AND_TEMPERATURE = 33
    AQUA_TROLL_SENSOR_S30_FOOT_FULL_SCALE_LEVEL_WITH_ABSOLUTE_PRESSURE_AND_TEMPERATURE = 34
    AQUA_TROLL_SENSOR_CONDUCTIVITY_AND_TEMPERATURE = 35
    AQUA_TROLL_SENSOR_S5_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_TEMPERATURE_HEAD_AND_FLOW = 36
    AQUA_TROLL_SENSOR_S15_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_TEMPERATURE_HEAD_AND_FLOW = 37
    AQUA_TROLL_SENSOR_S30_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_TEMPERATURE_HEAD_AND_FLOW = 38
    AQUA_TROLL_SENSOR_S100_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_TEMPERATURE_HEAD_AND_FLOW = 39
    AQUA_TROLL_SENSOR_S300_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_TEMPERATURE_HEAD_AND_FLOW = 40
    AQUA_TROLL_SENSOR_S500_PSI_FULL_SCALE_GAUGE_PRESSURE_WITH_TEMPERATURE_HEAD_AND_FLOW = 41
    AQUA_TROLL_SENSOR_OPTICAL_DISSOLVED_OXYGEN_WITH_TEMPERATURE = 42
    AQUA_TROLL_SENSOR_S1_BAR = 43
    AQUA_TROLL_SENSOR_S2_BAR = 44
    AQUA_TROLL_SENSOR_S5_BAR = 45
    AQUA_TROLL_SENSOR_TURBIDITY_SENSOR = 50
    AQUA_TROLL_SENSOR_TEMPERATURE_SENSOR = 55
    AQUA_TROLL_SENSOR_CONDUCTIVITY_SENSOR = 56
    AQUA_TROLL_SENSOR_RDO_SENSOR = 57
    AQUA_TROLL_SENSOR_PH_ORP_SENSOR = 58
    AQUA_TROLL_SENSOR_RHODAMINE_WT_SENSOR = 60
    AQUA_TROLL_SENSOR_CHLOROPHYLL_A_SENSOR = 62
    AQUA_TROLL_SENSOR_BLUE_GREEN_ALGAE_PHYCOCYANIN_SENSOR = 64
    AQUA_TROLL_SENSOR_BLUE_GREEN_ALGAE_PHYCOERYTHRIN_SENSOR = 65
    AQUA_TROLL_SENSOR_NITRATE_ISE_SENSOR = 70
    AQUA_TROLL_SENSOR_AMMONIUM_ISE_SENSOR = 71
    AQUA_TROLL_SENSOR_CHLORIDE_ISE_SENSOR = 72
    AQUA_TROLL_SENSOR_PROBE_PARAMETERS = 79


class AquaTrollParameterBlock(proto.Message):
    r"""-

    In-Situ Parameter Block

    Up to NUMBER_OF_SENSOR_PARAMETERS blocks may be part of a sensor

    Attributes:
        measured_value (float):

        parameter_id (blueye.protocol.types.AquaTrollParameter):

        units_id (blueye.protocol.types.AquaTrollUnit):

        data_quality_id (blueye.protocol.types.AquaTrollQuality):

        off_line_sentinel_value (float):

        available_units (Sequence[blueye.protocol.types.AquaTrollUnit]):

    """

    measured_value = proto.Field(proto.FLOAT, number=1)

    parameter_id = proto.Field(proto.ENUM, number=2,
        enum='AquaTrollParameter',
    )

    units_id = proto.Field(proto.ENUM, number=3,
        enum='AquaTrollUnit',
    )

    data_quality_id = proto.Field(proto.ENUM, number=4,
        enum='AquaTrollQuality',
    )

    off_line_sentinel_value = proto.Field(proto.FLOAT, number=5)

    available_units = proto.RepeatedField(proto.ENUM, number=6,
        enum='AquaTrollUnit',
    )


class AquaTrollSensorMetadata(proto.Message):
    r"""-

    In-Situ AquaTroll 500 sensor metadata

    (Mostly) static information about a connected sensor.

    Refer to Section 7 Sensor Common Registers in the In-Situ Modbus
    Communication Protocol

    Attributes:
        timestamp (google.protobuf.timestamp_pb2.Timestamp):

        sensor_id (blueye.protocol.types.AquaTrollSensor):

        sensor_serial_number (int):

        sensor_status (int):

        last_factory_calibration (google.protobuf.timestamp_pb2.Timestamp):

        next_factory_calibration (google.protobuf.timestamp_pb2.Timestamp):

        last_user_calibration (google.protobuf.timestamp_pb2.Timestamp):

        next_user_calibration (google.protobuf.timestamp_pb2.Timestamp):

        warm_up_time_in_milliseconds (int):

        fast_sample_rate_in_milliseconds (int):

        number_of_sensor_parameters (int):

        alarm_and_warning_parameter_number (int):

        alarm_and_warning_enable_bits (int):

        high_alarm_set_value (float):

        high_alarm_clear_value (float):

        high_warning_set_value (float):

        high_warning_clear_value (float):

        low_warning_clear_value (float):

        low_warning_set_value (float):

        low_alarm_clear_value (float):

        low_alarm_set_value (float):

        parameter_blocks (Sequence[blueye.protocol.types.AquaTrollParameterBlock]):

    """

    timestamp = proto.Field(proto.MESSAGE, number=1,
        message=gp_timestamp.Timestamp,
    )

    sensor_id = proto.Field(proto.ENUM, number=2,
        enum='AquaTrollSensor',
    )

    sensor_serial_number = proto.Field(proto.UINT32, number=3)

    sensor_status = proto.Field(proto.UINT32, number=4)

    last_factory_calibration = proto.Field(proto.MESSAGE, number=5,
        message=gp_timestamp.Timestamp,
    )

    next_factory_calibration = proto.Field(proto.MESSAGE, number=6,
        message=gp_timestamp.Timestamp,
    )

    last_user_calibration = proto.Field(proto.MESSAGE, number=7,
        message=gp_timestamp.Timestamp,
    )

    next_user_calibration = proto.Field(proto.MESSAGE, number=8,
        message=gp_timestamp.Timestamp,
    )

    warm_up_time_in_milliseconds = proto.Field(proto.UINT32, number=9)

    fast_sample_rate_in_milliseconds = proto.Field(proto.UINT32, number=10)

    number_of_sensor_parameters = proto.Field(proto.UINT32, number=11)

    alarm_and_warning_parameter_number = proto.Field(proto.UINT32, number=12)

    alarm_and_warning_enable_bits = proto.Field(proto.UINT32, number=13)

    high_alarm_set_value = proto.Field(proto.FLOAT, number=14)

    high_alarm_clear_value = proto.Field(proto.FLOAT, number=15)

    high_warning_set_value = proto.Field(proto.FLOAT, number=16)

    high_warning_clear_value = proto.Field(proto.FLOAT, number=17)

    low_warning_clear_value = proto.Field(proto.FLOAT, number=18)

    low_warning_set_value = proto.Field(proto.FLOAT, number=19)

    low_alarm_clear_value = proto.Field(proto.FLOAT, number=20)

    low_alarm_set_value = proto.Field(proto.FLOAT, number=21)

    parameter_blocks = proto.RepeatedField(proto.MESSAGE, number=22,
        message='AquaTrollParameterBlock',
    )


class AquaTrollSensorMetadataArray(proto.Message):
    r"""

    Attributes:
        timestamp (google.protobuf.timestamp_pb2.Timestamp):

        sensors (Sequence[blueye.protocol.types.AquaTrollSensorMetadata]):

    """

    timestamp = proto.Field(proto.MESSAGE, number=1,
        message=gp_timestamp.Timestamp,
    )

    sensors = proto.RepeatedField(proto.MESSAGE, number=2,
        message='AquaTrollSensorMetadata',
    )


class AquaTrollProbeMetadata(proto.Message):
    r"""

    Attributes:
        timestamp (google.protobuf.timestamp_pb2.Timestamp):

        register_map_template_version (int):

        device_id (blueye.protocol.types.AquaTrollDevice):

        device_serial_number (int):

        manufacture_date (google.protobuf.timestamp_pb2.Timestamp):

        firmware_version (int):

        boot_code_version (int):

        hardware_version (int):

        max_data_logs (int):

        total_data_log_memory (int):

        total_battery_ticks (int):

        last_battery_change (google.protobuf.timestamp_pb2.Timestamp):

        device_name (str):

        site_name (str):

        latitude_coordinate (float):

        longitude_coordinate (float):

        altitude_coordinate (float):

        current_time_utc (google.protobuf.timestamp_pb2.Timestamp):

        device_status (int):

        used_battery_ticks (int):

        used_data_log_memory (int):

        sensors (Sequence[blueye.protocol.types.AquaTrollSensor]):

    """

    timestamp = proto.Field(proto.MESSAGE, number=1,
        message=gp_timestamp.Timestamp,
    )

    register_map_template_version = proto.Field(proto.UINT32, number=2)

    device_id = proto.Field(proto.ENUM, number=3,
        enum='AquaTrollDevice',
    )

    device_serial_number = proto.Field(proto.UINT32, number=4)

    manufacture_date = proto.Field(proto.MESSAGE, number=5,
        message=gp_timestamp.Timestamp,
    )

    firmware_version = proto.Field(proto.UINT32, number=6)

    boot_code_version = proto.Field(proto.UINT32, number=7)

    hardware_version = proto.Field(proto.UINT32, number=8)

    max_data_logs = proto.Field(proto.UINT32, number=9)

    total_data_log_memory = proto.Field(proto.UINT32, number=10)

    total_battery_ticks = proto.Field(proto.UINT32, number=11)

    last_battery_change = proto.Field(proto.MESSAGE, number=12,
        message=gp_timestamp.Timestamp,
    )

    device_name = proto.Field(proto.STRING, number=13)

    site_name = proto.Field(proto.STRING, number=14)

    latitude_coordinate = proto.Field(proto.DOUBLE, number=15)

    longitude_coordinate = proto.Field(proto.DOUBLE, number=16)

    altitude_coordinate = proto.Field(proto.DOUBLE, number=17)

    current_time_utc = proto.Field(proto.MESSAGE, number=18,
        message=gp_timestamp.Timestamp,
    )

    device_status = proto.Field(proto.UINT32, number=19)

    used_battery_ticks = proto.Field(proto.UINT32, number=20)

    used_data_log_memory = proto.Field(proto.UINT32, number=21)

    sensors = proto.RepeatedField(proto.ENUM, number=22,
        enum='AquaTrollSensor',
    )


class AquaTrollSensorParameters(proto.Message):
    r"""

    Attributes:
        sensor_id (blueye.protocol.types.AquaTrollSensor):

        parameter_blocks (Sequence[blueye.protocol.types.AquaTrollParameterBlock]):

    """

    sensor_id = proto.Field(proto.ENUM, number=2,
        enum='AquaTrollSensor',
    )

    parameter_blocks = proto.RepeatedField(proto.MESSAGE, number=3,
        message='AquaTrollParameterBlock',
    )


class AquaTrollSensorParametersArray(proto.Message):
    r"""

    Attributes:
        timestamp (google.protobuf.timestamp_pb2.Timestamp):

        sensors (Sequence[blueye.protocol.types.AquaTrollSensorParameters]):

    """

    timestamp = proto.Field(proto.MESSAGE, number=1,
        message=gp_timestamp.Timestamp,
    )

    sensors = proto.RepeatedField(proto.MESSAGE, number=2,
        message='AquaTrollSensorParameters',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
