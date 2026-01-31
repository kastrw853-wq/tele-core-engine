from setuptools import setup, find_packages

setup(
    name="tele-core-engine",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pyTelegramBotAPI',
        'flask',
        'requests',
    ],
)
