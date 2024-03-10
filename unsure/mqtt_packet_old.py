class MQTT_PACKET():
    _mqtt_header_len = 2
    _mqtt_ACK_len = 4
    _connack_byte = 0x20
    _publish_byte = 0x30
    _puback_byte = 0x40
    _pubrec_byte = 0x50
    _pubrel_byte = 0x60
    _pubcomp_byte = 0x70
    _suback_byte = 0x90
    _unsuback_byte = 0xB0
    _pingresp_byte = 0xD0 
    packet_types = [
        'CONNECT',
        'CONNACK',
        'PUBLISH',
        'PUBACK',
        'PUBREC',
        'PUBREL',
        'PUBCOMP',
        'SUBSCRIBE',
        'SUBACK',
        'UNSUBSCRIBE',
        'UNSUBACK',
        'PINGREQ',
        'PINGRESP',
        'DISCONNECT'
    ]
    
    def __init__(self) -> None:
        pass