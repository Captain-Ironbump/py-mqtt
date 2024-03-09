import ctypes
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unsure.mqtt_header as mqtt_header


class MqttSuback(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("rcs_len", ctypes.c_ushort),
                ("rcs", ctypes.POINTER(ctypes.c_ubyte))]

