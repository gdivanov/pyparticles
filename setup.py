from setuptools import setup, find_packages
from os import path
import sys

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Setup Packages for both `pip` and `distutils`/`easy_install`
extras_require = {
    "test": ["pytest-runner>=5.1", "pytest>=5.2", "pytest-cov>=2.8"],
    "dev": [
        "better-setuptools-git-version>=1.0",
        "flake8>=3.7",
        "setuptools>=41",
        "wheel>=0.33",
    ],
}

# Setup requirements
setup_requires = ["better-setuptools-git-version>=1.0"]

# Conditionally load additional requirements into setup_requires
if {"pytest", "test", "ptr"}.intersection(sys.argv):
    setup_requires += extras_require["test"]

setup(
    name="pyparticles",
    version_config={"version_format": "{tag}.dev{sha}", "starting_version": "0.1.0"},
    description="Simple physics simulator for a collection of particles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gdivanov/pyparticles",
    author="Grisha Ivanov",
    author_email="grigoriy.ivanov@yahoo.com",
    license="Other/Proprietary License",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    keywords="particles physics equations motion",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3.6",
    install_requires=["numpy==1.15.4", "pyyaml==5.2"],
    tests_require=extras_require["test"],
    setup_requires=setup_requires,
    extras_require=extras_require,
)
