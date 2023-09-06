from setuptools import setup
from .pyquizjp.__version__ import __version__

setup(
    name='pyquizjp',
    description='A quiz module for interactive Python quizzes',
    author='Justin Paul',
    author_email='justin@jpaul.me',
    packages=['pyquizjp'],
    install_requires=[
        # List any dependencies your module may have here
        'ipywidgets',
        'requests'
    ],
)
