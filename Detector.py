import numpy as np

from DL import DataLoader
from sklearn.neighbors import LocalOutlierFactor


class Detector:
    def __init__(self, filename):
        self.dataloader = DataLoader(filename)

    def cal_lof(self, vec):
        norm_data = self.dataloader.load_norm_data()
        min_gap = self.dataloader.load_min_gap()
        norm_vec = []
        for i in range(158):
            if min_gap[i][1] != 0:
                norm_vec.append((vec[i] - min_gap[i][0]) / min_gap[i][1])
        norm_vec = np.array([norm_vec])
        lof_data = np.append(norm_data, norm_vec, axis=0)
        clf = LocalOutlierFactor()
        clf.fit_predict(lof_data)
        return -clf.negative_outlier_factor_[-1]

    def detect(self, vec, alpha=1.5):
        result = self.cal_lof(vec)
        if result > alpha:
            print("abnormal detected.")
        else:
            self.dataloader.add_vec(vec)


if __name__ == "__main__":
    detector = Detector("data/original/2020-03-01.csv")
    test_vec = [0.4784816802, 8.9906406403, 10.3044052124, 13.2327795029, 19.1111812592, 31.8610610962, 10.0203638077,
                2.6406121254, 1.232784152, 8.2557468414, 0.3826809227, 9.0958042145, 12.0, 12.0, 700.0, 740.5,
                0.5165616274, 0.497658968, 0.4873544872, 0.5239039063, 0.565318346, 1200.0, 3447.9465332031,
                3756.9077148438, 3310.0432128906, 3003.2619628906, 1789.5577392578, 1908.1804199219, 1811.4333496094,
                1766.2430419922, 11825.8955078125, 12486.611328125, 17641.826171875, 640.4683837891, 15799.1103515625,
                1398.7619628906, 709.1765136719, -1.7174036503, 13518.4619140625, 6984.1977539062, 3447.9440917969,
                3756.9077148438, 3310.0275878906, 3003.2585449219, 1719.3493652344, 1833.337890625, 1740.4241943359,
                1696.9521484375, 1206.1491699219, 560.9344482422, 1.764051795, 0.1176360771, 1.6717302799, 2.8788003922,
                0.0, 3440.5539550781, 0.0, 3303.5471191406, 3000.5471191406, 1770.7722167969, 1861.4984130859,
                1810.9974365234, 1758.4298095703, 15310.5615234375, 100.0, 64.182762146, 100.0, 79.6285705566,
                13518.4619140625, 0.5166423917, 53.0701980591, 36.7637214661, 59.4674263, 67.8163452148, 56.4612312317,
                48.0090866089, 66.2219619751, 56.4612312317, 95.3553314209, 0.0179711003, 0.0328527987, -0.00726825,
                -0.0511906594, 0.5158573389, 68.2730712891, 375.1807861328, -61.7269287109, -381.7269287109,
                -0.4011477828, 0.2197336257, 0.1215571091, 0.2922704518, -54.309967041, -56.1528434753, -46.6847991943,
                0.5676493645, 0.7267109156, 0.2858230472, 0.2875634432, 0.2830244601, 0.2597535551, -0.00030679,
                -0.00061722, 0.0851546824, 0.0851831511, 0.1221671626, 0.1225500107, 0.122258611, 0.0868671089,
                0.0712954476, -53.9035339355, 11.3975887299, 0.1222466901, 0.1222466901, 0.0866356269, 0.0866356269,
                86.9499511719, 71.9847717285, 0.1222466901, 515.3182373047, 576.3061523438, 579.8001098633,
                578.4520263672, 574.1005859375, 377.0616760254, 374.746673584, 215.20362854, 48.9751052856,
                980.5055541992, 1025.0687255859, 958.0111083984, 370.4786682129, 106.3240814209, 856.043762207,
                856.8104858398, 856.5881958008, 857.7528076172, 254.6856536865, 189.7446594238, 400.6804199219,
                401.7689208984, 402.9701843262, 413.2763366699, 371.5738220215, 369.4096374512, 471.7105712891,
                859.3872680664, 859.4057006836, 859.6556396484, 859.9738769531, 859.6556396484, 472.6930541992,
                859.3872680664, 859.4057006836, 859.6556396484, 859.9738769531, 371.9176940918, 369.2017211914]
    print(detector.cal_lof(test_vec))
    detector.detect(np.ones((158,)))
    detector.detect(test_vec)
