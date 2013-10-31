""" A script that converts new-style decorator syntax to old-style.

NOTE: this script also destroys any formatting (and comments) that the module may have.

"""
import os
import sys
import ast

import codegen


class RewriteDecorator(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        if not node.decorator_list:
            return node
        decorator_list = node.decorator_list
        node.decorator_list = []
        # TODO: enhance to support multiple decorators
        assert len(decorator_list) == 1, 'Multiple decorators unsupported!'
        decorator = decorator_list[0]
        return [
            node,
            ast.Assign(
                targets=[ast.Name(id=node.name, ctx=ast.Store())],
                value=ast.Call(
                    func=decorator,
                    args=[ast.Name(id=node.name, ctxt=ast.Load())],
                    keywords=[],
                    starargs=None,
                    kwargs=None)
            )
        ]


def main(args):
    assert len(args) == 1
    filepath = args[0]
    filename = os.path.basename(filepath)
    with open(filepath) as f:
        source = f.read()
        module = ast.parse(source, filename)

    RewriteDecorator().visit(module)
    print codegen.to_source(module)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except:
        import traceback
        traceback.print_exc()
        sys.exit(1)
