#!/usr/bin/env python3
"""Setup script for PB2S Agentic Framework."""

from setuptools import setup, find_packages
import os

# Read README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="agentic-pb2s",
    version="1.0.0",
    author="PB2S Framework Team",
    author_email="",
    description="PB2S Ethos Framework for emergent-safe recursive AI systems",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/SHYAMALSOLANKI/PB2S-PB2A-watever-agentic_framework",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    include_package_data=True,
    package_data={
        "extensions.schemas": ["*.json"],
    },
    entry_points={
        "console_scripts": [
            "pb2s-framework=core.pb2s_framework:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/SHYAMALSOLANKI/PB2S-PB2A-watever-agentic_framework/issues",
        "Source": "https://github.com/SHYAMALSOLANKI/PB2S-PB2A-watever-agentic_framework",
    },
)