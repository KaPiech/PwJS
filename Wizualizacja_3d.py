
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def get_params(time):

    Yaw_deg = time*10
    Pitch_deg = time*5
    Roll_deg =  time*2
    X = 0
    Y = 0
    Z = 0

    return Yaw_deg, Pitch_deg, Roll_deg, X, Y, Z


def plot_IMU(time):


    Yaw_deg, Pitch_deg, Roll_deg, X, Y, Z = get_params(time)
    Yaw=Yaw_deg*np.pi/180
    Pitch=Pitch_deg*np.pi/180
    Roll=Roll_deg*np.pi/180


    fig.clf()
    ax = fig.add_subplot(111, projection='3d')

    euler_Rx=np.array([[1,0,0],[0,np.cos(Roll),-np.sin(Roll)],[0,np.sin(Roll),np.cos(Roll)]])
    euler_Ry=np.array([[np.cos(Pitch),0,np.sin(Pitch)], [0,1,0], [-np.sin(Pitch),0,np.cos(Pitch)]])
    euler_Rz=np.array([[np.cos(Yaw),-np.sin(Yaw),0],[np.sin(Yaw),np.cos(Yaw),0], [0,0,1]])
    euler_Rzyx=np.dot(np.dot(euler_Rz,euler_Ry),euler_Rx)


    x_s=np.dot(euler_Rzyx,np.array([[1,0,0]]).T)
    y_s=np.dot(euler_Rzyx,np.array([[0,1,0]]).T)
    z_s=np.dot(euler_Rzyx,np.array([[0,0,1]]).T)


    ax.quiver(X,Y,Z,x_s[0],x_s[1],x_s[2],pivot='tail')
    ax.quiver(X,Y,Z,y_s[0],y_s[1],y_s[2],pivot='tail')
    ax.quiver(X,Y,Z,z_s[0],z_s[1],z_s[2],pivot='tail')


    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.xticks(np.linspace(-2,2,num=5))
    plt.yticks(np.linspace(-2,2,num=5))
    ax.set_zticks(np.linspace(-1,1,num=5))
    ax.view_init(30,-115)


ani = FuncAnimation(fig, plot_IMU, frames=np.linspace(1,998,998))
plt.show()

