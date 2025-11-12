<h1 align="center">Trekking 2025 🚗</h1>
<p align="center">Projeto real de um veículo autônomo com ROS 2 Humble.</p>

<p align="center">
  <a href="https://docs.ros.org/en/humble/index.html">
    <img src="https://img.shields.io/badge/ROS%202-Humble-informational?style=for-the-badge" alt="ROS 2 Humble"/>
  </a>
  <a href="https://gazebosim.org/">
    <img src="https://img.shields.io/badge/Gazebo-Fortress-important?style=for-the-badge" alt="Gazebo Fortress"/>
  </a>
  <a href="https://docs.nav2.org/">
  <img src="https://img.shields.io/badge/ROS%202-NAV2-brightgreen?style=for-the-badge" alt="ROS 2 NAV2"/>
  </a>
  <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
  <a href="#-contribuidores">
    <img src="https://img.shields.io/badge/all_contributors-1-orange.svg?style=for-the-badge" alt="Contribuidores"/>
  </a>
  <!-- ALL-CONTRIBUTORS-BADGE:END -->
</p>

> **Aviso de Direitos Autorais**

Este repositório e seu conteúdo são protegidos por direitos autorais © 2025 Carlos Leonardo Lazzari.  
Todos os direitos estão reservados.

**É proibida** a cópia, modificação, redistribuição ou uso de qualquer parte deste projeto, para qualquer finalidade, sem permissão expressa e por escrito do autor.

## Contato

Para solicitações de uso ou dúvidas, entre em contato: [carlos.leonardo290403@gmail.com]

### Editor: Carlos Leonardo Lazzari

## Conteúdo
- [🎈 Introdução](#-introdução)
- [⚙️ Dependências](#-dependências)
- [🧪 Compilação e Testes](#-compilação-e-testes)
- [📚 Tutoriais](#-tutoriais)
- [🔗 Referências](#-referências)

---
## 🎈 Introdução

Clone o projeto dentro de um workspace ROS 2 baseado em `colcon`.  
Para criar um workspace, siga [este tutorial oficial](https://docs.ros.org/en/humble/Tutorials/Workspace/Creating-A-Workspace.html).

Depois de clonar o projeto e instalar as dependências, compile com:

```bash
colcon build
source install/setup.bash
```

Para gerar os frames do robô. 

```bash
ros2 launch trekking_amr robot.launch.py
```

Para rodar os nós do robô. 
```bash
ros2 run trekking_amr bno085_node

ros2 run trekking_amr odom_node
```

Para rodar o drive do LiDAR SICK PICOSCAN150. 
```bash
ros2 launch sick_scan_xd sick_picoscan.launch.py
```

Para visualização dos dados e do robô.

```bash
ros2 run rviz2 rviz2
```

Para controlar manualmente o robô (Controle PS4).

```bash
ros2 launch trekking_amr teleop.launch.py

run cmd_vel_to_pwm.py
```

Para rodar o SLAM (modo mapeamento).

```bash
ros2 launch trekking_amr slam.launch.mapper.py
```

Para salvar o mapa gerado.

```bash
ros2 run nav2_map_server map_saver_cli -f ~/dev_ws/src/trekking_amr/maps/mapa_trekking
```

```bash
ros2 service call /slam_toolbox/serialize_map slam_toolbox/srv/SerializePoseGraph "{filename: '/home/westbots/dev_ws/src/trekking_amr/maps/mapa_trekking'}"
```

> 💬 **Nota:** Os comandos acima irão gerar os seguintes arquivos no diretório especificado:
>
> - `mapa_trekking.pgm`: imagem da grade de ocupação
> - `mapa_trekking.yaml`: arquivo de metadados do mapa
> - `mapa_trekking.data`: dados serializados do mapa (utilizado internamente pelo SLAM Toolbox)
> - `mapa_trekking.posegraph`: grafo de poses serializado (usado para localização e fusão de mapas)

Para rodar o SLAM (modo localização - mapa previamente gerado).

```bash
ros2 launch trekking_amr slam.launch.localization.py
```

Para ativar o modo de navegação autônoma do robô (NAV2).

```bash
ros2 launch trekking_amr navigation_launch.py use_sim_time:=false
```

Para salvar a rota gerada pela NAV2. 
```bash
ros2 run trekking_amr nav_plan_node
```

Para salvar a rota realizada pelo robô.
```bash
ros2 run trekking_amr odom_path_node
```

---
## ⚙️ Dependências

Dependências necessárias para o pacote no ROS 2. 

```bash
sudo apt install ros-humble-ros-gz-sim ros-humble-joy ros-humble-teleop-twist-joy ros-humble-robot-localization ros-humble-slam-toolbox ros-humble-ros-gz-bridge ros-humble-nav2-bringup ros-humble-navigation2 ros-humble-xacro ros-humble-joint-state-publisher* ros-humble-rqt*
```

Configuração do CYCLONEDDS (.bashrc).

```bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI=file:///home/westbots/dev_ws/src/trekking_amr/config/dds_configuration.xml
```

---
## 📦 Criando o Pacote ROS (Python)

No seu workspace do ROS 2 e crie um pacote Python. Os pacotes `urdf`, `rclpy` e `xacro` são dependências necessárias para esse pacote.
```bash
cd ~/dev_ws/src \
ros2 pkg create trekking_2025 --build-type ament_python --dependencies rclpy urdf xacro
```

---
## ▶️ Executando a Simulação

---
## 🧪 Compilação e Testes

Para compilar o projeto, é necessário adicionar todos os diretórios ao arquivo `setup.py .

```bash
(os.path.join("share", package_name, "launch"), glob("launch/*")),
(os.path.join("share", package_name, "rviz"), glob("rviz/*")),
(os.path.join("share", package_name, "config"), glob("config/*")),
(os.path.join("share", package_name, "scripts"), glob("scripts/*")),
(os.path.join("share", package_name, "sensors"), glob("sensors/*")),
```

```bash
entry_points={
  "console_scripts": [
      'bno085_node = sensors.bno085_node:main',
      'odom_node = sensors.odom_node:main',
],
```

**IMPORTANTE**: Se você fizer qualquer alteração nos arquivos deste projeto, é necessário executar novamente os comandos de build e source!

---
## 📚 Tutoriais

Para executar este projeto, é necessário ter o **ROS 2 Humble** e o **Gazebo Sim** instalados no seu sistema.

- [Instalar o ROS 2 Humble (Ubuntu)](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
- [Instalar o Gazebo Sim (integração com ROS)](https://gazebosim.org/docs/latest/ros_installation/)

---
## 🔗 Referências

- [ROS 2 Documentation](https://docs.ros.org/en/humble/)
- [Ignition Gazebo Documentation](https://gazebosim.org/docs)
- [Nav2 Tutorials](https://docs.nav2.org/)
- [SLAM Toolbox](https://docs.nav2.org/tutorials/docs/navigation2_with_slam.html)











