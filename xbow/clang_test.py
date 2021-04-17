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

from clang.cindex import CursorKind

def get_diag_info(diag):
    return { 'severity' : diag.severity,
             'location' : diag.location,
             'spelling' : diag.spelling,
             'ranges' : diag.ranges,
             'fixits' : diag.fixits }

def get_cursor_id(cursor, cursor_list = []):
    if not opts.showIDs:
        return None

    if cursor is None:
        return None

    # FIXME: This is really slow. It would be nice if the index API exposed
    # something that let us hash cursors.
    for i,c in enumerate(cursor_list):
        if cursor == c:
            return i
    cursor_list.append(cursor)
    return len(cursor_list) - 1

def get_defns(node):
    defns = []
    for child in node.get_children():
        usr = child.get_usr().replace('@N@', '::').replace('@', '::').replace('c:::', '')
        var_decl = child.is_definition and child.kind == CursorKind.VAR_DECL and 'ranges::' in usr and '.hpp' not in usr and 'detail' not in usr and '::_' not in usr
        struct_decl = child.is_definition and child.kind == CursorKind.STRUCT_DECL and usr.endswith('_fn')
        if var_decl or struct_decl:
            defns.append({'id': get_cursor_id(child),
                    'kind': child.kind,
                    'usr': usr,
                    'spelling': child.spelling,
                    'location': child.location,
                    'extent.start': child.extent.start,
                    'extent.end': child.extent.end,
                    'is_definition': child.is_definition(),
                    'definition id': get_cursor_id(child.get_definition())})
        defns.extend(get_defns(child))
    return defns



def get_info(node, depth=0):
    if opts.maxDepth is not None and depth >= opts.maxDepth:
        children = None
    else:
        children = [
            get_info(c, depth+1)
            for c in node.get_children()
            if c.is_definition
        ]
    return { 'id' : get_cursor_id(node),
             'kind' : node.kind,
             'usr' : node.get_usr(),
             'spelling' : node.spelling,
             'location' : node.location,
             'extent.start' : node.extent.start,
             'extent.end' : node.extent.end,
             'is_definition' : node.is_definition(),
             'definition id' : get_cursor_id(node.get_definition()),
             'children' : children }

EXTRA_ARGS = '-DARROW_STATIC -DBOOST_HANA_CONFIG_ENABLE_STRING_UDL -DBOOST_STACKTRACE_LINK -DCURL_STATICLIB=1 -DJSON_USE_IMPLICIT_CONVERSIONS=1 -DSPDLOG_FMT_EXTERNAL -DUSE_OS_TZDB=0 -DUTF8PROC_STATIC -DXTENSOR_USE_XSIMD -I../../include -I/home/mpercossi/.pyenv/versions/3.9.1/include/python3.9 -isystem /home/mpercossi/.conan/data/aws-c-common/0.4.25/_/_/package/d988447fa516eac7400b2f34e2d4b89e42b4b1a8/include -isystem /home/mpercossi/.conan/data/abseil/20200923.3/_/_/package/5123c6a281213ff9b37e6cf441b7be9ce4182462/include -isystem /home/mpercossi/.conan/data/lz4/1.9.3/_/_/package/d988447fa516eac7400b2f34e2d4b89e42b4b1a8/include -isystem /home/mpercossi/.conan/data/utf8proc/2.6.0/_/_/package/d988447fa516eac7400b2f34e2d4b89e42b4b1a8/include -isystem /home/mpercossi/.conan/data/arrow/2.0.0/_/_/package/c12eb445ac65a0df9b10649277bc9c007efcd276/include -isystem /home/mpercossi/.conan/data/thrift/0.13.0/_/_/package/6ad12b4a708a0335c40bd17fa9e2b4b0c819f702/include -isystem /home/mpercossi/.conan/data/boost/1.75.0/_/_/package/2f252965901826f5cefe03c2afebf278958cd469/include -isystem /home/mpercossi/.conan/data/zlib/1.2.11/_/_/package/d988447fa516eac7400b2f34e2d4b89e42b4b1a8/include -isystem /home/mpercossi/.conan/data/bzip2/1.0.8/_/_/package/a0279858937b0968952a9784938616e26eb7c2dd/include -isystem /home/mpercossi/.conan/data/libiconv/1.16/_/_/package/d988447fa516eac7400b2f34e2d4b89e42b4b1a8/include -isystem /home/mpercossi/.conan/data/openssl/1.1.1i/_/_/package/d988447fa516eac7400b2f34e2d4b89e42b4b1a8/include -isystem /home/mpercossi/.conan/data/libevent/2.1.11/_/_/package/caebb417dda8140b464c0f92ac45b273085a8803/include -isystem /home/mpercossi/.conan/data/protobuf/3.13.0/_/_/package/5123c6a281213ff9b37e6cf441b7be9ce4182462/include -isystem /home/mpercossi/.conan/data/snappy/1.1.8/_/_/package/5123c6a281213ff9b37e6cf441b7be9ce4182462/include -isystem /home/mpercossi/.conan/data/magic_enum/0.7.2/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/range-v3/0.11.0/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/catch2/2.13.4/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/date/3.0.0/_/_/package/bf35398a1747e5b5231a06df1d0903eedc01a425/include -isystem /home/mpercossi/.conan/data/libcurl/7.69.1/_/_/package/66e521f5bd3f967fc897a2a060eceb272067f4c0/include -isystem /home/mpercossi/.conan/data/xtensor/0.21.5/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/xtl/0.6.21/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/nlohmann_json/3.9.1/_/_/package/d1091b2ed420e6d287293709a907ae824d5de508/include -isystem /home/mpercossi/.conan/data/xsimd/7.4.9/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/spdlog/1.8.2/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/fmt/7.1.3/_/_/package/5123c6a281213ff9b37e6cf441b7be9ce4182462/include -isystem /home/mpercossi/.conan/data/rapidjson/cci.20200410/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/pybind11/2.6.1/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include -isystem /home/mpercossi/.conan/data/pybind11/2.6.1/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include/pybind11  -m64 -stdlib=libc++ -O3 -DNDEBUG -Wno-logical-op-parentheses -Wno-ambiguous-reversed-operator -Wunused-command-line-argument -Wl,--export-dynamic -Wno-unused-result -std=gnu++20'

def main():
    from clang.cindex import Index, Config
    from pprint import pprint

    from optparse import OptionParser, OptionGroup

    global opts

    parser = OptionParser("usage: %prog [options] {filename} [clang-args*]")
    parser.add_option("", "--show-ids", dest="showIDs",
                      help="Compute cursor IDs (very slow)",
                      action="store_true", default=False)
    parser.add_option("", "--max-depth", dest="maxDepth",
                      help="Limit cursor expansion to depth N",
                      metavar="N", type=int, default=None)
    parser.disable_interspersed_args()

    from pathlib import Path as path

    file = path('../src/simple.cpp')
    #file = path('/home/mpercossi/.conan/data/range-v3/0.11.0/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/include/range/v3/view/single.hpp')

    all_args = ['--show-ids', str(file.absolute()), '-stdlib=libc++', '-std=c++20', '-L/usr/lib/llvm-11/lib', '-I/usr/lib/llvm-11/include', '-std=c++20'] + EXTRA_ARGS.split(' ')
    print(f"{' '.join(all_args)}")
    (opts, args) = parser.parse_args(['--show-ids', str(file.absolute()), '-stdlib=libc++', '-std=c++20', '-L/usr/lib/llvm-11/lib', '-I/usr/lib/llvm-11/include', '-std=c++20'] + EXTRA_ARGS.split(' '))

    if len(args) == 0:
        parser.error('invalid number arguments')

    Config.set_library_file('/usr/lib/llvm-11/lib/libclang-11.so')
    index = Index.create()
    tu = index.parse(None, args)
    if not tu:
        parser.error("unable to load input")

    #pprint(('diags', [get_diag_info(d) for d in  tu.diagnostics]))
    pprint(('nodes', get_defns(tu.cursor)))

if __name__ == '__main__':
    main()

#print("\n".join(c.name for c in CursorKind.get_all_kinds()))