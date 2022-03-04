import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta


class Postprocessor:
    def __init__(self, filename):
        with open(filename, "r") as f:
            self.log = []
            self.timestamp_log = []
            for line in f.readlines():
                self.log.append([self.to_date(int(line.strip().split(",")[0].split(":")[1].strip())),
                                 float(line.strip().split(",")[1].split(":")[1])])
                self.timestamp_log.append([int(line.strip().split(",")[0].split(":")[1].strip()),
                                           float(line.strip().split(",")[1].split(":")[1])])
        self.timestamp_log = np.array(self.timestamp_log).transpose()
        self.ln_log = np.array([self.timestamp_log[0], np.log(self.timestamp_log[1])])

    def print_log(self):
        for line in self.log:
            print(line[0], line[1])

    def to_date(self, time_stamp=0):
        init_date = datetime(2020, 3, 2, 0, 0, 0)
        min = timedelta(minutes=time_stamp)
        return init_date + min

    def draw_fig(self):
        plt.figure()
        plt.plot(self.timestamp_log[0], self.ln_log[1])
        plt.show()


if __name__ == "__main__":
    postprocessor = Postprocessor("log.txt")
    for i in range(len(postprocessor.timestamp_log[0])):
        if postprocessor.timestamp_log[1][i]>10000:
            print(postprocessor.timestamp_log[0][i],postprocessor.timestamp_log[1][i])
    # postprocessor.draw_fig()
    # print (postprocessor.log[1][0].time())
    # print(np.sort(postprocessor.timestamp_log[1])[-100:])
    # for i in range(len(postprocessor.timestamp_log[0])):
    #     if postprocessor.timestamp_log[1][i] > 5000:
    #         print(i, postprocessor.to_date(i), postprocessor.timestamp_log[1][i])
