from setuptools import setup, find_packages
from codecs import open
from os import path
from re import compile

here = path.abspath(path.dirname(__file__))

# Get the long description
long_desc_file = 'README.rst'
with open(path.join(here, long_desc_file), encoding='utf-8') as f:
    long_description = f.read()

# Get version
version_file = '.bumpversion.cfg'
version_re = compile(
    r'current_version = (.+)')
fp = open(path.join(here, version_file))
version = None
for line in fp:
    match = version_re.search(line)
    if match:
        version = match.group(1)
        break
else:
    raise Exception("Cannot find version in " + version_file)
fp.close()


setup(
    name='dsteli',
    version=version,
    description='A domain specific template library',
    long_description=long_description,
    url='https://github.com/manboubird/dsteli',
    author='Toshiaki Toyama',
    author_email='manboubird@gmail.com',
    license='ASL2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='template DSL',
    packages=find_packages(exclude=['docs', 'tests']),
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        # 'sample': ['package_data.dat'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('dsteli_templates', ['templates/rst'])],
    entry_points={
        'console_scripts': [
            'dsteli=dsteli:main',
        ],
    },
)
