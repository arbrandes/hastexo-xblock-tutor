import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="tutor-hastexo-xblock",
    use_scm_version=True,
    url="https://github.com/hastexo/tutor-hastexo-xblock",
    license="AGPL-3.0",
    author='hastexo',
    author_email='pypi@hastexo.com',
    description="A Tutor plugin for the hastexo XBlock",
    long_description=readme,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=[
        "setuptools-scm",
        "tutor-openedx",
    ],
    entry_points={
        "tutor.plugin.v0": [
            "hastexo = tutorhastexo.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: Education",
    ],
    setup_requires=["setuptools-scm"],
)
