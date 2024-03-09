import ctypes
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unsure.mqtt_header as mqtt_header
from packet.mqtt_factory import create_tuple_class

class MqttUnsubscribe(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("tuples_len", ctypes.c_ushort),
                ("tuples", ctypes.POINTER(create_tuple_class('UNSUBSCRIBE')))]