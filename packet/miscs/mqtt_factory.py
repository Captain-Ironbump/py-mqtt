import ctypes
from typing import Type, TypeVar, Union, Tuple

from packet.bit_classes.mqtt_packet_bits import *

def create_variable_header_class(type: str):
    VariableHeader = TypeVar('VariableHeader')
    def _create_variable_header(second_field: Tuple[str, Union[ctypes._SimpleCData, ctypes.Structure]]) -> Type[VariableHeader]:
        class VariableHeader(ctypes.Union):
            _fields_ = [("byte", ctypes.c_uint8),
                        second_field]
        return VariableHeader

    packet_type_create_dict = {
        'CONNECT': _create_variable_header(("bits", ConnectBits)),
        'CONNACK': _create_variable_header(("bits", ConnackBits)),
    }
    return packet_type_create_dict[type]

def create_payload_class(type: str):
    Payload = TypeVar('Payload')
    def _create_payload(fields: list) -> Union[Payload, Tuple[str, ctypes.c_ubyte], ctypes.c_void_p]:
        if not fields or len(fields) == 0:
            return ("rc", ctypes.c_ubyte)
        class Payload(ctypes.Structure):
            _fields_ = fields
        return Payload
    
    packet_type_create_dict = {
        'CONNECT': _create_payload([("keep_alive", ctypes.c_ushort),
                                    ("client_id", ctypes.c_char_p),
                                    ("username", ctypes.c_char_p),
                                    ("password", ctypes.c_char_p),
                                    ("will_topic", ctypes.c_char_p),
                                    ("will_message", ctypes.c_char_p)]),
        'CONNACK': _create_payload([]),
        'PUBLISH': ctypes.c_void_p,
    }
    return packet_type_create_dict[type]


def create_tuple_class(type: str):
    MqttTuple = TypeVar('MqttTuple')
    def _create_tuple(fields: list) -> Type[MqttTuple]:
        class MqttTuple(ctypes.Structure):
            _fields_ = fields
        return MqttTuple
    packet_type_create_dict = {
        'SUBSCRIBE': _create_tuple([("topic_len", ctypes.c_ushort), ("topic_ptr", ctypes.c_char_p), ("qos", ctypes.c_uint)]),
        'UNSUBSCRIBE': _create_tuple([("topic_len", ctypes.c_ushort), ("topic_ptr", ctypes.c_char_p)]),
    }
    return packet_type_create_dict[type]

