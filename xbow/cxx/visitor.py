from clang.cindex import CursorKind
class Visitor:
    def visit_children(self: 'Visitor', node):
        for child in node.get_children():
            self.visit(child)

    def pre_visit(self: 'Visitor', node):
        pass

    def post_visit(self: 'Visitor', node):
        pass

    def visit_generic(self: 'Visitor', node):
        pass

    def visit(self: 'Visitor', node):
        self.pre_visit(node)

        if node.kind == CursorKind.UNEXPOSED_DECL:
            self.visit_UnexposedDecl(node)


        if node.kind == CursorKind.STRUCT_DECL:
            self.visit_StructDecl(node)


        if node.kind == CursorKind.UNION_DECL:
            self.visit_UnionDecl(node)


        if node.kind == CursorKind.CLASS_DECL:
            self.visit_ClassDecl(node)


        if node.kind == CursorKind.ENUM_DECL:
            self.visit_EnumDecl(node)


        if node.kind == CursorKind.FIELD_DECL:
            self.visit_FieldDecl(node)


        if node.kind == CursorKind.ENUM_CONSTANT_DECL:
            self.visit_EnumConstantDecl(node)


        if node.kind == CursorKind.FUNCTION_DECL:
            self.visit_FunctionDecl(node)


        if node.kind == CursorKind.VAR_DECL:
            self.visit_VarDecl(node)


        if node.kind == CursorKind.PARM_DECL:
            self.visit_ParmDecl(node)


        if node.kind == CursorKind.OBJC_INTERFACE_DECL:
            self.visit_ObjcInterfaceDecl(node)


        if node.kind == CursorKind.OBJC_CATEGORY_DECL:
            self.visit_ObjcCategoryDecl(node)


        if node.kind == CursorKind.OBJC_PROTOCOL_DECL:
            self.visit_ObjcProtocolDecl(node)


        if node.kind == CursorKind.OBJC_PROPERTY_DECL:
            self.visit_ObjcPropertyDecl(node)


        if node.kind == CursorKind.OBJC_IVAR_DECL:
            self.visit_ObjcIvarDecl(node)


        if node.kind == CursorKind.OBJC_INSTANCE_METHOD_DECL:
            self.visit_ObjcInstanceMethodDecl(node)


        if node.kind == CursorKind.OBJC_CLASS_METHOD_DECL:
            self.visit_ObjcClassMethodDecl(node)


        if node.kind == CursorKind.OBJC_IMPLEMENTATION_DECL:
            self.visit_ObjcImplementationDecl(node)


        if node.kind == CursorKind.OBJC_CATEGORY_IMPL_DECL:
            self.visit_ObjcCategoryImplDecl(node)


        if node.kind == CursorKind.TYPEDEF_DECL:
            self.visit_TypedefDecl(node)


        if node.kind == CursorKind.CXX_METHOD:
            self.visit_CxxMethod(node)


        if node.kind == CursorKind.NAMESPACE:
            self.visit_Namespace(node)


        if node.kind == CursorKind.LINKAGE_SPEC:
            self.visit_LinkageSpec(node)


        if node.kind == CursorKind.CONSTRUCTOR:
            self.visit_Constructor(node)


        if node.kind == CursorKind.DESTRUCTOR:
            self.visit_Destructor(node)


        if node.kind == CursorKind.CONVERSION_FUNCTION:
            self.visit_ConversionFunction(node)


        if node.kind == CursorKind.TEMPLATE_TYPE_PARAMETER:
            self.visit_TemplateTypeParameter(node)


        if node.kind == CursorKind.TEMPLATE_NON_TYPE_PARAMETER:
            self.visit_TemplateNonTypeParameter(node)


        if node.kind == CursorKind.TEMPLATE_TEMPLATE_PARAMETER:
            self.visit_TemplateTemplateParameter(node)


        if node.kind == CursorKind.FUNCTION_TEMPLATE:
            self.visit_FunctionTemplate(node)


        if node.kind == CursorKind.CLASS_TEMPLATE:
            self.visit_ClassTemplate(node)


        if node.kind == CursorKind.CLASS_TEMPLATE_PARTIAL_SPECIALIZATION:
            self.visit_ClassTemplatePartialSpecialization(node)


        if node.kind == CursorKind.NAMESPACE_ALIAS:
            self.visit_NamespaceAlias(node)


        if node.kind == CursorKind.USING_DIRECTIVE:
            self.visit_UsingDirective(node)


        if node.kind == CursorKind.USING_DECLARATION:
            self.visit_UsingDeclaration(node)


        if node.kind == CursorKind.TYPE_ALIAS_DECL:
            self.visit_TypeAliasDecl(node)


        if node.kind == CursorKind.OBJC_SYNTHESIZE_DECL:
            self.visit_ObjcSynthesizeDecl(node)


        if node.kind == CursorKind.OBJC_DYNAMIC_DECL:
            self.visit_ObjcDynamicDecl(node)


        if node.kind == CursorKind.CXX_ACCESS_SPEC_DECL:
            self.visit_CxxAccessSpecDecl(node)


        if node.kind == CursorKind.OBJC_SUPER_CLASS_REF:
            self.visit_ObjcSuperClassRef(node)


        if node.kind == CursorKind.OBJC_PROTOCOL_REF:
            self.visit_ObjcProtocolRef(node)


        if node.kind == CursorKind.OBJC_CLASS_REF:
            self.visit_ObjcClassRef(node)


        if node.kind == CursorKind.TYPE_REF:
            self.visit_TypeRef(node)


        if node.kind == CursorKind.CXX_BASE_SPECIFIER:
            self.visit_CxxBaseSpecifier(node)


        if node.kind == CursorKind.TEMPLATE_REF:
            self.visit_TemplateRef(node)


        if node.kind == CursorKind.NAMESPACE_REF:
            self.visit_NamespaceRef(node)


        if node.kind == CursorKind.MEMBER_REF:
            self.visit_MemberRef(node)


        if node.kind == CursorKind.LABEL_REF:
            self.visit_LabelRef(node)


        if node.kind == CursorKind.OVERLOADED_DECL_REF:
            self.visit_OverloadedDeclRef(node)


        if node.kind == CursorKind.VARIABLE_REF:
            self.visit_VariableRef(node)


        if node.kind == CursorKind.INVALID_FILE:
            self.visit_InvalidFile(node)


        if node.kind == CursorKind.NO_DECL_FOUND:
            self.visit_NoDeclFound(node)


        if node.kind == CursorKind.NOT_IMPLEMENTED:
            self.visit_NotImplemented(node)


        if node.kind == CursorKind.INVALID_CODE:
            self.visit_InvalidCode(node)


        if node.kind == CursorKind.UNEXPOSED_EXPR:
            self.visit_UnexposedExpr(node)


        if node.kind == CursorKind.DECL_REF_EXPR:
            self.visit_DeclRefExpr(node)


        if node.kind == CursorKind.MEMBER_REF_EXPR:
            self.visit_MemberRefExpr(node)


        if node.kind == CursorKind.CALL_EXPR:
            self.visit_CallExpr(node)


        if node.kind == CursorKind.OBJC_MESSAGE_EXPR:
            self.visit_ObjcMessageExpr(node)


        if node.kind == CursorKind.BLOCK_EXPR:
            self.visit_BlockExpr(node)


        if node.kind == CursorKind.INTEGER_LITERAL:
            self.visit_IntegerLiteral(node)


        if node.kind == CursorKind.FLOATING_LITERAL:
            self.visit_FloatingLiteral(node)


        if node.kind == CursorKind.IMAGINARY_LITERAL:
            self.visit_ImaginaryLiteral(node)


        if node.kind == CursorKind.STRING_LITERAL:
            self.visit_StringLiteral(node)


        if node.kind == CursorKind.CHARACTER_LITERAL:
            self.visit_CharacterLiteral(node)


        if node.kind == CursorKind.PAREN_EXPR:
            self.visit_ParenExpr(node)


        if node.kind == CursorKind.UNARY_OPERATOR:
            self.visit_UnaryOperator(node)


        if node.kind == CursorKind.ARRAY_SUBSCRIPT_EXPR:
            self.visit_ArraySubscriptExpr(node)


        if node.kind == CursorKind.BINARY_OPERATOR:
            self.visit_BinaryOperator(node)


        if node.kind == CursorKind.COMPOUND_ASSIGNMENT_OPERATOR:
            self.visit_CompoundAssignmentOperator(node)


        if node.kind == CursorKind.CONDITIONAL_OPERATOR:
            self.visit_ConditionalOperator(node)


        if node.kind == CursorKind.CSTYLE_CAST_EXPR:
            self.visit_CstyleCastExpr(node)


        if node.kind == CursorKind.COMPOUND_LITERAL_EXPR:
            self.visit_CompoundLiteralExpr(node)


        if node.kind == CursorKind.INIT_LIST_EXPR:
            self.visit_InitListExpr(node)


        if node.kind == CursorKind.ADDR_LABEL_EXPR:
            self.visit_AddrLabelExpr(node)


        if node.kind == CursorKind.StmtExpr:
            self.visit_Stmtexpr(node)


        if node.kind == CursorKind.GENERIC_SELECTION_EXPR:
            self.visit_GenericSelectionExpr(node)


        if node.kind == CursorKind.GNU_NULL_EXPR:
            self.visit_GnuNullExpr(node)


        if node.kind == CursorKind.CXX_STATIC_CAST_EXPR:
            self.visit_CxxStaticCastExpr(node)


        if node.kind == CursorKind.CXX_DYNAMIC_CAST_EXPR:
            self.visit_CxxDynamicCastExpr(node)


        if node.kind == CursorKind.CXX_REINTERPRET_CAST_EXPR:
            self.visit_CxxReinterpretCastExpr(node)


        if node.kind == CursorKind.CXX_CONST_CAST_EXPR:
            self.visit_CxxConstCastExpr(node)


        if node.kind == CursorKind.CXX_FUNCTIONAL_CAST_EXPR:
            self.visit_CxxFunctionalCastExpr(node)


        if node.kind == CursorKind.CXX_TYPEID_EXPR:
            self.visit_CxxTypeidExpr(node)


        if node.kind == CursorKind.CXX_BOOL_LITERAL_EXPR:
            self.visit_CxxBoolLiteralExpr(node)


        if node.kind == CursorKind.CXX_NULL_PTR_LITERAL_EXPR:
            self.visit_CxxNullPtrLiteralExpr(node)


        if node.kind == CursorKind.CXX_THIS_EXPR:
            self.visit_CxxThisExpr(node)


        if node.kind == CursorKind.CXX_THROW_EXPR:
            self.visit_CxxThrowExpr(node)


        if node.kind == CursorKind.CXX_NEW_EXPR:
            self.visit_CxxNewExpr(node)


        if node.kind == CursorKind.CXX_DELETE_EXPR:
            self.visit_CxxDeleteExpr(node)


        if node.kind == CursorKind.CXX_UNARY_EXPR:
            self.visit_CxxUnaryExpr(node)


        if node.kind == CursorKind.OBJC_STRING_LITERAL:
            self.visit_ObjcStringLiteral(node)


        if node.kind == CursorKind.OBJC_ENCODE_EXPR:
            self.visit_ObjcEncodeExpr(node)


        if node.kind == CursorKind.OBJC_SELECTOR_EXPR:
            self.visit_ObjcSelectorExpr(node)


        if node.kind == CursorKind.OBJC_PROTOCOL_EXPR:
            self.visit_ObjcProtocolExpr(node)


        if node.kind == CursorKind.OBJC_BRIDGE_CAST_EXPR:
            self.visit_ObjcBridgeCastExpr(node)


        if node.kind == CursorKind.PACK_EXPANSION_EXPR:
            self.visit_PackExpansionExpr(node)


        if node.kind == CursorKind.SIZE_OF_PACK_EXPR:
            self.visit_SizeOfPackExpr(node)


        if node.kind == CursorKind.LAMBDA_EXPR:
            self.visit_LambdaExpr(node)


        if node.kind == CursorKind.OBJ_BOOL_LITERAL_EXPR:
            self.visit_ObjBoolLiteralExpr(node)


        if node.kind == CursorKind.OBJ_SELF_EXPR:
            self.visit_ObjSelfExpr(node)


        if node.kind == CursorKind.OMP_ARRAY_SECTION_EXPR:
            self.visit_OmpArraySectionExpr(node)


        if node.kind == CursorKind.OBJC_AVAILABILITY_CHECK_EXPR:
            self.visit_ObjcAvailabilityCheckExpr(node)


        if node.kind == CursorKind.UNEXPOSED_STMT:
            self.visit_UnexposedStmt(node)


        if node.kind == CursorKind.LABEL_STMT:
            self.visit_LabelStmt(node)


        if node.kind == CursorKind.COMPOUND_STMT:
            self.visit_CompoundStmt(node)


        if node.kind == CursorKind.CASE_STMT:
            self.visit_CaseStmt(node)


        if node.kind == CursorKind.DEFAULT_STMT:
            self.visit_DefaultStmt(node)


        if node.kind == CursorKind.IF_STMT:
            self.visit_IfStmt(node)


        if node.kind == CursorKind.SWITCH_STMT:
            self.visit_SwitchStmt(node)


        if node.kind == CursorKind.WHILE_STMT:
            self.visit_WhileStmt(node)


        if node.kind == CursorKind.DO_STMT:
            self.visit_DoStmt(node)


        if node.kind == CursorKind.FOR_STMT:
            self.visit_ForStmt(node)


        if node.kind == CursorKind.GOTO_STMT:
            self.visit_GotoStmt(node)


        if node.kind == CursorKind.INDIRECT_GOTO_STMT:
            self.visit_IndirectGotoStmt(node)


        if node.kind == CursorKind.CONTINUE_STMT:
            self.visit_ContinueStmt(node)


        if node.kind == CursorKind.BREAK_STMT:
            self.visit_BreakStmt(node)


        if node.kind == CursorKind.RETURN_STMT:
            self.visit_ReturnStmt(node)


        if node.kind == CursorKind.ASM_STMT:
            self.visit_AsmStmt(node)


        if node.kind == CursorKind.OBJC_AT_TRY_STMT:
            self.visit_ObjcAtTryStmt(node)


        if node.kind == CursorKind.OBJC_AT_CATCH_STMT:
            self.visit_ObjcAtCatchStmt(node)


        if node.kind == CursorKind.OBJC_AT_FINALLY_STMT:
            self.visit_ObjcAtFinallyStmt(node)


        if node.kind == CursorKind.OBJC_AT_THROW_STMT:
            self.visit_ObjcAtThrowStmt(node)


        if node.kind == CursorKind.OBJC_AT_SYNCHRONIZED_STMT:
            self.visit_ObjcAtSynchronizedStmt(node)


        if node.kind == CursorKind.OBJC_AUTORELEASE_POOL_STMT:
            self.visit_ObjcAutoreleasePoolStmt(node)


        if node.kind == CursorKind.OBJC_FOR_COLLECTION_STMT:
            self.visit_ObjcForCollectionStmt(node)


        if node.kind == CursorKind.CXX_CATCH_STMT:
            self.visit_CxxCatchStmt(node)


        if node.kind == CursorKind.CXX_TRY_STMT:
            self.visit_CxxTryStmt(node)


        if node.kind == CursorKind.CXX_FOR_RANGE_STMT:
            self.visit_CxxForRangeStmt(node)


        if node.kind == CursorKind.SEH_TRY_STMT:
            self.visit_SehTryStmt(node)


        if node.kind == CursorKind.SEH_EXCEPT_STMT:
            self.visit_SehExceptStmt(node)


        if node.kind == CursorKind.SEH_FINALLY_STMT:
            self.visit_SehFinallyStmt(node)


        if node.kind == CursorKind.MS_ASM_STMT:
            self.visit_MsAsmStmt(node)


        if node.kind == CursorKind.NULL_STMT:
            self.visit_NullStmt(node)


        if node.kind == CursorKind.DECL_STMT:
            self.visit_DeclStmt(node)


        if node.kind == CursorKind.OMP_PARALLEL_DIRECTIVE:
            self.visit_OmpParallelDirective(node)


        if node.kind == CursorKind.OMP_SIMD_DIRECTIVE:
            self.visit_OmpSimdDirective(node)


        if node.kind == CursorKind.OMP_FOR_DIRECTIVE:
            self.visit_OmpForDirective(node)


        if node.kind == CursorKind.OMP_SECTIONS_DIRECTIVE:
            self.visit_OmpSectionsDirective(node)


        if node.kind == CursorKind.OMP_SECTION_DIRECTIVE:
            self.visit_OmpSectionDirective(node)


        if node.kind == CursorKind.OMP_SINGLE_DIRECTIVE:
            self.visit_OmpSingleDirective(node)


        if node.kind == CursorKind.OMP_PARALLEL_FOR_DIRECTIVE:
            self.visit_OmpParallelForDirective(node)


        if node.kind == CursorKind.OMP_PARALLEL_SECTIONS_DIRECTIVE:
            self.visit_OmpParallelSectionsDirective(node)


        if node.kind == CursorKind.OMP_TASK_DIRECTIVE:
            self.visit_OmpTaskDirective(node)


        if node.kind == CursorKind.OMP_MASTER_DIRECTIVE:
            self.visit_OmpMasterDirective(node)


        if node.kind == CursorKind.OMP_CRITICAL_DIRECTIVE:
            self.visit_OmpCriticalDirective(node)


        if node.kind == CursorKind.OMP_TASKYIELD_DIRECTIVE:
            self.visit_OmpTaskyieldDirective(node)


        if node.kind == CursorKind.OMP_BARRIER_DIRECTIVE:
            self.visit_OmpBarrierDirective(node)


        if node.kind == CursorKind.OMP_TASKWAIT_DIRECTIVE:
            self.visit_OmpTaskwaitDirective(node)


        if node.kind == CursorKind.OMP_FLUSH_DIRECTIVE:
            self.visit_OmpFlushDirective(node)


        if node.kind == CursorKind.SEH_LEAVE_STMT:
            self.visit_SehLeaveStmt(node)


        if node.kind == CursorKind.OMP_ORDERED_DIRECTIVE:
            self.visit_OmpOrderedDirective(node)


        if node.kind == CursorKind.OMP_ATOMIC_DIRECTIVE:
            self.visit_OmpAtomicDirective(node)


        if node.kind == CursorKind.OMP_FOR_SIMD_DIRECTIVE:
            self.visit_OmpForSimdDirective(node)


        if node.kind == CursorKind.OMP_PARALLELFORSIMD_DIRECTIVE:
            self.visit_OmpParallelforsimdDirective(node)


        if node.kind == CursorKind.OMP_TARGET_DIRECTIVE:
            self.visit_OmpTargetDirective(node)


        if node.kind == CursorKind.OMP_TEAMS_DIRECTIVE:
            self.visit_OmpTeamsDirective(node)


        if node.kind == CursorKind.OMP_TASKGROUP_DIRECTIVE:
            self.visit_OmpTaskgroupDirective(node)


        if node.kind == CursorKind.OMP_CANCELLATION_POINT_DIRECTIVE:
            self.visit_OmpCancellationPointDirective(node)


        if node.kind == CursorKind.OMP_CANCEL_DIRECTIVE:
            self.visit_OmpCancelDirective(node)


        if node.kind == CursorKind.OMP_TARGET_DATA_DIRECTIVE:
            self.visit_OmpTargetDataDirective(node)


        if node.kind == CursorKind.OMP_TASK_LOOP_DIRECTIVE:
            self.visit_OmpTaskLoopDirective(node)


        if node.kind == CursorKind.OMP_TASK_LOOP_SIMD_DIRECTIVE:
            self.visit_OmpTaskLoopSimdDirective(node)


        if node.kind == CursorKind.OMP_DISTRIBUTE_DIRECTIVE:
            self.visit_OmpDistributeDirective(node)


        if node.kind == CursorKind.OMP_TARGET_ENTER_DATA_DIRECTIVE:
            self.visit_OmpTargetEnterDataDirective(node)


        if node.kind == CursorKind.OMP_TARGET_EXIT_DATA_DIRECTIVE:
            self.visit_OmpTargetExitDataDirective(node)


        if node.kind == CursorKind.OMP_TARGET_PARALLEL_DIRECTIVE:
            self.visit_OmpTargetParallelDirective(node)


        if node.kind == CursorKind.OMP_TARGET_PARALLELFOR_DIRECTIVE:
            self.visit_OmpTargetParallelforDirective(node)


        if node.kind == CursorKind.OMP_TARGET_UPDATE_DIRECTIVE:
            self.visit_OmpTargetUpdateDirective(node)


        if node.kind == CursorKind.OMP_DISTRIBUTE_PARALLELFOR_DIRECTIVE:
            self.visit_OmpDistributeParallelforDirective(node)


        if node.kind == CursorKind.OMP_DISTRIBUTE_PARALLEL_FOR_SIMD_DIRECTIVE:
            self.visit_OmpDistributeParallelForSimdDirective(node)


        if node.kind == CursorKind.OMP_DISTRIBUTE_SIMD_DIRECTIVE:
            self.visit_OmpDistributeSimdDirective(node)


        if node.kind == CursorKind.OMP_TARGET_PARALLEL_FOR_SIMD_DIRECTIVE:
            self.visit_OmpTargetParallelForSimdDirective(node)


        if node.kind == CursorKind.OMP_TARGET_SIMD_DIRECTIVE:
            self.visit_OmpTargetSimdDirective(node)


        if node.kind == CursorKind.OMP_TEAMS_DISTRIBUTE_DIRECTIVE:
            self.visit_OmpTeamsDistributeDirective(node)


        if node.kind == CursorKind.TRANSLATION_UNIT:
            self.visit_TranslationUnit(node)


        if node.kind == CursorKind.UNEXPOSED_ATTR:
            self.visit_UnexposedAttr(node)


        if node.kind == CursorKind.IB_ACTION_ATTR:
            self.visit_IbActionAttr(node)


        if node.kind == CursorKind.IB_OUTLET_ATTR:
            self.visit_IbOutletAttr(node)


        if node.kind == CursorKind.IB_OUTLET_COLLECTION_ATTR:
            self.visit_IbOutletCollectionAttr(node)


        if node.kind == CursorKind.CXX_FINAL_ATTR:
            self.visit_CxxFinalAttr(node)


        if node.kind == CursorKind.CXX_OVERRIDE_ATTR:
            self.visit_CxxOverrideAttr(node)


        if node.kind == CursorKind.ANNOTATE_ATTR:
            self.visit_AnnotateAttr(node)


        if node.kind == CursorKind.ASM_LABEL_ATTR:
            self.visit_AsmLabelAttr(node)


        if node.kind == CursorKind.PACKED_ATTR:
            self.visit_PackedAttr(node)


        if node.kind == CursorKind.PURE_ATTR:
            self.visit_PureAttr(node)


        if node.kind == CursorKind.CONST_ATTR:
            self.visit_ConstAttr(node)


        if node.kind == CursorKind.NODUPLICATE_ATTR:
            self.visit_NoduplicateAttr(node)


        if node.kind == CursorKind.CUDACONSTANT_ATTR:
            self.visit_CudaconstantAttr(node)


        if node.kind == CursorKind.CUDADEVICE_ATTR:
            self.visit_CudadeviceAttr(node)


        if node.kind == CursorKind.CUDAGLOBAL_ATTR:
            self.visit_CudaglobalAttr(node)


        if node.kind == CursorKind.CUDAHOST_ATTR:
            self.visit_CudahostAttr(node)


        if node.kind == CursorKind.CUDASHARED_ATTR:
            self.visit_CudasharedAttr(node)


        if node.kind == CursorKind.VISIBILITY_ATTR:
            self.visit_VisibilityAttr(node)


        if node.kind == CursorKind.DLLEXPORT_ATTR:
            self.visit_DllexportAttr(node)


        if node.kind == CursorKind.DLLIMPORT_ATTR:
            self.visit_DllimportAttr(node)


        if node.kind == CursorKind.CONVERGENT_ATTR:
            self.visit_ConvergentAttr(node)


        if node.kind == CursorKind.WARN_UNUSED_ATTR:
            self.visit_WarnUnusedAttr(node)


        if node.kind == CursorKind.WARN_UNUSED_RESULT_ATTR:
            self.visit_WarnUnusedResultAttr(node)


        if node.kind == CursorKind.ALIGNED_ATTR:
            self.visit_AlignedAttr(node)


        if node.kind == CursorKind.PREPROCESSING_DIRECTIVE:
            self.visit_PreprocessingDirective(node)


        if node.kind == CursorKind.MACRO_DEFINITION:
            self.visit_MacroDefinition(node)


        if node.kind == CursorKind.MACRO_INSTANTIATION:
            self.visit_MacroInstantiation(node)


        if node.kind == CursorKind.INCLUSION_DIRECTIVE:
            self.visit_InclusionDirective(node)


        if node.kind == CursorKind.MODULE_IMPORT_DECL:
            self.visit_ModuleImportDecl(node)


        if node.kind == CursorKind.TYPE_ALIAS_TEMPLATE_DECL:
            self.visit_TypeAliasTemplateDecl(node)


        if node.kind == CursorKind.STATIC_ASSERT:
            self.visit_StaticAssert(node)


        if node.kind == CursorKind.FRIEND_DECL:
            self.visit_FriendDecl(node)


        if node.kind == CursorKind.OVERLOAD_CANDIDATE:
            self.visit_OverloadCandidate(node)


        self.visit_generic(node)
        self.visit_children(node)
        self.post_visit(node)
        


    def visit_UnexposedDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_StructDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_UnionDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ClassDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_EnumDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_FieldDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_EnumConstantDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_FunctionDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_VarDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ParmDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcInterfaceDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcCategoryDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcProtocolDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcPropertyDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcIvarDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcInstanceMethodDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcClassMethodDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcImplementationDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcCategoryImplDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_TypedefDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxMethod(self: 'Visitor', node) -> None:
        pass
    

    def visit_Namespace(self: 'Visitor', node) -> None:
        pass
    

    def visit_LinkageSpec(self: 'Visitor', node) -> None:
        pass
    

    def visit_Constructor(self: 'Visitor', node) -> None:
        pass
    

    def visit_Destructor(self: 'Visitor', node) -> None:
        pass
    

    def visit_ConversionFunction(self: 'Visitor', node) -> None:
        pass
    

    def visit_TemplateTypeParameter(self: 'Visitor', node) -> None:
        pass
    

    def visit_TemplateNonTypeParameter(self: 'Visitor', node) -> None:
        pass
    

    def visit_TemplateTemplateParameter(self: 'Visitor', node) -> None:
        pass
    

    def visit_FunctionTemplate(self: 'Visitor', node) -> None:
        pass
    

    def visit_ClassTemplate(self: 'Visitor', node) -> None:
        pass
    

    def visit_ClassTemplatePartialSpecialization(self: 'Visitor', node) -> None:
        pass
    

    def visit_NamespaceAlias(self: 'Visitor', node) -> None:
        pass
    

    def visit_UsingDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_UsingDeclaration(self: 'Visitor', node) -> None:
        pass
    

    def visit_TypeAliasDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcSynthesizeDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcDynamicDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxAccessSpecDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcSuperClassRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcProtocolRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcClassRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_TypeRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxBaseSpecifier(self: 'Visitor', node) -> None:
        pass
    

    def visit_TemplateRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_NamespaceRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_MemberRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_LabelRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_OverloadedDeclRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_VariableRef(self: 'Visitor', node) -> None:
        pass
    

    def visit_InvalidFile(self: 'Visitor', node) -> None:
        pass
    

    def visit_NoDeclFound(self: 'Visitor', node) -> None:
        pass
    

    def visit_NotImplemented(self: 'Visitor', node) -> None:
        pass
    

    def visit_InvalidCode(self: 'Visitor', node) -> None:
        pass
    

    def visit_UnexposedExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_DeclRefExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_MemberRefExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CallExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcMessageExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_BlockExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_IntegerLiteral(self: 'Visitor', node) -> None:
        pass
    

    def visit_FloatingLiteral(self: 'Visitor', node) -> None:
        pass
    

    def visit_ImaginaryLiteral(self: 'Visitor', node) -> None:
        pass
    

    def visit_StringLiteral(self: 'Visitor', node) -> None:
        pass
    

    def visit_CharacterLiteral(self: 'Visitor', node) -> None:
        pass
    

    def visit_ParenExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_UnaryOperator(self: 'Visitor', node) -> None:
        pass
    

    def visit_ArraySubscriptExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_BinaryOperator(self: 'Visitor', node) -> None:
        pass
    

    def visit_CompoundAssignmentOperator(self: 'Visitor', node) -> None:
        pass
    

    def visit_ConditionalOperator(self: 'Visitor', node) -> None:
        pass
    

    def visit_CstyleCastExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CompoundLiteralExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_InitListExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_AddrLabelExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_Stmtexpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_GenericSelectionExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_GnuNullExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxStaticCastExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxDynamicCastExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxReinterpretCastExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxConstCastExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxFunctionalCastExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxTypeidExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxBoolLiteralExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxNullPtrLiteralExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxThisExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxThrowExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxNewExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxDeleteExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxUnaryExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcStringLiteral(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcEncodeExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcSelectorExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcProtocolExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcBridgeCastExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_PackExpansionExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_SizeOfPackExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_LambdaExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjBoolLiteralExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjSelfExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpArraySectionExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcAvailabilityCheckExpr(self: 'Visitor', node) -> None:
        pass
    

    def visit_UnexposedStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_LabelStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_CompoundStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_CaseStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_DefaultStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_IfStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_SwitchStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_WhileStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_DoStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ForStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_GotoStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_IndirectGotoStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ContinueStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_BreakStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ReturnStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_AsmStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcAtTryStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcAtCatchStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcAtFinallyStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcAtThrowStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcAtSynchronizedStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcAutoreleasePoolStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_ObjcForCollectionStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxCatchStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxTryStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxForRangeStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_SehTryStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_SehExceptStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_SehFinallyStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_MsAsmStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_NullStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_DeclStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpParallelDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpSimdDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpForDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpSectionsDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpSectionDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpSingleDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpParallelForDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpParallelSectionsDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTaskDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpMasterDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpCriticalDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTaskyieldDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpBarrierDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTaskwaitDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpFlushDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_SehLeaveStmt(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpOrderedDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpAtomicDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpForSimdDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpParallelforsimdDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTeamsDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTaskgroupDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpCancellationPointDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpCancelDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetDataDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTaskLoopDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTaskLoopSimdDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpDistributeDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetEnterDataDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetExitDataDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetParallelDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetParallelforDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetUpdateDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpDistributeParallelforDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpDistributeParallelForSimdDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpDistributeSimdDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetParallelForSimdDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTargetSimdDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_OmpTeamsDistributeDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_TranslationUnit(self: 'Visitor', node) -> None:
        pass
    

    def visit_UnexposedAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_IbActionAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_IbOutletAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_IbOutletCollectionAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxFinalAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CxxOverrideAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_AnnotateAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_AsmLabelAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_PackedAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_PureAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ConstAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_NoduplicateAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CudaconstantAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CudadeviceAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CudaglobalAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CudahostAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_CudasharedAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_VisibilityAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_DllexportAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_DllimportAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_ConvergentAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_WarnUnusedAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_WarnUnusedResultAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_AlignedAttr(self: 'Visitor', node) -> None:
        pass
    

    def visit_PreprocessingDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_MacroDefinition(self: 'Visitor', node) -> None:
        pass
    

    def visit_MacroInstantiation(self: 'Visitor', node) -> None:
        pass
    

    def visit_InclusionDirective(self: 'Visitor', node) -> None:
        pass
    

    def visit_ModuleImportDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_TypeAliasTemplateDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_StaticAssert(self: 'Visitor', node) -> None:
        pass
    

    def visit_FriendDecl(self: 'Visitor', node) -> None:
        pass
    

    def visit_OverloadCandidate(self: 'Visitor', node) -> None:
        pass
    
