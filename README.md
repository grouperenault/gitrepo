# repo

Repo is a tool built on top of Git.  Repo helps manage many Git repositories,
does the uploads to revision control systems, and automates parts of the
development workflow.  Repo is not meant to replace Git, only to make it
easier to work with Git.  The repo command is an executable Python script
that you can put anywhere in your path.

* Homepage: https://gerrit.googlesource.com/git-repo/
* Bug reports: https://bugs.chromium.org/p/gerrit/issues/list?q=component:repo
* Source: https://gerrit.googlesource.com/git-repo/
* Overview: https://source.android.com/source/developing.html
* Docs: https://source.android.com/source/using-repo.html
* [repo Manifest Format](./docs/manifest-format.md)
* [repo Hooks](./docs/repo-hooks.md)
* [Submitting patches](./SUBMITTING_PATCHES.md)


# About pypi version

Version in pypi is not the official version from google, but a friendly fork, with support for normal setup.py style installation

- local imports replaced by module imports, "repo" being the name of the python module
- subcommand discovery uses the python entrypoint system
- support for custom repo subcommand in an separate python package

## Installation

```
pip3 install --user gitrepo
```

## Custom commands

- create a python module starting from any example in the repo/subcmds directory

- add an entrypoint to your setup.py module:

```python
  setup(...,
    install_requires=["gitrepo"],
    entry_points={
      'repo.subcmds': [
        'my_custom_cmd = mycustomrepo.my_custom_cmd:CustomCmd',
    }
  )
```
Then you can ask your developers to install your own `mycustomrepo` package instead of the `gitrepo` package.
