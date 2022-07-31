import cffi
import os

ffi = cffi.FFI()

# Load library
lib = ffi.dlopen("./libpromql.so")


# Define the function prototypes
ffi.cdef('''
    typedef struct { char* json_result; char* err; } Result;
    Result* split(char* code);
''')


result = lib.split('sum(rate(foo{bar="baz"}[5m])) by (job) > 0'.encode())
p=ffi.unpack(ffi.cast("Result*", result), 1)
p1 = ffi.string(p.json_result).decode()
print("StringFromGo(): {}".format(p))
print("StringFromGo(): {}".format(p1))
