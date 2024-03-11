import ctypes
import miscs

class MqttUnsubscribe(ctypes.Structure):
    _fields_ = [("header", miscs.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("tuples_len", ctypes.c_ushort),
                ("tuples", ctypes.POINTER(miscs.create_tuple_class('UNSUBSCRIBE')))]