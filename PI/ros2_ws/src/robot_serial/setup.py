from setuptools import find_packages, setup

package_name = 'robot_serial'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='pi@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial = robot_serial.puerto_serie:main',
            'serial_salida = robot_serial.puerto_serie_salida:main',
            'find = robot_serial.find_ports:main',
        ],
    },
)
