from setuptools import setup, find_packages
setup(
  name="git-repo",
  version="0.1",
  packages=find_packages(),

  package_data={
    # If any package contains *.txt or *.rst files, include them:
    '': ['*.txt', '*.rst'],
    # And include any *.msg files found in the 'hello' package, too:
    'hello': ['*.msg'],
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
    ]
  }
)