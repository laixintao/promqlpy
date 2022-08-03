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

struct SplitBinaryOp_return {
    char* r0;
    char* r1;
};
extern struct SplitBinaryOp_return SplitBinaryOp(char* code);
extern void FreeString(char* str);

"""
)


class PromQLException(Exception):
    ...


def split_binary_op(code: str):
    """
    split PromQL/MetricsQL alert rules into multiple expressions
    """

    result = lib.SplitBinaryOp(code.encode())
    json_result = ffi.string(result.r0).decode()
    err = ffi.string(result.r1).decode()

    lib.FreeString(result.r0)
    lib.FreeString(result.r1)

    if err:
        raise PromQLException(err)

    return json.loads(json_result)
