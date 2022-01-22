import socket
import threading
import struct

#starts server process to listen to incoming udp data from Horizon 5
class ForzaListen():
    def __init__(self,port):
        self.port = port
        self.hostname = socket.gethostname()          
        self.local_ip = socket.gethostbyname(self.hostname)#local ip to be used in Forza (eg 192.168.1.17)

    def setLocalIp(self, local_ip): #if you need to use a different ip than gathered by gethostbyname
        self.local_ip = local_ip
    
    def start(self): #open socket to watch for udp data from horizon 5
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSock.bind((self.local_ip, self.port))
        print('\n[SERVER STARTING]\n[WAITING TO RECIEVE DATA]\n')

    def recieve(self):  #return raw byte data from UDP transmission
        self.data, self.addr = self.serverSock.recvfrom(324)
        return self.data

#takes data from ForzaListen to be available as telemtry output
class Telemetry():
    def dataRefresh(self, data_in):  #has to be ran prior to get to get live data
        self.data_in = data_in

    def parse(self, format, index, size): #get specified byte by index and size
        if format == "float":   
            return struct.unpack('<f',self.data_in[index:index+size])[0]
        else: 
            return int.from_bytes(self.data_in[index:index+size],"little")  
            
    def getIsRaceOn(self):
        return self.parse('int32', 0, 4)
    def getTimeStampMS(self): 
        return self.parse('int32', 4, 4)

    def getEngineMaxRPM(self): 
        return self.parse('float', 8, 4)
    def getEngineIdleRPM(self): 
        return self.parse('float', 12, 4)
    def getEngineCurrentRPM(self): 
        return self.parse('float', 16, 4)

    def getAccelerationX(self): 
        return self.parse('float', 20, 4)
    def getAccelerationY(self): 
        return self.parse('float', 24, 4)
    def getAccelerationZ(self): 
        return self.parse('float', 28, 4)

    def getVelocityX(self): 
        return self.parse('float', 32, 4)
    def getVelocityY(self): 
        return self.parse('float', 36, 4)
    def getVelocityZ(self): 
        return self.parse('float', 40, 4)

    def getAngularVelocityX(self): 
        return self.parse('float', 44, 4)
    def getAngularVelocityY(self): 
        return self.parse('float', 48, 4)
    def getAngularVelocity(self): 
        return self.parse('float', 52, 4)

    def getYaw(self): 
        return self.parse('float', 56, 4)
    def getPitch(self): 
        return self.parse('float', 60, 4)
    def getRoll(self): 
        return self.parse('float', 64, 4)

    def getNormalizedSuspensionTravelFrontLeft(self): 
        return self.parse('float', 68, 4)
    def getNormalizedSuspensionTravelFrontRight(self): 
        return self.parse('float', 72, 4)
    def getNormalizedSuspensionTravelRearLeft(self): 
        return self.parse('float', 76, 4)
    def getNormalizedSuspensionTravelRearRight(self): 
        return self.parse('float', 80, 4)

    def getTireSlipRatioFrontLeft(self): 
        return self.parse('float', 84, 4)
    def getTireSlipRatioFrontRight(self): 
        return self.parse('float', 88, 4)
    def getTireSlipRatioRearLeft(self): 
        return self.parse('float', 92, 4)
    def getTireSlipRatioRearRight(self): 
        return self.parse('float', 96, 4)

    def getWheelRotationSpeedFrontLeft(self): 
        return self.parse('float', 100, 4)
    def getWheelRotationSpeedFrontRight(self): 
        return self.parse('float', 104, 4)
    def getWheelRotationSpeedRearLeft(self): 
        return self.parse('float', 108, 4)
    def getWheelRotationSpeedRearRight(self): 
        return self.parse('float', 112, 4)

    def getWheelOnRumbleStripFrontLeft(self): 
        return self.parse('float', 116, 4)
    def getWheelOnRumbleStripFrontRight(self): 
        return self.parse('float', 120, 4)
    def getWheelOnRumbleStripRearLeft(self): 
        return self.parse('float', 124, 4)
    def getWheelOnRumbleStripRearRight(self): 
        return self.parse('float', 128, 4)

    def getWheelInPuddleDepthFrontLeft(self): 
        return self.parse('float', 132, 4)
    def getWheelInPuddleDepthFrontRight(self): 
        return self.parse('float', 136, 4)
    def getWheelInPuddleDepthRearLeft(self): 
        return self.parse('float', 140, 4)
    def getWheelInPuddleDepthRearRight(self): 
        return self.parse('float', 144, 4)

    def getSurfaceRumbleFrontLeft(self): 
        return self.parse('float', 148, 4)
    def getSurfaceRumbleFrontRight(self): 
        return self.parse('float', 152, 4)
    def getSurfaceRumbleRearLeft(self): 
        return self.parse('float', 156, 4)
    def getSurfaceRumbleRearRight(self): 
        return self.parse('float', 160, 4)

    def getTireSlipAngleFrontLeft(self): 
        return self.parse('float', 164, 4)
    def getTireSlipAngleFrontRight(self): 
        return self.parse('float', 168, 4)
    def getTireSlipAngleRearLeft(self): 
        return self.parse('float', 172, 4)
    def getTireSlipAngleRearRight(self): 
        return self.parse('float', 176, 4)

    def getTireCombinedSlipFrontLeft(self): 
        return self.parse('float', 180, 4)    
    def getTireCombinedSlipFrontRight(self): 
        return self.parse('float', 184, 4)
    def getTireCombinedSlipRearLeft(self): 
        return self.parse('float', 188, 4)
    def getTireCombinedSlipRearRight(self): 
        return self.parse('float', 192, 4)

    def getSuspensionTravelMetersFrontLeft(self): 
        return self.parse('float', 196, 4)
    def getSuspensionTravelMetersFrontRight(self): 
        return self.parse('float', 200, 4)
    def getSuspensionTravelMetersRearLeft(self): 
        return self.parse('float', 204, 4)
    def getSuspensionTravelMetersRearRight(self): 
        return self.parse('float', 208, 4)

    def getCarOrdinal(self): 
        return self.parse('uint8', 212, 4)
    def getCarClass(self):  
        return self.parse('uint8', 216, 4)
    def getCarPerformance(self): 
        return self.parse('uint8', 220, 4)
    def getDriveTrain(self): 
        return self.parse('uint8', 224, 4)
    def getNUmberOfCylinders(self): 
        return self.parse('uint8', 228, 4)
    def getCarCategory(self): 
        return self.parse('uint8', 232, 4)
    def getUnknown1(self): 
        return self.parse('ignore',236, 4)
    def getUnknown2(self): 
        return self.parse('ignore', 240, 4)

    def getPositionX(self): 
        return self.parse('float', 244, 4)
    def getPositionY(self): 
        return self.parse('float', 248, 4)
    def getPositionZ(self): 
        return self.parse('float', 252, 4)

    def getSpeed(self): 
        return self.parse('float', 256, 4)
    def getPower(self):  
        return self.parse('float', 260, 4)
    def getTorque(self): 
        return self.parse('float', 264, 4)

    def getTireTempFrontLeft(self): 
        return self.parse('float', 268, 4)
    def getTireTempFrontRight(self): 
        return self.parse('float', 272, 4)
    def getTireTempRearLeft(self): 
        return self.parse('float', 276, 4)
    def getTireTempRearRight(self): 
        return self.parse('float', 280, 4)

    def getBoost(self): 
        return self.parse('float', 284, 4)
    def getFuel(self): 
        return self.parse('float', 288, 4)
    def getDistanceTraveled(self): 
        return self.parse('float', 292, 4)
    def getBestLapTime(self): 
        return self.parse('float', 296, 4)
    def getLastLapTime(self): 
        return self.parse('float', 300, 4)
    def getCurrentLapTime(self): 
        return self.parse('float', 304, 4)
    def getLap(self): 
        return self.parse('uint16', 308, 2) 

    def getRacePosition(self): 
        return self.parse('uint8', 314, 1)
    def getAccelerator(self): 
        return self.parse('uint8', 315, 1) 
    def getBrake(self): 
        return self.parse('uint8', 316, 1)
    def getClutch(self): 
        return self.parse('uint8', 317, 1)
    def getHandbrake(self): 
        return self.parse('uint8', 318, 1)
    def getGear(self): 
        return self.parse('uint8', 319, 1)
    def getSteer(self): 
        return self.parse('uint8', 320, 1)
    def getNormalizedDrivingLine(self): 
        return self.parse('uint8', 321, 1)
    def getNormalizedAIBrakeDifference(self): 
        return self.parse('uint8', 322, 1)