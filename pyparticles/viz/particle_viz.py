import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def animate(iteration: int,
            frames: int,
            positions: np.array):

    current_index = int(positions[0].shape[0] / frames * iteration)
    ax.cla()

    for position in positions:
        ax.plot3D(position[:current_index, 0],
                  position[:current_index, 1],
                  position[:current_index, 2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

def run_3d_animation(animate: object):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    anim = animation.FuncAnimation(fig, animate,
                                   frames=FRAMES, interval=100)

    display_animation(anim)