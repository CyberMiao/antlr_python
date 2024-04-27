# 访问者模式生成抽象语法树
from src.gen.MIDLVisitor import MIDLVisitor
from src.gen.MIDLParser import MIDLParser
from src.TreeNode import TreeNode
from antlr4.tree.Tree import TerminalNodeImpl


class MIDLVisitorAST(MIDLVisitor):

    def __init__(self):
        self.AST = None
        pass

    def visitSpecification(self, ctx: MIDLParser.SpecificationContext):
        root = self.visit(ctx.children[0])
        node = root
        for i in range(1, len(ctx.children)):
            if type(ctx.children[i]) is not TerminalNodeImpl:
                node.add_child(self.visit(ctx.children[i]))
                node = node.get_child(0)
        self.AST = root
        return root

    def visitDefinition(self, ctx: MIDLParser.DefinitionContext):
        return self.visit(ctx.children[0])

    def visitModule(self, ctx: MIDLParser.ModuleContext):
        module = TreeNode('module<'+ctx.children[1].getText()+'>', 'Module')
        definition_root = self.visit(ctx.children[3])
        node = definition_root
        for i in range(4, len(ctx.children)):
            if type(ctx.children[i]) is not TerminalNodeImpl:
                node.add_child(self.visit(ctx.children[i]))
                node = node.get_child(0)
        module.add_child(definition_root)
        return module

    def visitType_decl(self, ctx: MIDLParser.Type_declContext):
        if len(ctx.children) == 2:
            type_decl = TreeNode('type<'+ctx.children[1].getText()+'>', 'Type_decl')
        else:
            type_decl = self.visit(ctx.children[0])
        return type_decl

    def visitStruct_type(self, ctx: MIDLParser.Struct_typeContext):
        struct_type = TreeNode('struct<'+ctx.children[1].getText()+'>', 'Struct_type')
        member_list = self.visit(ctx.children[3])
        struct_type.add_child(member_list)
        return struct_type

    def visitMember_list(self, ctx: MIDLParser.Member_listContext):
        member_list = TreeNode('member_list', 'Member_list')
        if ctx.children is None:
            return member_list
        for i in range(len(ctx.children)):
            if type(ctx.children[i]) is MIDLParser.Type_specContext:
                type_spec = self.visit(ctx.children[i])
                declarators = self.visit(ctx.children[i+1])
                type_spec.add_child(declarators)
                member_list.add_child(type_spec)
        return member_list

    def visitType_spec(self, ctx: MIDLParser.Type_specContext):
        return self.visit(ctx.children[0])

    def visitScoped_name(self, ctx: MIDLParser.Scoped_nameContext):
        # 判断是否含有‘::’
        if ctx.children[0].getText() == '::':
            root = TreeNode('::', 'Scoped_name')
        else:
            root = TreeNode('::'+ctx.children[0].getText(), 'Scoped_name')
        node = root
        for i in range(len(ctx.children)):
            if i >= 2 and ctx.children[i].getText() != '::':
                node.add_child(TreeNode('::'+ctx.children[i].getText()))
                node = node.get_child(0)
        return root

    def visitBase_type_spec(self, ctx: MIDLParser.Base_type_specContext):
        if type(ctx.children[0]) is TerminalNodeImpl:
            return TreeNode(ctx.children[0].getText())
        else:
            return self.visit(ctx.children[0])

    def visitFloating_pt_type(self, ctx: MIDLParser.Floating_pt_typeContext):
        return TreeNode(ctx.children[0].getText())

    def visitInteger_type(self, ctx: MIDLParser.Integer_typeContext):
        return self.visit(ctx.children[0])

    def visitSigned_int(self, ctx: MIDLParser.Signed_intContext):
        return TreeNode(ctx.children[0].getText())

    def visitUnsigned_int(self, ctx: MIDLParser.Unsigned_intContext):
        return TreeNode(ctx.children[0].getText())

    def visitDeclarators(self, ctx: MIDLParser.DeclaratorsContext):
        root = self.visit(ctx.children[0])
        node = root
        for i in range(len(ctx.children)):
            if i != 0 and type(ctx.children[i]) is not TerminalNodeImpl:
                node.add_child(self.visit(ctx.children[i]))
                node = node.get_child(0)
        return root

    def visitDeclarator(self, ctx: MIDLParser.DeclaratorContext):
        return self.visit(ctx.children[0])

    def visitSimple_declarator(self, ctx: MIDLParser.Simple_declaratorContext):
        sim_decl = TreeNode(ctx.children[0].getText()+'=', 'Simple_declarator')
        if len(ctx.children) == 3:
            or_expr = self.visit(ctx.children[2])
            sim_decl.add_child(or_expr)
        return sim_decl

    def visitArray_declarator(self, ctx: MIDLParser.Array_declaratorContext):
        arr_decl = TreeNode(ctx.children[0].getText() + "[]", 'Array_declarator')
        or_expr = self.visit(ctx.children[2])
        arr_decl.add_child(or_expr)
        if len(ctx.children) == 6:
            exp_list = self.visit(ctx.children[5])
            arr_decl.add_child(exp_list)
        return arr_decl

    def visitExp_list(self, ctx: MIDLParser.Exp_listContext):
        root = self.visit(ctx.children[1])
        node = root
        for i in range(len(ctx.children)):
            if i != 1 and type(ctx.children[i]) is not TerminalNodeImpl:
                node.add_child(self.visit(ctx.children[i]))
                node = node.get_child(0)
        return root

    def visitOr_expr(self, ctx: MIDLParser.Or_exprContext):
        or_expr_root = self.visit(ctx.children[0])
        if len(ctx.children) > 1:
            for i in range(1, len(ctx.children)):
                if type(ctx.children[i]) is TerminalNodeImpl:
                    # 匹配到运算符
                    op = TreeNode(ctx.children[i].getText() + self.visit(ctx.children[i+1]).value, 'Or_expr')
                    or_expr_root.add_child(op)
        return or_expr_root

    def visitXor_expr(self, ctx: MIDLParser.Xor_exprContext):
        xor_expr_root = self.visit(ctx.children[0])
        if len(ctx.children) > 1:
            for i in range(1, len(ctx.children)):
                if type(ctx.children[i]) is TerminalNodeImpl:
                    # 匹配到运算符
                    op = TreeNode(ctx.children[i].getText() + self.visit(ctx.children[i + 1]).value, 'Xor_expr')
                    xor_expr_root.add_child(op)
        return xor_expr_root

    def visitAnd_expr(self, ctx: MIDLParser.And_exprContext):
        and_expr_root = self.visit(ctx.children[0])
        if len(ctx.children) > 1:
            for i in range(1, len(ctx.children)):
                if type(ctx.children[i]) is TerminalNodeImpl:
                    # 匹配到运算符
                    op = TreeNode(ctx.children[i].getText() + self.visit(ctx.children[i + 1]).value, 'And_expr')
                    and_expr_root.add_child(op)
        return and_expr_root

    def visitShift_expr(self, ctx: MIDLParser.Shift_exprContext):
        shift_expr_root = self.visit(ctx.children[0])
        if len(ctx.children) > 1:
            for i in range(1, len(ctx.children)):
                if type(ctx.children[i]) is TerminalNodeImpl:
                    # 匹配到运算符
                    op = TreeNode(ctx.children[i].getText() + self.visit(ctx.children[i + 1]).value, 'Shift_expr')
                    shift_expr_root.add_child(op)
        return shift_expr_root

    def visitAdd_expr(self, ctx: MIDLParser.Add_exprContext):
        add_expr_root = self.visit(ctx.children[0])
        if len(ctx.children) > 1:
            for i in range(1, len(ctx.children)):
                if type(ctx.children[i]) is TerminalNodeImpl:
                    # 匹配到运算符
                    op = TreeNode(ctx.children[i].getText() + self.visit(ctx.children[i + 1]).value, 'Add_expr')
                    add_expr_root.add_child(op)
        return add_expr_root

    def visitMult_expr(self, ctx: MIDLParser.Mult_exprContext):
        mult_expr_root = self.visit(ctx.children[0])
        if len(ctx.children) > 1:
            for i in range(1, len(ctx.children)):
                if type(ctx.children[i]) is TerminalNodeImpl:
                    # 匹配到运算符
                    op = TreeNode(ctx.children[i].getText() + self.visit(ctx.children[i + 1]).value, 'Mult_expr')
                    mult_expr_root.add_child(op)
        return mult_expr_root

    def visitUnary_expr(self, ctx: MIDLParser.Unary_exprContext):
        if len(ctx.children) == 2:  # 含有 '+' | '-' | '~'
            value = ctx.children[0].getText() + self.visit(ctx.children[1]).value
            unary_expr = TreeNode(value, 'Unary_expr')
        else:   # 不含前缀
            unary_expr = self.visit(ctx.children[0])
        return unary_expr

    def visitLiteral(self, ctx: MIDLParser.LiteralContext):
        literal = TreeNode(ctx.getText(), 'Literal')
        self.visit(ctx.children[0])
        return literal
