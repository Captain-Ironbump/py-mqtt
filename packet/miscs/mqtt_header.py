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
        

class MqttVariableHeader():
    __packet_type_flags = {
        'CONNECT': ('bits', 'keep_alive', 'client_id', 'username', 'password', 'will_topic', 'will_message'),
        'CONNACK': ('bits', 'rc'),
        'PUBLISH': ('topic_len', 'topic_ptr', 'packet_id'),
        'PUBACK': ('packet_id',),
        'PUBREC': ('packet_id',),
        'PUBREL': ('packet_id',),
        'PUBCOMP': ('packet_id',),
        'SUBSCRIBE': ('packet_id',),
        'SUBACK': ('packet_id',),
        'UNSUBSCRIBE': ('packet_id',),
        'UNSUBACK': ('packet_id',),
        'PINGREQ': (),
        'PINGRESP': (),
        'DISCONNECT': ()
    }
    
    def __init__(self, package_type: str) -> None:
        self.__slots__ = MqttVariableHeader.__packet_type_flags[package_type]