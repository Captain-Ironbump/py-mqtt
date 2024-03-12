from mqtt_helper import encode_16bit_number
import struct

class MqttFixedHeader():
    __slots__ = ('package_type', 'remaining_length', 'flags') # flags -> retein, qos, qos, dup -> 2^4

    _packet_type_flags = {
        'CONNECT': (1, 0),
        'CONNACK': (2, 0),
        'PUBLISH': (3, {
            'AT_MOST_ONCE': 0,
            'AT_LEAST_ONCE': 1,
            'EXACTLY_ONCE': 2
        }),
        'PUBACK': (4, 0),
        'PUBREC': (5, 0),
        'PUBREL': (6, 2),
        'PUBCOMP': (7, 0),
        'SUBSCRIBE': (8, 2),
        'SUBACK': (9, 0),
        'UNSUBSCRIBE': (10, 2),
        'UNSUBACK': (11, 0),
        'PINGREQ': (12, 0),
        'PINGRESP': (13, 0),
        'DISCONNECT': (14, 0)
    }

    def __init__(self, package_type: str, lenght=0) -> None:
        try:
            self.package_type = (package_type, MqttFixedHeader._packet_type_flags[package_type][0])
        except KeyError:
            raise ValueError(f"Invalid package type: {package_type}")
        self.flags = MqttFixedHeader._packet_type_flags[package_type][1] if package_type != 'PUBLISH' else MqttFixedHeader._packet_type_flags[package_type]['AT_MOST_ONCE']
        self.remaining_length = lenght

    def pack(self):
        return struct.pack('!B', (self.package_type[1] << 4) | self.flags) + encode_16bit_number(self.remaining_length)
        

class MqttVariableHeader():
    _packet_type_flags = {
        'CONNECT': ('reserved', 'clean_session', 'will', 'will_qos', 'will_retain', 'username', 'password'),
        'CONNACK': ('session_present', 'reserved'),
        'PUBLISH': ('packet_id', 'topic_len', 'topic_ptr', 'payload_len', 'payload_ptr'),
        'PUBACK': ('packet_id',),
        'PUBREC': ('packet_id',),
        'PUBREL': ('packet_id',),
        'PUBCOMP': ('packet_id',),
        'SUBSCRIBE': ('packet_id', 'tuples_len'),
        'SUBACK': ('packet_id', 'rcs_len'),
        'UNSUBSCRIBE': ('packet_id', 'tuples_len'),
        'UNSUBACK': ('packet_id',),
        'PINGREQ': (),
        'PINGRESP': (),
        'DISCONNECT': ()
    }
    
    def __init__(self, package_type: str) -> None:
        self.__slots__ = MqttVariableHeader._packet_type_flags[package_type]


class ConnectHeader(MqttFixedHeader):
    __slots__ = ['protocol_name', 'protocol_level', 'connect_flags', 'keep_alive']
    def __init__(self) -> None:
        super().__init__('CONNECT')
        self.protocol_name = 'MQTT'
        self.protocol_level = bin(4)
        self.connect_flags = {
            'reserved': 0b0,
            'clean_session': 0b1,
            'will': 0b1,
            'will_qos': 0b01,
            'will_retain': 0b0,
            'username': 0b1,
            'password': 0b1
        }
        self.keep_alive = 10
    
    def pack_flags(self):
        byte = 0b0
        for i, (flag, value) in enumerate(self.connect_flags.items()):
            byte |= value << i
        return byte

    def pack(self):
        return super().pack() + encode_16bit_number(len(self.protocol_name)) + self.protocol_name.encode() + struct.pack('!B', self.protocol_level) + struct.pack('!B', self.pack_flags()) + encode_16bit_number(self.keep_alive)