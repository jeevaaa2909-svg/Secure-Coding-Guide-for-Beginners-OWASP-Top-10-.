"""Small educational AST scanner for a few risky Python coding patterns.

This is a teaching aid, not a replacement for code review or a full SAST tool.
It reports obvious examples such as eval/exec calls and SQL execute calls
whose first argument is built using string concatenation or f-strings.
"""
import ast
import sys
from pathlib import Path


class ChecklistVisitor(ast.NodeVisitor):
    def __init__(self):
        self.findings = []

    def visit_Call(self, node):
        name = ""
        if isinstance(node.func, ast.Name):
            name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            name = node.func.attr

        if name in {"eval", "exec"}:
            self.findings.append(
                (node.lineno, "CHK-01", f"Review use of {name}() with untrusted input")
            )

        if name == "execute" and node.args:
            query = node.args[0]
            if isinstance(query, (ast.JoinedStr, ast.BinOp)):
                self.findings.append(
                    (node.lineno, "CHK-02", "Possible dynamically-built SQL; use bound parameters")
                )

        self.generic_visit(node)


def scan(path: Path) -> int:
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
    except (OSError, SyntaxError) as exc:
        print(f"Could not scan {path}: {exc}")
        return 2

    visitor = ChecklistVisitor()
    visitor.visit(tree)

    if not visitor.findings:
        print(f"[OK] No selected patterns detected in {path}")
        print("Note: this limited scanner cannot prove that code is secure.")
        return 0

    for line, code, advice in visitor.findings:
        print(f"[REVIEW] {path}:{line} {code} - {advice}")
    return 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python automation/security_checklist_scanner.py <python-file>")
        raise SystemExit(2)
    raise SystemExit(scan(Path(sys.argv[1])))
