from setuptools import setup, find_packages

setup(
    name='discohooks',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A simple library for interacting with Discord webhooks',
    author='Nyxoy201',
    author_email='discord.nyxoy@proton.me',
    url='https://github.com/Nyxoy201/discohooks',
)
