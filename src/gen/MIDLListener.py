# Generated from E:/work/compile/antlr-python/MIDL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MIDLParser import MIDLParser
else:
    from MIDLParser import MIDLParser

# This class defines a complete listener for a parse tree produced by MIDLParser.
class MIDLListener(ParseTreeListener):

    # Enter a parse tree produced by MIDLParser#specification.
    def enterSpecification(self, ctx:MIDLParser.SpecificationContext):
        pass

    # Exit a parse tree produced by MIDLParser#specification.
    def exitSpecification(self, ctx:MIDLParser.SpecificationContext):
        pass


    # Enter a parse tree produced by MIDLParser#definition.
    def enterDefinition(self, ctx:MIDLParser.DefinitionContext):
        pass

    # Exit a parse tree produced by MIDLParser#definition.
    def exitDefinition(self, ctx:MIDLParser.DefinitionContext):
        pass


    # Enter a parse tree produced by MIDLParser#module.
    def enterModule(self, ctx:MIDLParser.ModuleContext):
        pass

    # Exit a parse tree produced by MIDLParser#module.
    def exitModule(self, ctx:MIDLParser.ModuleContext):
        pass


    # Enter a parse tree produced by MIDLParser#type_decl.
    def enterType_decl(self, ctx:MIDLParser.Type_declContext):
        pass

    # Exit a parse tree produced by MIDLParser#type_decl.
    def exitType_decl(self, ctx:MIDLParser.Type_declContext):
        pass


    # Enter a parse tree produced by MIDLParser#struct_type.
    def enterStruct_type(self, ctx:MIDLParser.Struct_typeContext):
        pass

    # Exit a parse tree produced by MIDLParser#struct_type.
    def exitStruct_type(self, ctx:MIDLParser.Struct_typeContext):
        pass


    # Enter a parse tree produced by MIDLParser#member_list.
    def enterMember_list(self, ctx:MIDLParser.Member_listContext):
        pass

    # Exit a parse tree produced by MIDLParser#member_list.
    def exitMember_list(self, ctx:MIDLParser.Member_listContext):
        pass


    # Enter a parse tree produced by MIDLParser#type_spec.
    def enterType_spec(self, ctx:MIDLParser.Type_specContext):
        pass

    # Exit a parse tree produced by MIDLParser#type_spec.
    def exitType_spec(self, ctx:MIDLParser.Type_specContext):
        pass


    # Enter a parse tree produced by MIDLParser#scoped_name.
    def enterScoped_name(self, ctx:MIDLParser.Scoped_nameContext):
        pass

    # Exit a parse tree produced by MIDLParser#scoped_name.
    def exitScoped_name(self, ctx:MIDLParser.Scoped_nameContext):
        pass


    # Enter a parse tree produced by MIDLParser#base_type_spec.
    def enterBase_type_spec(self, ctx:MIDLParser.Base_type_specContext):
        pass

    # Exit a parse tree produced by MIDLParser#base_type_spec.
    def exitBase_type_spec(self, ctx:MIDLParser.Base_type_specContext):
        pass


    # Enter a parse tree produced by MIDLParser#floating_pt_type.
    def enterFloating_pt_type(self, ctx:MIDLParser.Floating_pt_typeContext):
        pass

    # Exit a parse tree produced by MIDLParser#floating_pt_type.
    def exitFloating_pt_type(self, ctx:MIDLParser.Floating_pt_typeContext):
        pass


    # Enter a parse tree produced by MIDLParser#integer_type.
    def enterInteger_type(self, ctx:MIDLParser.Integer_typeContext):
        pass

    # Exit a parse tree produced by MIDLParser#integer_type.
    def exitInteger_type(self, ctx:MIDLParser.Integer_typeContext):
        pass


    # Enter a parse tree produced by MIDLParser#signed_int.
    def enterSigned_int(self, ctx:MIDLParser.Signed_intContext):
        pass

    # Exit a parse tree produced by MIDLParser#signed_int.
    def exitSigned_int(self, ctx:MIDLParser.Signed_intContext):
        pass


    # Enter a parse tree produced by MIDLParser#unsigned_int.
    def enterUnsigned_int(self, ctx:MIDLParser.Unsigned_intContext):
        pass

    # Exit a parse tree produced by MIDLParser#unsigned_int.
    def exitUnsigned_int(self, ctx:MIDLParser.Unsigned_intContext):
        pass


    # Enter a parse tree produced by MIDLParser#declarators.
    def enterDeclarators(self, ctx:MIDLParser.DeclaratorsContext):
        pass

    # Exit a parse tree produced by MIDLParser#declarators.
    def exitDeclarators(self, ctx:MIDLParser.DeclaratorsContext):
        pass


    # Enter a parse tree produced by MIDLParser#declarator.
    def enterDeclarator(self, ctx:MIDLParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by MIDLParser#declarator.
    def exitDeclarator(self, ctx:MIDLParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by MIDLParser#simple_declarator.
    def enterSimple_declarator(self, ctx:MIDLParser.Simple_declaratorContext):
        pass

    # Exit a parse tree produced by MIDLParser#simple_declarator.
    def exitSimple_declarator(self, ctx:MIDLParser.Simple_declaratorContext):
        pass


    # Enter a parse tree produced by MIDLParser#array_declarator.
    def enterArray_declarator(self, ctx:MIDLParser.Array_declaratorContext):
        pass

    # Exit a parse tree produced by MIDLParser#array_declarator.
    def exitArray_declarator(self, ctx:MIDLParser.Array_declaratorContext):
        pass


    # Enter a parse tree produced by MIDLParser#exp_list.
    def enterExp_list(self, ctx:MIDLParser.Exp_listContext):
        pass

    # Exit a parse tree produced by MIDLParser#exp_list.
    def exitExp_list(self, ctx:MIDLParser.Exp_listContext):
        pass


    # Enter a parse tree produced by MIDLParser#or_expr.
    def enterOr_expr(self, ctx:MIDLParser.Or_exprContext):
        pass

    # Exit a parse tree produced by MIDLParser#or_expr.
    def exitOr_expr(self, ctx:MIDLParser.Or_exprContext):
        pass


    # Enter a parse tree produced by MIDLParser#xor_expr.
    def enterXor_expr(self, ctx:MIDLParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by MIDLParser#xor_expr.
    def exitXor_expr(self, ctx:MIDLParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by MIDLParser#and_expr.
    def enterAnd_expr(self, ctx:MIDLParser.And_exprContext):
        pass

    # Exit a parse tree produced by MIDLParser#and_expr.
    def exitAnd_expr(self, ctx:MIDLParser.And_exprContext):
        pass


    # Enter a parse tree produced by MIDLParser#shift_expr.
    def enterShift_expr(self, ctx:MIDLParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by MIDLParser#shift_expr.
    def exitShift_expr(self, ctx:MIDLParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by MIDLParser#add_expr.
    def enterAdd_expr(self, ctx:MIDLParser.Add_exprContext):
        pass

    # Exit a parse tree produced by MIDLParser#add_expr.
    def exitAdd_expr(self, ctx:MIDLParser.Add_exprContext):
        pass


    # Enter a parse tree produced by MIDLParser#mult_expr.
    def enterMult_expr(self, ctx:MIDLParser.Mult_exprContext):
        pass

    # Exit a parse tree produced by MIDLParser#mult_expr.
    def exitMult_expr(self, ctx:MIDLParser.Mult_exprContext):
        pass


    # Enter a parse tree produced by MIDLParser#unary_expr.
    def enterUnary_expr(self, ctx:MIDLParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by MIDLParser#unary_expr.
    def exitUnary_expr(self, ctx:MIDLParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by MIDLParser#literal.
    def enterLiteral(self, ctx:MIDLParser.LiteralContext):
        pass

    # Exit a parse tree produced by MIDLParser#literal.
    def exitLiteral(self, ctx:MIDLParser.LiteralContext):
        pass



del MIDLParser