from dataclasses import dataclass
from clang.cindex import CursorKind, SourceLocation

SourceRange = tuple[SourceLocation, SourceLocation]


@dataclass
class Node:
    parent: 'Node'
    definition_id: int
    extent: SourceRange
    id: int
    is_definition: bool
    kind: CursorKind
    spelling: str
    usr: str
    children: list['Node']


class UnexposedDecl(Node):
    def __init__(
            self: 'UnexposedDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.UNEXPOSED_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'UnexposedDecl') -> str:
        return f"UnexposedDecl[{self.super().__repr__()}]"


class StructDecl(Node):
    def __init__(
            self: 'StructDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.STRUCT_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'StructDecl') -> str:
        return f"StructDecl[{self.super().__repr__()}]"


class UnionDecl(Node):
    def __init__(
            self: 'UnionDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.UNION_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'UnionDecl') -> str:
        return f"UnionDecl[{self.super().__repr__()}]"


class ClassDecl(Node):
    def __init__(
            self: 'ClassDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CLASS_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ClassDecl') -> str:
        return f"ClassDecl[{self.super().__repr__()}]"


class EnumDecl(Node):
    def __init__(
            self: 'EnumDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.ENUM_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'EnumDecl') -> str:
        return f"EnumDecl[{self.super().__repr__()}]"


class FieldDecl(Node):
    def __init__(
            self: 'FieldDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.FIELD_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'FieldDecl') -> str:
        return f"FieldDecl[{self.super().__repr__()}]"


class EnumConstantDecl(Node):
    def __init__(
            self: 'EnumConstantDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.ENUM_CONSTANT_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'EnumConstantDecl') -> str:
        return f"EnumConstantDecl[{self.super().__repr__()}]"


class FunctionDecl(Node):
    def __init__(
            self: 'FunctionDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.FUNCTION_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'FunctionDecl') -> str:
        return f"FunctionDecl[{self.super().__repr__()}]"


class VarDecl(Node):
    def __init__(
            self: 'VarDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.VAR_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'VarDecl') -> str:
        return f"VarDecl[{self.super().__repr__()}]"


class ParmDecl(Node):
    def __init__(
            self: 'ParmDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.PARM_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ParmDecl') -> str:
        return f"ParmDecl[{self.super().__repr__()}]"


class ObjcInterfaceDecl(Node):
    def __init__(
            self: 'ObjcInterfaceDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_INTERFACE_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcInterfaceDecl') -> str:
        return f"ObjcInterfaceDecl[{self.super().__repr__()}]"


class ObjcCategoryDecl(Node):
    def __init__(
            self: 'ObjcCategoryDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_CATEGORY_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcCategoryDecl') -> str:
        return f"ObjcCategoryDecl[{self.super().__repr__()}]"


class ObjcProtocolDecl(Node):
    def __init__(
            self: 'ObjcProtocolDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_PROTOCOL_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcProtocolDecl') -> str:
        return f"ObjcProtocolDecl[{self.super().__repr__()}]"


class ObjcPropertyDecl(Node):
    def __init__(
            self: 'ObjcPropertyDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_PROPERTY_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcPropertyDecl') -> str:
        return f"ObjcPropertyDecl[{self.super().__repr__()}]"


class ObjcIvarDecl(Node):
    def __init__(
            self: 'ObjcIvarDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_IVAR_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcIvarDecl') -> str:
        return f"ObjcIvarDecl[{self.super().__repr__()}]"


class ObjcInstanceMethodDecl(Node):
    def __init__(
            self: 'ObjcInstanceMethodDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_INSTANCE_METHOD_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcInstanceMethodDecl') -> str:
        return f"ObjcInstanceMethodDecl[{self.super().__repr__()}]"


class ObjcClassMethodDecl(Node):
    def __init__(
            self: 'ObjcClassMethodDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_CLASS_METHOD_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcClassMethodDecl') -> str:
        return f"ObjcClassMethodDecl[{self.super().__repr__()}]"


class ObjcImplementationDecl(Node):
    def __init__(
            self: 'ObjcImplementationDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_IMPLEMENTATION_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcImplementationDecl') -> str:
        return f"ObjcImplementationDecl[{self.super().__repr__()}]"


class ObjcCategoryImplDecl(Node):
    def __init__(
            self: 'ObjcCategoryImplDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_CATEGORY_IMPL_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcCategoryImplDecl') -> str:
        return f"ObjcCategoryImplDecl[{self.super().__repr__()}]"


class TypedefDecl(Node):
    def __init__(
            self: 'TypedefDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TYPEDEF_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TypedefDecl') -> str:
        return f"TypedefDecl[{self.super().__repr__()}]"


class CxxMethod(Node):
    def __init__(
            self: 'CxxMethod',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_METHOD,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxMethod') -> str:
        return f"CxxMethod[{self.super().__repr__()}]"


class Namespace(Node):
    def __init__(
            self: 'Namespace',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.NAMESPACE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'Namespace') -> str:
        return f"Namespace[{self.super().__repr__()}]"


class LinkageSpec(Node):
    def __init__(
            self: 'LinkageSpec',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.LINKAGE_SPEC,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'LinkageSpec') -> str:
        return f"LinkageSpec[{self.super().__repr__()}]"


class Constructor(Node):
    def __init__(
            self: 'Constructor',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CONSTRUCTOR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'Constructor') -> str:
        return f"Constructor[{self.super().__repr__()}]"


class Destructor(Node):
    def __init__(
            self: 'Destructor',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.DESTRUCTOR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'Destructor') -> str:
        return f"Destructor[{self.super().__repr__()}]"


class ConversionFunction(Node):
    def __init__(
            self: 'ConversionFunction',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CONVERSION_FUNCTION,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ConversionFunction') -> str:
        return f"ConversionFunction[{self.super().__repr__()}]"


class TemplateTypeParameter(Node):
    def __init__(
            self: 'TemplateTypeParameter',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TEMPLATE_TYPE_PARAMETER,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TemplateTypeParameter') -> str:
        return f"TemplateTypeParameter[{self.super().__repr__()}]"


class TemplateNonTypeParameter(Node):
    def __init__(
            self: 'TemplateNonTypeParameter',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TEMPLATE_NON_TYPE_PARAMETER,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TemplateNonTypeParameter') -> str:
        return f"TemplateNonTypeParameter[{self.super().__repr__()}]"


class TemplateTemplateParameter(Node):
    def __init__(
            self: 'TemplateTemplateParameter',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TEMPLATE_TEMPLATE_PARAMETER,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TemplateTemplateParameter') -> str:
        return f"TemplateTemplateParameter[{self.super().__repr__()}]"


class FunctionTemplate(Node):
    def __init__(
            self: 'FunctionTemplate',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.FUNCTION_TEMPLATE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'FunctionTemplate') -> str:
        return f"FunctionTemplate[{self.super().__repr__()}]"


class ClassTemplate(Node):
    def __init__(
            self: 'ClassTemplate',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CLASS_TEMPLATE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ClassTemplate') -> str:
        return f"ClassTemplate[{self.super().__repr__()}]"


class ClassTemplatePartialSpecialization(Node):
    def __init__(
            self: 'ClassTemplatePartialSpecialization',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CLASS_TEMPLATE_PARTIAL_SPECIALIZATION,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ClassTemplatePartialSpecialization') -> str:
        return f"ClassTemplatePartialSpecialization[{self.super().__repr__()}]"


class NamespaceAlias(Node):
    def __init__(
            self: 'NamespaceAlias',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.NAMESPACE_ALIAS,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'NamespaceAlias') -> str:
        return f"NamespaceAlias[{self.super().__repr__()}]"


class UsingDirective(Node):
    def __init__(
            self: 'UsingDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.USING_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'UsingDirective') -> str:
        return f"UsingDirective[{self.super().__repr__()}]"


class UsingDeclaration(Node):
    def __init__(
            self: 'UsingDeclaration',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.USING_DECLARATION,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'UsingDeclaration') -> str:
        return f"UsingDeclaration[{self.super().__repr__()}]"


class TypeAliasDecl(Node):
    def __init__(
            self: 'TypeAliasDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TYPE_ALIAS_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TypeAliasDecl') -> str:
        return f"TypeAliasDecl[{self.super().__repr__()}]"


class ObjcSynthesizeDecl(Node):
    def __init__(
            self: 'ObjcSynthesizeDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_SYNTHESIZE_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcSynthesizeDecl') -> str:
        return f"ObjcSynthesizeDecl[{self.super().__repr__()}]"


class ObjcDynamicDecl(Node):
    def __init__(
            self: 'ObjcDynamicDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_DYNAMIC_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcDynamicDecl') -> str:
        return f"ObjcDynamicDecl[{self.super().__repr__()}]"


class CxxAccessSpecDecl(Node):
    def __init__(
            self: 'CxxAccessSpecDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_ACCESS_SPEC_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxAccessSpecDecl') -> str:
        return f"CxxAccessSpecDecl[{self.super().__repr__()}]"


class ObjcSuperClassRef(Node):
    def __init__(
            self: 'ObjcSuperClassRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_SUPER_CLASS_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcSuperClassRef') -> str:
        return f"ObjcSuperClassRef[{self.super().__repr__()}]"


class ObjcProtocolRef(Node):
    def __init__(
            self: 'ObjcProtocolRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_PROTOCOL_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcProtocolRef') -> str:
        return f"ObjcProtocolRef[{self.super().__repr__()}]"


class ObjcClassRef(Node):
    def __init__(
            self: 'ObjcClassRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_CLASS_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcClassRef') -> str:
        return f"ObjcClassRef[{self.super().__repr__()}]"


class TypeRef(Node):
    def __init__(
            self: 'TypeRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TYPE_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TypeRef') -> str:
        return f"TypeRef[{self.super().__repr__()}]"


class CxxBaseSpecifier(Node):
    def __init__(
            self: 'CxxBaseSpecifier',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_BASE_SPECIFIER,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxBaseSpecifier') -> str:
        return f"CxxBaseSpecifier[{self.super().__repr__()}]"


class TemplateRef(Node):
    def __init__(
            self: 'TemplateRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TEMPLATE_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TemplateRef') -> str:
        return f"TemplateRef[{self.super().__repr__()}]"


class NamespaceRef(Node):
    def __init__(
            self: 'NamespaceRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.NAMESPACE_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'NamespaceRef') -> str:
        return f"NamespaceRef[{self.super().__repr__()}]"


class MemberRef(Node):
    def __init__(
            self: 'MemberRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.MEMBER_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'MemberRef') -> str:
        return f"MemberRef[{self.super().__repr__()}]"


class LabelRef(Node):
    def __init__(
            self: 'LabelRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.LABEL_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'LabelRef') -> str:
        return f"LabelRef[{self.super().__repr__()}]"


class OverloadedDeclRef(Node):
    def __init__(
            self: 'OverloadedDeclRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OVERLOADED_DECL_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OverloadedDeclRef') -> str:
        return f"OverloadedDeclRef[{self.super().__repr__()}]"


class VariableRef(Node):
    def __init__(
            self: 'VariableRef',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.VARIABLE_REF,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'VariableRef') -> str:
        return f"VariableRef[{self.super().__repr__()}]"


class InvalidFile(Node):
    def __init__(
            self: 'InvalidFile',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.INVALID_FILE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'InvalidFile') -> str:
        return f"InvalidFile[{self.super().__repr__()}]"


class NoDeclFound(Node):
    def __init__(
            self: 'NoDeclFound',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.NO_DECL_FOUND,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'NoDeclFound') -> str:
        return f"NoDeclFound[{self.super().__repr__()}]"


class NotImplemented(Node):
    def __init__(
            self: 'NotImplemented',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.NOT_IMPLEMENTED,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'NotImplemented') -> str:
        return f"NotImplemented[{self.super().__repr__()}]"


class InvalidCode(Node):
    def __init__(
            self: 'InvalidCode',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.INVALID_CODE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'InvalidCode') -> str:
        return f"InvalidCode[{self.super().__repr__()}]"


class UnexposedExpr(Node):
    def __init__(
            self: 'UnexposedExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.UNEXPOSED_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'UnexposedExpr') -> str:
        return f"UnexposedExpr[{self.super().__repr__()}]"


class DeclRefExpr(Node):
    def __init__(
            self: 'DeclRefExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.DECL_REF_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'DeclRefExpr') -> str:
        return f"DeclRefExpr[{self.super().__repr__()}]"


class MemberRefExpr(Node):
    def __init__(
            self: 'MemberRefExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.MEMBER_REF_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'MemberRefExpr') -> str:
        return f"MemberRefExpr[{self.super().__repr__()}]"


class CallExpr(Node):
    def __init__(
            self: 'CallExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CALL_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CallExpr') -> str:
        return f"CallExpr[{self.super().__repr__()}]"


class ObjcMessageExpr(Node):
    def __init__(
            self: 'ObjcMessageExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_MESSAGE_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcMessageExpr') -> str:
        return f"ObjcMessageExpr[{self.super().__repr__()}]"


class BlockExpr(Node):
    def __init__(
            self: 'BlockExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.BLOCK_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'BlockExpr') -> str:
        return f"BlockExpr[{self.super().__repr__()}]"


class IntegerLiteral(Node):
    def __init__(
            self: 'IntegerLiteral',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.INTEGER_LITERAL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'IntegerLiteral') -> str:
        return f"IntegerLiteral[{self.super().__repr__()}]"


class FloatingLiteral(Node):
    def __init__(
            self: 'FloatingLiteral',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.FLOATING_LITERAL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'FloatingLiteral') -> str:
        return f"FloatingLiteral[{self.super().__repr__()}]"


class ImaginaryLiteral(Node):
    def __init__(
            self: 'ImaginaryLiteral',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.IMAGINARY_LITERAL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ImaginaryLiteral') -> str:
        return f"ImaginaryLiteral[{self.super().__repr__()}]"


class StringLiteral(Node):
    def __init__(
            self: 'StringLiteral',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.STRING_LITERAL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'StringLiteral') -> str:
        return f"StringLiteral[{self.super().__repr__()}]"


class CharacterLiteral(Node):
    def __init__(
            self: 'CharacterLiteral',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CHARACTER_LITERAL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CharacterLiteral') -> str:
        return f"CharacterLiteral[{self.super().__repr__()}]"


class ParenExpr(Node):
    def __init__(
            self: 'ParenExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.PAREN_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ParenExpr') -> str:
        return f"ParenExpr[{self.super().__repr__()}]"


class UnaryOperator(Node):
    def __init__(
            self: 'UnaryOperator',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.UNARY_OPERATOR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'UnaryOperator') -> str:
        return f"UnaryOperator[{self.super().__repr__()}]"


class ArraySubscriptExpr(Node):
    def __init__(
            self: 'ArraySubscriptExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.ARRAY_SUBSCRIPT_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ArraySubscriptExpr') -> str:
        return f"ArraySubscriptExpr[{self.super().__repr__()}]"


class BinaryOperator(Node):
    def __init__(
            self: 'BinaryOperator',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.BINARY_OPERATOR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'BinaryOperator') -> str:
        return f"BinaryOperator[{self.super().__repr__()}]"


class CompoundAssignmentOperator(Node):
    def __init__(
            self: 'CompoundAssignmentOperator',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.COMPOUND_ASSIGNMENT_OPERATOR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CompoundAssignmentOperator') -> str:
        return f"CompoundAssignmentOperator[{self.super().__repr__()}]"


class ConditionalOperator(Node):
    def __init__(
            self: 'ConditionalOperator',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CONDITIONAL_OPERATOR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ConditionalOperator') -> str:
        return f"ConditionalOperator[{self.super().__repr__()}]"


class CstyleCastExpr(Node):
    def __init__(
            self: 'CstyleCastExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CSTYLE_CAST_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CstyleCastExpr') -> str:
        return f"CstyleCastExpr[{self.super().__repr__()}]"


class CompoundLiteralExpr(Node):
    def __init__(
            self: 'CompoundLiteralExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.COMPOUND_LITERAL_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CompoundLiteralExpr') -> str:
        return f"CompoundLiteralExpr[{self.super().__repr__()}]"


class InitListExpr(Node):
    def __init__(
            self: 'InitListExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.INIT_LIST_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'InitListExpr') -> str:
        return f"InitListExpr[{self.super().__repr__()}]"


class AddrLabelExpr(Node):
    def __init__(
            self: 'AddrLabelExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.ADDR_LABEL_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'AddrLabelExpr') -> str:
        return f"AddrLabelExpr[{self.super().__repr__()}]"


class Stmtexpr(Node):
    def __init__(
            self: 'Stmtexpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.StmtExpr,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'Stmtexpr') -> str:
        return f"Stmtexpr[{self.super().__repr__()}]"


class GenericSelectionExpr(Node):
    def __init__(
            self: 'GenericSelectionExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.GENERIC_SELECTION_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'GenericSelectionExpr') -> str:
        return f"GenericSelectionExpr[{self.super().__repr__()}]"


class GnuNullExpr(Node):
    def __init__(
            self: 'GnuNullExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.GNU_NULL_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'GnuNullExpr') -> str:
        return f"GnuNullExpr[{self.super().__repr__()}]"


class CxxStaticCastExpr(Node):
    def __init__(
            self: 'CxxStaticCastExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_STATIC_CAST_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxStaticCastExpr') -> str:
        return f"CxxStaticCastExpr[{self.super().__repr__()}]"


class CxxDynamicCastExpr(Node):
    def __init__(
            self: 'CxxDynamicCastExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_DYNAMIC_CAST_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxDynamicCastExpr') -> str:
        return f"CxxDynamicCastExpr[{self.super().__repr__()}]"


class CxxReinterpretCastExpr(Node):
    def __init__(
            self: 'CxxReinterpretCastExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_REINTERPRET_CAST_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxReinterpretCastExpr') -> str:
        return f"CxxReinterpretCastExpr[{self.super().__repr__()}]"


class CxxConstCastExpr(Node):
    def __init__(
            self: 'CxxConstCastExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_CONST_CAST_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxConstCastExpr') -> str:
        return f"CxxConstCastExpr[{self.super().__repr__()}]"


class CxxFunctionalCastExpr(Node):
    def __init__(
            self: 'CxxFunctionalCastExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_FUNCTIONAL_CAST_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxFunctionalCastExpr') -> str:
        return f"CxxFunctionalCastExpr[{self.super().__repr__()}]"


class CxxTypeidExpr(Node):
    def __init__(
            self: 'CxxTypeidExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_TYPEID_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxTypeidExpr') -> str:
        return f"CxxTypeidExpr[{self.super().__repr__()}]"


class CxxBoolLiteralExpr(Node):
    def __init__(
            self: 'CxxBoolLiteralExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_BOOL_LITERAL_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxBoolLiteralExpr') -> str:
        return f"CxxBoolLiteralExpr[{self.super().__repr__()}]"


class CxxNullPtrLiteralExpr(Node):
    def __init__(
            self: 'CxxNullPtrLiteralExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_NULL_PTR_LITERAL_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxNullPtrLiteralExpr') -> str:
        return f"CxxNullPtrLiteralExpr[{self.super().__repr__()}]"


class CxxThisExpr(Node):
    def __init__(
            self: 'CxxThisExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_THIS_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxThisExpr') -> str:
        return f"CxxThisExpr[{self.super().__repr__()}]"


class CxxThrowExpr(Node):
    def __init__(
            self: 'CxxThrowExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_THROW_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxThrowExpr') -> str:
        return f"CxxThrowExpr[{self.super().__repr__()}]"


class CxxNewExpr(Node):
    def __init__(
            self: 'CxxNewExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_NEW_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxNewExpr') -> str:
        return f"CxxNewExpr[{self.super().__repr__()}]"


class CxxDeleteExpr(Node):
    def __init__(
            self: 'CxxDeleteExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_DELETE_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxDeleteExpr') -> str:
        return f"CxxDeleteExpr[{self.super().__repr__()}]"


class CxxUnaryExpr(Node):
    def __init__(
            self: 'CxxUnaryExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_UNARY_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxUnaryExpr') -> str:
        return f"CxxUnaryExpr[{self.super().__repr__()}]"


class ObjcStringLiteral(Node):
    def __init__(
            self: 'ObjcStringLiteral',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_STRING_LITERAL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcStringLiteral') -> str:
        return f"ObjcStringLiteral[{self.super().__repr__()}]"


class ObjcEncodeExpr(Node):
    def __init__(
            self: 'ObjcEncodeExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_ENCODE_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcEncodeExpr') -> str:
        return f"ObjcEncodeExpr[{self.super().__repr__()}]"


class ObjcSelectorExpr(Node):
    def __init__(
            self: 'ObjcSelectorExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_SELECTOR_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcSelectorExpr') -> str:
        return f"ObjcSelectorExpr[{self.super().__repr__()}]"


class ObjcProtocolExpr(Node):
    def __init__(
            self: 'ObjcProtocolExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_PROTOCOL_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcProtocolExpr') -> str:
        return f"ObjcProtocolExpr[{self.super().__repr__()}]"


class ObjcBridgeCastExpr(Node):
    def __init__(
            self: 'ObjcBridgeCastExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_BRIDGE_CAST_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcBridgeCastExpr') -> str:
        return f"ObjcBridgeCastExpr[{self.super().__repr__()}]"


class PackExpansionExpr(Node):
    def __init__(
            self: 'PackExpansionExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.PACK_EXPANSION_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'PackExpansionExpr') -> str:
        return f"PackExpansionExpr[{self.super().__repr__()}]"


class SizeOfPackExpr(Node):
    def __init__(
            self: 'SizeOfPackExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.SIZE_OF_PACK_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'SizeOfPackExpr') -> str:
        return f"SizeOfPackExpr[{self.super().__repr__()}]"


class LambdaExpr(Node):
    def __init__(
            self: 'LambdaExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.LAMBDA_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'LambdaExpr') -> str:
        return f"LambdaExpr[{self.super().__repr__()}]"


class ObjBoolLiteralExpr(Node):
    def __init__(
            self: 'ObjBoolLiteralExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJ_BOOL_LITERAL_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjBoolLiteralExpr') -> str:
        return f"ObjBoolLiteralExpr[{self.super().__repr__()}]"


class ObjSelfExpr(Node):
    def __init__(
            self: 'ObjSelfExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJ_SELF_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjSelfExpr') -> str:
        return f"ObjSelfExpr[{self.super().__repr__()}]"


class OmpArraySectionExpr(Node):
    def __init__(
            self: 'OmpArraySectionExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_ARRAY_SECTION_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpArraySectionExpr') -> str:
        return f"OmpArraySectionExpr[{self.super().__repr__()}]"


class ObjcAvailabilityCheckExpr(Node):
    def __init__(
            self: 'ObjcAvailabilityCheckExpr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_AVAILABILITY_CHECK_EXPR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcAvailabilityCheckExpr') -> str:
        return f"ObjcAvailabilityCheckExpr[{self.super().__repr__()}]"


class UnexposedStmt(Node):
    def __init__(
            self: 'UnexposedStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.UNEXPOSED_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'UnexposedStmt') -> str:
        return f"UnexposedStmt[{self.super().__repr__()}]"


class LabelStmt(Node):
    def __init__(
            self: 'LabelStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.LABEL_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'LabelStmt') -> str:
        return f"LabelStmt[{self.super().__repr__()}]"


class CompoundStmt(Node):
    def __init__(
            self: 'CompoundStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.COMPOUND_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CompoundStmt') -> str:
        return f"CompoundStmt[{self.super().__repr__()}]"


class CaseStmt(Node):
    def __init__(
            self: 'CaseStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CASE_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CaseStmt') -> str:
        return f"CaseStmt[{self.super().__repr__()}]"


class DefaultStmt(Node):
    def __init__(
            self: 'DefaultStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.DEFAULT_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'DefaultStmt') -> str:
        return f"DefaultStmt[{self.super().__repr__()}]"


class IfStmt(Node):
    def __init__(
            self: 'IfStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.IF_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'IfStmt') -> str:
        return f"IfStmt[{self.super().__repr__()}]"


class SwitchStmt(Node):
    def __init__(
            self: 'SwitchStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.SWITCH_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'SwitchStmt') -> str:
        return f"SwitchStmt[{self.super().__repr__()}]"


class WhileStmt(Node):
    def __init__(
            self: 'WhileStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.WHILE_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'WhileStmt') -> str:
        return f"WhileStmt[{self.super().__repr__()}]"


class DoStmt(Node):
    def __init__(
            self: 'DoStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.DO_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'DoStmt') -> str:
        return f"DoStmt[{self.super().__repr__()}]"


class ForStmt(Node):
    def __init__(
            self: 'ForStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.FOR_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ForStmt') -> str:
        return f"ForStmt[{self.super().__repr__()}]"


class GotoStmt(Node):
    def __init__(
            self: 'GotoStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.GOTO_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'GotoStmt') -> str:
        return f"GotoStmt[{self.super().__repr__()}]"


class IndirectGotoStmt(Node):
    def __init__(
            self: 'IndirectGotoStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.INDIRECT_GOTO_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'IndirectGotoStmt') -> str:
        return f"IndirectGotoStmt[{self.super().__repr__()}]"


class ContinueStmt(Node):
    def __init__(
            self: 'ContinueStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CONTINUE_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ContinueStmt') -> str:
        return f"ContinueStmt[{self.super().__repr__()}]"


class BreakStmt(Node):
    def __init__(
            self: 'BreakStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.BREAK_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'BreakStmt') -> str:
        return f"BreakStmt[{self.super().__repr__()}]"


class ReturnStmt(Node):
    def __init__(
            self: 'ReturnStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.RETURN_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ReturnStmt') -> str:
        return f"ReturnStmt[{self.super().__repr__()}]"


class AsmStmt(Node):
    def __init__(
            self: 'AsmStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.ASM_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'AsmStmt') -> str:
        return f"AsmStmt[{self.super().__repr__()}]"


class ObjcAtTryStmt(Node):
    def __init__(
            self: 'ObjcAtTryStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_AT_TRY_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcAtTryStmt') -> str:
        return f"ObjcAtTryStmt[{self.super().__repr__()}]"


class ObjcAtCatchStmt(Node):
    def __init__(
            self: 'ObjcAtCatchStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_AT_CATCH_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcAtCatchStmt') -> str:
        return f"ObjcAtCatchStmt[{self.super().__repr__()}]"


class ObjcAtFinallyStmt(Node):
    def __init__(
            self: 'ObjcAtFinallyStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_AT_FINALLY_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcAtFinallyStmt') -> str:
        return f"ObjcAtFinallyStmt[{self.super().__repr__()}]"


class ObjcAtThrowStmt(Node):
    def __init__(
            self: 'ObjcAtThrowStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_AT_THROW_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcAtThrowStmt') -> str:
        return f"ObjcAtThrowStmt[{self.super().__repr__()}]"


class ObjcAtSynchronizedStmt(Node):
    def __init__(
            self: 'ObjcAtSynchronizedStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_AT_SYNCHRONIZED_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcAtSynchronizedStmt') -> str:
        return f"ObjcAtSynchronizedStmt[{self.super().__repr__()}]"


class ObjcAutoreleasePoolStmt(Node):
    def __init__(
            self: 'ObjcAutoreleasePoolStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_AUTORELEASE_POOL_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcAutoreleasePoolStmt') -> str:
        return f"ObjcAutoreleasePoolStmt[{self.super().__repr__()}]"


class ObjcForCollectionStmt(Node):
    def __init__(
            self: 'ObjcForCollectionStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OBJC_FOR_COLLECTION_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ObjcForCollectionStmt') -> str:
        return f"ObjcForCollectionStmt[{self.super().__repr__()}]"


class CxxCatchStmt(Node):
    def __init__(
            self: 'CxxCatchStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_CATCH_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxCatchStmt') -> str:
        return f"CxxCatchStmt[{self.super().__repr__()}]"


class CxxTryStmt(Node):
    def __init__(
            self: 'CxxTryStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_TRY_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxTryStmt') -> str:
        return f"CxxTryStmt[{self.super().__repr__()}]"


class CxxForRangeStmt(Node):
    def __init__(
            self: 'CxxForRangeStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_FOR_RANGE_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxForRangeStmt') -> str:
        return f"CxxForRangeStmt[{self.super().__repr__()}]"


class SehTryStmt(Node):
    def __init__(
            self: 'SehTryStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.SEH_TRY_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'SehTryStmt') -> str:
        return f"SehTryStmt[{self.super().__repr__()}]"


class SehExceptStmt(Node):
    def __init__(
            self: 'SehExceptStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.SEH_EXCEPT_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'SehExceptStmt') -> str:
        return f"SehExceptStmt[{self.super().__repr__()}]"


class SehFinallyStmt(Node):
    def __init__(
            self: 'SehFinallyStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.SEH_FINALLY_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'SehFinallyStmt') -> str:
        return f"SehFinallyStmt[{self.super().__repr__()}]"


class MsAsmStmt(Node):
    def __init__(
            self: 'MsAsmStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.MS_ASM_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'MsAsmStmt') -> str:
        return f"MsAsmStmt[{self.super().__repr__()}]"


class NullStmt(Node):
    def __init__(
            self: 'NullStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.NULL_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'NullStmt') -> str:
        return f"NullStmt[{self.super().__repr__()}]"


class DeclStmt(Node):
    def __init__(
            self: 'DeclStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.DECL_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'DeclStmt') -> str:
        return f"DeclStmt[{self.super().__repr__()}]"


class OmpParallelDirective(Node):
    def __init__(
            self: 'OmpParallelDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_PARALLEL_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpParallelDirective') -> str:
        return f"OmpParallelDirective[{self.super().__repr__()}]"


class OmpSimdDirective(Node):
    def __init__(
            self: 'OmpSimdDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_SIMD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpSimdDirective') -> str:
        return f"OmpSimdDirective[{self.super().__repr__()}]"


class OmpForDirective(Node):
    def __init__(
            self: 'OmpForDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_FOR_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpForDirective') -> str:
        return f"OmpForDirective[{self.super().__repr__()}]"


class OmpSectionsDirective(Node):
    def __init__(
            self: 'OmpSectionsDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_SECTIONS_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpSectionsDirective') -> str:
        return f"OmpSectionsDirective[{self.super().__repr__()}]"


class OmpSectionDirective(Node):
    def __init__(
            self: 'OmpSectionDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_SECTION_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpSectionDirective') -> str:
        return f"OmpSectionDirective[{self.super().__repr__()}]"


class OmpSingleDirective(Node):
    def __init__(
            self: 'OmpSingleDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_SINGLE_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpSingleDirective') -> str:
        return f"OmpSingleDirective[{self.super().__repr__()}]"


class OmpParallelForDirective(Node):
    def __init__(
            self: 'OmpParallelForDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_PARALLEL_FOR_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpParallelForDirective') -> str:
        return f"OmpParallelForDirective[{self.super().__repr__()}]"


class OmpParallelSectionsDirective(Node):
    def __init__(
            self: 'OmpParallelSectionsDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_PARALLEL_SECTIONS_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpParallelSectionsDirective') -> str:
        return f"OmpParallelSectionsDirective[{self.super().__repr__()}]"


class OmpTaskDirective(Node):
    def __init__(
            self: 'OmpTaskDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TASK_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTaskDirective') -> str:
        return f"OmpTaskDirective[{self.super().__repr__()}]"


class OmpMasterDirective(Node):
    def __init__(
            self: 'OmpMasterDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_MASTER_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpMasterDirective') -> str:
        return f"OmpMasterDirective[{self.super().__repr__()}]"


class OmpCriticalDirective(Node):
    def __init__(
            self: 'OmpCriticalDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_CRITICAL_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpCriticalDirective') -> str:
        return f"OmpCriticalDirective[{self.super().__repr__()}]"


class OmpTaskyieldDirective(Node):
    def __init__(
            self: 'OmpTaskyieldDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TASKYIELD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTaskyieldDirective') -> str:
        return f"OmpTaskyieldDirective[{self.super().__repr__()}]"


class OmpBarrierDirective(Node):
    def __init__(
            self: 'OmpBarrierDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_BARRIER_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpBarrierDirective') -> str:
        return f"OmpBarrierDirective[{self.super().__repr__()}]"


class OmpTaskwaitDirective(Node):
    def __init__(
            self: 'OmpTaskwaitDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TASKWAIT_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTaskwaitDirective') -> str:
        return f"OmpTaskwaitDirective[{self.super().__repr__()}]"


class OmpFlushDirective(Node):
    def __init__(
            self: 'OmpFlushDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_FLUSH_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpFlushDirective') -> str:
        return f"OmpFlushDirective[{self.super().__repr__()}]"


class SehLeaveStmt(Node):
    def __init__(
            self: 'SehLeaveStmt',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.SEH_LEAVE_STMT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'SehLeaveStmt') -> str:
        return f"SehLeaveStmt[{self.super().__repr__()}]"


class OmpOrderedDirective(Node):
    def __init__(
            self: 'OmpOrderedDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_ORDERED_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpOrderedDirective') -> str:
        return f"OmpOrderedDirective[{self.super().__repr__()}]"


class OmpAtomicDirective(Node):
    def __init__(
            self: 'OmpAtomicDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_ATOMIC_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpAtomicDirective') -> str:
        return f"OmpAtomicDirective[{self.super().__repr__()}]"


class OmpForSimdDirective(Node):
    def __init__(
            self: 'OmpForSimdDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_FOR_SIMD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpForSimdDirective') -> str:
        return f"OmpForSimdDirective[{self.super().__repr__()}]"


class OmpParallelforsimdDirective(Node):
    def __init__(
            self: 'OmpParallelforsimdDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_PARALLELFORSIMD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpParallelforsimdDirective') -> str:
        return f"OmpParallelforsimdDirective[{self.super().__repr__()}]"


class OmpTargetDirective(Node):
    def __init__(
            self: 'OmpTargetDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetDirective') -> str:
        return f"OmpTargetDirective[{self.super().__repr__()}]"


class OmpTeamsDirective(Node):
    def __init__(
            self: 'OmpTeamsDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TEAMS_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTeamsDirective') -> str:
        return f"OmpTeamsDirective[{self.super().__repr__()}]"


class OmpTaskgroupDirective(Node):
    def __init__(
            self: 'OmpTaskgroupDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TASKGROUP_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTaskgroupDirective') -> str:
        return f"OmpTaskgroupDirective[{self.super().__repr__()}]"


class OmpCancellationPointDirective(Node):
    def __init__(
            self: 'OmpCancellationPointDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_CANCELLATION_POINT_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpCancellationPointDirective') -> str:
        return f"OmpCancellationPointDirective[{self.super().__repr__()}]"


class OmpCancelDirective(Node):
    def __init__(
            self: 'OmpCancelDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_CANCEL_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpCancelDirective') -> str:
        return f"OmpCancelDirective[{self.super().__repr__()}]"


class OmpTargetDataDirective(Node):
    def __init__(
            self: 'OmpTargetDataDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_DATA_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetDataDirective') -> str:
        return f"OmpTargetDataDirective[{self.super().__repr__()}]"


class OmpTaskLoopDirective(Node):
    def __init__(
            self: 'OmpTaskLoopDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TASK_LOOP_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTaskLoopDirective') -> str:
        return f"OmpTaskLoopDirective[{self.super().__repr__()}]"


class OmpTaskLoopSimdDirective(Node):
    def __init__(
            self: 'OmpTaskLoopSimdDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TASK_LOOP_SIMD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTaskLoopSimdDirective') -> str:
        return f"OmpTaskLoopSimdDirective[{self.super().__repr__()}]"


class OmpDistributeDirective(Node):
    def __init__(
            self: 'OmpDistributeDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_DISTRIBUTE_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpDistributeDirective') -> str:
        return f"OmpDistributeDirective[{self.super().__repr__()}]"


class OmpTargetEnterDataDirective(Node):
    def __init__(
            self: 'OmpTargetEnterDataDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_ENTER_DATA_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetEnterDataDirective') -> str:
        return f"OmpTargetEnterDataDirective[{self.super().__repr__()}]"


class OmpTargetExitDataDirective(Node):
    def __init__(
            self: 'OmpTargetExitDataDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_EXIT_DATA_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetExitDataDirective') -> str:
        return f"OmpTargetExitDataDirective[{self.super().__repr__()}]"


class OmpTargetParallelDirective(Node):
    def __init__(
            self: 'OmpTargetParallelDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_PARALLEL_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetParallelDirective') -> str:
        return f"OmpTargetParallelDirective[{self.super().__repr__()}]"


class OmpTargetParallelforDirective(Node):
    def __init__(
            self: 'OmpTargetParallelforDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_PARALLELFOR_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetParallelforDirective') -> str:
        return f"OmpTargetParallelforDirective[{self.super().__repr__()}]"


class OmpTargetUpdateDirective(Node):
    def __init__(
            self: 'OmpTargetUpdateDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_UPDATE_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetUpdateDirective') -> str:
        return f"OmpTargetUpdateDirective[{self.super().__repr__()}]"


class OmpDistributeParallelforDirective(Node):
    def __init__(
            self: 'OmpDistributeParallelforDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_DISTRIBUTE_PARALLELFOR_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpDistributeParallelforDirective') -> str:
        return f"OmpDistributeParallelforDirective[{self.super().__repr__()}]"


class OmpDistributeParallelForSimdDirective(Node):
    def __init__(
            self: 'OmpDistributeParallelForSimdDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_DISTRIBUTE_PARALLEL_FOR_SIMD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpDistributeParallelForSimdDirective') -> str:
        return f"OmpDistributeParallelForSimdDirective[{self.super().__repr__()}]"


class OmpDistributeSimdDirective(Node):
    def __init__(
            self: 'OmpDistributeSimdDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_DISTRIBUTE_SIMD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpDistributeSimdDirective') -> str:
        return f"OmpDistributeSimdDirective[{self.super().__repr__()}]"


class OmpTargetParallelForSimdDirective(Node):
    def __init__(
            self: 'OmpTargetParallelForSimdDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_PARALLEL_FOR_SIMD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetParallelForSimdDirective') -> str:
        return f"OmpTargetParallelForSimdDirective[{self.super().__repr__()}]"


class OmpTargetSimdDirective(Node):
    def __init__(
            self: 'OmpTargetSimdDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TARGET_SIMD_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTargetSimdDirective') -> str:
        return f"OmpTargetSimdDirective[{self.super().__repr__()}]"


class OmpTeamsDistributeDirective(Node):
    def __init__(
            self: 'OmpTeamsDistributeDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OMP_TEAMS_DISTRIBUTE_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OmpTeamsDistributeDirective') -> str:
        return f"OmpTeamsDistributeDirective[{self.super().__repr__()}]"


class TranslationUnit(Node):
    def __init__(
            self: 'TranslationUnit',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TRANSLATION_UNIT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TranslationUnit') -> str:
        return f"TranslationUnit[{self.super().__repr__()}]"


class UnexposedAttr(Node):
    def __init__(
            self: 'UnexposedAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.UNEXPOSED_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'UnexposedAttr') -> str:
        return f"UnexposedAttr[{self.super().__repr__()}]"


class IbActionAttr(Node):
    def __init__(
            self: 'IbActionAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.IB_ACTION_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'IbActionAttr') -> str:
        return f"IbActionAttr[{self.super().__repr__()}]"


class IbOutletAttr(Node):
    def __init__(
            self: 'IbOutletAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.IB_OUTLET_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'IbOutletAttr') -> str:
        return f"IbOutletAttr[{self.super().__repr__()}]"


class IbOutletCollectionAttr(Node):
    def __init__(
            self: 'IbOutletCollectionAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.IB_OUTLET_COLLECTION_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'IbOutletCollectionAttr') -> str:
        return f"IbOutletCollectionAttr[{self.super().__repr__()}]"


class CxxFinalAttr(Node):
    def __init__(
            self: 'CxxFinalAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_FINAL_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxFinalAttr') -> str:
        return f"CxxFinalAttr[{self.super().__repr__()}]"


class CxxOverrideAttr(Node):
    def __init__(
            self: 'CxxOverrideAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CXX_OVERRIDE_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CxxOverrideAttr') -> str:
        return f"CxxOverrideAttr[{self.super().__repr__()}]"


class AnnotateAttr(Node):
    def __init__(
            self: 'AnnotateAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.ANNOTATE_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'AnnotateAttr') -> str:
        return f"AnnotateAttr[{self.super().__repr__()}]"


class AsmLabelAttr(Node):
    def __init__(
            self: 'AsmLabelAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.ASM_LABEL_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'AsmLabelAttr') -> str:
        return f"AsmLabelAttr[{self.super().__repr__()}]"


class PackedAttr(Node):
    def __init__(
            self: 'PackedAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.PACKED_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'PackedAttr') -> str:
        return f"PackedAttr[{self.super().__repr__()}]"


class PureAttr(Node):
    def __init__(
            self: 'PureAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.PURE_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'PureAttr') -> str:
        return f"PureAttr[{self.super().__repr__()}]"


class ConstAttr(Node):
    def __init__(
            self: 'ConstAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CONST_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ConstAttr') -> str:
        return f"ConstAttr[{self.super().__repr__()}]"


class NoduplicateAttr(Node):
    def __init__(
            self: 'NoduplicateAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.NODUPLICATE_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'NoduplicateAttr') -> str:
        return f"NoduplicateAttr[{self.super().__repr__()}]"


class CudaconstantAttr(Node):
    def __init__(
            self: 'CudaconstantAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CUDACONSTANT_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CudaconstantAttr') -> str:
        return f"CudaconstantAttr[{self.super().__repr__()}]"


class CudadeviceAttr(Node):
    def __init__(
            self: 'CudadeviceAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CUDADEVICE_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CudadeviceAttr') -> str:
        return f"CudadeviceAttr[{self.super().__repr__()}]"


class CudaglobalAttr(Node):
    def __init__(
            self: 'CudaglobalAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CUDAGLOBAL_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CudaglobalAttr') -> str:
        return f"CudaglobalAttr[{self.super().__repr__()}]"


class CudahostAttr(Node):
    def __init__(
            self: 'CudahostAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CUDAHOST_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CudahostAttr') -> str:
        return f"CudahostAttr[{self.super().__repr__()}]"


class CudasharedAttr(Node):
    def __init__(
            self: 'CudasharedAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CUDASHARED_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'CudasharedAttr') -> str:
        return f"CudasharedAttr[{self.super().__repr__()}]"


class VisibilityAttr(Node):
    def __init__(
            self: 'VisibilityAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.VISIBILITY_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'VisibilityAttr') -> str:
        return f"VisibilityAttr[{self.super().__repr__()}]"


class DllexportAttr(Node):
    def __init__(
            self: 'DllexportAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.DLLEXPORT_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'DllexportAttr') -> str:
        return f"DllexportAttr[{self.super().__repr__()}]"


class DllimportAttr(Node):
    def __init__(
            self: 'DllimportAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.DLLIMPORT_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'DllimportAttr') -> str:
        return f"DllimportAttr[{self.super().__repr__()}]"


class ConvergentAttr(Node):
    def __init__(
            self: 'ConvergentAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.CONVERGENT_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ConvergentAttr') -> str:
        return f"ConvergentAttr[{self.super().__repr__()}]"


class WarnUnusedAttr(Node):
    def __init__(
            self: 'WarnUnusedAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.WARN_UNUSED_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'WarnUnusedAttr') -> str:
        return f"WarnUnusedAttr[{self.super().__repr__()}]"


class WarnUnusedResultAttr(Node):
    def __init__(
            self: 'WarnUnusedResultAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.WARN_UNUSED_RESULT_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'WarnUnusedResultAttr') -> str:
        return f"WarnUnusedResultAttr[{self.super().__repr__()}]"


class AlignedAttr(Node):
    def __init__(
            self: 'AlignedAttr',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.ALIGNED_ATTR,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'AlignedAttr') -> str:
        return f"AlignedAttr[{self.super().__repr__()}]"


class PreprocessingDirective(Node):
    def __init__(
            self: 'PreprocessingDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.PREPROCESSING_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'PreprocessingDirective') -> str:
        return f"PreprocessingDirective[{self.super().__repr__()}]"


class MacroDefinition(Node):
    def __init__(
            self: 'MacroDefinition',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.MACRO_DEFINITION,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'MacroDefinition') -> str:
        return f"MacroDefinition[{self.super().__repr__()}]"


class MacroInstantiation(Node):
    def __init__(
            self: 'MacroInstantiation',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.MACRO_INSTANTIATION,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'MacroInstantiation') -> str:
        return f"MacroInstantiation[{self.super().__repr__()}]"


class InclusionDirective(Node):
    def __init__(
            self: 'InclusionDirective',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.INCLUSION_DIRECTIVE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'InclusionDirective') -> str:
        return f"InclusionDirective[{self.super().__repr__()}]"


class ModuleImportDecl(Node):
    def __init__(
            self: 'ModuleImportDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.MODULE_IMPORT_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'ModuleImportDecl') -> str:
        return f"ModuleImportDecl[{self.super().__repr__()}]"


class TypeAliasTemplateDecl(Node):
    def __init__(
            self: 'TypeAliasTemplateDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.TYPE_ALIAS_TEMPLATE_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'TypeAliasTemplateDecl') -> str:
        return f"TypeAliasTemplateDecl[{self.super().__repr__()}]"


class StaticAssert(Node):
    def __init__(
            self: 'StaticAssert',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.STATIC_ASSERT,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'StaticAssert') -> str:
        return f"StaticAssert[{self.super().__repr__()}]"


class FriendDecl(Node):
    def __init__(
            self: 'FriendDecl',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.FRIEND_DECL,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'FriendDecl') -> str:
        return f"FriendDecl[{self.super().__repr__()}]"


class OverloadCandidate(Node):
    def __init__(
            self: 'OverloadCandidate',
            parent: Node,
            definition_id: int,
            extent: SourceRange,
            id: int,
            is_definition: bool,
            spelling: str,
            usr: str,
            children: list[Node]
    ):
        self.super().__init__(
            parent,
            definition_id,
            extent,
            id,
            is_definition,
            CursorKind.OVERLOAD_CANDIDATE,
            spelling,
            usr,
            children
        )

    def __repr__(self: 'OverloadCandidate') -> str:
        return f"OverloadCandidate[{self.super().__repr__()}]"


class Visitor:
    def visit_children(self: 'Visitor', node: Node):
        for child in node.children:
            self.visit(child)

    def visit(self: 'Visitor', node: Node):
        if isinstance(node, UnexposedDecl):
            self.visit_UnexposedDecl(node)

        if isinstance(node, StructDecl):
            self.visit_StructDecl(node)

        if isinstance(node, UnionDecl):
            self.visit_UnionDecl(node)

        if isinstance(node, ClassDecl):
            self.visit_ClassDecl(node)

        if isinstance(node, EnumDecl):
            self.visit_EnumDecl(node)

        if isinstance(node, FieldDecl):
            self.visit_FieldDecl(node)

        if isinstance(node, EnumConstantDecl):
            self.visit_EnumConstantDecl(node)

        if isinstance(node, FunctionDecl):
            self.visit_FunctionDecl(node)

        if isinstance(node, VarDecl):
            self.visit_VarDecl(node)

        if isinstance(node, ParmDecl):
            self.visit_ParmDecl(node)

        if isinstance(node, ObjcInterfaceDecl):
            self.visit_ObjcInterfaceDecl(node)

        if isinstance(node, ObjcCategoryDecl):
            self.visit_ObjcCategoryDecl(node)

        if isinstance(node, ObjcProtocolDecl):
            self.visit_ObjcProtocolDecl(node)

        if isinstance(node, ObjcPropertyDecl):
            self.visit_ObjcPropertyDecl(node)

        if isinstance(node, ObjcIvarDecl):
            self.visit_ObjcIvarDecl(node)

        if isinstance(node, ObjcInstanceMethodDecl):
            self.visit_ObjcInstanceMethodDecl(node)

        if isinstance(node, ObjcClassMethodDecl):
            self.visit_ObjcClassMethodDecl(node)

        if isinstance(node, ObjcImplementationDecl):
            self.visit_ObjcImplementationDecl(node)

        if isinstance(node, ObjcCategoryImplDecl):
            self.visit_ObjcCategoryImplDecl(node)

        if isinstance(node, TypedefDecl):
            self.visit_TypedefDecl(node)

        if isinstance(node, CxxMethod):
            self.visit_CxxMethod(node)

        if isinstance(node, Namespace):
            self.visit_Namespace(node)

        if isinstance(node, LinkageSpec):
            self.visit_LinkageSpec(node)

        if isinstance(node, Constructor):
            self.visit_Constructor(node)

        if isinstance(node, Destructor):
            self.visit_Destructor(node)

        if isinstance(node, ConversionFunction):
            self.visit_ConversionFunction(node)

        if isinstance(node, TemplateTypeParameter):
            self.visit_TemplateTypeParameter(node)

        if isinstance(node, TemplateNonTypeParameter):
            self.visit_TemplateNonTypeParameter(node)

        if isinstance(node, TemplateTemplateParameter):
            self.visit_TemplateTemplateParameter(node)

        if isinstance(node, FunctionTemplate):
            self.visit_FunctionTemplate(node)

        if isinstance(node, ClassTemplate):
            self.visit_ClassTemplate(node)

        if isinstance(node, ClassTemplatePartialSpecialization):
            self.visit_ClassTemplatePartialSpecialization(node)

        if isinstance(node, NamespaceAlias):
            self.visit_NamespaceAlias(node)

        if isinstance(node, UsingDirective):
            self.visit_UsingDirective(node)

        if isinstance(node, UsingDeclaration):
            self.visit_UsingDeclaration(node)

        if isinstance(node, TypeAliasDecl):
            self.visit_TypeAliasDecl(node)

        if isinstance(node, ObjcSynthesizeDecl):
            self.visit_ObjcSynthesizeDecl(node)

        if isinstance(node, ObjcDynamicDecl):
            self.visit_ObjcDynamicDecl(node)

        if isinstance(node, CxxAccessSpecDecl):
            self.visit_CxxAccessSpecDecl(node)

        if isinstance(node, ObjcSuperClassRef):
            self.visit_ObjcSuperClassRef(node)

        if isinstance(node, ObjcProtocolRef):
            self.visit_ObjcProtocolRef(node)

        if isinstance(node, ObjcClassRef):
            self.visit_ObjcClassRef(node)

        if isinstance(node, TypeRef):
            self.visit_TypeRef(node)

        if isinstance(node, CxxBaseSpecifier):
            self.visit_CxxBaseSpecifier(node)

        if isinstance(node, TemplateRef):
            self.visit_TemplateRef(node)

        if isinstance(node, NamespaceRef):
            self.visit_NamespaceRef(node)

        if isinstance(node, MemberRef):
            self.visit_MemberRef(node)

        if isinstance(node, LabelRef):
            self.visit_LabelRef(node)

        if isinstance(node, OverloadedDeclRef):
            self.visit_OverloadedDeclRef(node)

        if isinstance(node, VariableRef):
            self.visit_VariableRef(node)

        if isinstance(node, InvalidFile):
            self.visit_InvalidFile(node)

        if isinstance(node, NoDeclFound):
            self.visit_NoDeclFound(node)

        if isinstance(node, NotImplemented):
            self.visit_NotImplemented(node)

        if isinstance(node, InvalidCode):
            self.visit_InvalidCode(node)

        if isinstance(node, UnexposedExpr):
            self.visit_UnexposedExpr(node)

        if isinstance(node, DeclRefExpr):
            self.visit_DeclRefExpr(node)

        if isinstance(node, MemberRefExpr):
            self.visit_MemberRefExpr(node)

        if isinstance(node, CallExpr):
            self.visit_CallExpr(node)

        if isinstance(node, ObjcMessageExpr):
            self.visit_ObjcMessageExpr(node)

        if isinstance(node, BlockExpr):
            self.visit_BlockExpr(node)

        if isinstance(node, IntegerLiteral):
            self.visit_IntegerLiteral(node)

        if isinstance(node, FloatingLiteral):
            self.visit_FloatingLiteral(node)

        if isinstance(node, ImaginaryLiteral):
            self.visit_ImaginaryLiteral(node)

        if isinstance(node, StringLiteral):
            self.visit_StringLiteral(node)

        if isinstance(node, CharacterLiteral):
            self.visit_CharacterLiteral(node)

        if isinstance(node, ParenExpr):
            self.visit_ParenExpr(node)

        if isinstance(node, UnaryOperator):
            self.visit_UnaryOperator(node)

        if isinstance(node, ArraySubscriptExpr):
            self.visit_ArraySubscriptExpr(node)

        if isinstance(node, BinaryOperator):
            self.visit_BinaryOperator(node)

        if isinstance(node, CompoundAssignmentOperator):
            self.visit_CompoundAssignmentOperator(node)

        if isinstance(node, ConditionalOperator):
            self.visit_ConditionalOperator(node)

        if isinstance(node, CstyleCastExpr):
            self.visit_CstyleCastExpr(node)

        if isinstance(node, CompoundLiteralExpr):
            self.visit_CompoundLiteralExpr(node)

        if isinstance(node, InitListExpr):
            self.visit_InitListExpr(node)

        if isinstance(node, AddrLabelExpr):
            self.visit_AddrLabelExpr(node)

        if isinstance(node, Stmtexpr):
            self.visit_Stmtexpr(node)

        if isinstance(node, GenericSelectionExpr):
            self.visit_GenericSelectionExpr(node)

        if isinstance(node, GnuNullExpr):
            self.visit_GnuNullExpr(node)

        if isinstance(node, CxxStaticCastExpr):
            self.visit_CxxStaticCastExpr(node)

        if isinstance(node, CxxDynamicCastExpr):
            self.visit_CxxDynamicCastExpr(node)

        if isinstance(node, CxxReinterpretCastExpr):
            self.visit_CxxReinterpretCastExpr(node)

        if isinstance(node, CxxConstCastExpr):
            self.visit_CxxConstCastExpr(node)

        if isinstance(node, CxxFunctionalCastExpr):
            self.visit_CxxFunctionalCastExpr(node)

        if isinstance(node, CxxTypeidExpr):
            self.visit_CxxTypeidExpr(node)

        if isinstance(node, CxxBoolLiteralExpr):
            self.visit_CxxBoolLiteralExpr(node)

        if isinstance(node, CxxNullPtrLiteralExpr):
            self.visit_CxxNullPtrLiteralExpr(node)

        if isinstance(node, CxxThisExpr):
            self.visit_CxxThisExpr(node)

        if isinstance(node, CxxThrowExpr):
            self.visit_CxxThrowExpr(node)

        if isinstance(node, CxxNewExpr):
            self.visit_CxxNewExpr(node)

        if isinstance(node, CxxDeleteExpr):
            self.visit_CxxDeleteExpr(node)

        if isinstance(node, CxxUnaryExpr):
            self.visit_CxxUnaryExpr(node)

        if isinstance(node, ObjcStringLiteral):
            self.visit_ObjcStringLiteral(node)

        if isinstance(node, ObjcEncodeExpr):
            self.visit_ObjcEncodeExpr(node)

        if isinstance(node, ObjcSelectorExpr):
            self.visit_ObjcSelectorExpr(node)

        if isinstance(node, ObjcProtocolExpr):
            self.visit_ObjcProtocolExpr(node)

        if isinstance(node, ObjcBridgeCastExpr):
            self.visit_ObjcBridgeCastExpr(node)

        if isinstance(node, PackExpansionExpr):
            self.visit_PackExpansionExpr(node)

        if isinstance(node, SizeOfPackExpr):
            self.visit_SizeOfPackExpr(node)

        if isinstance(node, LambdaExpr):
            self.visit_LambdaExpr(node)

        if isinstance(node, ObjBoolLiteralExpr):
            self.visit_ObjBoolLiteralExpr(node)

        if isinstance(node, ObjSelfExpr):
            self.visit_ObjSelfExpr(node)

        if isinstance(node, OmpArraySectionExpr):
            self.visit_OmpArraySectionExpr(node)

        if isinstance(node, ObjcAvailabilityCheckExpr):
            self.visit_ObjcAvailabilityCheckExpr(node)

        if isinstance(node, UnexposedStmt):
            self.visit_UnexposedStmt(node)

        if isinstance(node, LabelStmt):
            self.visit_LabelStmt(node)

        if isinstance(node, CompoundStmt):
            self.visit_CompoundStmt(node)

        if isinstance(node, CaseStmt):
            self.visit_CaseStmt(node)

        if isinstance(node, DefaultStmt):
            self.visit_DefaultStmt(node)

        if isinstance(node, IfStmt):
            self.visit_IfStmt(node)

        if isinstance(node, SwitchStmt):
            self.visit_SwitchStmt(node)

        if isinstance(node, WhileStmt):
            self.visit_WhileStmt(node)

        if isinstance(node, DoStmt):
            self.visit_DoStmt(node)

        if isinstance(node, ForStmt):
            self.visit_ForStmt(node)

        if isinstance(node, GotoStmt):
            self.visit_GotoStmt(node)

        if isinstance(node, IndirectGotoStmt):
            self.visit_IndirectGotoStmt(node)

        if isinstance(node, ContinueStmt):
            self.visit_ContinueStmt(node)

        if isinstance(node, BreakStmt):
            self.visit_BreakStmt(node)

        if isinstance(node, ReturnStmt):
            self.visit_ReturnStmt(node)

        if isinstance(node, AsmStmt):
            self.visit_AsmStmt(node)

        if isinstance(node, ObjcAtTryStmt):
            self.visit_ObjcAtTryStmt(node)

        if isinstance(node, ObjcAtCatchStmt):
            self.visit_ObjcAtCatchStmt(node)

        if isinstance(node, ObjcAtFinallyStmt):
            self.visit_ObjcAtFinallyStmt(node)

        if isinstance(node, ObjcAtThrowStmt):
            self.visit_ObjcAtThrowStmt(node)

        if isinstance(node, ObjcAtSynchronizedStmt):
            self.visit_ObjcAtSynchronizedStmt(node)

        if isinstance(node, ObjcAutoreleasePoolStmt):
            self.visit_ObjcAutoreleasePoolStmt(node)

        if isinstance(node, ObjcForCollectionStmt):
            self.visit_ObjcForCollectionStmt(node)

        if isinstance(node, CxxCatchStmt):
            self.visit_CxxCatchStmt(node)

        if isinstance(node, CxxTryStmt):
            self.visit_CxxTryStmt(node)

        if isinstance(node, CxxForRangeStmt):
            self.visit_CxxForRangeStmt(node)

        if isinstance(node, SehTryStmt):
            self.visit_SehTryStmt(node)

        if isinstance(node, SehExceptStmt):
            self.visit_SehExceptStmt(node)

        if isinstance(node, SehFinallyStmt):
            self.visit_SehFinallyStmt(node)

        if isinstance(node, MsAsmStmt):
            self.visit_MsAsmStmt(node)

        if isinstance(node, NullStmt):
            self.visit_NullStmt(node)

        if isinstance(node, DeclStmt):
            self.visit_DeclStmt(node)

        if isinstance(node, OmpParallelDirective):
            self.visit_OmpParallelDirective(node)

        if isinstance(node, OmpSimdDirective):
            self.visit_OmpSimdDirective(node)

        if isinstance(node, OmpForDirective):
            self.visit_OmpForDirective(node)

        if isinstance(node, OmpSectionsDirective):
            self.visit_OmpSectionsDirective(node)

        if isinstance(node, OmpSectionDirective):
            self.visit_OmpSectionDirective(node)

        if isinstance(node, OmpSingleDirective):
            self.visit_OmpSingleDirective(node)

        if isinstance(node, OmpParallelForDirective):
            self.visit_OmpParallelForDirective(node)

        if isinstance(node, OmpParallelSectionsDirective):
            self.visit_OmpParallelSectionsDirective(node)

        if isinstance(node, OmpTaskDirective):
            self.visit_OmpTaskDirective(node)

        if isinstance(node, OmpMasterDirective):
            self.visit_OmpMasterDirective(node)

        if isinstance(node, OmpCriticalDirective):
            self.visit_OmpCriticalDirective(node)

        if isinstance(node, OmpTaskyieldDirective):
            self.visit_OmpTaskyieldDirective(node)

        if isinstance(node, OmpBarrierDirective):
            self.visit_OmpBarrierDirective(node)

        if isinstance(node, OmpTaskwaitDirective):
            self.visit_OmpTaskwaitDirective(node)

        if isinstance(node, OmpFlushDirective):
            self.visit_OmpFlushDirective(node)

        if isinstance(node, SehLeaveStmt):
            self.visit_SehLeaveStmt(node)

        if isinstance(node, OmpOrderedDirective):
            self.visit_OmpOrderedDirective(node)

        if isinstance(node, OmpAtomicDirective):
            self.visit_OmpAtomicDirective(node)

        if isinstance(node, OmpForSimdDirective):
            self.visit_OmpForSimdDirective(node)

        if isinstance(node, OmpParallelforsimdDirective):
            self.visit_OmpParallelforsimdDirective(node)

        if isinstance(node, OmpTargetDirective):
            self.visit_OmpTargetDirective(node)

        if isinstance(node, OmpTeamsDirective):
            self.visit_OmpTeamsDirective(node)

        if isinstance(node, OmpTaskgroupDirective):
            self.visit_OmpTaskgroupDirective(node)

        if isinstance(node, OmpCancellationPointDirective):
            self.visit_OmpCancellationPointDirective(node)

        if isinstance(node, OmpCancelDirective):
            self.visit_OmpCancelDirective(node)

        if isinstance(node, OmpTargetDataDirective):
            self.visit_OmpTargetDataDirective(node)

        if isinstance(node, OmpTaskLoopDirective):
            self.visit_OmpTaskLoopDirective(node)

        if isinstance(node, OmpTaskLoopSimdDirective):
            self.visit_OmpTaskLoopSimdDirective(node)

        if isinstance(node, OmpDistributeDirective):
            self.visit_OmpDistributeDirective(node)

        if isinstance(node, OmpTargetEnterDataDirective):
            self.visit_OmpTargetEnterDataDirective(node)

        if isinstance(node, OmpTargetExitDataDirective):
            self.visit_OmpTargetExitDataDirective(node)

        if isinstance(node, OmpTargetParallelDirective):
            self.visit_OmpTargetParallelDirective(node)

        if isinstance(node, OmpTargetParallelforDirective):
            self.visit_OmpTargetParallelforDirective(node)

        if isinstance(node, OmpTargetUpdateDirective):
            self.visit_OmpTargetUpdateDirective(node)

        if isinstance(node, OmpDistributeParallelforDirective):
            self.visit_OmpDistributeParallelforDirective(node)

        if isinstance(node, OmpDistributeParallelForSimdDirective):
            self.visit_OmpDistributeParallelForSimdDirective(node)

        if isinstance(node, OmpDistributeSimdDirective):
            self.visit_OmpDistributeSimdDirective(node)

        if isinstance(node, OmpTargetParallelForSimdDirective):
            self.visit_OmpTargetParallelForSimdDirective(node)

        if isinstance(node, OmpTargetSimdDirective):
            self.visit_OmpTargetSimdDirective(node)

        if isinstance(node, OmpTeamsDistributeDirective):
            self.visit_OmpTeamsDistributeDirective(node)

        if isinstance(node, TranslationUnit):
            self.visit_TranslationUnit(node)

        if isinstance(node, UnexposedAttr):
            self.visit_UnexposedAttr(node)

        if isinstance(node, IbActionAttr):
            self.visit_IbActionAttr(node)

        if isinstance(node, IbOutletAttr):
            self.visit_IbOutletAttr(node)

        if isinstance(node, IbOutletCollectionAttr):
            self.visit_IbOutletCollectionAttr(node)

        if isinstance(node, CxxFinalAttr):
            self.visit_CxxFinalAttr(node)

        if isinstance(node, CxxOverrideAttr):
            self.visit_CxxOverrideAttr(node)

        if isinstance(node, AnnotateAttr):
            self.visit_AnnotateAttr(node)

        if isinstance(node, AsmLabelAttr):
            self.visit_AsmLabelAttr(node)

        if isinstance(node, PackedAttr):
            self.visit_PackedAttr(node)

        if isinstance(node, PureAttr):
            self.visit_PureAttr(node)

        if isinstance(node, ConstAttr):
            self.visit_ConstAttr(node)

        if isinstance(node, NoduplicateAttr):
            self.visit_NoduplicateAttr(node)

        if isinstance(node, CudaconstantAttr):
            self.visit_CudaconstantAttr(node)

        if isinstance(node, CudadeviceAttr):
            self.visit_CudadeviceAttr(node)

        if isinstance(node, CudaglobalAttr):
            self.visit_CudaglobalAttr(node)

        if isinstance(node, CudahostAttr):
            self.visit_CudahostAttr(node)

        if isinstance(node, CudasharedAttr):
            self.visit_CudasharedAttr(node)

        if isinstance(node, VisibilityAttr):
            self.visit_VisibilityAttr(node)

        if isinstance(node, DllexportAttr):
            self.visit_DllexportAttr(node)

        if isinstance(node, DllimportAttr):
            self.visit_DllimportAttr(node)

        if isinstance(node, ConvergentAttr):
            self.visit_ConvergentAttr(node)

        if isinstance(node, WarnUnusedAttr):
            self.visit_WarnUnusedAttr(node)

        if isinstance(node, WarnUnusedResultAttr):
            self.visit_WarnUnusedResultAttr(node)

        if isinstance(node, AlignedAttr):
            self.visit_AlignedAttr(node)

        if isinstance(node, PreprocessingDirective):
            self.visit_PreprocessingDirective(node)

        if isinstance(node, MacroDefinition):
            self.visit_MacroDefinition(node)

        if isinstance(node, MacroInstantiation):
            self.visit_MacroInstantiation(node)

        if isinstance(node, InclusionDirective):
            self.visit_InclusionDirective(node)

        if isinstance(node, ModuleImportDecl):
            self.visit_ModuleImportDecl(node)

        if isinstance(node, TypeAliasTemplateDecl):
            self.visit_TypeAliasTemplateDecl(node)

        if isinstance(node, StaticAssert):
            self.visit_StaticAssert(node)

        if isinstance(node, FriendDecl):
            self.visit_FriendDecl(node)

        if isinstance(node, OverloadCandidate):
            self.visit_OverloadCandidate(node)

            def visit_UnexposedDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_StructDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_UnionDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ClassDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_EnumDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_FieldDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_EnumConstantDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_FunctionDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_VarDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ParmDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcInterfaceDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcCategoryDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcProtocolDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcPropertyDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcIvarDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcInstanceMethodDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcClassMethodDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcImplementationDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcCategoryImplDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TypedefDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxMethod(self: Visitor) -> None:
                self.visit_children(node)

            def visit_Namespace(self: Visitor) -> None:
                self.visit_children(node)

            def visit_LinkageSpec(self: Visitor) -> None:
                self.visit_children(node)

            def visit_Constructor(self: Visitor) -> None:
                self.visit_children(node)

            def visit_Destructor(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ConversionFunction(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TemplateTypeParameter(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TemplateNonTypeParameter(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TemplateTemplateParameter(self: Visitor) -> None:
                self.visit_children(node)

            def visit_FunctionTemplate(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ClassTemplate(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ClassTemplatePartialSpecialization(self: Visitor) -> None:
                self.visit_children(node)

            def visit_NamespaceAlias(self: Visitor) -> None:
                self.visit_children(node)

            def visit_UsingDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_UsingDeclaration(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TypeAliasDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcSynthesizeDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcDynamicDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxAccessSpecDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcSuperClassRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcProtocolRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcClassRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TypeRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxBaseSpecifier(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TemplateRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_NamespaceRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_MemberRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_LabelRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OverloadedDeclRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_VariableRef(self: Visitor) -> None:
                self.visit_children(node)

            def visit_InvalidFile(self: Visitor) -> None:
                self.visit_children(node)

            def visit_NoDeclFound(self: Visitor) -> None:
                self.visit_children(node)

            def visit_NotImplemented(self: Visitor) -> None:
                self.visit_children(node)

            def visit_InvalidCode(self: Visitor) -> None:
                self.visit_children(node)

            def visit_UnexposedExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_DeclRefExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_MemberRefExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CallExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcMessageExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_BlockExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_IntegerLiteral(self: Visitor) -> None:
                self.visit_children(node)

            def visit_FloatingLiteral(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ImaginaryLiteral(self: Visitor) -> None:
                self.visit_children(node)

            def visit_StringLiteral(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CharacterLiteral(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ParenExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_UnaryOperator(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ArraySubscriptExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_BinaryOperator(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CompoundAssignmentOperator(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ConditionalOperator(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CstyleCastExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CompoundLiteralExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_InitListExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_AddrLabelExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_Stmtexpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_GenericSelectionExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_GnuNullExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxStaticCastExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxDynamicCastExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxReinterpretCastExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxConstCastExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxFunctionalCastExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxTypeidExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxBoolLiteralExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxNullPtrLiteralExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxThisExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxThrowExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxNewExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxDeleteExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxUnaryExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcStringLiteral(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcEncodeExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcSelectorExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcProtocolExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcBridgeCastExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_PackExpansionExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_SizeOfPackExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_LambdaExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjBoolLiteralExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjSelfExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpArraySectionExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcAvailabilityCheckExpr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_UnexposedStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_LabelStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CompoundStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CaseStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_DefaultStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_IfStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_SwitchStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_WhileStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_DoStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ForStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_GotoStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_IndirectGotoStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ContinueStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_BreakStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ReturnStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_AsmStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcAtTryStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcAtCatchStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcAtFinallyStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcAtThrowStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcAtSynchronizedStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcAutoreleasePoolStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ObjcForCollectionStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxCatchStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxTryStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxForRangeStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_SehTryStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_SehExceptStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_SehFinallyStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_MsAsmStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_NullStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_DeclStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpParallelDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpSimdDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpForDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpSectionsDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpSectionDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpSingleDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpParallelForDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpParallelSectionsDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTaskDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpMasterDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpCriticalDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTaskyieldDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpBarrierDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTaskwaitDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpFlushDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_SehLeaveStmt(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpOrderedDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpAtomicDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpForSimdDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpParallelforsimdDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTeamsDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTaskgroupDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpCancellationPointDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpCancelDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetDataDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTaskLoopDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTaskLoopSimdDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpDistributeDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetEnterDataDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetExitDataDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetParallelDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetParallelforDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetUpdateDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpDistributeParallelforDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpDistributeParallelForSimdDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpDistributeSimdDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetParallelForSimdDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTargetSimdDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OmpTeamsDistributeDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TranslationUnit(self: Visitor) -> None:
                self.visit_children(node)

            def visit_UnexposedAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_IbActionAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_IbOutletAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_IbOutletCollectionAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxFinalAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CxxOverrideAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_AnnotateAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_AsmLabelAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_PackedAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_PureAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ConstAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_NoduplicateAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CudaconstantAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CudadeviceAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CudaglobalAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CudahostAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_CudasharedAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_VisibilityAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_DllexportAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_DllimportAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ConvergentAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_WarnUnusedAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_WarnUnusedResultAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_AlignedAttr(self: Visitor) -> None:
                self.visit_children(node)

            def visit_PreprocessingDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_MacroDefinition(self: Visitor) -> None:
                self.visit_children(node)

            def visit_MacroInstantiation(self: Visitor) -> None:
                self.visit_children(node)

            def visit_InclusionDirective(self: Visitor) -> None:
                self.visit_children(node)

            def visit_ModuleImportDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_TypeAliasTemplateDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_StaticAssert(self: Visitor) -> None:
                self.visit_children(node)

            def visit_FriendDecl(self: Visitor) -> None:
                self.visit_children(node)

            def visit_OverloadCandidate(self: Visitor) -> None:
                self.visit_children(node)
