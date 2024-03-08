import ctypes
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import packet.mqtt_header as mqtt_header
from packet.mqtt_factory import create_variable_header_class, create_payload_class


class MQTT_CONNECT(ctypes.Structure):
    _fields_ = [("header", mqtt_header),
                ("variable-headers", create_variable_header_class("CONNECT")),
                ("payload", create_payload_class("CONNECT"))]