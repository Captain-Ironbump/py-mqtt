class MqttTuple():
    _packet_type_tuples = {
        'SUBSCRIBE': ('topic_len', 'topic', 'qos'),
        'UNSUBSCRIBE': ('topic_len', 'topic',)
    }

    def __init__(self, package_type: str) -> None:
        self.__slots__ = MqttTuple._packet_type_tuples[package_type]