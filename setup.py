#!/usr/bin/env python3
# Copyright 2019 The Android Open Source Project
#
# Copyright (C) 2020 The Android Open Source Project
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

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name="gitrepo",
  version="2.15.4",
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
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="Apache",
  keywords="git repo android workflow",
  url="https://gerrit.googlesource.com/git-repo/",
  project_urls={
      'Bug Tracker': 'https://bugs.chromium.org/p/gerrit/issues/list?q=component:repo',
  },
  # https://pypi.org/classifiers/
  classifiers=[
      'Development Status :: 6 - Mature',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache Software License',
      'Natural Language :: English',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows :: Windows 10',
      'Operating System :: POSIX :: Linux',
      'Topic :: Software Development :: Version Control :: Git',
  ],
  # We support Python 3.6+.
  python_requires=', '.join('!=3.%i.*' % x for x in range(0, 6)),
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
