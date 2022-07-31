import cffi
import os
import json

ffi = cffi.FFI()

# Load library
lib = ffi.dlopen("./libpromql.so")


# Define the function prototypes
ffi.cdef('''

struct split_return {
	char* json_result;
	char* err;
};

extern struct split_return split(char* code);
''')


print(dir(lib))
result = lib.split('sum(rate(foo{bar="baz"}[5m])) by (job) > 0'.encode())
p1 = ffi.string(result.json_result).decode()
p2 =  ffi.string(result.err).decode()

print(json.loads(p1))
print(p2)
import time
time.sleep(111111)
