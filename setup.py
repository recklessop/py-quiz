from setuptools import setup

setup(
    name='pyquizjp',
    version='0.1',
    description='A quiz module for interactive Python quizzes',
    author='Justin Paul',
    author_email='justin@jpaul.me',
    packages=['pyquizjp'],
    install_requires=[
        # List any dependencies your module may have here
        'ipywidgets',
    ],
)
