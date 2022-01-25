from Detector import Detector
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str,
                    default=r"C:/Users/mista/PycharmProjects/huagong/data/original/2020-03-03.csv")
args=parser.parse_args()

detector = Detector(args.filename)

while True:
    line = input()
    if line == "exit":
        exit()
    vec = np.array(list(map(float, line.strip().split(","))))
    detector.detect(vec)

# 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1