package promql

import (
	"fmt"

	"encoding/json"
	"github.com/VictoriaMetrics/metricsql"
)

type Expression struct {
	Left  *Expression `json:"left"`
	Right *Expression `json:"right"`
	Op    string      `json:"op"`

	Code string `json:"code"`

	// if true, left,right,op is set
	// if false, then only code is set
	IsBinaryOp bool `json:"is_binary_op"`
}

var compareOps = map[string]bool{
	"==": true,
	"!=": true,
	">":  true,
	"<":  true,
	">=": true,
	"<=": true,

	// logical set ops
	"and":    true,
	"or":     true,
	"unless": true,
}

func parseExpr(expr metricsql.Expr) *Expression {

	if bop, ok := expr.(*metricsql.BinaryOpExpr); ok {

        // treat +,-,* etc still as normal expression
		if compareOps[bop.Op] {

			return &Expression{
				Left:       parseExpr(bop.Left),
				Right:      parseExpr(bop.Right),
				Op:         bop.Op,
				Code:       string(bop.AppendString(nil)),
				IsBinaryOp: true,
			}
		}
	}

	// default: just return the literal code as it is
	return &Expression{
		Code:       string(expr.AppendString(nil)),
		IsBinaryOp: false,
	}
}

func Expr2Json(tree *Expression) (string, error) {
	result, err := json.Marshal(tree)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("%s", result), nil
}

func SplitBinaryOp(code string) (string, error) {
	expr, err := metricsql.Parse(code)

	if err != nil {
		return "", err
	}

	node := parseExpr(expr)

	result, err := Expr2Json(node)

	if err != nil {
		return "", err
	}

	return result, nil
}
