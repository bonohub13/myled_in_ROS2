from setuptools import setup

package_name = 'cpu_temp2led'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kensuke Saito',
    maintainer_email='ken.saito.0813@gmail.com',
    description='TODO: Package description',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cpu_temp2led = cpu_temp2led.cpu_temp2led:main'
        ],
    },
)
