#!/usr/bin/env python3

import json
import os

from jinja2 import Environment, FileSystemLoader


def get_protocol(protocol_path):
    with open(protocol_path) as json_file:
        jdata = json.load(json_file)
    return jdata


class Context:
    def __init__(self, path=os.path.dirname(os.path.abspath(__file__))):
        self.path = path
        self.module_path = os.path.join(path, "../blueye/protocol")
        template_path = os.path.join(path, "templates")
        self.template_environment = Environment(autoescape=False,
                                                trim_blocks=True,
                                                lstrip_blocks=True,
                                                loader=FileSystemLoader(template_path))
        self.output_file_path = os.path.join(self.module_path, "tcp_protocol_class.py")
        json_path = os.path.join(path, "..", "tcp_protocol.json")
        self.tcp_protocol = get_protocol(json_path)


def dtype_to_format_char(dtype):
    STRUCT_CONVERSION = {"<u1": "B", "<i1": "b", "<u2": "H", "<i2": "h",
                         "<u4": "I", "<i4": "i", "<u8": "Q", "<i8": "q",
                         "<f4": "f", "<f8": "d"}
    return STRUCT_CONVERSION[dtype]


def write_tcp_send_functions(context):
    with open(context.output_file_path, "w") as f:
        f.write("# This file is autogenerated. Please do not edit\n")
        f.write("import struct\n")
        f.write("from .tcp_client import TcpClientBase\n")
        protocol_selector_context = {'protocol_versions_list': []}
        for protocol_version in context.tcp_protocol:
            class_template_context = protocol_version
            protocol_name = 'TcpClientV' + protocol_version['version']
            protocol_selector_context['protocol_versions_list'].append(protocol_name)
            protocol_selector_context['latest_protocol_version'] = protocol_name
            print(f"protocol selector context: {protocol_selector_context}")
            class_template_context['protocol_name'] = protocol_name
            protocol_class = context.template_environment.get_template(
                "protocol_class.template").render(class_template_context)
            f.write(protocol_class)
            for command in protocol_version["commands"]:
                template_context = command
                if 'fields' in command:
                    format_string = ""
                    for field in command['fields']:
                        format_string += dtype_to_format_char(field['dtype'])
                    template_context['format_string'] = format_string
                if 'returned_fields' in command:
                    return_format_string = "<"
                    read_size = 0
                    for field in command['returned_fields']:
                        return_format_string += dtype_to_format_char(field['dtype'])
                        read_size += int(field['dtype'][2])  # get byte count from dtype of field
                    template_context['return_format_string'] = return_format_string
                    template_context['read_size'] = read_size
                python_command = context.template_environment\
                    .get_template("send_command_function.template")\
                    .render(template_context)
                f.write(python_command)

        protocol_selector_class = context.template_environment.get_template(
            "protocol_selector_class.template").render(protocol_selector_context)
        f.write(protocol_selector_class)


def write_tcp_protocol(context):
    write_tcp_send_functions(context)


if __name__ == "__main__":
    context = Context()
    write_tcp_protocol(context)
