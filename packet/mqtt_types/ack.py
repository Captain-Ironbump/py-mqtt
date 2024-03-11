import ctypes
import miscs

class MqttAck(ctypes.Structure):
    _fields_ = [("header", miscs.MQTTHeader),
                ("packet_id", ctypes.c_ushort)]
