import os
from glob import glob
from setuptools import find_packages, setup

package_name = "trekking_amr"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*")),
        (os.path.join("share", package_name, "rviz"), glob("rviz/*")),
        (os.path.join("share", package_name, "config"), glob("config/*")),
        (os.path.join("share", package_name, "scripts"), glob("scripts/*")),
        (os.path.join("share", package_name, "sensors"), glob("sensors/*")),
        (os.path.join("share", package_name, "meshes"), glob("meshes/*")),
        (os.path.join("share", package_name, "urdf"), glob("urdf/*")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="nuke",
    maintainer_email="unoesc.westbots@gmail.com",
    description="Autonomous robot integration in ROS 2",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            'bno085_node = sensors.bno085_node:main',
            'odom_node = sensors.odom_node:main',
        ],
    },
)
