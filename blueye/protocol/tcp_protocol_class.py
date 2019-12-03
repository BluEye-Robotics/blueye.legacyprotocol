# This file is autogenerated. Please do not edit
import struct
from .tcp_client import TcpClientBase

class TcpClientV1(TcpClientBase):
    protocol_version = 1
    def motion_input(self, surge_motion_input, sway_motion_input, heave_motion_input, yaw_motion_input, slow_input, boost_input):
        """Send a motion_input command over TCP

        Args:
            surge_motion_input (numpy data type:<f4): valid range is <-1, 1> 
            sway_motion_input (numpy data type:<f4): valid range is <-1, 1> 
            heave_motion_input (numpy data type:<f4): valid range is <-1, 1> 
            yaw_motion_input (numpy data type:<f4): valid range is <-1, 1> 
            slow_input (numpy data type:<f4): valid range is <0, 1> 
            boost_input (numpy data type:<f4): valid range is <0, 1> 
        """
        if not -1 <= surge_motion_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for surge_motion_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=-1, upper_limit=1) +
                " but got value: {name}".format(name=surge_motion_input))

        if not -1 <= sway_motion_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for sway_motion_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=-1, upper_limit=1) +
                " but got value: {name}".format(name=sway_motion_input))

        if not -1 <= heave_motion_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for heave_motion_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=-1, upper_limit=1) +
                " but got value: {name}".format(name=heave_motion_input))

        if not -1 <= yaw_motion_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for yaw_motion_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=-1, upper_limit=1) +
                " but got value: {name}".format(name=yaw_motion_input))

        if not 0 <= slow_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for slow_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=0, upper_limit=1) +
                " but got value: {name}".format(name=slow_input))

        if not 0 <= boost_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for boost_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=0, upper_limit=1) +
                " but got value: {name}".format(name=boost_input))

        command_identifier = b'j'
        msg = command_identifier
        msg += struct.pack('ffffff', surge_motion_input, sway_motion_input, heave_motion_input, yaw_motion_input, slow_input, boost_input)
        self.send_and_receive(msg, expects_reply=False)

    def set_lights(self, brightness_upper, brightness_lower):
        """Send a set_lights command over TCP

        Args:
            brightness_upper (numpy data type:<u1): valid range is <0, 255> 
            brightness_lower (numpy data type:<u1): valid range is <0, 255> 
        """
        if not 0 <= brightness_upper <= 255:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for brightness_upper is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=0, upper_limit=255) +
                " but got value: {name}".format(name=brightness_upper))

        if not 0 <= brightness_lower <= 255:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for brightness_lower is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=0, upper_limit=255) +
                " but got value: {name}".format(name=brightness_lower))

        command_identifier = b'l'
        msg = command_identifier
        msg += struct.pack('BB', brightness_upper, brightness_lower)
        self.send_and_receive(msg, expects_reply=False)

    def ping(self):
        """Send a ping command over TCP
        """
        command_identifier = b'p'
        msg = command_identifier
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'P')

    def start_recording(self):
        """Send a start_recording command over TCP
        """
        command_identifier = b'r'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def stop_recording(self):
        """Send a stop_recording command over TCP
        """
        command_identifier = b'R'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def start_compass_calibration(self):
        """Send a start_compass_calibration command over TCP
        """
        command_identifier = b'i'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def cancel_compass_calibration(self):
        """Send a cancel_compass_calibration command over TCP
        """
        command_identifier = b'I'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def save_compass_calibration(self):
        """Send a save_compass_calibration command over TCP
        """
        command_identifier = b'c'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def user_geo_location(self, longitude, latitude):
        """Send a user_geo_location command over TCP

        Args:
            longitude (numpy data type:<f8): longitude that is included in the log file in degrees
            latitude (numpy data type:<f8): latitude that is included in the log file in degrees
        """
        command_identifier = b'g'
        msg = command_identifier
        msg += struct.pack('dd', longitude, latitude)
        self.send_and_receive(msg, expects_reply=False)

    def watchdog(self, connection_duration):
        """Send a watchdog command over TCP

        Args:
            connection_duration (numpy data type:<i2): time in seconds since connected to drone
        """
        command_identifier = b'w'
        msg = command_identifier
        msg += struct.pack('h', connection_duration)
        self.send_and_receive(msg, expects_reply=False)

    def auto_heading_on(self):
        """Send a auto_heading_on command over TCP
        """
        command_identifier = b'h'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def auto_heading_off(self):
        """Send a auto_heading_off command over TCP
        """
        command_identifier = b'H'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def auto_depth_on(self):
        """Send a auto_depth_on command over TCP
        """
        command_identifier = b'd'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def auto_depth_off(self):
        """Send a auto_depth_off command over TCP
        """
        command_identifier = b'D'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def auto_depth_step(self, direction):
        """Send a auto_depth_step command over TCP

        Args:
            direction (numpy data type:<i2):  1 for up, -1 for down
        """
        command_identifier = b'a'
        msg = command_identifier
        msg += struct.pack('h', direction)
        self.send_and_receive(msg, expects_reply=False)

    def auto_heading_step(self, direction):
        """Send a auto_heading_step command over TCP

        Args:
            direction (numpy data type:<i2): 1 for up, -1 for down
        """
        command_identifier = b'A'
        msg = command_identifier
        msg += struct.pack('h', direction)
        self.send_and_receive(msg, expects_reply=False)

    def set_system_time(self, unix_timestamp):
        """Send a set_system_time command over TCP

        set the system time on the on-board computer

        Args:
            unix_timestamp (numpy data type:<i4): 
        """
        command_identifier = b't'
        msg = command_identifier
        msg += struct.pack('i', unix_timestamp)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_exposure(self, exposure_value):
        """Send a set_camera_exposure command over TCP

        Args:
            exposure_value (numpy data type:<i4): 1 = 1/1000th of a second, 5 = 1/200th of a second. Valid values are in the range <1, 5000>
        """
        command_identifier = b've'
        msg = command_identifier
        msg += struct.pack('i', exposure_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_whitebalance(self, whitebalance_value):
        """Send a set_camera_whitebalance command over TCP

        Args:
            whitebalance_value (numpy data type:<i4): valid values are in the range <2800, 9300>
        """
        command_identifier = b'vw'
        msg = command_identifier
        msg += struct.pack('i', whitebalance_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_hue(self, hue_value):
        """Send a set_camera_hue command over TCP

        Args:
            hue_value (numpy data type:<i4): valid values are in the range <-40, 40>
        """
        command_identifier = b'vh'
        msg = command_identifier
        msg += struct.pack('i', hue_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_bitrate(self, bitrate_value):
        """Send a set_camera_bitrate command over TCP

        Args:
            bitrate_value (numpy data type:<i4): set camera bitrate in bits. Valid values are in range <1 000 000, 16 000 000> 
        """
        command_identifier = b'vb'
        msg = command_identifier
        msg += struct.pack('i', bitrate_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def get_camera_parameters(self):
        """Send a get_camera_parameters command over TCP

        Returns:
            parameter (numtyp data type:<u1)
            camera_bitrate (numtyp data type:<i4)
            camera_exposure (numtyp data type:<i4)
            camera_whitebalance (numtyp data type:<i4)
            camera_hue (numtyp data type:<i4)
        """
        command_identifier = b'Va'
        msg = command_identifier
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=17)
        return struct.unpack('<Biiii', reply)


class TcpClientV2(TcpClientBase):
    protocol_version = 2
    def motion_input(self, surge_motion_input, sway_motion_input, heave_motion_input, yaw_motion_input, slow_input, boost_input):
        """Send a motion_input command over TCP

        Args:
            surge_motion_input (numpy data type:<f4): valid range is <-1, 1> 
            sway_motion_input (numpy data type:<f4): valid range is <-1, 1> 
            heave_motion_input (numpy data type:<f4): valid range is <-1, 1> 
            yaw_motion_input (numpy data type:<f4): valid range is <-1, 1> 
            slow_input (numpy data type:<f4): valid range is <0, 1> 
            boost_input (numpy data type:<f4): valid range is <0, 1> 
        """
        if not -1 <= surge_motion_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for surge_motion_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=-1, upper_limit=1) +
                " but got value: {name}".format(name=surge_motion_input))

        if not -1 <= sway_motion_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for sway_motion_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=-1, upper_limit=1) +
                " but got value: {name}".format(name=sway_motion_input))

        if not -1 <= heave_motion_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for heave_motion_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=-1, upper_limit=1) +
                " but got value: {name}".format(name=heave_motion_input))

        if not -1 <= yaw_motion_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for yaw_motion_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=-1, upper_limit=1) +
                " but got value: {name}".format(name=yaw_motion_input))

        if not 0 <= slow_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for slow_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=0, upper_limit=1) +
                " but got value: {name}".format(name=slow_input))

        if not 0 <= boost_input <= 1:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for boost_input is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=0, upper_limit=1) +
                " but got value: {name}".format(name=boost_input))

        command_identifier = b'j'
        msg = command_identifier
        msg += struct.pack('ffffff', surge_motion_input, sway_motion_input, heave_motion_input, yaw_motion_input, slow_input, boost_input)
        self.send_and_receive(msg, expects_reply=False)

    def set_lights(self, brightness_upper, brightness_lower):
        """Send a set_lights command over TCP

        Args:
            brightness_upper (numpy data type:<u1): valid range is <0, 255> 
            brightness_lower (numpy data type:<u1): valid range is <0, 255> 
        """
        if not 0 <= brightness_upper <= 255:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for brightness_upper is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=0, upper_limit=255) +
                " but got value: {name}".format(name=brightness_upper))

        if not 0 <= brightness_lower <= 255:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for brightness_lower is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit=0, upper_limit=255) +
                " but got value: {name}".format(name=brightness_lower))

        command_identifier = b'l'
        msg = command_identifier
        msg += struct.pack('BB', brightness_upper, brightness_lower)
        self.send_and_receive(msg, expects_reply=False)

    def ping(self):
        """Send a ping command over TCP
        """
        command_identifier = b'p'
        msg = command_identifier
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'P')

    def start_recording(self):
        """Send a start_recording command over TCP
        """
        command_identifier = b'r'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def stop_recording(self):
        """Send a stop_recording command over TCP
        """
        command_identifier = b'R'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def start_compass_calibration(self):
        """Send a start_compass_calibration command over TCP
        """
        command_identifier = b'i'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def cancel_compass_calibration(self):
        """Send a cancel_compass_calibration command over TCP
        """
        command_identifier = b'I'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def save_compass_calibration(self):
        """Send a save_compass_calibration command over TCP
        """
        command_identifier = b'c'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def user_geo_location(self, longitude, latitude):
        """Send a user_geo_location command over TCP

        Args:
            longitude (numpy data type:<f8): longitude that is included in the log file in degrees
            latitude (numpy data type:<f8): latitude that is included in the log file in degrees
        """
        command_identifier = b'g'
        msg = command_identifier
        msg += struct.pack('dd', longitude, latitude)
        self.send_and_receive(msg, expects_reply=False)

    def watchdog(self, connection_duration):
        """Send a watchdog command over TCP

        Args:
            connection_duration (numpy data type:<i2): time in seconds since connected to drone
        """
        command_identifier = b'w'
        msg = command_identifier
        msg += struct.pack('h', connection_duration)
        self.send_and_receive(msg, expects_reply=False)

    def auto_heading_on(self):
        """Send a auto_heading_on command over TCP
        """
        command_identifier = b'h'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def auto_heading_off(self):
        """Send a auto_heading_off command over TCP
        """
        command_identifier = b'H'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def auto_depth_on(self):
        """Send a auto_depth_on command over TCP
        """
        command_identifier = b'd'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def auto_depth_off(self):
        """Send a auto_depth_off command over TCP
        """
        command_identifier = b'D'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def auto_depth_step(self, direction):
        """Send a auto_depth_step command over TCP

        Args:
            direction (numpy data type:<i2):  1 for up, -1 for down
        """
        command_identifier = b'a'
        msg = command_identifier
        msg += struct.pack('h', direction)
        self.send_and_receive(msg, expects_reply=False)

    def auto_heading_step(self, direction):
        """Send a auto_heading_step command over TCP

        Args:
            direction (numpy data type:<i2): 1 for up, -1 for down
        """
        command_identifier = b'A'
        msg = command_identifier
        msg += struct.pack('h', direction)
        self.send_and_receive(msg, expects_reply=False)

    def set_system_time(self, unix_timestamp):
        """Send a set_system_time command over TCP

        set the system time on the on-board computer

        Args:
            unix_timestamp (numpy data type:<i4): 
        """
        command_identifier = b't'
        msg = command_identifier
        msg += struct.pack('i', unix_timestamp)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def take_still_picture(self):
        """Send a take_still_picture command over TCP

        Takes a still picture and stores it locally on the drone.
        """
        command_identifier = b's'
        msg = command_identifier
        self.send_and_receive(msg, expects_reply=False)

    def set_camera_exposure(self, exposure_value):
        """Send a set_camera_exposure command over TCP

        Args:
            exposure_value (numpy data type:<i4): 1 = 1/1000th of a second, 5 = 1/200th of a second. Valid values are in the range <1, 5000>
        """
        command_identifier = b've'
        msg = command_identifier
        msg += struct.pack('i', exposure_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_whitebalance(self, whitebalance_value):
        """Send a set_camera_whitebalance command over TCP

        Args:
            whitebalance_value (numpy data type:<i4): valid values are in the range <2800, 9300>
        """
        command_identifier = b'vw'
        msg = command_identifier
        msg += struct.pack('i', whitebalance_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_hue(self, hue_value):
        """Send a set_camera_hue command over TCP

        Args:
            hue_value (numpy data type:<i4): valid values are in the range <-40, 40>
        """
        command_identifier = b'vh'
        msg = command_identifier
        msg += struct.pack('i', hue_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_bitrate(self, bitrate_value):
        """Send a set_camera_bitrate command over TCP

        Args:
            bitrate_value (numpy data type:<i4): set camera bitrate in bits. Valid values are in range <1 000 000, 16 000 000> 
        """
        command_identifier = b'vb'
        msg = command_identifier
        msg += struct.pack('i', bitrate_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_framerate(self, framerate_value):
        """Send a set_camera_framerate command over TCP

        Args:
            framerate_value (numpy data type:<i4): valid values are 25 or 30
        """
        command_identifier = b'vf'
        msg = command_identifier
        msg += struct.pack('i', framerate_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def set_camera_resolution(self, resolution_value):
        """Send a set_camera_resolution command over TCP

        Args:
            resolution_value (numpy data type:<i4): valid values are 480, 720 or 1080
        """
        command_identifier = b'vr'
        msg = command_identifier
        msg += struct.pack('i', resolution_value)
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=1)
        self.check_reply(reply, b'a')

    def get_camera_parameters(self):
        """Send a get_camera_parameters command over TCP

        Returns:
            parameter (numtyp data type:<u1)
            camera_bitrate (numtyp data type:<i4)
            camera_exposure (numtyp data type:<i4)
            camera_whitebalance (numtyp data type:<i4)
            camera_hue (numtyp data type:<i4)
            camera_resolution (numtyp data type:<i4)
            camera_framerate (numtyp data type:<i4)
        """
        command_identifier = b'Va'
        msg = command_identifier
        reply = self.send_and_receive(msg, expects_reply=True, receive_size=25)
        return struct.unpack('<Biiiiii', reply)


class TcpClient:
    def __new__(self, protocol_version=None, *args, **kwargs):
        if protocol_version == None:
            return TcpClientV2(*args, **kwargs)
        elif protocol_version == 1:
            return TcpClientV1(*args, **kwargs)
        elif protocol_version == 2:
            return TcpClientV2(*args, **kwargs)
        else:
            raise ValueError(f"Unsupported protocol version: {protocol_version}")
            