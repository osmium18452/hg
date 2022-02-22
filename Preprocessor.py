import os
from tqdm import tqdm

import numpy as np


class Preprocessor:
    def __init__(self, filename):
        self.original_data = []
        with open(filename, "r") as f:
            for line in f.readlines():
                if not line[0] == "t":
                    self.original_data.append(list(map(float, line.strip().split(","))))
        self.original_data = np.array(self.original_data).transpose()
        for i in range(len(self.original_data)):
            pass

    def save_as_npy(self, filename):
        np.save(filename, self.original_data)

    def save_as_csv(self, filename):
        with open(filename, "w") as f:
            for line in self.original_data:
                for i in range(len(line)):
                    if i < len(line - 1):
                        print(i, file=f, end=",")
                    else:
                        print(i, file=f)


if __name__ == "__main__":
    pathname = r"data/original"
    all_data = []
    for path, dirs, files in os.walk(pathname):
        sorted_files=np.sort(files)
        with tqdm(total=len(files), ascii=True, postfix="") as pbar:
            for file in sorted_files:
                pbar.set_postfix_str(file)
                with open(os.path.join("data/original", file)) as f:
                    for line in f.readlines():
                        if not line[0] == "t":
                            all_data.append(list(map(float, line.strip().split(","))))
                pbar.update()
    all_data=np.array(all_data).transpose()[1:].transpose()
    test_data=all_data[1440:]
    np.save("data/testdata.npy",test_data)
    np.save("data/all_data.npy",all_data)
    print(all_data.shape,test_data.shape)
