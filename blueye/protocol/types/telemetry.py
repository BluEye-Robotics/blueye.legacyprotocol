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


from blueye.protocol.types import message_formats


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'AttitudeTel',
        'AltitudeTel',
        'ForwardDistanceTel',
        'PositionEstimateTel',
        'DepthTel',
        'ReferenceTel',
        'ControllerHealthTel',
        'LightsTel',
        'GuestPortLightsTel',
        'PilotGPSPositionTel',
        'RecordStateTel',
        'BatteryTel',
        'BatteryBQ40Z50Tel',
        'DiveTimeTel',
        'DroneTimeTel',
        'WaterTemperatureTel',
        'CPUTemperatureTel',
        'CanisterTemperatureTel',
        'CanisterHumidityTel',
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
        'ConnectedClientsTel',
    },
)


class AttitudeTel(proto.Message):
    r"""-

    Receive the current attitude of the drone.

    Attributes:
        attitude (blueye.protocol.types.Attitude):
            The attitude of the drone.
    """

    attitude = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Attitude,
    )


class AltitudeTel(proto.Message):
    r"""-

    Receive the current altitude of the drone.

    Attributes:
        altitude (blueye.protocol.types.Altitude):
            The altitude of the drone.
    """

    altitude = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Altitude,
    )


class ForwardDistanceTel(proto.Message):
    r"""

    Attributes:
        forward_distance (blueye.protocol.types.ForwardDistance):

    """

    forward_distance = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.ForwardDistance,
    )


class PositionEstimateTel(proto.Message):
    r"""

    Attributes:
        position_estimate (blueye.protocol.types.PositionEstimate):

    """

    position_estimate = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.PositionEstimate,
    )


class DepthTel(proto.Message):
    r"""

    Attributes:
        depth (blueye.protocol.types.Depth):

    """

    depth = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Depth,
    )


class ReferenceTel(proto.Message):
    r"""

    Attributes:
        reference (blueye.protocol.types.Reference):

    """

    reference = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Reference,
    )


class ControllerHealthTel(proto.Message):
    r"""

    Attributes:
        controller_health (blueye.protocol.types.ControllerHealth):

    """

    controller_health = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.ControllerHealth,
    )


class LightsTel(proto.Message):
    r"""

    Attributes:
        lights (blueye.protocol.types.Lights):

    """

    lights = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Lights,
    )


class GuestPortLightsTel(proto.Message):
    r"""

    Attributes:
        lights (blueye.protocol.types.Lights):

    """

    lights = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Lights,
    )


class PilotGPSPositionTel(proto.Message):
    r"""

    Attributes:
        position (blueye.protocol.types.LatLongPosition):

    """

    position = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.LatLongPosition,
    )


class RecordStateTel(proto.Message):
    r"""

    Attributes:
        record_state (blueye.protocol.types.RecordState):

    """

    record_state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.RecordState,
    )


class BatteryTel(proto.Message):
    r"""

    Attributes:
        battery (blueye.protocol.types.Battery):

    """

    battery = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Battery,
    )


class BatteryBQ40Z50Tel(proto.Message):
    r"""

    Attributes:
        battery (blueye.protocol.types.BatteryBQ40Z50):

    """

    battery = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.BatteryBQ40Z50,
    )


class DiveTimeTel(proto.Message):
    r"""Receive the dive time of the drone.

    Attributes:
        dive_time (blueye.protocol.types.DiveTime):
            The current dive time of the drone.
    """

    dive_time = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.DiveTime,
    )


class DroneTimeTel(proto.Message):
    r"""Receive time information from the drone.

    Attributes:
        real_time_clock (blueye.protocol.types.SystemTime):
            The real-time clock of the drone.
        monotonic_clock (blueye.protocol.types.SystemTime):
            The monotonic clock of the drone (time since
            power on).
    """

    real_time_clock = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.SystemTime,
    )

    monotonic_clock = proto.Field(proto.MESSAGE, number=2,
        message=message_formats.SystemTime,
    )


class WaterTemperatureTel(proto.Message):
    r"""

    Attributes:
        temperature (blueye.protocol.types.WaterTemperature):

    """

    temperature = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.WaterTemperature,
    )


class CPUTemperatureTel(proto.Message):
    r"""

    Attributes:
        temperature (blueye.protocol.types.CPUTemperature):

    """

    temperature = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CPUTemperature,
    )


class CanisterTemperatureTel(proto.Message):
    r"""

    Attributes:
        temperature (blueye.protocol.types.CanisterTemperature):

    """

    temperature = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CanisterTemperature,
    )


class CanisterHumidityTel(proto.Message):
    r"""

    Attributes:
        humidity (blueye.protocol.types.CanisterHumidity):

    """

    humidity = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CanisterHumidity,
    )


class VideoStorageSpaceTel(proto.Message):
    r"""

    Attributes:
        storage_space (blueye.protocol.types.StorageSpace):

    """

    storage_space = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.StorageSpace,
    )


class DataStorageSpaceTel(proto.Message):
    r"""

    Attributes:
        storage_space (blueye.protocol.types.StorageSpace):

    """

    storage_space = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.StorageSpace,
    )


class CalibrationStateTel(proto.Message):
    r"""

    Attributes:
        calibration_state (blueye.protocol.types.CalibrationState):

    """

    calibration_state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CalibrationState,
    )


class TiltStabilizationTel(proto.Message):
    r"""

    Attributes:
        state (blueye.protocol.types.TiltStabilizationState):

    """

    state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.TiltStabilizationState,
    )


class IperfTel(proto.Message):
    r"""

    Attributes:
        status (blueye.protocol.types.IperfStatus):

    """

    status = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.IperfStatus,
    )


class NStreamersTel(proto.Message):
    r"""

    Attributes:
        n_streamers (blueye.protocol.types.NStreamers):

    """

    n_streamers = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.NStreamers,
    )


class TiltAngleTel(proto.Message):
    r"""

    Attributes:
        angle (blueye.protocol.types.TiltAngle):

    """

    angle = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.TiltAngle,
    )


class DroneInfoTel(proto.Message):
    r"""Receive metadata and information about the connected drone.

    Attributes:
        drone_info (blueye.protocol.types.DroneInfo):
            Various metadata such as software versions
            and serial number.
    """

    drone_info = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.DroneInfo,
    )


class ErrorFlagsTel(proto.Message):
    r"""-

    Receive currently set error flags.

    Attributes:
        error_flags (blueye.protocol.types.ErrorFlags):
            Currently set error flags on the drone.
    """

    error_flags = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.ErrorFlags,
    )


class ControlModeTel(proto.Message):
    r"""-

    Receive the current state of the control system.

    Attributes:
        state (blueye.protocol.types.ControlMode):
            State of the control system.
    """

    state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.ControlMode,
    )


class ThicknessGaugeTel(proto.Message):
    r"""-

    Thickness gauge measurement telemetry message.

    Attributes:
        thickness_gauge (blueye.protocol.types.ThicknessGauge):
            Tickness measurement with a cygnus gauge.
    """

    thickness_gauge = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.ThicknessGauge,
    )


class CpProbeTel(proto.Message):
    r"""-

    Cathodic Protection Potential probe telemetry message

    Attributes:
        cp_probe (blueye.protocol.types.CpProbe):
            Reading from cp probe.
    """

    cp_probe = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CpProbe,
    )


class ConnectedClientsTel(proto.Message):
    r"""-

    List of connected clients telemetry message.

    Attributes:
        client_id_in_control (int):
            The client id of the client in control.
        connected_clients (Sequence[blueye.protocol.types.ConnectedClient]):
            List of connected clients.
    """

    client_id_in_control = proto.Field(proto.UINT32, number=1)

    connected_clients = proto.RepeatedField(proto.MESSAGE, number=2,
        message=message_formats.ConnectedClient,
    )


__all__ = tuple(sorted(__protobuf__.manifest))