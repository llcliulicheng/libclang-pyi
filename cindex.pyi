import typing
from ctypes import *

c_object_p = POINTER(c_void_p)
callbacks = {}

class TranslationUnitLoadError(Exception):...

class TranslationUnitSaveError(Exception):
    ERROR_UNKNOWN = 1
    ERROR_TRANSLATION_ERRORS = 2
    ERROR_INVALID_TU = 3

    def __init__(self, enumeration, message):...

class CachedProperty:
    def __init__(self, wrapped):...

    def __get__(self, instance, instance_type=None):...

class SourceLocation(Structure):
    @staticmethod
    def from_position(tu, file, line, column) -> SourceLocation:...

    @staticmethod
    def from_offset(tu, file, offset) -> SourceLocation:...

    @property
    def file(self) -> File:...

    @property
    def line(self) -> int:...

    @property
    def column(self) -> int:...

    @property
    def offset(self) -> int:...

    @property
    def is_in_system_header(self) -> bool:...

    def __eq__(self, other) -> bool:...

    def __ne__(self, other) -> bool:...

class SourceRange(Structure):
    @staticmethod
    def from_locations(start, end) -> SourceRange:...

    @property
    def start(self) -> SourceLocation:...

    @property
    def end(self) -> SourceLocation:...

    def __eq__(self, other) -> bool:...

    def __ne__(self, other) -> bool:...

    def __contains__(self, other) -> bool:...

class Diagnostic:
    Ignored = 0
    Note = 1
    Warning = 2
    Error = 3
    Fatal = 4

    DisplaySourceLocation = 0x01
    DisplayColumn = 0x02
    DisplaySourceRanges = 0x04
    DisplayOption = 0x08
    DisplayCategoryId = 0x10
    DisplayCategoryName = 0x20
    _FormatOptionsMask = 0x3F

    def __init__(self, ptr):...

    @property
    def severity(self) -> int:...

    @property
    def location(self) -> SourceLocation:...

    @property
    def spelling(self) -> str:...

    @property
    def ranges(self) -> typing.Iterable[SourceRange]:...

    @property
    def fixits(self) -> typing.Iterable[FixIt]:...

    @property
    def children(self) -> typing.Iterable[Diagnostic]:...

    @property
    def category_number(self) -> int:...

    @property
    def category_name(self) -> str:...

    @property
    def option(self) -> str:...

    @property
    def disable_option(self) -> str:...

    def format(self, options=None) -> str:...

    def from_param(self) -> int:...

class FixIt:
    def __init__(self, range, value):...

class TokenKind:
    def __init__(self, value, name):...

    @staticmethod
    def from_value(value) -> TokenKind:...

    @staticmethod
    def register(value, name):...

class BaseEnumeration:
    @staticmethod
    def from_value(value):...

    def from_param(self):...

    @property
    def name(self) -> str:...

class CursorKind(BaseEnumeration):
    UNEXPOSED_DECL: CursorKind
    STRUCT_DECL: CursorKind
    UNION_DECL: CursorKind
    CLASS_DECL: CursorKind
    ENUM_DECL: CursorKind
    FIELD_DECL: CursorKind
    ENUM_CONSTANT_DECL: CursorKind
    FUNCTION_DECL: CursorKind
    VAR_DECL: CursorKind
    PARM_DECL: CursorKind
    OBJC_INTERFACE_DECL: CursorKind
    OBJC_CATEGORY_DECL: CursorKind
    OBJC_PROTOCOL_DECL: CursorKind
    OBJC_PROPERTY_DECL: CursorKind
    OBJC_IVAR_DECL: CursorKind
    OBJC_INSTANCE_METHOD_DECL: CursorKind
    OBJC_CLASS_METHOD_DECL: CursorKind
    OBJC_IMPLEMENTATION_DECL: CursorKind
    OBJC_CATEGORY_IMPL_DECL: CursorKind
    TYPEDEF_DECL: CursorKind
    CXX_METHOD: CursorKind
    NAMESPACE: CursorKind
    LINKAGE_SPEC: CursorKind
    CONSTRUCTOR: CursorKind
    DESTRUCTOR: CursorKind
    CONVERSION_FUNCTION: CursorKind
    TEMPLATE_TYPE_PARAMETER: CursorKind
    TEMPLATE_NON_TYPE_PARAMETER: CursorKind
    TEMPLATE_TEMPLATE_PARAMETER: CursorKind
    FUNCTION_TEMPLATE: CursorKind
    CLASS_TEMPLATE: CursorKind
    CLASS_TEMPLATE_PARTIAL_SPECIALIZATION: CursorKind
    NAMESPACE_ALIAS: CursorKind
    USING_DIRECTIVE: CursorKind
    USING_DECLARATION: CursorKind
    TYPE_ALIAS_DECL: CursorKind
    OBJC_SYNTHESIZE_DECL: CursorKind
    OBJC_DYNAMIC_DECL: CursorKind
    CXX_ACCESS_SPEC_DECL: CursorKind
    OBJC_SUPER_CLASS_REF: CursorKind
    OBJC_PROTOCOL_REF: CursorKind
    OBJC_CLASS_REF: CursorKind
    TYPE_REF: CursorKind
    CXX_BASE_SPECIFIER: CursorKind
    TEMPLATE_REF: CursorKind
    NAMESPACE_REF: CursorKind
    MEMBER_REF: CursorKind
    LABEL_REF: CursorKind
    OVERLOADED_DECL_REF: CursorKind
    VARIABLE_REF: CursorKind
    INVALID_FILE: CursorKind
    NO_DECL_FOUND: CursorKind
    NOT_IMPLEMENTED: CursorKind
    INVALID_CODE: CursorKind
    UNEXPOSED_EXPR: CursorKind
    DECL_REF_EXPR: CursorKind
    MEMBER_REF_EXPR: CursorKind
    CALL_EXPR: CursorKind
    OBJC_MESSAGE_EXPR: CursorKind
    BLOCK_EXPR: CursorKind
    INTEGER_LITERAL: CursorKind
    FLOATING_LITERAL: CursorKind
    IMAGINARY_LITERAL: CursorKind
    STRING_LITERAL: CursorKind
    CHARACTER_LITERAL: CursorKind
    PAREN_EXPR: CursorKind
    UNARY_OPERATOR: CursorKind
    ARRAY_SUBSCRIPT_EXPR: CursorKind
    BINARY_OPERATOR: CursorKind
    COMPOUND_ASSIGNMENT_OPERATOR: CursorKind
    CONDITIONAL_OPERATOR: CursorKind
    CSTYLE_CAST_EXPR: CursorKind
    COMPOUND_LITERAL_EXPR: CursorKind
    INIT_LIST_EXPR: CursorKind
    ADDR_LABEL_EXPR: CursorKind
    StmtExpr: CursorKind
    GENERIC_SELECTION_EXPR: CursorKind
    GNU_NULL_EXPR: CursorKind
    CXX_STATIC_CAST_EXPR: CursorKind
    CXX_DYNAMIC_CAST_EXPR: CursorKind
    CXX_REINTERPRET_CAST_EXPR: CursorKind
    CXX_CONST_CAST_EXPR: CursorKind
    CXX_FUNCTIONAL_CAST_EXPR: CursorKind
    CXX_TYPEID_EXPR: CursorKind
    CXX_BOOL_LITERAL_EXPR: CursorKind
    CXX_NULL_PTR_LITERAL_EXPR: CursorKind
    CXX_THIS_EXPR: CursorKind
    CXX_THROW_EXPR: CursorKind
    CXX_NEW_EXPR: CursorKind
    CXX_DELETE_EXPR: CursorKind
    CXX_UNARY_EXPR: CursorKind
    OBJC_STRING_LITERAL: CursorKind
    OBJC_ENCODE_EXPR: CursorKind
    OBJC_SELECTOR_EXPR: CursorKind
    OBJC_PROTOCOL_EXPR: CursorKind
    OBJC_BRIDGE_CAST_EXPR: CursorKind
    PACK_EXPANSION_EXPR: CursorKind
    SIZE_OF_PACK_EXPR: CursorKind
    LAMBDA_EXPR: CursorKind
    OBJ_BOOL_LITERAL_EXPR: CursorKind
    OBJ_SELF_EXPR: CursorKind
    OMP_ARRAY_SECTION_EXPR: CursorKind
    OBJC_AVAILABILITY_CHECK_EXPR: CursorKind
    FIXED_POINT_LITERAL: CursorKind
    OMP_ARRAY_SHAPING_EXPR: CursorKind
    OMP_ITERATOR_EXPR: CursorKind
    CXX_ADDRSPACE_CAST_EXPR: CursorKind
    CONCEPT_SPECIALIZATION_EXPR: CursorKind
    REQUIRES_EXPR: CursorKind
    UNEXPOSED_STMT: CursorKind
    LABEL_STMT: CursorKind
    COMPOUND_STMT: CursorKind
    CASE_STMT: CursorKind
    DEFAULT_STMT: CursorKind
    IF_STMT: CursorKind
    SWITCH_STMT: CursorKind
    WHILE_STMT: CursorKind
    DO_STMT: CursorKind
    FOR_STMT: CursorKind
    GOTO_STMT: CursorKind
    INDIRECT_GOTO_STMT: CursorKind
    CONTINUE_STMT: CursorKind
    BREAK_STMT: CursorKind
    RETURN_STMT: CursorKind
    ASM_STMT: CursorKind
    OBJC_AT_TRY_STMT: CursorKind
    OBJC_AT_CATCH_STMT: CursorKind
    OBJC_AT_FINALLY_STMT: CursorKind
    OBJC_AT_THROW_STMT: CursorKind
    OBJC_AT_SYNCHRONIZED_STMT: CursorKind
    OBJC_AUTORELEASE_POOL_STMT: CursorKind
    OBJC_FOR_COLLECTION_STMT: CursorKind
    CXX_CATCH_STMT: CursorKind
    CXX_TRY_STMT: CursorKind
    CXX_FOR_RANGE_STMT: CursorKind
    SEH_TRY_STMT: CursorKind
    SEH_EXCEPT_STMT: CursorKind
    SEH_FINALLY_STMT: CursorKind
    MS_ASM_STMT: CursorKind
    NULL_STMT: CursorKind
    DECL_STMT: CursorKind
    OMP_PARALLEL_DIRECTIVE: CursorKind
    OMP_SIMD_DIRECTIVE: CursorKind
    OMP_FOR_DIRECTIVE: CursorKind
    OMP_SECTIONS_DIRECTIVE: CursorKind
    OMP_SECTION_DIRECTIVE: CursorKind
    OMP_SINGLE_DIRECTIVE: CursorKind
    OMP_PARALLEL_FOR_DIRECTIVE: CursorKind
    OMP_PARALLEL_SECTIONS_DIRECTIVE: CursorKind
    OMP_TASK_DIRECTIVE: CursorKind
    OMP_MASTER_DIRECTIVE: CursorKind
    OMP_CRITICAL_DIRECTIVE: CursorKind
    OMP_TASKYIELD_DIRECTIVE: CursorKind
    OMP_BARRIER_DIRECTIVE: CursorKind
    OMP_TASKWAIT_DIRECTIVE: CursorKind
    OMP_FLUSH_DIRECTIVE: CursorKind
    SEH_LEAVE_STMT: CursorKind
    OMP_ORDERED_DIRECTIVE: CursorKind
    OMP_ATOMIC_DIRECTIVE: CursorKind
    OMP_FOR_SIMD_DIRECTIVE: CursorKind
    OMP_PARALLELFORSIMD_DIRECTIVE: CursorKind
    OMP_TARGET_DIRECTIVE: CursorKind
    OMP_TEAMS_DIRECTIVE: CursorKind
    OMP_TASKGROUP_DIRECTIVE: CursorKind
    OMP_CANCELLATION_POINT_DIRECTIVE: CursorKind
    OMP_CANCEL_DIRECTIVE: CursorKind
    OMP_TARGET_DATA_DIRECTIVE: CursorKind
    OMP_TASK_LOOP_DIRECTIVE: CursorKind
    OMP_TASK_LOOP_SIMD_DIRECTIVE: CursorKind
    OMP_DISTRIBUTE_DIRECTIVE: CursorKind
    OMP_TARGET_ENTER_DATA_DIRECTIVE: CursorKind
    OMP_TARGET_EXIT_DATA_DIRECTIVE: CursorKind
    OMP_TARGET_PARALLEL_DIRECTIVE: CursorKind
    OMP_TARGET_PARALLELFOR_DIRECTIVE: CursorKind
    OMP_TARGET_UPDATE_DIRECTIVE: CursorKind
    OMP_DISTRIBUTE_PARALLELFOR_DIRECTIVE: CursorKind
    OMP_DISTRIBUTE_PARALLEL_FOR_SIMD_DIRECTIVE: CursorKind
    OMP_DISTRIBUTE_SIMD_DIRECTIVE: CursorKind
    OMP_TARGET_PARALLEL_FOR_SIMD_DIRECTIVE: CursorKind
    OMP_TARGET_SIMD_DIRECTIVE: CursorKind
    OMP_TEAMS_DISTRIBUTE_DIRECTIVE: CursorKind
    OMP_TEAMS_DISTRIBUTE_SIMD_DIRECTIVE: CursorKind
    OMP_TEAMS_DISTRIBUTE_PARALLEL_FOR_SIMD_DIRECTIVE: CursorKind
    OMP_TEAMS_DISTRIBUTE_PARALLEL_FOR_DIRECTIVE: CursorKind
    OMP_TARGET_TEAMS_DIRECTIVE: CursorKind
    OMP_TARGET_TEAMS_DISTRIBUTE_DIRECTIVE: CursorKind
    OMP_TARGET_TEAMS_DISTRIBUTE_PARALLEL_FOR_DIRECTIVE: CursorKind
    OMP_TARGET_TEAMS_DISTRIBUTE_PARALLEL_FOR_SIMD_DIRECTIVE: CursorKind
    OMP_TARGET_TEAMS_DISTRIBUTE_SIMD_DIRECTIVE: CursorKind
    BUILTIN_BIT_CAST_EXPR: CursorKind
    OMP_MASTER_TASK_LOOP_DIRECTIVE: CursorKind
    OMP_PARALLEL_MASTER_TASK_LOOP_DIRECTIVE: CursorKind
    OMP_MASTER_TASK_LOOP_SIMD_DIRECTIVE: CursorKind
    OMP_PARALLEL_MASTER_TASK_LOOP_SIMD_DIRECTIVE: CursorKind
    OMP_PARALLEL_MASTER_DIRECTIVE: CursorKind
    OMP_DEPOBJ_DIRECTIVE: CursorKind
    OMP_SCAN_DIRECTIVE: CursorKind
    OMP_TILE_DIRECTIVE: CursorKind
    OMP_CANONICAL_LOOP: CursorKind
    OMP_INTEROP_DIRECTIVE: CursorKind
    OMP_DISPATCH_DIRECTIVE: CursorKind
    OMP_MASKED_DIRECTIVE: CursorKind
    OMP_UNROLL_DIRECTIVE: CursorKind
    OMP_META_DIRECTIVE: CursorKind
    OMP_GENERIC_LOOP_DIRECTIVE: CursorKind
    OMP_TEAMS_GENERIC_LOOP_DIRECTIVE: CursorKind
    OMP_TARGET_TEAMS_GENERIC_LOOP_DIRECTIVE: CursorKind
    OMP_PARALLEL_GENERIC_LOOP_DIRECTIVE: CursorKind
    OMP_TARGET_PARALLEL_GENERIC_LOOP_DIRECTIVE: CursorKind
    OMP_PARALLEL_MASKED_DIRECTIVE: CursorKind
    OMP_MASKED_TASK_LOOP_DIRECTIVE: CursorKind
    OMP_MASKED_TASK_LOOP_SIMD_DIRECTIVE: CursorKind
    OMP_PARALLEL_MASKED_TASK_LOOP_DIRECTIVE: CursorKind
    OMP_PARALLEL_MASKED_TASK_LOOP_SIMD_DIRECTIVE: CursorKind
    TRANSLATION_UNIT: CursorKind
    UNEXPOSED_ATTR: CursorKind
    IB_ACTION_ATTR: CursorKind
    IB_OUTLET_ATTR: CursorKind
    IB_OUTLET_COLLECTION_ATTR: CursorKind
    CXX_FINAL_ATTR: CursorKind
    CXX_OVERRIDE_ATTR: CursorKind
    ANNOTATE_ATTR: CursorKind
    ASM_LABEL_ATTR: CursorKind
    PACKED_ATTR: CursorKind
    PURE_ATTR: CursorKind
    CONST_ATTR: CursorKind
    NODUPLICATE_ATTR: CursorKind
    CUDACONSTANT_ATTR: CursorKind
    CUDADEVICE_ATTR: CursorKind
    CUDAGLOBAL_ATTR: CursorKind
    CUDAHOST_ATTR: CursorKind
    CUDASHARED_ATTR: CursorKind
    VISIBILITY_ATTR: CursorKind
    DLLEXPORT_ATTR: CursorKind
    DLLIMPORT_ATTR: CursorKind
    CONVERGENT_ATTR: CursorKind
    WARN_UNUSED_ATTR: CursorKind
    WARN_UNUSED_RESULT_ATTR: CursorKind
    ALIGNED_ATTR: CursorKind
    PREPROCESSING_DIRECTIVE: CursorKind
    MACRO_DEFINITION: CursorKind
    MACRO_INSTANTIATION: CursorKind
    INCLUSION_DIRECTIVE: CursorKind
    MODULE_IMPORT_DECL: CursorKind
    TYPE_ALIAS_TEMPLATE_DECL: CursorKind
    STATIC_ASSERT: CursorKind
    FRIEND_DECL: CursorKind
    CONCEPT_DECL: CursorKind
    OVERLOAD_CANDIDATE: CursorKind

    @staticmethod
    def get_all_kinds() -> typing.Iterable[CursorKind]:...

    def is_declaration(self) -> bool:...

    def is_reference(self) -> bool:...

    def is_expression(self) -> bool:...

    def is_statement(self) -> bool:...

    def is_attribute(self) -> bool:...

    def is_invalid(self) -> bool:...

    def is_translation_unit(self) -> bool:...

    def is_preprocessing(self) -> bool:...

    def is_unexposed(self) -> bool:...

class TemplateArgumentKind(BaseEnumeration):
    NULL: TemplateArgumentKind
    TYPE: TemplateArgumentKind
    DECLARATION: TemplateArgumentKind
    NULLPTR: TemplateArgumentKind
    INTEGRAL: TemplateArgumentKind

class ExceptionSpecificationKind(BaseEnumeration):
    NONE: ExceptionSpecificationKind
    DYNAMIC_NONE: ExceptionSpecificationKind
    DYNAMIC: ExceptionSpecificationKind
    MS_ANY: ExceptionSpecificationKind
    BASIC_NOEXCEPT: ExceptionSpecificationKind
    COMPUTED_NOEXCEPT: ExceptionSpecificationKind
    UNEVALUATED: ExceptionSpecificationKind
    UNINSTANTIATED: ExceptionSpecificationKind
    UNPARSED: ExceptionSpecificationKind

class Cursor:
    @staticmethod
    def from_location(tu, location) -> Cursor:...

    def __hash__(self) -> int:...

    def __eq__(self, other) -> bool:...

    def __ne__(self, other) -> bool:...

    def is_definition(self) -> bool:...

    def is_const_method(self) -> bool:...

    def is_converting_constructor(self) -> bool:...

    def is_copy_constructor(self) -> bool:...

    def is_default_constructor(self) -> bool:...

    def is_move_constructor(self) -> bool:...

    def is_default_method(self) -> bool:...

    def is_deleted_method(self) -> bool:...

    def is_copy_assignment_operator_method(self) -> bool:...

    def is_move_assignment_operator_method(self) -> bool:...

    def is_explicit_method(self) -> bool:...

    def is_mutable_field(self) -> bool:...

    def is_pure_virtual_method(self) -> bool:...

    def is_static_method(self) -> bool:...

    def is_virtual_method(self) -> bool:...

    def is_abstract_record(self) -> bool:...

    def is_scoped_enum(self) -> bool:...

    def get_definition(self) -> Cursor:...

    def get_usr(self) -> str | None:...

    def get_included_file(self) -> File:...

    @property
    def kind(self) -> CursorKind:...

    @property
    def spelling(self) -> str:...

    @property
    def displayname(self) -> str:...

    @property
    def mangled_name(self) -> str:...

    @property
    def location(self) -> SourceLocation:...

    @property
    def linkage(self) -> LinkageKind:...

    @property
    def tls_kind(self) -> TLSKind:...

    @property
    def extent(self) -> SourceRange:...

    @property
    def storage_class(self) -> StorageClass:...

    @property
    def availability(self) -> AvailabilityKind:...

    @property
    def access_specifier(self) -> AccessSpecifier:...

    @property
    def type(self) -> Type:...

    @property
    def canonical(self) -> Type:...

    @property
    def result_type(self) -> Type:...

    @property
    def exception_specification_kind(self) -> ExceptionSpecificationKind:...

    @property
    def underlying_typedef_type(self) -> Type:...

    @property
    def enum_type(self) -> Type:...

    @property
    def enum_value(self) -> int:...

    @property
    def objc_type_encoding(self) -> str:...

    @property
    def hash(self) -> int:...

    @property
    def semantic_parent(self) -> Cursor:...

    @property
    def lexical_parent(self) -> Cursor:...

    @property
    def translation_unit(self) -> TranslationUnit:...

    @property
    def referenced(self) -> Cursor:...

    @property
    def brief_comment(self) -> str:...

    @property
    def raw_comment(self) -> str:...

    def get_arguments(self) -> typing.Iterable[Cursor]: ...

    def get_num_template_arguments(self) -> int:...

    def get_template_argument_kind(self, num: int) -> TemplateArgumentKind:...

    def get_template_argument_type(self, num: int) -> Type:...

    def get_template_argument_value(self, num: int) -> int:...

    def get_template_argument_unsigned_value(self, num: int) -> int:...

    def get_children(self) -> typing.Iterable[Cursor]:...

    def walk_preorder(self) -> typing.Iterable[Cursor]:...

    def get_tokens(self) -> typing.Iterable[Token]:...

    def get_field_offsetof(self) -> int:...

    def is_anonymous(self) -> bool:...

    def is_bitfield(self) -> bool:...

    def get_bitfield_width(self) -> int:...

    @staticmethod
    def from_result(res, fn, args) -> Cursor:...

    @staticmethod
    def from_cursor_result(res, fn, args) -> Cursor:...

class StorageClass:
    INVALID: StorageClass
    NONE: StorageClass
    EXTERN: StorageClass
    STATIC: StorageClass
    PRIVATEEXTERN: StorageClass
    OPENCLWORKGROUPLOCAL: StorageClass
    AUTO: StorageClass
    REGISTER: StorageClass

    def __init__(self, value):...

    @property
    def name(self) -> str:...

    @staticmethod
    def from_id(id) -> StorageClass:...

class AvailabilityKind(BaseEnumeration):
    AVAILABLE: AvailabilityKind
    DEPRECATED: AvailabilityKind
    NOT_AVAILABLE: AvailabilityKind
    NOT_ACCESSIBLE: AvailabilityKind

class AccessSpecifier(BaseEnumeration):
    INVALID: AccessSpecifier
    PUBLIC: AccessSpecifier
    PROTECTED: AccessSpecifier
    PRIVATE: AccessSpecifier
    NONE: AccessSpecifier

class TypeKind(BaseEnumeration):
    INVALID: TypeKind
    UNEXPOSED: TypeKind
    VOID: TypeKind
    BOOL: TypeKind
    CHAR_U: TypeKind
    UCHAR: TypeKind
    CHAR16: TypeKind
    CHAR32: TypeKind
    USHORT: TypeKind
    UINT: TypeKind
    ULONG: TypeKind
    ULONGLONG: TypeKind
    UINT128: TypeKind
    CHAR_S: TypeKind
    SCHAR: TypeKind
    WCHAR: TypeKind
    SHORT: TypeKind
    INT: TypeKind
    LONG: TypeKind
    LONGLONG: TypeKind
    INT128: TypeKind
    FLOAT: TypeKind
    DOUBLE: TypeKind
    LONGDOUBLE: TypeKind
    NULLPTR: TypeKind
    OVERLOAD: TypeKind
    DEPENDENT: TypeKind
    OBJCID: TypeKind
    OBJCCLASS: TypeKind
    OBJCSEL: TypeKind
    FLOAT128: TypeKind
    HALF: TypeKind
    IBM128: TypeKind
    COMPLEX: TypeKind
    POINTER: TypeKind
    BLOCKPOINTER: TypeKind
    LVALUEREFERENCE: TypeKind
    RVALUEREFERENCE: TypeKind
    RECORD: TypeKind
    ENUM: TypeKind
    TYPEDEF: TypeKind
    OBJCINTERFACE: TypeKind
    OBJCOBJECTPOINTER: TypeKind
    FUNCTIONNOPROTO: TypeKind
    FUNCTIONPROTO: TypeKind
    CONSTANTARRAY: TypeKind
    VECTOR: TypeKind
    INCOMPLETEARRAY: TypeKind
    VARIABLEARRAY: TypeKind
    DEPENDENTSIZEDARRAY: TypeKind
    MEMBERPOINTER: TypeKind
    AUTO: TypeKind
    ELABORATED: TypeKind
    PIPE: TypeKind
    OCLIMAGE1DRO: TypeKind
    OCLIMAGE1DARRAYRO: TypeKind
    OCLIMAGE1DBUFFERRO: TypeKind
    OCLIMAGE2DRO: TypeKind
    OCLIMAGE2DARRAYRO: TypeKind
    OCLIMAGE2DDEPTHRO: TypeKind
    OCLIMAGE2DARRAYDEPTHRO: TypeKind
    OCLIMAGE2DMSAARO: TypeKind
    OCLIMAGE2DARRAYMSAARO: TypeKind
    OCLIMAGE2DMSAADEPTHRO: TypeKind
    OCLIMAGE2DARRAYMSAADEPTHRO: TypeKind
    OCLIMAGE3DRO: TypeKind
    OCLIMAGE1DWO: TypeKind
    OCLIMAGE1DARRAYWO: TypeKind
    OCLIMAGE1DBUFFERWO: TypeKind
    OCLIMAGE2DWO: TypeKind
    OCLIMAGE2DARRAYWO: TypeKind
    OCLIMAGE2DDEPTHWO: TypeKind
    OCLIMAGE2DARRAYDEPTHWO: TypeKind
    OCLIMAGE2DMSAAWO: TypeKind
    OCLIMAGE2DARRAYMSAAWO: TypeKind
    OCLIMAGE2DMSAADEPTHWO: TypeKind
    OCLIMAGE2DARRAYMSAADEPTHWO: TypeKind
    OCLIMAGE3DWO: TypeKind
    OCLIMAGE1DRW: TypeKind
    OCLIMAGE1DARRAYRW: TypeKind
    OCLIMAGE1DBUFFERRW: TypeKind
    OCLIMAGE2DRW: TypeKind
    OCLIMAGE2DARRAYRW: TypeKind
    OCLIMAGE2DDEPTHRW: TypeKind
    OCLIMAGE2DARRAYDEPTHRW: TypeKind
    OCLIMAGE2DMSAARW: TypeKind
    OCLIMAGE2DARRAYMSAARW: TypeKind
    OCLIMAGE2DMSAADEPTHRW: TypeKind
    OCLIMAGE2DARRAYMSAADEPTHRW: TypeKind
    OCLIMAGE3DRW: TypeKind
    OCLSAMPLER: TypeKind
    OCLEVENT: TypeKind
    OCLQUEUE: TypeKind
    OCLRESERVEID: TypeKind
    EXTVECTOR: TypeKind
    ATOMIC: TypeKind

    @property
    def spelling(self) -> str:...

class RefQualifierKind:
    NONE: RefQualifierKind
    LVALUE: RefQualifierKind
    RVALUE: RefQualifierKind

class LinkageKind:
    INVALID: LinkageKind
    NO_LINKAGE: LinkageKind
    INTERNAL: LinkageKind
    UNIQUE_EXTERNAL: LinkageKind
    EXTERNAL: LinkageKind

class TLSKind:
    NONE: TLSKind
    DYNAMIC: TLSKind
    STATIC: TLSKind

class Type:
    @property
    def kind(self) -> TypeKind:...

    def argument_types(self) -> typing.Iterable[Type]:...

    @property
    def element_type(self) -> Type:...

    @property
    def element_count(self) -> int:...

    @property
    def translation_unit(self) -> TranslationUnit:...

    def get_num_template_arguments(self) -> int:...

    def get_template_argument_type(self, num) -> Type:...

    def get_canonical(self) -> Type:...

    def is_const_qualified(self) -> bool:...

    def is_volatile_qualified(self) -> bool:...

    def is_restrict_qualified(self) -> bool:...

    def is_function_variadic(self) -> bool:...

    def get_address_space(self) -> int:...

    def get_typedef_name(self) -> str:...

    def is_pod(self) -> bool:...

    def get_pointee(self) -> Type:...

    def get_declaration(self) -> Cursor:...

    def get_result(self) -> Type:...

    def get_array_element_type(self) -> Type:...

    def get_array_size(self) -> int:...

    def get_class_type(self) -> Type:...

    def get_named_type(self) -> Type:...

    def get_align(self) -> int:...

    def get_size(self) -> int:...

    def get_offset(self, fieldname) -> int:...

    def get_ref_qualifier(self) -> RefQualifierKind:...

    def get_fields(self) -> typing.Iterable[Cursor]:...

    def get_exception_specification_kind(self) -> ExceptionSpecificationKind:...

    @property
    def spelling(self) -> str:...

    def __eq__(self, other) -> bool:...

    def __ne__(self, other) -> bool:...

class ClangObject:
    def from_param(self):...

class CompletionChunk:
    class Kind:
        def __init__(self, name):
            self.name:...

    def __init__(self, completionString, key):...

    @CachedProperty
    def spelling(self):...

    @CachedProperty
    def kind(self):...

    @CachedProperty
    def string(self):...

    def isKindOptional(self) -> bool:...

    def isKindTypedText(self) -> bool:...

    def isKindPlaceHolder(self) -> bool:...

    def isKindInformative(self) -> bool:...

    def isKindResultType(self) -> bool:...

class CompletionString(ClangObject):
    class Availability:
        def __init__(self, name):
            self.name = name

    def __len__(self):...

    @CachedProperty
    def num_chunks(self):...

    def __getitem__(self, key):...

    @property
    def priority(self):...

    @property
    def availability(self):...

    @property
    def briefComment(self):...

class CodeCompletionResult(ClangObject):
    @property
    def kind(self) -> CursorKind:...

    @property
    def string(self) -> str:...

class CodeCompletionResults(ClangObject):
    def __init__(self, ptr):...

    @property
    def results(self):...

    @property
    def diagnostics(self):...

class Index:
    @staticmethod
    def create(excludeDecls=False) -> Index:...

    def read(self, path):...

    def parse(self, path, args=None, unsaved_files=None, options=0) -> TranslationUnit:...

class TranslationUnit:
    PARSE_NONE = 0
    PARSE_DETAILED_PROCESSING_RECORD = 1
    PARSE_INCOMPLETE = 2
    PARSE_PRECOMPILED_PREAMBLE = 4
    PARSE_CACHE_COMPLETION_RESULTS = 8
    PARSE_SKIP_FUNCTION_BODIES = 64
    PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION = 128

    @classmethod
    def from_source(
        cls, filename, args=None, unsaved_files=None, options=0, index=None
    ) -> TranslationUnit:...

    @classmethod
    def from_ast_file(cls, filename, index=None)-> TranslationUnit:...

    @property
    def cursor(self) -> Cursor:...

    @property
    def spelling(self) -> str:...

    def get_includes(self) -> typing.Iterable[FileInclusion]:...

    def get_file(self, filename) -> File:...

    def get_location(self, filename, position) -> SourceLocation:...

    def get_extent(self, filename, locations) -> SourceRange:...

    @property
    def diagnostics(self) -> typing.Iterable[Diagnostic]:...

    def reparse(self, unsaved_files=None, options=0):...

    def save(self, filename):...

    def codeComplete(
        self,
        path,
        line,
        column,
        unsaved_files=None,
        include_macros=False,
        include_code_patterns=False,
        include_brief_comments=False,
    ) -> CodeCompletionResults:...

    def get_tokens(self, locations=None, extent=None) -> typing.Iterable[Token]:...

class File(ClangObject):
    @staticmethod
    def from_name(translation_unit, file_name) -> File:...

    @property
    def name(self) -> str:...

    @property
    def time(self):...

    @staticmethod
    def from_result(res, fn, args) -> File:...

class FileInclusion:
    def __init__(self, src, tgt, loc, depth):...

    @property
    def is_input_file(self) -> bool:...

class CompilationDatabaseError(Exception):
    ERROR_UNKNOWN = 0
    ERROR_CANNOTLOADDATABASE = 1
    def __init__(self, enumeration, message):...

class CompileCommand:
    def __init__(self, cmd, ccmds):...

    @property
    def directory(self) -> str:...

    @property
    def filename(self) -> str:...

    @property
    def arguments(self) -> typing.Iterable[str]:...

class CompileCommands:
    def __init__(self, ccmds):...

    def __len__(self) -> int:...

    def __getitem__(self, i) -> CompileCommand:...

    @staticmethod
    def from_result(res, fn, args) -> CompileCommands:...

class CompilationDatabase(ClangObject):
    def __del__(self):...

    @staticmethod
    def from_result(res, fn, args) -> CompilationDatabase:...

    @staticmethod
    def fromDirectory(buildDir) -> CompilationDatabase:...

    def getCompileCommands(self, filename) -> typing.Iterable[CompileCommands]:...

    def getAllCompileCommands(self) -> typing.Iterable[CompileCommands]:...

class Token(Structure):
    @property
    def spelling(self) -> str:...

    @property
    def location(self) -> TokenKind:...

    @property
    def extent(self) -> SourceRange:...

    @property
    def cursor(self) -> Cursor:...

class LibclangError(Exception):
    def __init__(self, message):...