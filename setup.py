from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['easy_kinesthetic_recording'],
    package_dir={'': 'src'}
)

setup(**d)
