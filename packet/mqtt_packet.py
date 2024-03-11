import ctypes
import miscs
import mqtt_types

class MqttPacket(ctypes.Union):
    _fields_ = [("ack", mqtt_types.MqttAck),
                ("header", miscs.MQTTHeader),
                ("connect", mqtt_types.MqttConnect),
                ("connack", mqtt_types.MqttConnack),
                ("suback", mqtt_types.MqttSuback),
                ("publish", mqtt_types.MqttPublish),
                ("subscribe", mqtt_types.MqttSubscribe),
                ("unsubscribe", mqtt_types.MqttUnsubscribe)]
    _MAX_LEN_BYTES = 4
    
    def encode_lenght(self, length):
        bytes = 0
        buf = bytearray(MqttPacket._MAX_LEN_BYTES)
        while True:
            if bytes + 1 > MqttPacket._MAX_LEN_BYTES:
                return buf[:bytes]
            d = length % 128
            length /= 128
            if length > 0:
                d |= 128
            buf[bytes] = d
            bytes += 1
            if length == 0:
                return buf[:bytes]
    

    def decode_lenght(self, buf_ptr):
        """ 
        Decode a length from the buffer.
        The parameter buf_ptr is a pointer to the buffer.
        The provided buffer should be parssed as a bytearray.

        Returns the length and the number of bytes read.
        """
        multiplier = 1
        value = 0
        index = 0
        buf = ctypes.cast(buf_ptr, ctypes.POINTER(ctypes.c_ubyte))
        while True:
            c = buf[index]
            value += (c & 127) * multiplier
            multiplier *= 128
            index += 1
            if (c & 128) == 0:
                break
            if index > len(buf):
                raise ValueError("Buffer too short for decoding length")
        return value, index
    