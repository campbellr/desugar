"""usage: %prog [-i] FILE

Convert new-style decorator syntax to old-style.

NOTE: this script also destroys any formatting (and comments) that the module may have.

"""
import os
import sys
import ast
import optparse

import codegen


class RewriteDecorator(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        if not node.decorator_list:
            return node

        decorator_list = reversed(node.decorator_list)
        node.decorator_list = []
        args = [ast.Name(id=node.name, ctxt=ast.Load())]
        for deco in decorator_list:
            call = ast.Call(
                func=deco,
                args=args,
                keywords=[],
                starargs=None,
                kwargs=None)
            args = [call]

        assignment = ast.Assign(
            targets=[ast.Name(id=node.name, ctx=ast.Store())],
            value=call)
        return [node, assignment]


def parse_args(args):
    parser = optparse.OptionParser(usage=__doc__)
    parser.add_option(
        '-i', '--in-place', action='store_true', dest='inplace', default=False,
        help='Edit file in place.')

    opts, pargs = parser.parse_args(args)

    if len(pargs) != 1:
        parser.error("Unexpected argument count.")

    path = pargs[0]
    if not os.path.isfile(path):
        parser.error("No such file %r" % path)

    return opts, path


def main(args):
    opts, filepath = parse_args(args)

    filename = os.path.basename(filepath)
    with open(filepath) as f:
        source = f.read()
        module = ast.parse(source, filename)

    RewriteDecorator().visit(module)
    transformed = codegen.to_source(module)

    if opts.inplace:
        with open(filepath, 'w') as f:
            f.write(transformed)
    else:
        print transformed


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except (SystemExit, KeyboardInterrupt):
        pass
    except:
        import traceback
        traceback.print_exc()
        sys.exit(1)
