# Generated from E:/work/compile/antlr-python/MIDL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MIDLParser import MIDLParser
else:
    from MIDLParser import MIDLParser

# This class defines a complete generic visitor for a parse tree produced by MIDLParser.

class MIDLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MIDLParser#specification.
    def visitSpecification(self, ctx:MIDLParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#definition.
    def visitDefinition(self, ctx:MIDLParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#module.
    def visitModule(self, ctx:MIDLParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#type_decl.
    def visitType_decl(self, ctx:MIDLParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#struct_type.
    def visitStruct_type(self, ctx:MIDLParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#member_list.
    def visitMember_list(self, ctx:MIDLParser.Member_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#type_spec.
    def visitType_spec(self, ctx:MIDLParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#scoped_name.
    def visitScoped_name(self, ctx:MIDLParser.Scoped_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#base_type_spec.
    def visitBase_type_spec(self, ctx:MIDLParser.Base_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#floating_pt_type.
    def visitFloating_pt_type(self, ctx:MIDLParser.Floating_pt_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#integer_type.
    def visitInteger_type(self, ctx:MIDLParser.Integer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#signed_int.
    def visitSigned_int(self, ctx:MIDLParser.Signed_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#unsigned_int.
    def visitUnsigned_int(self, ctx:MIDLParser.Unsigned_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#declarators.
    def visitDeclarators(self, ctx:MIDLParser.DeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#declarator.
    def visitDeclarator(self, ctx:MIDLParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#simple_declarator.
    def visitSimple_declarator(self, ctx:MIDLParser.Simple_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#array_declarator.
    def visitArray_declarator(self, ctx:MIDLParser.Array_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#exp_list.
    def visitExp_list(self, ctx:MIDLParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#or_expr.
    def visitOr_expr(self, ctx:MIDLParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#xor_expr.
    def visitXor_expr(self, ctx:MIDLParser.Xor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#and_expr.
    def visitAnd_expr(self, ctx:MIDLParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#shift_expr.
    def visitShift_expr(self, ctx:MIDLParser.Shift_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#add_expr.
    def visitAdd_expr(self, ctx:MIDLParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#mult_expr.
    def visitMult_expr(self, ctx:MIDLParser.Mult_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#unary_expr.
    def visitUnary_expr(self, ctx:MIDLParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MIDLParser#literal.
    def visitLiteral(self, ctx:MIDLParser.LiteralContext):
        return self.visitChildren(ctx)



del MIDLParser