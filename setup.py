# Copyright 2025 Carlos Leonardo Lazzari
#
# Projeto: Desenvolvimento de um Veículo Autônomo com ROS para Mapeamento e Navegação em Ambientes Estáticos
#
# Trabalho de Conclusão de Curso – Engenharia Elétrica, UNOESC
# Equipe WEST BOTS – Campus Joaçaba/SC
# Plataforma: ROS 2 Humble + NVIDIA Jetson Orin Nano
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    maintainer="Carlos Leonardo Lazzari",
    maintainer_email="carlos.leonardo290403@gmail.com",
    description="Desenvolvimento de um Veículo Autônomo com ROS para mapeamento e navegação em ambientes estáticos utilizando algoritmos SLAM, A* Híbrido e controlador MPPI.",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            'bno085_node = sensors.bno085_node:main',
            'odom_node = sensors.odom_node:main',
            'odom_path_node = sensors.odom_path_node:main',
            'nav_plan_node = sensors.nav_plan_node:main',
        ],
    },
)
