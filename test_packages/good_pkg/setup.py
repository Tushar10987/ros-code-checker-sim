from setuptools import setup

package_name = 'good_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'simple_node = good_pkg.simple_node:main'
        ],
    },
)
