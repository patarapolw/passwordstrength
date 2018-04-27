from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='passwordstrength',
    version='0.2.4',
    description='Password strength calculator in Python',
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/patarapolw/passwordstrength',  # Optional
    author='Pacharapol Withayasakpunt',
    author_email='patarapolw@gmail.com',
    license='MIT',
    keywords='password password_strength password_meter',
    packages=['passwordstrength'],
    install_requires=['PyYAML'],
    python_requires='>=3.5',
    package_data={
        'passwordstrength': ['database/*']
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security :: Cryptography'
    ],
    extras_require={
        'tests': ['pytest'],
        'analysis': ['randomsentence', 'pronounceable', 'memorable_password']
    }
)
