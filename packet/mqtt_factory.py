import ctypes
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from typing import Type, TypeVar, Union, Tuple

from packet.bit_classes.mqtt_packet_bits import *

def create_variable_header_class(type: str):
    _VARIABLE_HEADER = TypeVar('_VARIABLE_HEADER')
    def _create_variable_header(second_field: Tuple[str, Union[ctypes._SimpleCData, ctypes.Structure]]) -> Type[_VARIABLE_HEADER]:
        class _VARIABLE_HEADER(ctypes.Union):
            _fields_ = [("byte", ctypes.c_uint8),
                        second_field]
        return _VARIABLE_HEADER

    packet_type_create_dict = {
        'CONNECT': _create_variable_header(("bits", CONNECT_BITS)),
        'CONNACK': _create_variable_header(("bits", CONNACK_BITS)),
    }
    return packet_type_create_dict[type]

def create_payload_class(type: str):
    _PAYLOAD = TypeVar('_PAYLOAD')
    def _create_payload(fields: list) -> Union[_PAYLOAD, Tuple[str, ctypes.c_ubyte]]:
        if not fields or len(fields) == 0:
            return ("rc", ctypes.c_ubyte)
        class _PAYLOAD(ctypes.Structure):
            _fields_ = fields
        return _PAYLOAD
    
    packet_type_create_dict = {
        'CONNECT': _create_payload([("keep_alive", ctypes.c_ushort),
                                    ("client_id", ctypes.c_char_p),
                                    ("username", ctypes.c_char_p),
                                    ("password", ctypes.c_char_p),
                                    ("will_topic", ctypes.c_char_p),
                                    ("will_message", ctypes.c_char_p)]),
        'CONNACK': _create_payload([]),
    }
    return packet_type_create_dict[type]