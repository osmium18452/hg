from Detector import Detector
import numpy as np
import argparse
from tqdm import tqdm
import os

from sklearn.neighbors import LocalOutlierFactor

all_data = []
with open("data/original/2020-03-01.csv", "r") as f:
    for line in f.readlines():
        if not line[0] == "t":
            all_data.append(list(map(float, line.strip().split(","))))

all_data = np.array(all_data).transpose()
lof_data = []
for line in all_data:
    line_max = np.max(line)
    line_min = np.min(line)
    # print(line_max - line_min)
    if line_max - line_min > 0.001:
        lof_data.append((line - line_min) / (line_max - line_min))
lof_data=np.array(lof_data).transpose()
clf=LocalOutlierFactor()
clf.fit_predict(lof_data)
outlier_factor=clf.negative_outlier_factor_*-1
np.save("data/20200301lofscore.npy",outlier_factor)
# other_outlier_factor=np.load("data/lof_score.npy")
# print(other_outlier_factor.shape)

exit()

test_data = np.load("data/testdata.npy")
detector = Detector("data/original/2020-03-01.csv")
cnt = 0
with tqdm(total=test_data.shape[0], ascii=True) as pbar:
    with open("log.txt", "w") as f:
        for vec in test_data:
            cnt += 1
            pbar.update()
            result = detector.cal_lof(vec)
            detector.dataloader.add_vec(vec)
            print("time stamp: %9d, result:%.5f" % (cnt, result), file=f)
            if result > 1.5:
                pbar.set_postfix_str("%.5f" % result)

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str,
                    default=r"C:/Users/mista/PycharmProjects/huagong/data/original/2020-03-03.csv")
args = parser.parse_args()

detector = Detector(args.filename)

while True:
    line = input()
    if line == "exit":
        exit()
    vec = np.array(list(map(float, line.strip().split(","))))
    detector.detect(vec)

# 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
