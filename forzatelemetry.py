import socket
import threading

#starts server process to listen to incoming udp data from Horizon 5
class ForzaListen():
    def __init__(self,port):
        self.port = port
        self.hostname = socket.gethostname()          
        self.local_ip = socket.gethostbyname(self.hostname)#local ip to be used in Forza (eg 192.168.1.17)
        self.loop = False

    def setLocalIp(self, local_ip): #if you need to use a different ip than gathered by gethostbyname
        self.local_ip = local_ip
    
    def start(self): #open socket to watch for udp data from horizon 5
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSock.bind((self.local_ip, self.port))
        print('\n[SERVER STARTING]\n[WAITING TO RECIEVE DATA]\n')

    def recieve(self):  #return raw byte data from UDP transmission
        self.data, self.addr = self.serverSock.recvfrom(323)
        return self.data



#takes data from ForzaListen to be available as telemtry output
class Telemetry():
    def __init__(self, data_in):
        self.data_in = data_in

    def dataRefresh(self, data_in):
        self.data_in = data_in

    def parse(self, format, index): # only index currently set is getCarOrdinal
        if format == "f32":
            return struct.unpack('<f',self.data_in[index:index+4])
        else: 
            return int.from_bytes(self.data_in[index:index+4],"little")

    def getIsRaceOn(self):#boolean
        return self.parse('s32', 0)
    def getTimeStampMS(self): #int
        return self.parse('u32', 0)

    def getEngineMaxRPM(self): #float
        return self.parse('f32', 0)
    def getEngineIdleRPM(self): #float
        return self.parse('f32', 0)
    def getEngineCurrentRPM(self): #float
        return self.parse('f32', 0)

    def getAccelerationX(self): #float
        return self.parse('f32', 0)
    def getAccelerationY(self): #float
        return self.parse('f32', 0)
    def getAccelerationZ(self): #float
        return self.parse('f32', 0)

    def getVelocityX(self): #float
        return self.parse('f32', 0)
    def getVelocityY(self): #float
        return self.parse('f32', 0)
    def getVelocityZ(self): #float
        return self.parse('f32', 0)

    def getAngularVelocityX(self): #float
        return self.parse('f32', 0)
    def getAngularVelocityY(self): #float
        return self.parse('f32', 0)
    def getAngularVelocity(self): #float
        return self.parse('f32', 0)

    def getYaw(self): #float
        return self.parse('f32', 0)
    def getPitch(self): #float
        return self.parse('f32', 0)
    def getRoll(self): #float
        return self.parse('f32', 0)

    def getNormalizedSuspensionTravelFrontLeft(self): #float
        return self.parse('f32', 0)
    def getNormalizedSuspensionTravelFrontRight(self): #float
        return self.parse('f32', 0)
    def getNormalizedSuspensionTravelRearLeft(self): #float
        return self.parse('f32', 0)
    def getNormalizedSuspensionTravelRearRight(self): #float
        return self.parse('f32', 0)

    def getTireSlipRatioFrontLeft(self): #float
        return self.parse('f32', 0)
    def getTireSlipRatioFrontRight(self): #float
        return self.parse('f32', 0)
    def getTireSlipRatioRearLeft(self): #float
        return self.parse('f32', 0)
    def getTireSlipRatioRearRight(self): #float
        return self.parse('f32', 0)

    def getWheelRotationSpeedFrontLeft(self): #ffloat
        return self.parse('f32', 0)
    def getWheelRotationSpeedFrontRight(self): #float
        return self.parse('f32', 0)
    def getWheelRotationSpeedRearLeft(self): #float
        return self.parse('f32', 0)
    def getWheelRotationSpeedRearRight(self): #float
        return self.parse('f32', 0)

    def getWheelOnRumbleStripFrontLeft(self): #float
        return self.parse('s32', 0)
    def getWheelOnRumbleStripFrontRight(self): #float
        return self.parse('s32', 0)
    def getWheelOnRumbleStripRearLeft(self): #float
        return self.parse('s32', 0)
    def getWheelOnRumbleStripRearRight(self): #float
        return self.parse('s32', 0)

    def getWheelInPuddleDepthFrontLeft(self): #float
        return self.parse('f32', 0)
    def getWheelInPuddleDepthFrontRight(self): #float
        return self.parse('f32', 0)
    def getWheelInPuddleDepthRearLeft(self): #float
        return self.parse('f32', 0)
    def getWheelInPuddleDepthRearRight(self): #float
        return self.parse('f32', 0)

    def getSurfaceRumbleFrontLeft(self): #float
        return self.parse('f32', 0)
    def getSurfaceRumbleFrontRight(self): #float
        return self.parse('f32', 0)
    def getSurfaceRumbleRearLeft(self): #float
        return self.parse('f32', 0)
    def getSurfaceRumbleRearRight(self): #float
        return self.parse('f32', 0)

    def getTireSlipAngleFrontLeft(self): #float
        return self.parse('f32', 0)
    def getTireSlipAngleFrontRight(self): #float
        return self.parse('f32', 0)
    def getTireSlipAngleRearLeft(self): #float
        return self.parse('f32', 0)
    def getTireSlipAngleRearRight(self): #float
        return self.parse('f32', 0)

    def getSuspensionTravelMetersFrontLeft(self): #float
        return self.parse('f32', 0)
    def getSuspensionTravelMetersFrontRight(self): #float
        return self.parse('f32', 0)
    def getSuspensionTravelMetersRearLeft(self): #float
        return self.parse('f32', 0)
    def getSuspensionTravelMetersRearRight(self): #float
        return self.parse('f32', 0)

    def getCarOrdinal(self): #int
        return self.parse('s32', 212)
    def getCarClass(self): #int 
        return self.parse('s32', 0)
    def getCarPerformance(self): #int
        return self.parse('s32', 0)
    def getDriveTrain(self): #int
        return self.parse('s32', 0)
    def getNUmberOfCylinders(self): #int
        return self.parse('s32', 0)
    def getCarCategory(self): #int
        return self.parse('s32', 0)
    def getUnknown1(self): #int
        return self.parse('s32', 0)
    def getUnknown2(self): #int
        return self.parse('s32', 0)

    def getPositionX(self): #float
        return self.parse('f32', 0)
    def getPositionY(self): #float
        return self.parse('f32', 0)
    def getPositionZ(self): #float
        return self.parse('f32', 0)

    def getSpeed(self): #float
        return self.parse('f32', 0)
    def getPower(self): #float 
        return self.parse('f32', 0)
    def getTorque(self): #float
        return self.parse('f32', 0)

    def getTireTempFrontLeft(self): #float
        return self.parse('f32', 0)
    def getTireTempFrontRight(self): #float
        return self.parse('f32', 0)
    def getTireTempRearLeft(self): #float
        return self.parse('f32', 0)
    def getTireTempRearRight(self): #float
        return self.parse('f32', 0)

    def getBoost(self): #float
        return self.parse('f32', 0)
    def getFuel(self): #float
        return self.parse('f32', 0)
    def getDistanceTraveled(self): #float
        return self.parse('f32', 0)
    def getBestLap(self): #float
        return self.parse('f32', 0)
    def getLastLap(self): #float
        return self.parse('f32', 0)
    def getCurrentLap(self): #float
        return self.parse('f32', 0)
    def getLapNumber(self): #short? 
        return self.parse('u16', 0)

    def getRacePosition(self): #byte?
        return self.parse('u8', 0)
    def getAccel(self): #byte?
        return self.parse('u8', 0)
    def getBrake(self): #byte?
        return self.parse('u8', 0)
    def getClutch(self): #byte?
        return self.parse('u8', 0)
    def getHandbrake(self): #byte
        return self.parse('u8', 0)
    def getGear(self): #byte?
        return self.parse('u8', 0)
    def getSteer(self): #byte?
        return self.parse('u8', 0)
    def getNormalizedDrivingLine(self): #byte?
        return self.parse('s8', 0)
    def getNormalizedAIBrakeDifference(self): #byte?
        return self.parse('s8', 0)

