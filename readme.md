<h1 align="center">TREKKING 2025 🚗</h1>
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

Para solicitações de uso ou dúvidas, entre em contato pelo e-mail: [carlos.leonardo290403@gmail.com].

## Projeto Desenvolvido

Este projeto foi desenvolvido pelo estudante Carlos Leonardo Lazzari e orientado pelo professor Kleyton Hoffmann como TCC do curso de Engenharia Elétrica, em conjunto com a equipe *WEST BOTS* da UNOESC, campus de Joaçaba/SC, Brasil (2025).  
Todos os equipamentos e componentes utilizados foram financiados pela FAPESC, por meio do Edital nº 51/2024, e pela UNOESC.

> ℹ️ **Nota:** O desenvolvimento deste projeto foi baseado na simulação publicada em: <https://github.com/CarlosLeonardo29/trekking_sim>.

---

### Equipe de Robótica da UNOESC - WEST BOTS

<p align="center">
  <img src="images/logo_westbots.jpg"
       alt="Logo WEST BOTS"
       width="193"
       style="border: 2px solid #000; padding: 8px; background: black;" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="images/logo_unoesc.png"
       alt="Logo UNOESC"
       width="240"
       style="border: 2px solid #ddd; padding: 7px; background: white;" />
</p>

<p align="center">
  <em>Figura 1 — Logotipos da equipe WEST BOTS e da Universidade do Oeste de Santa Catarina (UNOESC).</em>
</p>

---

### Imagens do Veículo Autônomo Desenvolvido

<p align="center">
  <img src="images/IMAGEM CARRO COMPETIÇÃO.jpg" alt="Carrinho em Competição" width="33.5%"/>
  &nbsp;&nbsp;
  <img src="images/CARRO REAL.jpg" alt="Protótipo Final do Carrinho" width="44.5%"/>
</p>

<p align="center">
  <em>Figura 2 — Veículo autônomo desenvolvido pela equipe WEST BOTS durante competição e em sua configuração final.</em>
</p>

---

### Arquitetura de Hardware do Sistema

A Figura **3** apresenta o diagrama de blocos da arquitetura de hardware do protótipo desenvolvido.

<p align="center">
  <img src="images/Arquitetura.png" alt="Diagrama de blocos da arquitetura de hardware do sistema" width="75%"/>
</p>

<p align="center">
  <em>Figura 3 — Diagrama de blocos da arquitetura de hardware do sistema.</em>
</p>

---

### ✍️⚡ Autor e Responsável pelo Projeto - **Eng. Eletricista Carlos Leonardo Lazzari**

### 🎓 Professor Orientador - **Dr. Eng. Eletricista Kleyton Hoffmann**

## Conteúdo
- [🎈 Introdução](#-introdução)
- [⚙️ Dependências](#-dependências)
- [🧪 Compilação e Build](#-compilação-e-build)
- [📊 Resultados Obtidos](#-resultados-obtidos)
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

Para rodar todos os arquivos principais do robô. 

```bash
ros2 run trekking_amr exec_robot.launch.py
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
sudo apt install ros-humble-ros-gz-sim ros-humble-joy ros-humble-teleop-twist-joy ros-humble-robot-localization ros-humble-slam-toolbox ros-humble-ros-gz-bridge ros-humble-nav2-bringup ros-humble-navigation2 ros-humble-xacro ros-humble-joint-state-publisher* ros-humble-rqt* ros-humble-sick-scan-xd 
```

Outras dependências necessárias para o pacote. 

```bash
sudo apt install python3-pip
sudo pip3 install adafruit-circuitpython-bno08x adafruit-circuitpython-pca9685 Jetson.GPIO
```

### Configuração do Ambiente

Para configurar o ambiente de desenvolvimento, adicione as seguintes linhas ao arquivo `~/.bashrc`:

```bash
source /opt/ros/humble/setup.bash
source ~/dev_ws/install/setup.bash
export ROS_DOMAIN_ID=0
```

#### Configuração do CYCLONEDDS.

```bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI=file:///home/westbots/dev_ws/src/trekking_amr/config/dds_configuration.xml
```

---
## 🧪 Compilação e Build

> ⚠️ Atenção: todos os diretórios devem estar listados no arquivo `setup.py` para que o build funcione.

```bash
(os.path.join("share", package_name, "launch"), glob("launch/*")),
(os.path.join("share", package_name, "rviz"), glob("rviz/*")),
(os.path.join("share", package_name, "config"), glob("config/*")),
(os.path.join("share", package_name, "scripts"), glob("scripts/*")),
(os.path.join("share", package_name, "sensors"), glob("sensors/*")),
(os.path.join("share", package_name, "meshes"), glob("meshes/*")),
(os.path.join("share", package_name, "urdf"), glob("urdf/*")),
```

```bash
entry_points={
    "console_scripts": [
        'bno085_node = sensors.bno085_node:main',
        'odom_node = sensors.odom_node:main',
        'odom_path_node = sensors.odom_path_node:main',
        'nav_plan_node = sensors.nav_plan_node:main',
    ],
```

**IMPORTANTE**: Se você fizer qualquer alteração nos arquivos deste projeto, é necessário executar novamente os comandos de build e source!

---
## 📊 Resultados Obtidos

A Figura **1** apresenta o mapa do ambiente construído utilizando a ferramenta **SLAM Toolbox** no modo manual de controle. No mapa estão representados os obstáculos, paredes, áreas navegáveis — como corredores e laboratórios — e áreas não navegáveis, incluindo rampas, trechos sem piso e salas inacessíveis durante a execução dos testes.

<p align="center">
  <img src="images/mapa_trekking.png" alt="Mapa do ambiente gerado com SLAM Toolbox" width="50%"/>
</p>

<p align="center">
  <em>Figura 1 — Mapa do ambiente gerado com a ferramenta SLAM Toolbox.</em>
</p>

---

A Figura **2** apresenta a trajetória efetivamente percorrida pelo robô no modo autônomo, registrada a partir dos dados de odometria acumulados e da estimativa de pose, considerando um ambiente previamente delimitado para os testes experimentais.

<p align="center">
  <img src="images/Rota Realizada no Ambiente.png" alt="Rota realizada pelo robô no modo autônomo" width="50%"/>
</p>

<p align="center">
  <em>Figura 2 — Rota realizada pelo robô no modo autônomo durante os testes.</em>
</p>

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











