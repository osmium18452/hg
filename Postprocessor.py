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

    def to_time_stamp(self, date):
        init_date = datetime(2020, 3, 2, 0, 0, 0)
        min = timedelta(minutes=1)
        return (date - init_date) / min

    def draw_fig(self, begin=0, end=522720, title="", vline_pos=None):
        plt.figure()
        plt.title(title)
        plt.plot(self.timestamp_log[0][begin:end], self.timestamp_log[1][begin:end])
        if vline_pos is not None:
            y_min=np.min(self.timestamp_log[1][begin:end])
            y_max = np.max(self.timestamp_log[1][begin:end])
            plt.vlines(vline_pos,y_min,y_max,linestyles='solid', colors='red',alpha=0.3,linewidth=5)
        plt.show()


if __name__ == "__main__":
    postprocessor = Postprocessor("log.txt")
    other_lof_score=postprocessor.timestamp_log[-1]
    lof_score=np.load("data/20200301lofscore.npy")
    all_lof_score=np.concatenate((lof_score,other_lof_score))
    np.save("data/all_lof_score.npy",all_lof_score)
    with open("data/all_lof_score.txt","w") as f:
        for i in all_lof_score:
            print("%.5f"%i,file=f)
    print(all_lof_score.shape)
    # print(other_lof_score)
    # print(lof_score)



    exit()
    postprocessor.draw_fig(114385 - 1440, 114385 + 1440, title="2020.5.20 10:25",vline_pos=114386)
    postprocessor.draw_fig(265505 - 1440, 265505 + 1440, title="2020.9.2 9:05",vline_pos=265506)
    postprocessor.draw_fig(395250 - 1440, 395250 + 1440, title="2020.12.1 11:30",vline_pos=395251)
    date1 = datetime(2020, 5, 20, 10, 25, 0)
    date2 = datetime(2020, 9, 2, 9, 5)
    date3 = datetime(2020, 12, 1, 11, 30)
    print(postprocessor.to_time_stamp(date1))
    print(postprocessor.to_time_stamp(date2))
    print(postprocessor.to_time_stamp(date3))
    # postprocessor.draw_fig()
    for i in range(len(postprocessor.timestamp_log[0])):
        if postprocessor.timestamp_log[1][i] > 10000:
            print(postprocessor.to_date(postprocessor.timestamp_log[0][i]), postprocessor.timestamp_log[1][i])
    # print (postprocessor.log[1][0].time())
    # print(np.sort(postprocessor.timestamp_log[1])[-100:])
    # for i in range(len(postprocessor.timestamp_log[0])):
    #     if postprocessor.timestamp_log[1][i] > 5000:
    #         print(i, postprocessor.to_date(i), postprocessor.timestamp_log[1][i])
