#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""setup.py
    setuptoolsを使う.コードの通り.
    開発時はPipenvを採用(Syllabus-parserに合わせた). 本番環境でPipenvを管理する手間等を考慮してSetup.pyも用意した.
"""
from codecs import open
from setuptools import setup, find_packages

# requires.
requires = ["Cerberus==1.3.4", "fastapi", "sqlalchemy", "uvicorn", "firebase-admin", "databases[sqlite]"]

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name="portfolio_api",
    version="1.0.0",
    description="portfolio api server",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="kkiyama117",
    author_email="k.kiyama117@gmail.com",
    maintainer="kkiyama117",
    maintainer_email="kkiyama117",
    url="https://github.com/kkiyama117/portfolio_api/",
    packages=find_packages(),
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"portfolio_api": "portfolio_api"},
    include_package_data=True,
    python_requires=">=3.7",
    setup_requires=["setuptools >= 30.3"],
    install_requires=requires,
    license="MIT",
    zip_safe=False,
    classifiers=[
        # "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: Japanese",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    # entry_points={"console_scripts": ["parse = event_parser.main:main"]},
)
