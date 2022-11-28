from PIL import Image
import math


def ReLU(x):
    if x > 0:
        return x
    else:
        return 0

class Network_221:
    def __init__(self, network_info):
        network_info_example = ['C_Bias', 'D_Bias', 'E_Bias'
                                                    'A-C_Weight', 'A-D_Weight', 'B-C_Weight', 'B-D_Weight',
                                'C-E_Weight', 'D-E_Weight']
        self.network_info = network_info
        self.net = []

    def test_network(self, A_interval, B_interval):
        out = []
        A_intervals = []
        if A_interval > 0:
            interval_size = 1 / A_interval
            val = 0 - interval_size
            A_interval += 1
            for i in range(A_interval):
                val += interval_size
                A_intervals.append(val)
        B_intervals = []
        if B_interval > 0:
            interval_size = 1 / B_interval
            val = 0 - interval_size
            B_interval += 1
            for i in range(B_interval):
                val += interval_size
                B_intervals.append(val)

        for a_val in A_intervals:
            for b_val in B_intervals:
                C = a_val * self.network_info[3]
                C += b_val * self.network_info[5]
                C += self.network_info[0]
                C = ReLU(C)

                D = a_val * self.network_info[4]
                D += b_val * self.network_info[6]
                D += self.network_info[1]
                D = ReLU(D)

                E = C * self.network_info[7]
                E += D * self.network_info[8]
                E += self.network_info[2]
                E = ReLU(E)

                self.net.append([a_val, b_val, E])
                out.append([f'A : {a_val}', f'B : {b_val}', f'C : {C}', f'D : {D}', f'E : {E}'])

        return out

    def disp_network(self):
        side_len = math.sqrt(len(self.net))
        if side_len == math.floor(side_len):
            out = Image.new("RGB", (int(side_len) + 1, int(side_len) + 1))
            max = 0
            for i in self.net:
                if i[2] > max:
                    max = i[2]

            pixel_map = out.load()
            for i in self.net:
                color = round(i[2] * (255/max))
                print(i, color)
                print(round(i[0] * side_len), round(i[1] * side_len))
                pixel_map[round(i[0] * side_len), side_len - round(i[1] * side_len)] = (color, color, color)
            out.show("Out")