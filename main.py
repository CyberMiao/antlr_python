import os.path
import shutil
import sys
from antlr4 import *

from src.SyntaxException import SyntaxException
from src.gen.MIDLLexer import MIDLLexer
from src.gen.MIDLParser import MIDLParser
from src.MIDLVisitorAST import MIDLVisitorAST


def main(input_file_path, output_dir_path):
    # 加载输入文件
    input_stream = FileStream(input_file_path)
    # 词法、语法检查
    lexer = MIDLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MIDLParser(stream)
    tree = parser.specification()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise Exception('语法错误')
    else:
        if os.path.exists(output_dir_path):
            # 删除原有文件夹
            shutil.rmtree(output_dir_path)
        # 重新创建文件夹
        os.mkdir(output_dir_path)
        # 定义抽象语法树
        visitor_ast = MIDLVisitorAST()
        try:
            visitor_ast.visit(tree)
        except SyntaxException as exception:
            print('文件{}第{}行错误，{}'.format(input_file_path, exception.line, exception.info))
            exit(0)
        ast = visitor_ast.AST
        # 保存到输出文件夹
        ast.save_tree_to_file(output_dir_path)


if __name__ == '__main__':
    if sys.argv[1] == 'test':
        test_case_path = 'test/test_case'
        case_list = os.listdir(test_case_path)
        for case in case_list:
            try:
                case_path = test_case_path + '/' + case
                out_path = 'test/test_output/' + case.removesuffix('.idl')
                main(case_path, out_path)
            except Exception as e:
                print(case, e)
            else:
                print(case, ' done!')

    else:
        input_path = sys.argv[1]
        # 定义输出文件夹名称
        if len(sys.argv) > 2:
            output_path = sys.argv[2]
        else:
            output_path = input_path.removesuffix('.idl')
        main(input_path, output_path)

