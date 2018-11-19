from setuptools import setup

setup(
    name='aws-adfs',
    version='0.1.0',
    author='duckgogo',
    author_email='zengjx92@hotmail.com',
    description='Login to AWS CLI using Active Directory Federation Services.',
    py_modules=['aws_cli_adfs'],
    packages=['aws_cli_adfs'],
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=[
        'awscli',
        'beautifulsoup4',
        'boto',
        'Click',
        'configparser',
        'requests',
        'toml'
    ],
    entry_points='''
        [console_scripts]
        aws-adfs = aws_cli_adfs.cli:cli
    ''',
)