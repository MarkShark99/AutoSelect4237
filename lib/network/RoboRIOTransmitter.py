import socket, threading, time

class RoboRIOTransmitter():

    def __init__(self, IP):
        self.ROBOT_IP = IP
        self.ROBOT_PORT = 5804


    def sendMessage(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         
        print(message)
        try:
            s.connect((self.ROBOT_IP, self.ROBOT_PORT))
            s.sendall(message)
            print("Successfully sent message")
        except Exception as e:
            s.close()
            print(e)