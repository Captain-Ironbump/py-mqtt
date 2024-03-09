import ctypes
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unsure.mqtt_header as mqtt_header

class MqttAck(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort)]