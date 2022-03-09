from sklearn.neighbors import LocalOutlierFactor
import numpy as np
import matplotlib.pyplot as plt


lof_score=np.load("data/lof_score.npy")*-1
# print(lof_score.size)
plt.figure()
plt.plot(range(lof_score.size),lof_score)
plt.show()

exit()
all_data = np.load("data/all_data.npy")
all_data = all_data.transpose()
lof_data = []
for line in all_data:
    line_max = np.max(line)
    line_min = np.min(line)
    # print(line_max - line_min)
    if line_max - line_min > 0.001:
        lof_data.append((line - line_min) / (line_max - line_min))
lof_data = np.array(lof_data).transpose()
print(lof_data.shape)

clf = LocalOutlierFactor()
clf.fit_predict(lof_data)
lof_score=clf.negative_outlier_factor_
np.save("data/lof_score.npy",lof_score)
