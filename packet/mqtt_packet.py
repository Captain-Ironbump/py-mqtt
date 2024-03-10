import ctypes
import miscs


class MqttPacket(ctypes.Union):
    _fields_ = [("ack", miscs.MqttAck),
                ("header", miscs.MQTTHeader),
                ("connect", miscs.MqttConnect),
                ("connack", miscs.MqttConnack),
                ("suback", miscs.MqttSuback),
                ("publish", miscs.MqttPublish),
                ("subscribe", miscs.MqttSubscribe),
                ("unsubscribe", miscs.MqttUnsubscribe)]
    