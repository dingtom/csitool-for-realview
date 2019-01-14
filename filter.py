# --coding: utf-8 --
import pywt
from scipy import signal

class Filter():
    def __init__(
            self,
            sequence):
        self.sequence = sequence

    def feedback(self):
        w = pywt.Wavelet('coif7')
        a = self.sequence
        ca, cd = [], []
        for i in range(3):
            (a, d) = pywt.dwt(a, w)
            ca.append(a)
            cd.append(d)

        rec_a, rec_d = [], []
        for i, coeff in enumerate(ca):
            coeff_list = [coeff, None] + [None] * i
            rec_a.append(pywt.waverec(coeff_list, w))

        for i, coeff in enumerate(cd):
            coeff_list = [None, coeff] + [None] * i
            rec_d.append(pywt.waverec(coeff_list, w))

        return  rec_a[-1]

    def butterWorth(self):
        b, a = signal.butter(3, 0.3, 'low')
        sf = signal.filtfilt(b, a, self.sequence)
        return sf

if __name__ =="__main__":
    import display
    raw, dwt,_,_ = display.date_wrapper()
    print raw[0]
    A = Filter(raw[0])
    print len(A.feedback())


    # fig = plt.figure()
    # ax_main = fig.add_subplot(len(rec_a) + 1, 1, 1)
    # ax_main.set_title(title)
    # ax_main.plot(data)
    # ax_main.set_xlim(0, len(data) - 1)
    #
    # for i, y in enumerate(rec_a):
    #     ax = fig.add_subplot(len(rec_a) + 1, 2, 3 + i * 2)
    #     ax.plot(y, 'r')
    #     ax.set_xlim(0, len(y) - 1)
    #     ax.set_ylabel("A%d" % (i + 1))
    #
    # for i, y in enumerate(rec_d):
    #     ax = fig.add_subplot(len(rec_d) + 1, 2, 4 + i * 2)
    #     ax.plot(y, 'g')
    #     ax.set_xlim(0, len(y) - 1)
    #     ax.set_ylabel("D%d" % (i + 1))