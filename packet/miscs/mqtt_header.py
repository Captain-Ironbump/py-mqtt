class MqttFixedHeader():
    __slots__ = ('package_type', 'remaining_length', 'flags') # flags -> retein, qos, qos, dup -> 2^4

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

    def __init__(self, package_type: str, lenght=0, flags=0) -> None:
        self.package_type = package_type if package_type in MqttFixedHeader._packet_types.keys() else None # x if x > y else y
        self.remaining_length = lenght
        self.flags = flags
        

class MqttVariableHeader():
    def __init__(self) -> None:
        pass