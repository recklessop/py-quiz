from setuptools import setup

setup(
    name='quiz',
    version='0.1',
    description='A quiz module for interactive Python quizzes',
    author='Justin Paul',
    author_email='justin@jpaul.me',
    packages=['quiz'],
    install_requires=[
        # List any dependencies your module may have here
        'ipywidgets',
    ],
)
