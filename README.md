# gitrepo, pypi version

This **not** the official git-repo. Official version is hosted on google's Gerrit (see later part of this readme)

This version is used by RenaultGroup as an effort to better integrate repo into its python based Continuous Integration library.

This version is a friendly fork (https://github.com/grouperenault/gitrepo), with support for normal setup.py style installation.
We intend to follow upstream about twice a year.


- local imports replaced by module imports, "repo" being the name of the python module
- subcommand discovery uses the python entrypoint system
- support for custom repo subcommand in an separate python package

It would be difficult to support a version that supports all of that *and* the "standard" repo installation mode, this is why we didn't work on upstreaming it yet.
We intend to find some time to upstream the import part as the patch is quite intrusive and make the merge from uptream quite painful.


This version is used in a large installation and backup by automated internal tests that we cannot really share yet (as dependent on our infra)

## Generate wheel

python setup.py bdist_wheel

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


# repo

Repo is a tool built on top of Git.  Repo helps manage many Git repositories,
does the uploads to revision control systems, and automates parts of the
development workflow.  Repo is not meant to replace Git, only to make it
easier to work with Git.  The repo command is an executable Python script
that you can put anywhere in your path.

* Homepage: <https://gerrit.googlesource.com/git-repo/>
* Mailing list: [repo-discuss on Google Groups][repo-discuss]
* Bug reports: <https://bugs.chromium.org/p/gerrit/issues/list?q=component:repo>
* Source: <https://gerrit.googlesource.com/git-repo/>
* Overview: <https://source.android.com/source/developing.html>
* Docs: <https://source.android.com/source/using-repo.html>
* [repo Manifest Format](./docs/manifest-format.md)
* [repo Hooks](./docs/repo-hooks.md)
* [Submitting patches](./SUBMITTING_PATCHES.md)
* Running Repo in [Microsoft Windows](./docs/windows.md)
* GitHub mirror: <https://github.com/GerritCodeReview/git-repo>
* Postsubmit tests: <https://github.com/GerritCodeReview/git-repo/actions>

## Contact

Please use the [repo-discuss] mailing list or [issue tracker] for questions.

You can [file a new bug report][new-bug] under the "repo" component.

Please do not e-mail individual developers for support.
They do not have the bandwidth for it, and often times questions have already
been asked on [repo-discuss] or bugs posted to the [issue tracker].
So please search those sites first.

## Install

Many distros include repo, so you might be able to install from there.
```sh
# Debian/Ubuntu.
$ sudo apt-get install repo

# Gentoo.
$ sudo emerge dev-vcs/repo
```

You can install it manually as well as it's a single script.
```sh
$ mkdir -p ~/.bin
$ PATH="${HOME}/.bin:${PATH}"
$ curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
$ chmod a+rx ~/.bin/repo
```

[new-bug]: https://bugs.chromium.org/p/gerrit/issues/entry?template=Repo+tool+issue
[issue tracker]: https://bugs.chromium.org/p/gerrit/issues/list?q=component:repo
[repo-discuss]: https://groups.google.com/forum/#!forum/repo-discuss
