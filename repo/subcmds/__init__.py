# -*- coding:utf-8 -*-
#
# Copyright (C) 2008 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import pkg_resources
import pkgutil
import sys


def iter_namespace(namespace):
  """Pyinstaller-compatible namespace iteration.

  Yields the name of all modules found at a given full-qualified module name.
  Use 'importlib.import_module' to import the found submodules.

  Usage:

  .. code-block:: python

      import importlib

      for found_submod in iter_namespace("module.submodule_to_iter"):
          m = importlib.import_module(found_submod)

  To have it running with pyinstaller, it still requires to ensure the wanted library
  is well packaged in your executable, and since there is no proper 'import' statements
  in your code pyinstaller might not find them. You might want to add a hook inject the
  "hidden" modules from your plugins folder inside the executable:

  - if your plugins are under the ``myappname/pluginfolder`` module
  - create a file ``specs/hook-<myappname.pluginfolder>.py``
  - content of this file should be:

      .. code-block:: python

          from PyInstaller.utils.hooks import collect_submodules
          hiddenimports = collect_submodules('<myappname.pluginfolder>')
  """
  ns_pkg = sys.modules[namespace]

  prefix = ns_pkg.__name__ + "."
  for p in pkgutil.iter_modules(ns_pkg.__path__, prefix):
    yield p[1]


  # special handling when the package is bundled with PyInstaller 3.5
  # See https://github.com/pyinstaller/pyinstaller/issues/1905#issuecomment-445787510
  toc = set()
  for importer in pkgutil.iter_importers(ns_pkg.__name__.partition(".")[0]):
    name = getattr(importer, "toc", None)
    if name:
      toc |= name
  for name in toc:
    if not name.startswith(prefix):
      continue
    rem_name = name[len(prefix) :]
    if "." in rem_name:
      continue
    yield name


all_commands = {}
eps = list(pkg_resources.iter_entry_points("repo.subcmds"))
if eps:
  for ep in eps:
    cmd = ep.resolve()
    cmdname = ep.name
    cmd.NAME = cmdname
    all_commands[cmdname] = cmd
else:
  for modname in iter_namespace(__name__):
    name = modname.rpartition('.')[2]
    clsn = name.capitalize()
    while clsn.find('_') > 0:
      h = clsn.index('_')
      clsn = clsn[0:h] + clsn[h + 1:].capitalize()

    import importlib
    mod = importlib.import_module(modname)
    try:
      cmd = getattr(mod, clsn)
    except AttributeError:
      raise SyntaxError('%s/%s does not define class %s' % (
        __name__, py, clsn))

    name = name.replace('_', '-')
    cmd.NAME = name
    all_commands[name] = cmd

if 'help' in all_commands:
  all_commands['help'].commands = all_commands
