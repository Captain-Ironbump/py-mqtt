import ctypes
import miscs

class MqttPublish(ctypes.Structure):
    _fields_ = [("header", miscs.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("topic_len", ctypes.c_ushort),
                ("topic", ctypes.POINTER(ctypes.c_ubyte)),
                ("payload_len", ctypes.c_ushort),
                ("payload", ctypes.POINTER(miscs.create_payload_class('PUBLISH')))]