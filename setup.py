from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'VERSION')) as f:
    VERSION = f.read().strip('\n')  # editors love to add newline

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bids0',
    version=VERSION,
    description='Transparent Object-Oriented Approach to BIDS in Python',
    long_description=long_description,
    url='https://github.com/gpiantoni/bidso',
    author="Gio Piantoni",
    author_email='bids@gpiantoni.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        ],
    keywords='bids',
    packages=find_packages(exclude=('test', )),
    install_requires=[
        'nibabel',
        ],
    extras_require={
        'test': [  # to run tests
            'pytest',
            'pytest-cov',
            'codecov',
            ],
        },
    )
