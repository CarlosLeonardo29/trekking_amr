import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

odom_path_file = '/home/westbots/dev_ws/src/trekking_amr/extras/odom_path.csv'   # trajetória real
nav_path_file = '/home/westbots/dev_ws/src/trekking_amr/extras/nav_plan.csv'      # trajetória planejada
save_dir = '/home/westbots/dev_ws/src/trekking_amr/extras'

odom_df = pd.read_csv(odom_path_file)
nav_df = pd.read_csv(nav_path_file)

odom_x = odom_df['x'].values
odom_y = odom_df['y'].values

nav_x = nav_df['x'].values
nav_y = nav_df['y'].values

plt.figure(figsize=(10,10))

plt.plot(nav_x, nav_y, label='Rota Gerada pela NAV2', color='blue', linewidth=2, linestyle='--')
plt.plot(odom_x, odom_y, label='Rota Realizada', color='red', linewidth=2)

plt.scatter(odom_x[0], odom_y[0], color='green', s=100, label='Início')
plt.scatter(odom_x[-1], odom_y[-1], color='black', s=100, label='Fim')

plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Trajetórias: Planejada vs Realizada')
plt.legend()
plt.axis('equal')
plt.grid(True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
save_path = os.path.join(save_dir, f"comparacao_trajetorias_{timestamp}.png")

plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"✅ Gráfico salvo em: {save_path}")

plt.show()
