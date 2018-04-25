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
    package_data={
        'passwordstrength': ['database/*']
    },
    include_package_data=True,
    extras_require={
        'analysis': ['randomsentence', 'pronounceable', 'memorable_password']
    }
)
