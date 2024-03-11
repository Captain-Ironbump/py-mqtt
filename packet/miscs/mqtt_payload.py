class MqttPayload():
    _packet_type_payloads = {
        'CONNECT': ('re', 'keep_alive', 'client_id', 'username', 'password', 'will_topic', 'will_message'),
        'PUBLISH': ('topic_len', 'topic_ptr', 'packet_id'),
        'SUBSCRIBE': ('packet_id',),
        'SUBACK': ('packet_id',),
        'UNSUBSCRIBE': ('packet_id',)
    }

    def __init__(self, package_type: str) -> None:
        self.__slots__ = MqttPayload._packet_type_payloads[package_type]