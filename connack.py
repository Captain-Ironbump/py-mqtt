import ctypes
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unsure.mqtt_header as mqtt_header
from packet.mqtt_factory import create_variable_header_class, create_payload_class

class MqttConnack(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("variable-headers", create_variable_header_class("CONNACK")),
                create_payload_class("CONNACK")]