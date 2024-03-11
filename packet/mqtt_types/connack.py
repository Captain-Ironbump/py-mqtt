import ctypes
import miscs

class MqttConnack(ctypes.Structure):
    _fields_ = [("header", miscs.MQTTHeader),
                ("variable-headers", miscs.create_variable_header_class("CONNACK")),
                miscs.create_payload_class("CONNACK")]