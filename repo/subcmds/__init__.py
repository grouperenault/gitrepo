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

import os
import pkg_resources

all_commands = {}
for ep in pkg_resources.iter_entry_points("repo.subcmds"):
  cmd = ep.load(require=False)()
  cmdname = ep.name
  cmd.NAME = cmdname
  all_commands[cmdname] = cmd

if 'help' in all_commands:
  all_commands['help'].commands = all_commands
