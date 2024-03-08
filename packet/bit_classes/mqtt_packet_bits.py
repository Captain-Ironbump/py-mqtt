import ctypes

class ConnectBits(ctypes.Structure):
    _fields_ = [("reserved", ctypes.c_int, 1),
                  ("clean_session", ctypes.c_uint, 1),
                  ("will", ctypes.c_uint, 1),
                  ("will_qos", ctypes.c_uint, 2),
                  ("will_retain", ctypes.c_uint, 1),
                  ("password", ctypes.c_uint, 1),
                  ("username", ctypes.c_uint, 1)]
    
class ConnackBits(ctypes.Structure):
    _fields_ = [("session_present", ctypes.c_uint, 1),
                ("reserved", ctypes.c_int, 7)]
    