######################################################
# Author: Andrea Fioraldi <andreafioraldi@gmail.com> #
# License: BSD 2-Clause                              #
######################################################

# from ckx import ckxval

import sys

# sys.path.append("C:\ckx\idapro\plugins\idangr")

sys.path.append("/Applications/IDA Pro 7.5/ida64.app/Contents/MacOS/plugins/idangr/")

from .manage import AngrDbgNotInstalled, remote, init, serve_all, close, has_modules, is_initialized
from .hook_lib_funcs import hook_lib_funcs