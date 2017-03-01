"""Setup.py for data-structures repo."""


from setuptools import setup

setup(
    name="data-structures",
    description="A series of katas to train on new concepts.",
    version=0.1,
    author="Conor Clary",
    author_email="sclary50@gmail.com",
    license="MIT",
    package_dir={'': 'katas'},
    py_modules=['proper_parenthetics, sum_series'],
    install_requires=['ipython'],
    extras_require={
        "test": ['tox', 'pytest', 'pytest-watch', 'pytest-cov']
    },
)
