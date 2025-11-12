import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Arquivos CSV
# -----------------------------
odom_path_file = '/home/westbots/dev_ws/src/trekking_amr/extras/odom_path.csv'   # realizada pelo robô
nav_path_file = '/home/westbots/dev_ws/src/trekking_amr/extras/nav_plan.csv'  # planejada pelo Nav2

# -----------------------------
# Ler CSVs
# -----------------------------
odom_df = pd.read_csv(odom_path_file)
nav_df = pd.read_csv(nav_path_file)

# -----------------------------
# Trajetórias
# -----------------------------
odom_x = odom_df['x'].values
odom_y = odom_df['y'].values

nav_x = nav_df['x'].values
nav_y = nav_df['y'].values

# -----------------------------
# Plotar apenas trajetórias
# -----------------------------
plt.figure(figsize=(10,10))

plt.plot(nav_x, nav_y, label='Nav2 Planejado', color='blue', linewidth=2, linestyle='--')
plt.plot(odom_x, odom_y, label='Rota Real do Robô', color='red', linewidth=2)

# Início e fim
plt.scatter(odom_x[0], odom_y[0], color='green', s=100, label='Início')
plt.scatter(odom_x[-1], odom_y[-1], color='black', s=100, label='Fim')

plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Trajetórias: planejada vs realizada')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
