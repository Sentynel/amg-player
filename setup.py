#!/usr/bin/env python3

import os
import re
import sys

from setuptools import find_packages, setup


if sys.hexversion < 0x3040000:
  print("Python version %s is unsupported, >= 3.4.0 is needed" % (".".join(map(str, sys.version_info[:3]))))
  exit(1)

with open(os.path.join("amg", "__init__.py"), "rt") as f:
  version = re.search("__version__ = \"([^\"]+)\"", f.read()).group(1)

with open("requirements.txt", "rt") as f:
  requirements = f.read().splitlines()

try:
  import pypandoc
  readme = pypandoc.convert("README.md", "rst")
except ImportError:
  with open("README.md", "rt") as f:
    readme = f.read()

setup(name="amg-player",
      version=version,
      author="desbma",
      packages=find_packages(exclude=("tests",)),
      entry_points={"console_scripts": ["amg = amg:cl_main"]},
      test_suite="tests",
      install_requires=requirements,
      description="Browse & play embedded tracks from Angry Metal Guy music reviews",
      long_description=readme,
      url="https://github.com/desbma/amg-player",
      download_url="https://github.com/desbma/amg-player/archive/%s.tar.gz" % (version),
      keywords=["music", "metal", "extreme", "angry", "guy", "player", "youtube", "bandcamp", "soundcloud"],
      classifiers=["Development Status :: 4 - Beta",
                   "Environment :: Console",
                   "Intended Audience :: End Users/Desktop",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3 :: Only",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Topic :: Multimedia :: Sound/Audio :: Players",
                   "Topic :: Utilities"])
