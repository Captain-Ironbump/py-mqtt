import ctypes
import miscs

class MqttConnect(ctypes.Structure):
    _fields_ = [("header", miscs.MQTTHeader),
                ("variable-headers", miscs.create_variable_header_class("CONNECT")),
                ("payload", miscs.create_payload_class("CONNECT"))]