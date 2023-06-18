######################################################
# Author: Andrea Fioraldi <andreafioraldi@gmail.com> #
# License: BSD 2-Clause                              #
######################################################

import sys
import os

# sys.sys.executable

# sys.executable
sys.path.append("/Users/puck/.idapro/plugins/idangr")
sys.path.append(os.path.join(os.path.dirname(sys.executable),"python/3"))


from manage import AngrDbgNotInstalled, remote, init, serve_all, close, has_modules, is_initialized
from hook_lib_funcs import hook_lib_funcs