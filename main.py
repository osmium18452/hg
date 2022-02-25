from Detector import Detector
import numpy as np
import argparse
from tqdm import tqdm
import os

test_data = np.load("data/testdata.npy")
detector = Detector("data/original/2020-03-01.csv")
cnt = 0
with tqdm(total=test_data.shape[0], ascii=True) as pbar:
    with open("log.txt","w") as f:
        for vec in test_data:
            cnt += 1
            pbar.update()
            result = detector.cal_lof(vec)
            detector.dataloader.add_vec(vec)
            print("time stamp: %9d, result:%.5f" % (cnt, result),file=f)
            if result > 1.5:
                pbar.set_postfix_str("%.5f" % result)
exit()

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
