# -*- coding: utf-8 -*-
"""
CommandLine:
    # Partially regenerate __init__.py
    mkinit ubelt
"""
# Todo:
#     The following functions and classes are candidates to be ported from utool:
#     * reload_class
#     * inject_func_as_property
#     * accumulate
#     * rsync
#     * ParamInfo - move to dtool
#     * parse_cfgstr3 - not relevant here
from __future__ import absolute_import, division, print_function, unicode_literals

__version__ = '0.5.3'

__submodules__ = [
    'util_arg',
    'util_cache',
    'util_colors',
    'util_const',
    'util_cmd',
    'util_dict',
    'util_download',
    'util_func',
    'util_format',
    'util_io',
    'util_links',
    'util_list',
    'util_hash',
    'util_import',
    'util_memoize',
    'util_mixins',
    'util_path',
    'util_platform',
    'util_str',
    'util_time',
    'orderedset',
    'progiter',
]

__DYNAMIC__ = False
if __DYNAMIC__:  # nocover
    import mkinit
    exec(mkinit.dynamic_init(__name__, __submodules__))
else:  # pragma: nobranch
    # <AUTOGEN_INIT>
    from ubelt import util_arg
    from ubelt import util_cache
    from ubelt import util_colors
    from ubelt import util_const
    from ubelt import util_cmd
    from ubelt import util_dict
    from ubelt import util_download
    from ubelt import util_func
    from ubelt import util_format
    from ubelt import util_io
    from ubelt import util_links
    from ubelt import util_list
    from ubelt import util_hash
    from ubelt import util_import
    from ubelt import util_memoize
    from ubelt import util_mixins
    from ubelt import util_path
    from ubelt import util_platform
    from ubelt import util_str
    from ubelt import util_time
    from ubelt import orderedset
    from ubelt import progiter

    from ubelt.util_arg import (argflag, argval,)
    from ubelt.util_cache import (CacheStamp, Cacher,)
    from ubelt.util_colors import (color_text, highlight_code,)
    from ubelt.util_const import (NoParam,)
    from ubelt.util_cmd import (cmd,)
    from ubelt.util_dict import (AutoDict, AutoOrderedDict, ddict, dict_hist,
                                 dict_subset, dict_take, dict_union, dzip,
                                 find_duplicates, group_items, invert_dict,
                                 map_keys, map_vals, odict,)
    from ubelt.util_download import (download, grabdata,)
    from ubelt.util_func import (identity, inject_method,)
    from ubelt.util_format import (repr2,)
    from ubelt.util_io import (delete, readfrom, touch, writeto,)
    from ubelt.util_links import (symlink,)
    from ubelt.util_list import (allsame, argmax, argmin, argsort, argunique,
                                 boolmask, chunks, compress, flatten, iter_window,
                                 iterable, take, unique, unique_flags,)
    from ubelt.util_hash import (hash_data, hash_file,)
    from ubelt.util_import import (import_module_from_name,
                                   import_module_from_path, modname_to_modpath,
                                   modpath_to_modname, split_modpath,)
    from ubelt.util_memoize import (memoize, memoize_method,)
    from ubelt.util_mixins import (NiceRepr,)
    from ubelt.util_path import (TempDir, augpath, compressuser, ensuredir,
                                 expandpath, truepath, userhome,)
    from ubelt.util_platform import (DARWIN, LINUX, POSIX, WIN32, editfile,
                                     ensure_app_cache_dir, ensure_app_resource_dir,
                                     find_exe, find_path, get_app_cache_dir,
                                     get_app_resource_dir, platform_cache_dir,
                                     platform_resource_dir, startfile,)
    from ubelt.util_str import (CaptureStdout, codeblock, ensure_unicode, hzcat,
                                indent,)
    from ubelt.util_time import (Timer, Timerit, timestamp,)
    from ubelt.orderedset import (OrderedSet, oset,)
    from ubelt.progiter import (ProgIter,)

    __all__ = ['AutoDict', 'AutoOrderedDict', 'CacheStamp', 'Cacher',
               'CaptureStdout', 'DARWIN', 'LINUX', 'NiceRepr', 'NoParam',
               'OrderedSet', 'POSIX', 'ProgIter', 'TempDir', 'Timer', 'Timerit',
               'WIN32', 'allsame', 'argflag', 'argmax', 'argmin', 'argsort',
               'argunique', 'argval', 'augpath', 'boolmask', 'chunks', 'cmd',
               'codeblock', 'color_text', 'compress', 'compressuser', 'ddict',
               'delete', 'dict_hist', 'dict_subset', 'dict_take', 'dict_union',
               'download', 'dzip', 'editfile', 'ensure_app_cache_dir',
               'ensure_app_resource_dir', 'ensure_unicode', 'ensuredir',
               'expandpath', 'find_duplicates', 'find_exe', 'find_path', 'flatten',
               'get_app_cache_dir', 'get_app_resource_dir', 'grabdata',
               'group_items', 'hash_data', 'hash_file', 'highlight_code', 'hzcat',
               'identity', 'import_module_from_name', 'import_module_from_path',
               'indent', 'inject_method', 'invert_dict', 'iter_window', 'iterable',
               'map_keys', 'map_vals', 'memoize', 'memoize_method',
               'modname_to_modpath', 'modpath_to_modname', 'odict', 'orderedset',
               'oset', 'platform_cache_dir', 'platform_resource_dir',
               'progiter', 'readfrom', 'repr2', 'split_modpath', 'startfile',
               'symlink', 'take', 'timestamp', 'touch', 'truepath', 'unique',
               'unique_flags', 'userhome', 'util_arg', 'util_cache', 'util_cmd',
               'util_colors', 'util_const', 'util_dict', 'util_download',
               'util_format', 'util_func', 'util_hash', 'util_import', 'util_io',
               'util_links', 'util_list', 'util_memoize', 'util_mixins',
               'util_path', 'util_platform', 'util_str', 'util_time', 'writeto']
    # </AUTOGEN_INIT>
