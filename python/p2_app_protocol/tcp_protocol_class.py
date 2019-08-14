# This file is autogenerated. Please do not edit
import struct


class TcpCommands:
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
        try:
            self.send_msg(msg)
        except IOError:
            pass

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
        try:
            self.send_msg(msg)
        except IOError:
            pass

    def ping(self):
        """Send a ping command over TCP
        """
        command_identifier = b'p'
        msg = command_identifier
        try:
            self.send_msg(msg)
            reply = self.receive_msg()
            self.check_reply(reply, b'P')
        except IOError:
            pass

    def start_recording(self):
        """Send a start_recording command over TCP
        """
        command_identifier = b'r'
        msg = command_identifier
        try:
            self.send_msg(msg)
        except IOError:
            pass

    def stop_recording(self):
        """Send a stop_recording command over TCP
        """
        command_identifier = b'R'
        msg = command_identifier
        try:
            self.send_msg(msg)
        except IOError:
            pass

    def auto_heading_on(self):
        """Send a auto_heading_on command over TCP
        """
        command_identifier = b'h'
        msg = command_identifier
        try:
            self.send_msg(msg)
        except IOError:
            pass

    def auto_heading_off(self):
        """Send a auto_heading_off command over TCP
        """
        command_identifier = b'H'
        msg = command_identifier
        try:
            self.send_msg(msg)
        except IOError:
            pass

    def auto_depth_on(self):
        """Send a auto_depth_on command over TCP
        """
        command_identifier = b'd'
        msg = command_identifier
        try:
            self.send_msg(msg)
        except IOError:
            pass

    def auto_depth_off(self):
        """Send a auto_depth_off command over TCP
        """
        command_identifier = b'D'
        msg = command_identifier
        try:
            self.send_msg(msg)
        except IOError:
            pass

