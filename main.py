import numpy as np
import matplotlib.pyplot as plt

# 定义起点和目标点
start = np.array([0, 0])
goal_R = np.array([1, 0])  # 目标G_R
goal_O = np.array([1, 1])  # 另一个可能的目标G_O

# 定义匀速直线运动的轨迹函数
def trajectory(t, start, goal, speed):
    direction = goal - start
    distance = np.linalg.norm(direction)
    direction_normalized = direction / distance
    return np.outer(t * speed, direction) + start

# 生成并绘制轨迹
def generate_and_plot_trajectories(start, goal_R, goal_O, beta_values):
    timesteps = np.linspace(0, 1, 100)  # 假设路径总时间为1
    plt.figure()
    
    # 绘制预期轨迹（灰色）
    expected_trajectory = trajectory(timesteps, start, goal_R, 1)
    plt.plot(expected_trajectory[:, 0], expected_trajectory[:, 1], 'k--', label='Expected Trajectory')
    
    # 对每个β值生成轨迹
    for beta in beta_values:
        # 根据β值确定速度和方向偏移量
        speed = np.sqrt(2 * beta)  # 假设直线轨迹速度为1，那么我们可以基于β调整速度
        # 计算目标方向
        goal_direction = goal_R if beta == 10 else goal_O
        # 生成轨迹
        traj = trajectory(timesteps, start, goal_direction, speed)
        plt.plot(traj[:, 0], traj[:, 1], label=f'β={beta}')
    
    # 添加图例和标题
    plt.scatter(*start, c='blue', label='Start (S)')
    plt.scatter(*goal_R, c='red', label='Goal (G_R)')
    plt.scatter(*goal_O, c='green', label='Alternate Goal (G_O)')
    plt.legend()
    plt.title('Trajectories with Different Trust Region Sizes')
    plt.show()

# 测试不同的β值
beta_values = [10, 20, 40, 80, 160]  # 不同的信任区域大小
generate_and_plot_trajectories(start, goal_R, goal_O, beta_values)
