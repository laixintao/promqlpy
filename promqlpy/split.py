import cffi
import json
from pathlib import Path
from distutils.sysconfig import get_config_var


here = Path(__file__).absolute().parent
ext_suffix = get_config_var("EXT_SUFFIX")
so_file = str(here / ("_libpromql" + str(ext_suffix)))

ffi = cffi.FFI()

# Load library
lib = ffi.dlopen(so_file)

# Define the function prototypes
ffi.cdef(
    """

struct split_return {
	char* json_result;
	char* err;
};

extern struct split_return split(char* code);
extern void FreeString(char* str);

"""
)


class PromQLException(Exception):
    ...


def split(code: str):
    """
    split PromQL/MetricsQL alert rules into multiple expressions
    """

    result = lib.split(code.encode())
    json_result = ffi.string(result.json_result).decode()
    err = ffi.string(result.err).decode()

    lib.FreeString(result.json_result)
    lib.FreeString(result.err)

    if err:
        raise PromQLException(err)

    return json.loads(json_result)
