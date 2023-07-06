import time
import math

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=0):
    if not stream:
        stream=EvenStream()
    for _ in range(n):
            print(stream.get_next())


def importdata(file):
    list_ = open(file).read().split()
    return list_

if __name__ == '__main__':
    start_time = time.time()
    #s=importdata(r'C:\Users\witol\Documents\Computing\HackerRank\input09.txt')
    #k=int(s[1])
    #del s[0:2]
    #s=list(map(int, s))

    #temp = '61197933 56459859 319018589 271720536 358582070 849720202 481165658 675266245 541667092 615618805 129027583 755570852 437001718 86763458 791564527 163795318 981341013 516958303 592324531 611671866 157795445 718701842 773810960 72800260 281252802 404319361 757224413 682600363 606641861 986674925 176725535 256166138 827035972 124896145 37969090 136814243 274957936 980688849 293456190 141209943 346065260 550594766 132159011 491368651 3772767 131852400 633124868 148168785 339205816 705527969 551343090 824338597 241776176 286091680 919941899 728704934 37548669 513249437 888944501 239457900 977532594 140391002 260004333 911069927 586821751 113740158 370372870 97014913 28011421 489017248 492953261 73530695 27277034 570013262 81306939 519086053 993680429 599609256 639477062 677313848 950497430 672417749 266140123 601572332 273157042 777834449 123586826'
    #temp='1 2 7 4'
    temp='1 2 3 4 5 6 7 8 9 10'
    #temp='278 576 496 727 410 124 338 149 209 702 282 718 771 575 436'
    #temp='576 496 727 410 338 149 209 702 282 718 575 436'

    s = importdata(r'D:\Witold\Documents\Computing\HackerRank\PythonDebug\input.txt')
    k=int(s[0])
    del s[0]
    #z=list((stream_name, n) for x in (x.split() for x in s))
    #stream_name = s[::2]
    #stream_name = s[1::2]
    for _ in range(0, len(s), 2):
        stream_name = s[_]
        n = int(s[_+1])
        if stream_name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())

    # s=list(map(int, temp.split(' ')))
    #
    # result = nonDivisibleSubset5(k, s)
    #
    # #result=combinations('ABCD',2)
    # print(result)
    print("--- %s seconds ---" % (round(time.time() - start_time, 2)))