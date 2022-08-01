package main

import (
	"github.com/laixintao/promqlpy/go/promql"
	"unsafe"
)

// #include <stdio.h>
// #include <stdlib.h>
import "C"

//export SplitBinaryOp
func SplitBinaryOp(code *C.char) (*C.char, *C.char) {
	codeGo := C.GoString(code)
	result, err := promql.SplitBinaryOp(codeGo)

	if err != nil {
		return C.CString(""), C.CString(err.Error())
	}

	return C.CString(result), C.CString("")
}

//export FreeString
func FreeString(str *C.char) {
	C.free(unsafe.Pointer(str))
}

func main() {}
