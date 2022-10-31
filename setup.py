from setuptools import find_packages, setup
import os

'''
In order to pip install this package, please use:
>$: pip install https://Securitized:4h5jit5eutnujfsccr5ehvavooyxtt3oytxp5qpe55qkrl6dhsha@pkgs.dev.azure.com/jhgonline/Securitized/_packaging/Securitized/pypi/download/api-intex/{version}/api_intex-{version}-py3-none-any.whl
'''

version = '0.1'
try:
    version = os.environ['BUILD_BUILDNUMBER']
except KeyError:
    pass

setup(
    name='test',
    python_requires='>=3.7.0, <3.9.0',
    packages=find_packages(),
    version=version,
    description='test libarary',
    author='Ian Draves',
    license='MIT',
    install_requires=['pandas', 'pytz', 'datetime', 'requests'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)
