#!/usr/bin/env python

#===- cindex-dump.py - cindex/Python Source Dump -------------*- python -*--===#
#
# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
#
#===------------------------------------------------------------------------===#

"""
A simple command line tool for dumping a source file using the Clang Index
Library.
"""

from clang.cindex import CursorKind, SourceRange
from dataclasses import dataclass
from textwrap import dedent, indent

# {'definition id': 1,
#  'extent.end': < SourceLocation
# file
# '/home/mpercossi/.conan/data/range-v3/0.11.0/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include/concepts/swap.hpp', line
# 271, column
# 10 >,
# 'extent.start': < SourceLocation
# file
# '/home/mpercossi/.conan/data/range-v3/0.11.0/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include/concepts/swap.hpp', line
# 188, column
# 9 >,
# 'id': 1,
# 'is_definition': True,
# 'kind': CursorKind.STRUCT_DECL,
# 'location': < SourceLocation
# file
# '/home/mpercossi/.conan/data/range-v3/0.11.0/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include/concepts/swap.hpp', line
# 188, column
# 16 >,
# 'spelling': 'swap_fn',
# 'usr': 'concepts::adl_swap_detail::S::swap_fn'},


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


visitor_py = open('/cxx/visitor.py', 'w')

print("from clang.cindex import CursorKind", file=visitor_py)

print(dedent("""
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
""".strip()), file=visitor_py)
for kind in CursorKind.get_all_kinds():
    klass = "".join(part.title() for part in kind.name.split("_"))
    print(indent(dedent(f"""
        if node.kind == {kind}:
            self.visit_{klass}(node)
    """), ' '*8), file=visitor_py)
print("""
        self.visit_generic(node)
        self.visit_children(node)
        self.post_visit(node)
        
""", file=visitor_py)
for kind in CursorKind.get_all_kinds():
    klass = "".join(part.title() for part in kind.name.split("_"))
    print(f"""
    def visit_{klass}(self: 'Visitor', node) -> None:
        pass
    """, file=visitor_py)
