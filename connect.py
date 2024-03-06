import ctypes
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import Packet.mqtt_header as mqtt_header


# TODO: The variable header and the payload object should be a generic class,
#       so that the user can create a new class for each MQTT packet.
class _CONNECT_BITS(ctypes.Structure):
    __fields__ = [("reserved", ctypes.c_int, 1),
                  ("clean_session", ctypes.c_uint, 1),
                  ("will", ctypes.c_uint, 1),
                  ("will_qos", ctypes.c_uint, 2),
                  ("will_retain", ctypes.c_uint, 1),
                  ("password", ctypes.c_uint, 1),
                  ("username", ctypes.c_uint, 1)]


class _CONNECT_VARIABLE_HEADER(ctypes.Union):
    _fields_ = [("byte", ctypes.c_uint8),
                ("bits", _CONNECT_BITS)]


class _CONNECT_PAYLOAD(ctypes.Structure):
    _fields_ = [("keep_alive", ctypes.c_uint16),
                ("client_id", ctypes.c_char_p),
                ("username", ctypes.c_char_p),
                ("password", ctypes.c_char_p),
                ("will_topic", ctypes.c_char_p),
                ("will_message", ctypes.c_char_p)]


class MQTT_CONNECT(ctypes.Structure):
    _fields_ = [("header", mqtt_header),
                ("variable-headers", _CONNECT_VARIABLE_HEADER),
                ("payload", _CONNECT_PAYLOAD)]