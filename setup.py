from setuptools import setup, find_packages

setup(
    name='long-to-short-cli',
    version='1.0.1',
    description='A CLI tool to extract a video clip and crop it to a 9:16 aspect ratio using MoviePy',
    author='Zach Bimson',
    author_email='zach@bison.digital',
    url='https://github.com/bimsonz/long-to-short-cli',
    packages=find_packages(),
    install_requires=[
        'moviepy',
    ],
    entry_points={
        'console_scripts': [
            'long-to-short-cli=long_to_short_cli:main',
        ],
    },
)
