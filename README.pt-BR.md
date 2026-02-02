<h1 align="center">Veículo Autônomo - Categoria TREKKING 🏎️</h1>
<p align="center">Projeto real de um veículo autônomo em escala 1/10 para mapeamento e navegação em ambientes estáticos com ROS.</p>

<p align="center">
  <a href="https://docs.ros.org/en/humble/index.html">
    <img src="https://img.shields.io/badge/ROS%202-Humble-informational?style=for-the-badge" alt="ROS 2 Humble"/>
  </a>
  <a href="https://releases.ubuntu.com/22.04/">
    <img src="https://img.shields.io/badge/Ubuntu-22.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu 22.04"/>
  </a>
  <a href="https://docs.nav2.org/">
  <img src="https://img.shields.io/badge/ROS%202-NAV2-brightgreen?style=for-the-badge" alt="ROS 2 NAV2"/>
  </a>
  <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
  <a href="#-contribuidores">
    <img src="https://img.shields.io/badge/Contribuidores-4-orange.svg?style=for-the-badge" alt="Contribuidores"/>
  </a>
  <!-- ALL-CONTRIBUTORS-BADGE:END -->
</p>

> **Aviso de Direitos Autorais**

Copyright © 2025 Carlos Leonardo Lazzari.

Este repositório pode ser utilizado, copiado, modificado e redistribuído de acordo com os termos da **Apache License 2.0**. Esta licença não concede direitos sobre marcas, nomes ou logotipos do projeto, da equipe WEST BOTS ou da UNOESC. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.

## Contato

### ⚡ Autor Principal e Responsável pelo Projeto - **Eng. Eletricista Carlos Leonardo Lazzari** 

<p align="left">
  <a href="https://www.linkedin.com/in/carlos-leonardo29/">
    <img src="https://img.shields.io/badge/LinkedIn-Carlos_Leonardo-blue?logo=linkedin&logoColor=white"/>
  </a>
  <a href="http://lattes.cnpq.br/1607061869218351">
    <img src="https://img.shields.io/badge/Currículo-Lattes-green"/>
  </a>
  <a href="https://linktr.ee/carlosleonardo29">
    <img src="https://img.shields.io/badge/Linktree-Carlos_Leonardo-brightgreen?logo=linktree&logoColor=white"/>
  </a>
</p>

## 🤝 Contribuidores
  
- **Murilo Ribeiro Bonato** – [LinkedIn](https://www.linkedin.com/in/murilo-bonato-0996a3226/)  
- **Prof. Dr. Kleyton Hoffmann** – [LinkedIn](https://www.linkedin.com/in/kleyton-hoffmann/)  
- **Prof. Dr. Renato Gregolon Scortegagna** – [LinkedIn](https://www.linkedin.com/in/renato-scortegagna-99028bab/)

> ℹ️ **Para solicitações de uso ou dúvidas:** Entre em contato pelo e-mail: [carlos.leonardo290403@gmail.com](mailto:carlos.leonardo290403@gmail.com) ou [kleyton.hoffmann@unoesc.edu.br](mailto:kleyton.hoffmann@unoesc.edu.br).

## 🗂️ Conteúdo
- [🎈 Introdução](#-introdução)
- [🚀 Inicialização do Sistema](#-inicialização-do-sistema)
- [⚙️ Dependências](#️-dependências)
- [📂 Estrutura do Pacote](#-estrutura-do-pacote)
- [🧪 Compilação e Build](#-compilação-e-build)
- [🖥️ Arquitetura do Sistema](#️-arquitetura-do-sistema)
  - [📦 Arquitetura de Hardware](#-arquitetura-de-hardware)
  - [💻 Arquitetura de Software](#-arquitetura-de-software)
- [📊 Resultados Obtidos](#-resultados-obtidos)
- [📚 Tutoriais](#-tutoriais)
- [🔗 Referências](#-referências)
- [🔬 Como Citar](#-como-citar)

## 🎈 Introdução

### Informações do Projeto

Este projeto foi desenvolvido pelos acadêmicos de Engenharia Elétrica **Carlos Leonardo Lazzari** e **Murilo Ribeiro Bonato**, atualmente engenheiros eletricistas, sob a orientação do Prof. Dr. Eng. Eletricista **Kleyton Hoffmann**, como Trabalho de Conclusão de Curso do curso de Engenharia Elétrica, em conjunto com a equipe WEST BOTS da UNOESC, campus de Joaçaba/SC, Brasil (2025). Todos os equipamentos e componentes utilizados foram financiados pela FAPESC, por meio do Edital nº 51/2024, e pela UNOESC.

O protótipo deve ser capaz de realizar o mapeamento prévio de um ambiente estático durante as fases de teste da competição, sob controle do operador. Nas etapas válidas, deverá localizar-se no ambiente mapeado, gerar e seguir trajetórias de forma autônoma e sequencial até pontos previamente conhecidos.

> ℹ️ **Título do TCC:** *Desenvolvimento de um Veículo Autônomo com ROS para Mapeamento e Navegação em Ambientes Estáticos.*

> ℹ️ **Nota:** O desenvolvimento deste projeto foi baseado na simulação disponível em: <https://github.com/CarlosLeonardo29/trekking_sim>.

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

### Veículo Autônomo Desenvolvido

<p align="center">
  <img src="images/carro_competicao.jpg" alt="Carrinho em Competição" width="33.5%"/>
  &nbsp;&nbsp;
  <img src="images/carro_lateral.jpg" alt="Protótipo Final do Carrinho" width="44.5%"/>
</p>

<p align="center">
  <em>Figura 2 — Configuração final do veículo autônomo desenvolvido pela equipe WEST BOTS.</em>
</p>

## 🚀 Inicialização do Sistema

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

Para rodar o driver do LiDAR SICK PICOSCAN150. 
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
ros2 service call /slam_toolbox/serialize_map slam_toolbox/srv/SerializePoseGraph "{filename: '/home/carloslazzari/dev_ws/src/trekking_amr/maps/mapa_trekking'}"
```

> 💬 **Nota:** Os comandos acima irão gerar os seguintes arquivos no diretório especificado:
>
> - `mapa_trekking.pgm`: imagem da grade de ocupação.
> - `mapa_trekking.yaml`: arquivo de metadados do mapa.
> - `mapa_trekking.data`: dados serializados do mapa (utilizado internamente pelo SLAM Toolbox).
> - `mapa_trekking.posegraph`: grafo de poses serializado (usado para localização e fusão de mapas).

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

## ⚙️ Dependências

Dependências necessárias para o pacote no ROS 2. 

```bash
sudo apt install ros-humble-ros-gz-sim ros-humble-joy ros-humble-teleop-twist-joy ros-humble-robot-localization ros-humble-slam-toolbox ros-humble-ros-gz-bridge ros-humble-nav2-bringup ros-humble-navigation2 ros-humble-xacro ros-humble-joint-state-publisher* ros-humble-rqt* ros-humble-sick-scan-xd ros-humble-rmw-cyclonedds-cpp
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
export ROS_LOCALHOST_ONLY=1
export LIBGL_ALWAYS_SOFTWARE=0 
```

### Configuração do CYCLONEDDS.

```bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI=file:///home/carloslazzari/dev_ws/src/trekking_amr/config/dds_configuration.xml
```

## 📂 Estrutura do Pacote

Descrição do conteúdo de cada diretório do pacote **trekking_amr**. 

| Pasta | Descrição |
|---|---|
| [**config/**](./config) | Arquivos de configuração dos nós e parâmetros do sistema. |
| [**launch/**](./launch) | Arquivos para inicialização dos componentes no ROS 2. |
| [**urdf/**](./urdf) | Descrição do robô em URDF/Xacro. |
| [**meshes/**](./meshes) | Modelos 3D do robô. |
| [**sensors/**](./sensors) | Configurações e definições dos sensores embarcados. |
| [**rviz/**](./rviz) | Configurações de visualização no RViz. |
| [**maps/**](./maps) | Mapas gerados e utilizados pelo sistema. |
| [**scripts/**](./scripts) | Scripts auxiliares em Python. |
| [**extras/**](./extras) | Arquivos complementares do projeto. |
| [**images/**](./images) | Imagens usadas na documentação. |

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

## 🖥️ Arquitetura do Sistema

### 📦 Arquitetura de Hardware

A Figura **3** apresenta o diagrama de blocos da arquitetura de hardware do protótipo desenvolvido.

<p align="center">
  <img src="images/Arquitetura.png" alt="Diagrama de blocos da arquitetura de hardware do sistema" width="75%"/>
</p>

<p align="center">
  <em>Figura 3 — Diagrama de blocos da arquitetura de hardware do sistema.</em>
</p>

---

A Figura **4** apresenta o projeto da PCB para extensão dos pinos da NVIDIA Jetson Orin Nano.

<p align="center">
  <img src="images/placa_extensao.png" alt="Placa de extensão do protótipo" width="50%"/>
</p>

<p align="center">
  <em>Figura 4 — Placa de extensão para NVIDIA Jetson Orin Nano.</em>
</p>

---

### 💻 Arquitetura de Software

#### 🛠️ Fluxograma de Funcionamento

A Figura **5** e **6** apresentam os fluxogramas de funcionamento do protótipo desenvolvido.

<p align="center">
  <img src="images/Fluxograma Selecionar Modo.png" alt="Fluxograma Selecionar Modo" width="32%" />
  <img src="images/Fluxograma Modo Manual.png" alt="Fluxograma Modo Manual" width="22.3%" />
</p>

<p align="center">
  <em>Figura 5 — Fluxogramas de seleção de modo e modo manual do protótipo.</em>
</p>

<p align="center">
  <img src="images/Fluxograma Modo Autônomo.png" alt="Fluxograma Modo Autônomo" width="50%" />
</p>

<p align="center">
  <em>Figura 6 — Fluxograma do modo autônomo do protótipo.</em>
</p>

---

#### 🛠️ Árvore de Transformadas (TF Tree)

A Figura **7** apresenta a hierarquia de frames do robô, indicando como cada referência de posição e orientação (*pose*) está conectada ao sistema de coordenadas. A seguir, é possível visualizar a árvore de transformadas do projeto desenvolvido.

<p align="center">
  <img src="images/tf_tree.jpg" alt="Árvore de transformadas (TF Tree) do sistema" width="50%"/>
</p>

<p align="center">
  <em>Figura 7 — Árvore de transformadas (TF Tree) do sistema.</em>
</p>

## 📊 Resultados Obtidos

A Figura **8** apresenta o mapa do ambiente construído utilizando a ferramenta **SLAM Toolbox** no modo manual de controle. No mapa estão representados os obstáculos, paredes, áreas navegáveis — como corredores e laboratórios — e áreas não navegáveis, incluindo rampas, trechos sem piso e salas inacessíveis durante a execução dos testes.

<p align="center">
  <img src="images/mapa_trekking.png" alt="Mapa do ambiente gerado com SLAM Toolbox" width="50%"/>
</p>

<p align="center">
  <em>Figura 8 — Mapa do ambiente gerado com a ferramenta SLAM Toolbox.</em>
</p>

---

A Figura **9** apresenta a trajetória efetivamente percorrida pelo robô no modo autônomo, registrada a partir dos dados de odometria acumulados e da estimativa de pose, considerando um ambiente previamente delimitado para os testes experimentais.

<p align="center">
  <img src="images/rota_realizada.png" alt="Rota realizada pelo robô no modo autônomo" width="50%"/>
</p>

<p align="center">
  <em>Figura 9 — Rota realizada pelo robô no modo autônomo durante os testes.</em>
</p>

## 📚 Tutoriais

Para executar este projeto, é necessário ter o **ROS 2 Humble** e o **Gazebo Sim** instalados no seu sistema.

- [Instalar o ROS 2 Humble (Ubuntu)](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
- [Instalar o Gazebo Sim (integração com ROS)](https://gazebosim.org/docs/latest/ros_installation/)

## 🔗 Referências

- [ROS 2 Documentation](https://docs.ros.org/en/humble/)
- [Ignition Gazebo Documentation](https://gazebosim.org/docs)
- [Nav2 Tutorials](https://docs.nav2.org/)
- [SLAM Toolbox](https://docs.nav2.org/tutorials/docs/navigation2_with_slam.html)

## 🔬 Como Citar

Se este projeto ou repositório for utilizado em trabalhos acadêmicos ou técnicos, solicita-se a seguinte citação:

**Referência (ABNT):**

LAZZARI, Carlos Leonardo; BONATO, Murilo Ribeiro. **Desenvolvimento de um Veículo Autônomo com ROS para Mapeamento e Navegação em Ambientes Estáticos.** Orientador: Prof. Dr. Kleyton Hoffmann. Trabalho de Conclusão de Curso (Bacharelado em Engenharia Elétrica) – Universidade do Oeste de Santa Catarina, Joaçaba, 2025.

**BibTeX:**

```bibtex
@thesis{Lazzari2025,
  author  = {Lazzari, Carlos Leonardo and Bonato, Murilo Ribeiro},
  title   = {Desenvolvimento de um Veículo Autônomo com ROS para Mapeamento e Navegação em Ambientes Estáticos},
  school  = {Universidade do Oeste de Santa Catarina - UNOESC},
  address = {Joaçaba, SC, Brasil},
  year    = {2025},
  type    = {Trabalho de Conclusão de Curso (Engenharia Elétrica)},
  note    = {Orientador: Prof. Dr. Kleyton Hoffmann}
}
```

---