from setuptools import setup

setup(
    name="ev_group05",
    version='0.1',
    py_modules=['ev_group05'],
    install_requires=['Click',],
    entry_points='''
        [console_scripts]
        ev_group05=ev_group05:main
        '''
)
