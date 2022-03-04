from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class PCAVisualizer:
    def __init__(self, filename, begin_date=0, gap=1440):
        self.all_data = np.load(filename)
        self.pca_data = self.all_data[begin_date:begin_date+gap]

    def select_date(self, begin_date, end_date):
        self.pca_data = self.all_data[begin_date:end_date]

    def cal_PCA(self, dimension=2):
        pca = PCA(n_components=dimension)
        pca_data=pca.fit_transform(self.pca_data)
        return pca_data

    def draw_fig(self,dimension=2):
        pca_data=self.cal_PCA(dimension)
        if dimension==2:
            plt.figure()
            pca_data=np.transpose(pca_data)
            plt.scatter(pca_data[0],pca_data[1])
            plt.show()

    def draw_3d(self):
        pca_data=np.transpose(self.cal_PCA())
        fig=plt.figure()
        z=range(len(pca_data[0]))
        print(pca_data.shape)
        ax = Axes3D(fig)
        ax.scatter(pca_data[0],pca_data[1],z)
        # ax.plot3D(pca_data[0],pca_data[1],z)
        plt.show()



if __name__ == '__main__':
    visualizer = PCAVisualizer("data/all_data.npy",begin_date=116000,gap=10000)
    visualizer.draw_3d()
