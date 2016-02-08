import re
from setuptools import setup, find_packages


with open('dronedemo/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name="dronedemo",
    version=version,
    author="Greg Taylor",
    author_email="gtaylor@gc-taylor.com",
    description="Drone + Python demo package.",
    long_description=open('README.rst').read(),
    license="Apache 2.0 License",
    keywords="drone ci examplei",
    url='https://github.com/drone-demos/drone-with-python',
    install_requires=['flask'],
    entry_points={
        'console_scripts': [
            'dronedemo = dronedemo.scripts.dronedemo:cli_entry',
        ]
    },
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['tests']),
    package_data={'': ['LICENSE', '*.txt', '*.rst']},
    tests_require=['nose'],
    test_suite='nose.collector',
)
