import ctypes
import miscs

class MqttSuback(ctypes.Structure):
    _fields_ = [("header", miscs.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("rcs_len", ctypes.c_ushort),
                ("rcs", ctypes.POINTER(ctypes.c_ubyte))]