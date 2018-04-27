from setuptools import setup

setup(
    name='passwordstrength',
    version='0.2.1',
    description='Editable password strength calculator for Python',
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
    dependency_links=['git+https://github.com/patarapolw/randomsentence.git#egg=randomsentence',
                      'git+https://github.com/patarapolw/pronounceable.git#egg=pronounceable',
                      'git+https://github.com/patarapolw/memorable-password.git#egg=memorable-password']
)
