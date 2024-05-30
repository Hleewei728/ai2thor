from setuptools import setup, find_packages
import os

__version__ = "0.0.1"

if os.path.isfile("ai2thor/_version.py"):
    exec(open("ai2thor/_version.py").read())

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

VERSION = __version__

def _read_reqs(relpath):
        fullpath = os.path.join(os.path.dirname(__file__), relpath)
        with open(fullpath) as f:
            return [
                s.strip()
                for s in f.readlines()
                if (s.strip() and not s.startswith("#"))
            ]

REQUIREMENTS = _read_reqs("requirements.txt")
REQUIREMENTS_TEST = _read_reqs("requirements-test.txt")

setup(
    name="ai2thor",
    version=VERSION,
    description="AI2-THOR: A Near Photo-Realistic Interactable Framework for Embodied AI Agents",
    long_description=long_description,
    license="Apache License 2.0",
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: MacOS",
        "Operating System :: Unix",
    ],
    keywords="AI2-THOR, Allen AI, Python, Reinforcement Learning, Computer Vision, Artificial Intelligence",
    url="https://github.com/allenai/ai2thor",
    author="Allen Institute for AI",
    author_email="ai2thor@allenai.org",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=REQUIREMENTS,
    setup_requires=["pytest-runner"],
    tests_require=REQUIREMENTS_TEST,
    scripts=["scripts/ai2thor-xorg"],
    include_package_data=False,
)

