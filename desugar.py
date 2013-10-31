""" A script that converts new-style decorator syntax to old-style.

eg:

"""
import sys
import ast

class RewriteDecorator(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        print node
        if not node.decorator_list:
            return node
        print dir(node)
        print node._fields
        super(RewriteDecorator, self).generic_visit(node)

def main(args):
    assert len(args) == 1
    filename = args[0]
    module = ast.parse(open(filename).read())
    transformed = RewriteDecorator().visit(module)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except:
        import traceback
        traceback.print_exc()
        sys.exit(1)
