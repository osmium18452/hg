import numpy as np


class DataLoader:
    def __init__(self, filename, dataset_size=None):
        self.ori_all_data = []
        with open(filename, "r") as f:
            for line in f.readlines():
                if not line[0] == "t":
                    self.ori_all_data.append(list(map(float, line.strip().split(","))))
        if dataset_size is None:
            self.dataset_size = len(self.ori_all_data)
        else:
            self.dataset_size = dataset_size
        self.ori_all_data = np.array(self.ori_all_data[len(self.ori_all_data) - self.dataset_size:])[:, 1:]

    def save_as_csv(self, filename, data="ori"):
        if data == "ori":
            np.savetxt(filename, self.ori_all_data, delimiter=',', fmt="%.10f")
        elif data == "filter":
            np.savetxt(filename, self.load_filtered_data(), delimiter=',', fmt="%.10f")
        elif data == "norm":
            np.savetxt(filename, self.load_norm_data(), delimiter=',', fmt="%.10f")

    def load_ori_data(self):
        return self.ori_all_data

    def load_filtered_data(self):
        transposed_data = np.transpose(self.ori_all_data)
        filtered_data = []
        for arr in transposed_data:
            if len(set(arr)) > 1:
                filtered_data.append(arr)
        filtered_data = np.array(filtered_data)
        return np.transpose(filtered_data)

    def load_norm_data(self):
        transposed_data = self.load_filtered_data().transpose()
        norm_data = []
        for arr in transposed_data:
            norm_data.append((arr - arr.min(initial=None)) / (arr.max(initial=None) - arr.min(initial=None)))
        norm_data = np.array(norm_data).transpose()
        return norm_data

    def load_min_gap(self):
        min_gap = []
        transposed_data = self.ori_all_data.transpose()
        for arr in transposed_data:
            arr_min = arr.min(initial=None)
            arr_max = arr.max(initial=None)
            arr_gap = arr_max - arr_min
            min_gap.append([arr_min, arr_gap])
        return np.array(min_gap)

    def add_vec(self, vec):
        self.ori_all_data = np.append(self.ori_all_data[1:], [vec], axis=0)


if __name__ == "__main__":
    dataloader = DataLoader("data/original/2020-03-03.csv")
    dataloader.add_vec(np.ones((158,)))
    x = dataloader.load_filtered_data()
    y = dataloader.load_norm_data()
    print(x.shape, y.shape)
    print(x[-1])
