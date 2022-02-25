import numpy as np
from datetime import datetime, timedelta


class Postprocessor:
    def __init__(self, filename):
        with open(filename, "r") as f:
            self.log = []
            self.timestamp_log=[]
            for line in f.readlines():
                self.log.append([self.to_date(int(line.strip().split(",")[0].split(":")[1].strip())),
                                 float(line.strip().split(",")[1].split(":")[1])])
                self.timestamp_log.append([int(line.strip().split(",")[0].split(":")[1].strip()),
                                 float(line.strip().split(",")[1].split(":")[1])])

    def print_log(self):
        for line in self.log:
            print(line[0],line[1])

    def to_date(self, time_stamp=0):
        init_date = datetime(2020, 3, 2, 0, 0, 0)
        min = timedelta(minutes=time_stamp)
        return init_date + min


if __name__ == "__main__":
    postprocessor = Postprocessor("log.txt")
    postprocessor.print_log()
    # print(int(line.strip().split(",")[0].split(":")[1].strip()))
    # print(float(line.strip().split(",")[1].split(":")[1]))
