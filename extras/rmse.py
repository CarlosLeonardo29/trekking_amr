import pandas as pd
import numpy as np

# -----------------------------
# Arquivos CSV
# -----------------------------
odom_path_file = '/home/westbots/dev_ws/src/trekking_amr/extras/odom_path.csv'   # trajetória real
nav_path_file = '/home/westbots/dev_ws/src/trekking_amr/extras/nav_plan.csv'    # trajetória planejada

# -----------------------------
# Ler CSVs
# -----------------------------
odom_df = pd.read_csv(odom_path_file)
nav_df = pd.read_csv(nav_path_file)

# -----------------------------
# Posições e tempos
# -----------------------------
odom_points = odom_df[['x','y']].values
nav_points = nav_df[['x','y']].values

if 'time' in odom_df.columns:
    odom_time = odom_df['time'].values
else:
    odom_time = np.arange(len(odom_points))

if 'time' in nav_df.columns:
    nav_time = nav_df['time'].values
else:
    nav_time = np.arange(len(nav_points))

# -----------------------------
# Ajustar tamanho
# -----------------------------
min_len = min(len(odom_points), len(nav_points))
odom_points = odom_points[:min_len]
nav_points = nav_points[:min_len]
odom_time = odom_time[:min_len]

# -----------------------------
# RMSE e MAE posição
# -----------------------------
diff = odom_points - nav_points
dist_error = np.linalg.norm(diff, axis=1)

rmse = np.sqrt(np.mean(dist_error**2))
mae = np.mean(np.abs(dist_error))

# -----------------------------
# Distância percorrida
# -----------------------------
def route_length(points):
    diffs = np.diff(points, axis=0)
    return np.sum(np.linalg.norm(diffs, axis=1))

odom_dist = route_length(odom_points)
nav_dist = route_length(nav_points)

# -----------------------------
# Velocidade média
# -----------------------------
dt = np.diff(odom_time)
dx = np.diff(odom_points, axis=0)
# evitar divisão por zero
dt[dt==0] = 1e-6
velocities = np.linalg.norm(dx, axis=1)/dt
mean_velocity = np.mean(velocities)

# -----------------------------
# Tempo total
# -----------------------------
total_time = odom_time[-1] - odom_time[0]

# -----------------------------
# Relatório
# -----------------------------
print("===== Métricas Essenciais da Trajetória =====")
print(f"RMSE posição: {rmse:.4f} m")
print(f"MAE posição: {mae:.4f} m")
print(f"Distância percorrida (real): {odom_dist:.4f} m")
print(f"Distância percorrida (planejada): {nav_dist:.4f} m")
print(f"Velocidade média (real): {mean_velocity:.4f} m/s")
print(f"Tempo total (real): {total_time:.2f} s")
