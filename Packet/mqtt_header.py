import ctypes 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mqtt_publish_flags import PUBLISH_FLAGS

class MQTTHeader(ctypes.Union):
    _packet_types = {
        'CONNECT': 1,
        'CONNACK': 2,
        'PUBLISH': 3,
        'PUBACK': 4,
        'PUBREC': 5,
        'PUBREL': 6,
        'PUBCOMP': 7,
        'SUBSCRIBE': 8,
        'SUBACK': 9,
        'UNSUBSCRIBE': 10,
        'UNSUBACK': 11,
        'PINGREQ': 12,
        'PINGRESP': 13,
        'DISCONNECT': 14
    }
    _fields_ = [("byte", ctypes.c_uint8),
                ("bits", PUBLISH_FLAGS)]
    
    
    def __init__(self, package_type: str) -> None:
        self.bits.type = MQTTHeader._packet_types[package_type]