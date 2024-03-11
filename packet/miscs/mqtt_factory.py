import mqtt_payload
import mqtt_tupl

mqtt_packet_types = [
    "CONNECT",          # 1
    "CONNACK",          # 2
    "PUBLISH",          # 3
    "PUBACK",           # 4
    "PUBREC",           # 5
    "PUBREL",           # 6
    "PUBCOMP",          # 7
    "SUBSCRIBE",        # 8
    "SUBACK",           # 9
    "UNSUBSCRIBE",      # 10
    "UNSUBACK",         # 11
    "PINGREQ",          # 12
    "PINGRESP",         # 13
    "DISCONNECT",       # 14
]

def create_payload(type: str):
    if type not in mqtt_packet_types:
        raise ValueError(f"Invalid package type: {type}")

    def _create_payload():
        return mqtt_payload.MqttPayload(type)

    switcher = {
        "CONNECT": _create_payload,
        "PUBLISH": _create_payload,
        "SUBSCRIBE": _create_payload,
        "SUBACK": _create_payload,
        "UNSUBSCRIBE": _create_payload,
    }
    return switcher.get(type, None)
    
    
def create_tuples(type: str):
    if type not in mqtt_packet_types:
        raise ValueError(f"Invalid package type: {type}")

    def _create_tuples():
        return mqtt_tupl.MqttTuple(type)

    switcher = {
        "SUBSCRIBE": _create_tuples,
        "UNSUBSCRIBE": _create_tuples
    }
    return switcher.get(type, None)