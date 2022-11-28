import pyximport; pyximport.install()
import Neurel_Network_Calculator_221

Network = Neurel_Network_Calculator_221.Network_221([0, 0, 0, 1, 1, -1, 1, -1, 1])
Network.test_network(100, 100)
Network.disp_network()