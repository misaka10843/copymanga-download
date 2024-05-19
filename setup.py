# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
try:
    long_description = open("README.md").read()
except IOError:
    long_description = "使用Python编译exe/bash来下载copymanga 拷贝漫画中的漫画，支持批量+选话下载和获取您收藏的漫画并下载！"
 
setup(
    name="copymanga-dl",
    version="3.5.1",
    description="Copymanga Downloader",
    long_description=long_description,
    license="GNU GENERAL PUBLIC LICENSE",
    author="misaka10843",
    author_email="misaka10843@outlook.jp",
    url="https://github.com/misaka10843/copymanga-downloader",
    py_modules=[
        "cbz",
        "config",
        "epub",
        "function",
        "login",
        "main",
        "settings",
    ],
    packages=find_packages(),
    package_data={'': ['*.json', '*.md']},
    python_requires='>=3.8',
    install_requires=[
        'requests',
        'rich',
    ],
    entry_points={'console_scripts': ['copymanga-dl=main:main']},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
    ]
)
