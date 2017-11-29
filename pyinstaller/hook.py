
import pkg_resources
eps = ['help = repo.subcmds.help:Help', 'overview = repo.subcmds.overview:Overview', 'sync = repo.subcmds.sync:Sync', 'gitc-delete = repo.subcmds.gitc_delete:GitcDelete', 'download = repo.subcmds.download:Download', 'diff = repo.subcmds.diff:Diff', 'diffmanifests = repo.subcmds.diffmanifests:Diffmanifests', 'start = repo.subcmds.start:Start', 'init = repo.subcmds.init:Init', 'version = repo.subcmds.version:Version', 'checkout = repo.subcmds.checkout:Checkout', 'status = repo.subcmds.status:Status', 'forall = repo.subcmds.forall:Forall', 'smartsync = repo.subcmds.smartsync:Smartsync', 'cherry-pick = repo.subcmds.cherry_pick:CherryPick', 'grep = repo.subcmds.grep:Grep', 'stage = repo.subcmds.stage:Stage', 'info = repo.subcmds.info:Info', 'gitc-init = repo.subcmds.gitc_init:GitcInit', 'branches = repo.subcmds.branches:Branches', 'prune = repo.subcmds.prune:Prune', 'rebase = repo.subcmds.rebase:Rebase', 'list = repo.subcmds.list:List', 'upload = repo.subcmds.upload:Upload', 'manifest = repo.subcmds.manifest:Manifest', 'abandon = repo.subcmds.abandon:Abandon']
def iter_entry_points(group, name=None):
  for ep in eps:
    yield pkg_resources.EntryPoint.parse(ep)
pkg_resources.iter_entry_points = iter_entry_points
print("hooked!")
