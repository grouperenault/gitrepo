from setuptools import setup, find_packages
setup(
  name="gitrepo",
  version="0.2.2",
  packages=find_packages(),

  package_data={
    # If any package contains *.txt or *.rst files, include them:
    'repo': ['git_ssh'],
    'repo.hooks': ['commit-msg', 'pre-auto-gc'],
  },

  # metadata for upload to PyPI
  author="git-repo contributors",
  author_email="repo-discuss@googlegroups.com",
  description="Repo helps manage many Git repositories, does the uploads to revision control systems, and automates parts of the development workflow.",
  license="Apache",
  keywords="git repo android workflow",
  url="https://gerrit.googlesource.com/git-repo/",
  entry_points={
    'console_scripts': [
      'repo = repo.main:main',
    ],
    'repo.subcmds': [
      'abandon = repo.subcmds.abandon:Abandon',
      'branches = repo.subcmds.branches:Branches',
      'checkout = repo.subcmds.checkout:Checkout',
      'cherry-pick = repo.subcmds.cherry_pick:CherryPick',
      'diff = repo.subcmds.diff:Diff',
      'diffmanifests = repo.subcmds.diffmanifests:Diffmanifests',
      'download = repo.subcmds.download:Download',
      'forall = repo.subcmds.forall:Forall',
      'gitc-delete = repo.subcmds.gitc_delete:GitcDelete',
      'gitc-init = repo.subcmds.gitc_init:GitcInit',
      'grep = repo.subcmds.grep:Grep',
      'help = repo.subcmds.help:Help',
      'info = repo.subcmds.info:Info',
      'init = repo.subcmds.init:Init',
      'list = repo.subcmds.list:List',
      'manifest = repo.subcmds.manifest:Manifest',
      'overview = repo.subcmds.overview:Overview',
      'prune = repo.subcmds.prune:Prune',
      'rebase = repo.subcmds.rebase:Rebase',
      'smartsync = repo.subcmds.smartsync:Smartsync',
      'stage = repo.subcmds.stage:Stage',
      'start = repo.subcmds.start:Start',
      'status = repo.subcmds.status:Status',
      'sync = repo.subcmds.sync:Sync',
      'upload = repo.subcmds.upload:Upload',
      'version = repo.subcmds.version:Version',
    ]
  }
)
