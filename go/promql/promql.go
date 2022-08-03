package promql

import (
	"fmt"

	"encoding/json"
	"github.com/VictoriaMetrics/metricsql"
)

// ModifierExpr represents MetricsQL modifier such as `<op> (...)`
type ModifierExpr struct {
	// Op is modifier operation.
	Op string `json:"op"`

	// Args contains modifier args from parens.
	Args []string `json:"args"`
}

type Expression struct {
	// if true, all fields are set
	// if false, then it's a normal expression, only `code` is set
	IsBinaryOp bool `json:"is_binary_op"`

	Left  *Expression `json:"left"`
	Right *Expression `json:"right"`
	Op    string      `json:"op"`
	// GroupModifier contains modifier such as "on" or "ignoring".
	GroupModifier ModifierExpr `json:"group_modifier"`
	// JoinModifier contains modifier such as "group_left" or "group_right".
	JoinModifier ModifierExpr `json:"join_modifier"`

	Code string `json:"code"`
}

var compareOps = map[string]bool{
	"==": true,
	"!=": true,
	">":  true,
	"<":  true,
	">=": true,
	"<=": true,
}

var logicalOps = map[string]bool{
	"and":    true,
	"or":     true,
	"unless": true,
}

// if `mustBeExpression` is true, means that the last level is compareOps
// or ready.
// example:
// (a > 10) > b
// result: a > 10 is expression, compare to b
func parseExpr(expr metricsql.Expr, mustBeExpression bool) *Expression {

    // I am sure it is a normal expression!
	if mustBeExpression {
		return &Expression{
			Code:       string(expr.AppendString(nil)),
			IsBinaryOp: false,
		}
	}

	if bop, ok := expr.(*metricsql.BinaryOpExpr); ok {

		if logicalOps[bop.Op] {

			return &Expression{
				Left:          parseExpr(bop.Left, false),
				Right:         parseExpr(bop.Right, false),
				GroupModifier: ModifierExpr(bop.GroupModifier),
				JoinModifier:  ModifierExpr(bop.JoinModifier),
				Op:            bop.Op,
				Code:          string(bop.AppendString(nil)),
				IsBinaryOp:    true,
			}
		}

		if compareOps[bop.Op] {
			return &Expression{
				Left:          parseExpr(bop.Left, true),
				Right:         parseExpr(bop.Right, true),
				GroupModifier: ModifierExpr(bop.GroupModifier),
				JoinModifier:  ModifierExpr(bop.JoinModifier),
				Op:            bop.Op,
				Code:          string(bop.AppendString(nil)),
				IsBinaryOp:    true,
			}

		}
	}

	// treat +,-,* etc still as normal expression
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

	node := parseExpr(expr, false)

	result, err := Expr2Json(node)

	if err != nil {
		return "", err
	}

	return result, nil
}
