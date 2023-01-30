# Standard Library
import errno
import os
import sys

REPODIR = '.repo'                # name of repo's private directory

def _FindRepo():
  """Look for a repo installation, starting at the current directory.
  """
  curdir = os.getcwd()
  repo = None

  olddir = None
  while curdir != '/' \
          and curdir != olddir \
          and not repo:
    repo = os.path.join(curdir, REPODIR)
    if not os.path.isdir(repo):
      repo = None
      olddir = curdir
      curdir = os.path.dirname(curdir)
  return repo

def _MkRepoDir(repodir):
  try:
    os.mkdir(repodir)
  except OSError as e:
    if e.errno != errno.EEXIST:
      print('fatal: cannot make %s directory: %s'
             % (repodir, e.strerror), file=sys.stderr)
      # Don't raise CloneFailure; that would delete the
      # name. Instead exit immediately.
      #
      sys.exit(1)

def getRepoDir():
  repodir = _FindRepo()
  if repodir is None:
    repodir = os.path.join(os.getcwd(), REPODIR)
    _MkRepoDir(repodir)
  return repodir
