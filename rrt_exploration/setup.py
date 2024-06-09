from setuptools import setup

package_name = 'rrt_exploration'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/rrt_exploration.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='StanleyChueh',
    maintainer_email='stanleychueh28@gmail.com',
    description='RRT-based exploration for autonomous SLAM',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rrt_exploration = rrt_exploration.rrt_exploration:main',
        ],
    },
)

