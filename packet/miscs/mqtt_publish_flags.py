import ctypes

class PublishFlags(ctypes.Structure):
    _fields_ = [("retein", ctypes.c_uint, 1),
                ("qos", ctypes.c_uint, 2),
                ("dup", ctypes.c_uint, 1),
                ("type", ctypes.c_uint, 4)]
