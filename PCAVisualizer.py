from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class PCAVisualizer:
    def __init__(self, filename, begin_date=0, gap=1440, restore_file=None):
        self.all_data = np.load(filename)
        self.pca_data = self.all_data[begin_date:begin_date + gap]
        if restore_file is None:
            self.restored_data = None
        else:
            self.restored_data = np.load(restore_file)

    def select_date(self, begin_date, end_date):
        self.pca_data = self.all_data[begin_date:end_date]

    def cal_PCA(self, dimension=2):
        pca = PCA(n_components=dimension)
        pca_data = pca.fit_transform(self.pca_data)
        return pca_data

    def draw_fig(self, dimension=2, restore_filename=None, title=None, color=False):
        if restore_filename is None:
            pca_data = self.cal_PCA(dimension)
        else:
            pca_data = np.load(restore_filename)
        pca_data = np.transpose(pca_data)
        if dimension == 2:
            plt.figure()
            if title is not None:
                plt.title(title)
            if color:
                z = np.arange(pca_data.shape[1])
                plt.scatter(pca_data[0], pca_data[1], c=z)
            else:
                plt.scatter(pca_data[0], pca_data[1])
            plt.show()
        if dimension == 3:
            fig = plt.figure()
            if title is not None:
                plt.title(title)
            ax = Axes3D(fig)
            if color:
                z = np.arange(pca_data.shape[1])
                ax.scatter(pca_data[0], pca_data[1], pca_data[2], c=z)
            else:
                ax.scatter(pca_data[0], pca_data[1], pca_data[2])
            plt.show()

    def draw_3d(self):
        pca_data = np.transpose(self.cal_PCA())
        fig = plt.figure()
        z = range(len(pca_data[0]))
        ax = Axes3D(fig)
        ax.scatter(pca_data[0], pca_data[1], z)
        ax.plot3D(pca_data[0], pca_data[1], z, "gray")
        plt.show()

    def save_pca_data(self, filename, dimension=2):
        pca_data = self.cal_PCA(dimension)
        np.save(filename, pca_data)


# title="2020.5.20 10:25"
# title="2020.9.2 9:05",v
# title="2020.12.1 11:30"


if __name__ == '__main__':
    # print(np.arange(10))
    # exit()
    visualizer = PCAVisualizer("data/all_data.npy", begin_date=112945+1000, gap=2880-2000)
    visualizer.draw_fig(dimension=2, title="2020.5.20 10:25", color=True)
    visualizer.draw_fig(dimension=3, title="2020.5.20 10:25", color=True)
    visualizer = PCAVisualizer("data/all_data.npy", begin_date=264065+1000, gap=2880-1000)
    visualizer.draw_fig(dimension=2, title="2020.9.2 9:05", color=True)
    visualizer.draw_fig(dimension=3, title="2020.9.2 9:05", color=True)
    visualizer = PCAVisualizer("data/all_data.npy", begin_date=393810+1000, gap=2880-1000)
    visualizer.draw_fig(dimension=2, title="2020.12.1 11:30", color=True)
    visualizer.draw_fig(dimension=3, title="2020.12.1 11:30", color=True)
    # for index,val in enumerate(visualizer.restored_data):
    #     if (val[1]>300000 or val[1]<-1000):
    #         print(index,val)
    # visualizer.save_pca_data("data/2dpca.npy", dimension=2)
    # visualizer.save_pca_data("data/3dpca.npy", dimension=3)
    # visualizer.draw_fig(dimension=3, restore_filename="data/3dpca.npy")
    # visualizer.draw_fig(dimension=2, restore_filename="data/3dpca.npy")
    #
