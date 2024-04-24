from twisted.internet.protocol import DatagramProtocol


class DanteControl(DatagramProtocol):
    """
    Handle UDP communicatio
    """
    def __init__(self, host, port):
        """
        Init host and port adress

        Parameters:
        ----------
        host : ip_adress
            IP adress of the host
        port : int
            Port of the communication
        """
        self.host = host
        self.port = port

    def startProtocol(self):
        """
        Start the UDP protocol
        """
        self.transport.connect(self.host, self.port)

    def sendMessage(self, data):
        """
        Send a message over the network

        Parameters:
        -----------
        data : UDP packet
            UDP packet that is send
        """
        self.transport.write(data)

    def datagramReceived(self, datagram, addr):
        pass
