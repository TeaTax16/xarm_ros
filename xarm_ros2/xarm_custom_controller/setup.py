from setuptools import setup

package_name = 'xarm_custom_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vror',
    maintainer_email='titastakrim@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "draw_circle = xarm_custom_controller.draw_circle:main",
            "move_up = xarm_custom_controller.move_up:main",
            "move_down = xarm_custom_controller.move_down:main",
            "move_fw = xarm_custom_controller.move_fw:main",
            "move_bw = xarm_custom_controller.move_bw:main",
            "move_left = xarm_custom_controller.move_left:main",
            "move_right = xarm_custom_controller.move_right:main",
            "angular_test = xarm_custom_controller.angular_test:main",
            
        ],
    },
)
