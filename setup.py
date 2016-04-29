"""
python-lorawan
---------------

LoRaWan for python
"""
from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='python-lorawan',
    version='0.9.0',
    url='https://github.com/qitianchan/lorawan-for-python.git',
    license='MIT',
    author='qitianchan',
    author_email='qitianchan@gmail.com',
    description='LoRaWan1.1 implement',
    long_description=long_description,
    packages=['lorawan'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'six>=1.9.0',
        'pyaes>=1.3.0'
    ],
    tests_require=[
        'mock',
        'eventlet',
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
