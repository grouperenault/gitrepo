# -*- mode: python -*-

block_cipher = None

from pkg_resources import iter_entry_points
import textwrap
all_commands = []
hiddenimports = []
for ep in iter_entry_points("repo.subcmds"):
  all_commands.append("{} = {}:{}".format(ep.name, ep.module_name, ep.attrs[0]))
  hiddenimports.append(ep.module_name)

with open("hook.py", "w") as f:
  f.write(textwrap.dedent("""
  import pkg_resources
  eps = {}
  def iter_entry_points(group, name=None):
    for ep in eps:
      yield pkg_resources.EntryPoint.parse(ep)
  pkg_resources.iter_entry_points = iter_entry_points
  print("hooked!")
  """.format(all_commands)))

a = Analysis(['repo_entry.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=["hook.py"],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='repo',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
