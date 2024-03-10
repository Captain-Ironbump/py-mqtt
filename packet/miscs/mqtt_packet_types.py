import ctypes
import mqtt_header
from mqtt_factory import create_variable_header_class, create_payload_class, create_tuple_class

class MqttAck(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort)]


class MqttConnack(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("variable-headers", create_variable_header_class("CONNACK")),
                create_payload_class("CONNACK")]
    

class MqttConnect(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("variable-headers", create_variable_header_class("CONNECT")),
                ("payload", create_payload_class("CONNECT"))]
    

class MqttPublish(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("topic_len", ctypes.c_ushort),
                ("topic", ctypes.POINTER(ctypes.c_ubyte)),
                ("payload_len", ctypes.c_ushort),
                ("payload", ctypes.POINTER(create_payload_class('PUBLISH')))]
    

class MqttSuback(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("rcs_len", ctypes.c_ushort),
                ("rcs", ctypes.POINTER(ctypes.c_ubyte))]
    

class MqttSubscribe(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("tuples_len", ctypes.c_ushort),
                ("tuples", ctypes.POINTER(create_tuple_class('SUBSCRIBE')))]
    

class MqttUnsubscribe(ctypes.Structure):
    _fields_ = [("header", mqtt_header.MQTTHeader),
                ("packet_id", ctypes.c_ushort),
                ("tuples_len", ctypes.c_ushort),
                ("tuples", ctypes.POINTER(create_tuple_class('UNSUBSCRIBE')))]