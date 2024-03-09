import ctypes
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unsure.mqtt_header as mqtt_header
from packet.mqtt_factory import create_payload_class

class MqttPublish(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("topic_len", ctypes.c_ushort),
                ("topic", ctypes.POINTER(ctypes.c_ubyte)),
                ("payload_len", ctypes.c_ushort),
                ("payload", ctypes.POINTER(create_payload_class('PUBLISH')))]
