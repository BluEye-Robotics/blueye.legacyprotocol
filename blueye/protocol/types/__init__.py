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

from .aquatroll import (
    AquaTrollParameterBlock,
    AquaTrollSensorMetadata,
    AquaTrollSensorMetadataArray,
    AquaTrollProbeMetadata,
    AquaTrollSensorParameters,
    AquaTrollSensorParametersArray,
    SetAquaTrollParameterUnit,
    SetAquaTrollConnectionStatus,
    Type,
    AquaTrollDevice,
    AquaTrollQuality,
    AquaTrollParameter,
    AquaTrollUnit,
    AquaTrollSensor,
    AquaTrollSensorStatus,
    AquaTrollDeviceStatus,
)
from .message_formats import (
    BinlogRecord,
    MotionInput,
    Lights,
    Laser,
    LatLongPosition,
    ConnectionDuration,
    AutoHeadingState,
    AutoDepthState,
    AutoAltitudeState,
    StationKeepingState,
    WeatherVaningState,
    AutoPilotSurgeYawState,
    AutoPilotHeaveState,
    ControlMode,
    TiltStabilizationState,
    SystemTime,
    GripperVelocities,
    ClientInfo,
    ConnectedClient,
    RecordState,
    TimeLapseState,
    WaterDensity,
    PingerConfiguration,
    WaterTemperature,
    CPUTemperature,
    CanisterTemperature,
    CanisterHumidity,
    Battery,
    BatteryBQ40Z50,
    Attitude,
    Altitude,
    ForwardDistance,
    PositionEstimate,
    ResetPositionSettings,
    Depth,
    Reference,
    Notification,
    ControlForce,
    ControllerHealth,
    DiveTime,
    RecordOn,
    StorageSpace,
    CalibrationState,
    IperfStatus,
    NStreamers,
    TiltAngle,
    TiltVelocity,
    DroneInfo,
    ErrorFlags,
    CameraParameters,
    OverlayParameters,
    NavigationSensorStatus,
    GuestPortDevice,
    GuestPortDeviceList,
    GuestPortConnectorInfo,
    GuestPortInfo,
    GuestPortRestartInfo,
    ThicknessGauge,
    CpProbe,
    GenericServo,
    MultibeamServo,
    GuestPortCurrent,
    Vector3,
    Imu,
    MedusaSpectrometerData,
    IntervalType,
    HeadingSource,
    ResetCoordinateSource,
    NotificationType,
    NotificationLevel,
    Model,
    PressureSensorType,
    Resolution,
    Framerate,
    Camera,
    TemperatureUnit,
    LogoType,
    DepthUnit,
    ThicknessUnit,
    FontSize,
    GuestPortDeviceID,
    GuestPortNumber,
    NavigationSensorID,
    GuestPortDetachStatus,
    GuestPortError,
)
from .mission_planning import (
    Mission,
    Instruction,
    DepthSetPoint,
    Waypoint,
    ControlModeCommand,
    WaypointCommand,
    DepthSetPointCommand,
    TiltMainCameraCommand,
    TiltMultibeamCommand,
    WaitForCommand,
    CameraCommand,
    GoToSurfaceCommand,
    GoToSeabedCommand,
    GoToHomeCommand,
    PathSegment,
    ReferenceAutoPilot,
    MissionStatus,
    DepthZeroReference,
    ControlModeVertical,
    ControlModeHorizontal,
    CameraAction,
    InstructionType,
    MissionState,
)
from .req_rep import (
    SetOverlayParametersReq,
    SetOverlayParametersRep,
    GetOverlayParametersReq,
    GetOverlayParametersRep,
    SetCameraParametersReq,
    SetCameraParametersRep,
    GetCameraParametersReq,
    GetCameraParametersRep,
    SyncTimeReq,
    SyncTimeRep,
    PingReq,
    PingRep,
    SetThicknessGaugeParametersReq,
    SetThicknessGaugeParametersRep,
    ConnectClientReq,
    ConnectClientRep,
    DisconnectClientReq,
    DisconnectClientRep,
    GetBatteryReq,
    GetBatteryRep,
    SetMissionReq,
    SetMissionRep,
    GetMissionReq,
    GetMissionRep,
    SetInstructionUpdateReq,
    SetInstructionUpdateRep,
    SetPubFrequencyReq,
    SetPubFrequencyRep,
    GetTelemetryReq,
    GetTelemetryRep,
)
from .telemetry import (
    AttitudeTel,
    AltitudeTel,
    ForwardDistanceTel,
    PositionEstimateTel,
    DepthTel,
    ReferenceTel,
    ReferenceAutoPilotTel,
    MissionStatusTel,
    NotificationTel,
    ControlForceTel,
    ControllerHealthTel,
    LightsTel,
    GuestPortLightsTel,
    LaserTel,
    PilotGPSPositionTel,
    RecordStateTel,
    TimeLapseStateTel,
    BatteryTel,
    BatteryBQ40Z50Tel,
    DiveTimeTel,
    DroneTimeTel,
    WaterTemperatureTel,
    CPUTemperatureTel,
    CanisterTopTemperatureTel,
    CanisterBottomTemperatureTel,
    CanisterTopHumidityTel,
    CanisterBottomHumidityTel,
    VideoStorageSpaceTel,
    DataStorageSpaceTel,
    CalibrationStateTel,
    TiltStabilizationTel,
    IperfTel,
    NStreamersTel,
    TiltAngleTel,
    DroneInfoTel,
    ErrorFlagsTel,
    ControlModeTel,
    ThicknessGaugeTel,
    CpProbeTel,
    AquaTrollProbeMetadataTel,
    AquaTrollSensorMetadataTel,
    AquaTrollSensorParametersTel,
    ConnectedClientsTel,
    GenericServoTel,
    MultibeamServoTel,
    GuestPortCurrentTel,
    CalibratedImuTel,
    Imu1Tel,
    Imu2Tel,
    MedusaSpectrometerDataTel,
)
from .control import (
    MotionInputCtrl,
    TiltVelocityCtrl,
    LightsCtrl,
    GuestportLightsCtrl,
    LaserCtrl,
    PilotGPSPositionCtrl,
    WatchdogCtrl,
    RecordCtrl,
    TakePictureCtrl,
    StartCalibrationCtrl,
    CancelCalibrationCtrl,
    FinishCalibrationCtrl,
    AutoHeadingCtrl,
    AutoDepthCtrl,
    AutoAltitudeCtrl,
    StationKeepingCtrl,
    WeatherVaningCtrl,
    AutoPilotSurgeYawCtrl,
    AutoPilotHeaveCtrl,
    RunMissionCtrl,
    PauseMissionCtrl,
    ClearMissionCtrl,
    ResetPositionCtrl,
    ResetOdometerCtrl,
    TiltStabilizationCtrl,
    WaterDensityCtrl,
    PingerConfigurationCtrl,
    SystemTimeCtrl,
    GripperCtrl,
    GenericServoCtrl,
    MultibeamServoCtrl,
    DeactivateGuestPortsCtrl,
    ActivateGuestPortsCtrl,
    RestartGuestPortsCtrl,
    SetAquaTrollParameterUnitCtrl,
    SetAquaTrollConnectionStatusCtrl,
)

__all__ = (
    'AquaTrollParameterBlock',
    'AquaTrollSensorMetadata',
    'AquaTrollSensorMetadataArray',
    'AquaTrollProbeMetadata',
    'AquaTrollSensorParameters',
    'AquaTrollSensorParametersArray',
    'SetAquaTrollParameterUnit',
    'SetAquaTrollConnectionStatus',
    'Type',
    'AquaTrollDevice',
    'AquaTrollQuality',
    'AquaTrollParameter',
    'AquaTrollUnit',
    'AquaTrollSensor',
    'AquaTrollSensorStatus',
    'AquaTrollDeviceStatus',
    'BinlogRecord',
    'MotionInput',
    'Lights',
    'Laser',
    'LatLongPosition',
    'ConnectionDuration',
    'AutoHeadingState',
    'AutoDepthState',
    'AutoAltitudeState',
    'StationKeepingState',
    'WeatherVaningState',
    'AutoPilotSurgeYawState',
    'AutoPilotHeaveState',
    'ControlMode',
    'TiltStabilizationState',
    'SystemTime',
    'GripperVelocities',
    'ClientInfo',
    'ConnectedClient',
    'RecordState',
    'TimeLapseState',
    'WaterDensity',
    'PingerConfiguration',
    'WaterTemperature',
    'CPUTemperature',
    'CanisterTemperature',
    'CanisterHumidity',
    'Battery',
    'BatteryBQ40Z50',
    'Attitude',
    'Altitude',
    'ForwardDistance',
    'PositionEstimate',
    'ResetPositionSettings',
    'Depth',
    'Reference',
    'Notification',
    'ControlForce',
    'ControllerHealth',
    'DiveTime',
    'RecordOn',
    'StorageSpace',
    'CalibrationState',
    'IperfStatus',
    'NStreamers',
    'TiltAngle',
    'TiltVelocity',
    'DroneInfo',
    'ErrorFlags',
    'CameraParameters',
    'OverlayParameters',
    'NavigationSensorStatus',
    'GuestPortDevice',
    'GuestPortDeviceList',
    'GuestPortConnectorInfo',
    'GuestPortInfo',
    'GuestPortRestartInfo',
    'ThicknessGauge',
    'CpProbe',
    'GenericServo',
    'MultibeamServo',
    'GuestPortCurrent',
    'Vector3',
    'Imu',
    'MedusaSpectrometerData',
    'IntervalType',
    'HeadingSource',
    'ResetCoordinateSource',
    'NotificationType',
    'NotificationLevel',
    'Model',
    'PressureSensorType',
    'Resolution',
    'Framerate',
    'Camera',
    'TemperatureUnit',
    'LogoType',
    'DepthUnit',
    'ThicknessUnit',
    'FontSize',
    'GuestPortDeviceID',
    'GuestPortNumber',
    'NavigationSensorID',
    'GuestPortDetachStatus',
    'GuestPortError',
    'Mission',
    'Instruction',
    'DepthSetPoint',
    'Waypoint',
    'ControlModeCommand',
    'WaypointCommand',
    'DepthSetPointCommand',
    'TiltMainCameraCommand',
    'TiltMultibeamCommand',
    'WaitForCommand',
    'CameraCommand',
    'GoToSurfaceCommand',
    'GoToSeabedCommand',
    'GoToHomeCommand',
    'PathSegment',
    'ReferenceAutoPilot',
    'MissionStatus',
    'DepthZeroReference',
    'ControlModeVertical',
    'ControlModeHorizontal',
    'CameraAction',
    'InstructionType',
    'MissionState',
    'SetOverlayParametersReq',
    'SetOverlayParametersRep',
    'GetOverlayParametersReq',
    'GetOverlayParametersRep',
    'SetCameraParametersReq',
    'SetCameraParametersRep',
    'GetCameraParametersReq',
    'GetCameraParametersRep',
    'SyncTimeReq',
    'SyncTimeRep',
    'PingReq',
    'PingRep',
    'SetThicknessGaugeParametersReq',
    'SetThicknessGaugeParametersRep',
    'ConnectClientReq',
    'ConnectClientRep',
    'DisconnectClientReq',
    'DisconnectClientRep',
    'GetBatteryReq',
    'GetBatteryRep',
    'SetMissionReq',
    'SetMissionRep',
    'GetMissionReq',
    'GetMissionRep',
    'SetInstructionUpdateReq',
    'SetInstructionUpdateRep',
    'SetPubFrequencyReq',
    'SetPubFrequencyRep',
    'GetTelemetryReq',
    'GetTelemetryRep',
    'AttitudeTel',
    'AltitudeTel',
    'ForwardDistanceTel',
    'PositionEstimateTel',
    'DepthTel',
    'ReferenceTel',
    'ReferenceAutoPilotTel',
    'MissionStatusTel',
    'NotificationTel',
    'ControlForceTel',
    'ControllerHealthTel',
    'LightsTel',
    'GuestPortLightsTel',
    'LaserTel',
    'PilotGPSPositionTel',
    'RecordStateTel',
    'TimeLapseStateTel',
    'BatteryTel',
    'BatteryBQ40Z50Tel',
    'DiveTimeTel',
    'DroneTimeTel',
    'WaterTemperatureTel',
    'CPUTemperatureTel',
    'CanisterTopTemperatureTel',
    'CanisterBottomTemperatureTel',
    'CanisterTopHumidityTel',
    'CanisterBottomHumidityTel',
    'VideoStorageSpaceTel',
    'DataStorageSpaceTel',
    'CalibrationStateTel',
    'TiltStabilizationTel',
    'IperfTel',
    'NStreamersTel',
    'TiltAngleTel',
    'DroneInfoTel',
    'ErrorFlagsTel',
    'ControlModeTel',
    'ThicknessGaugeTel',
    'CpProbeTel',
    'AquaTrollProbeMetadataTel',
    'AquaTrollSensorMetadataTel',
    'AquaTrollSensorParametersTel',
    'ConnectedClientsTel',
    'GenericServoTel',
    'MultibeamServoTel',
    'GuestPortCurrentTel',
    'CalibratedImuTel',
    'Imu1Tel',
    'Imu2Tel',
    'MedusaSpectrometerDataTel',
    'MotionInputCtrl',
    'TiltVelocityCtrl',
    'LightsCtrl',
    'GuestportLightsCtrl',
    'LaserCtrl',
    'PilotGPSPositionCtrl',
    'WatchdogCtrl',
    'RecordCtrl',
    'TakePictureCtrl',
    'StartCalibrationCtrl',
    'CancelCalibrationCtrl',
    'FinishCalibrationCtrl',
    'AutoHeadingCtrl',
    'AutoDepthCtrl',
    'AutoAltitudeCtrl',
    'StationKeepingCtrl',
    'WeatherVaningCtrl',
    'AutoPilotSurgeYawCtrl',
    'AutoPilotHeaveCtrl',
    'RunMissionCtrl',
    'PauseMissionCtrl',
    'ClearMissionCtrl',
    'ResetPositionCtrl',
    'ResetOdometerCtrl',
    'TiltStabilizationCtrl',
    'WaterDensityCtrl',
    'PingerConfigurationCtrl',
    'SystemTimeCtrl',
    'GripperCtrl',
    'GenericServoCtrl',
    'MultibeamServoCtrl',
    'DeactivateGuestPortsCtrl',
    'ActivateGuestPortsCtrl',
    'RestartGuestPortsCtrl',
    'SetAquaTrollParameterUnitCtrl',
    'SetAquaTrollConnectionStatusCtrl',
)
