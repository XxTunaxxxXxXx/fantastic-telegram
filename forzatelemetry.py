import socket
import struct

def convertMillis(millis):
    seconds=round((millis/1000)%60,2)
    minutes=round((millis/(1000*60))%60)
    hours=round((millis/(1000*60*60))%24)
    return f'{hours}h:{minutes}m:{seconds}s'

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
    def __init__(self):
        self.data_out = []
        self.loop = False # outside variable for thread looping

    def dataRefresh(self, data_in): #get specified byte by index and size
        self.data_out = struct.unpack("iifffffffffffffffffffffffffffffffffffffffffffffffffffiiiiiiiifffffffffffffffffHbbbbbbbBbb", data_in)
        return self.data_out

    def getIsRaceOn(self):
        if self.data_out[0] == 0:
            return False
        if self.data_out[0] == 1:
            return True
    def getTimeStampMS(self): 
        return self.data_out[1]
    def getTimeStampConverted(self):
        return convertMillis(self.data_out[1]) #returns as {hours}h:{minutes}m:{seconds}s to be easier to read
    
    def getEngineMaxRPM(self): 
        return round(self.data_out[2])
    def getEngineIdleRPM(self): 
        return round(self.data_out[3])
    def getEngineCurrentRPM(self): 
        return round(self.data_out[4])

    #In the car's local space; X = right, Y = up, Z = forward
    def getAccelerationX(self): 
        return self.data_out[5]
    def getAccelerationY(self): 
        return self.data_out[6]
    def getAccelerationZ(self): 
        return self.data_out[8]

    #In the car's local space; X = right, Y = up, Z = forward
    def getVelocityX(self): 
        return self.data_out[8]
    def getVelocityY(self): 
        return self.data_out[9]
    def getVelocityZ(self): 
        return self.data_out[10]

    #In the car's local space; X = pitch, Y = yaw, Z = roll
    def getAngularVelocityX(self): 
        return self.data_out[11]
    def getAngularVelocityY(self): 
        return self.data_out[12]
    def getAngularVelocity(self): 
        return self.data_out[13]

    def getYaw(self): 
        return self.data_out[14]
    def getPitch(self): 
        return self.data_out[15]
    def getRoll(self): 
        return self.data_out[16]

    #Suspension travel normalized: 0.0f = max stretch; 1.0 = max compression
    def getNormalizedSuspensionTravelFrontLeft(self): 
        return self.data_out[17]
    def getNormalizedSuspensionTravelFrontRight(self): 
        return self.data_out[18]
    def getNormalizedSuspensionTravelRearLeft(self): 
        return self.data_out[19]
    def getNormalizedSuspensionTravelRearRight(self): 
        return self.data_out[20]

    #Tire normalized slip ratio, = 0 means 100% grip and |ratio| > 1.0 means loss of grip
    def getTireSlipRatioFrontLeft(self): 
        return self.data_out[21]
    def getTireSlipRatioFrontRight(self): 
        return self.data_out[22]
    def getTireSlipRatioRearLeft(self): 
        return self.data_out[23]
    def getTireSlipRatioRearRight(self): 
        return self.data_out[24]

    #Wheel rotation speed radians/sec.
    def getWheelRotationSpeedFrontLeft(self): 
        return self.data_out[25]
    def getWheelRotationSpeedFrontRight(self): 
        return self.data_out[26]
    def getWheelRotationSpeedRearLeft(self): 
        return self.data_out[27]
    def getWheelRotationSpeedRearRight(self): 
        return self.data_out[28]

    #1 when wheel is on rumble strip, = 0 when off.
    def getWheelOnRumbleStripFrontLeft(self): 
        return self.data_out[29]
    def getWheelOnRumbleStripFrontRight(self): 
        return self.data_out[30]
    def getWheelOnRumbleStripRearLeft(self): 
        return self.data_out[31]
    def getWheelOnRumbleStripRearRight(self): 
        return self.data_out[32]

    #from 0 to 1, where 1 is the deepest puddle
    def getWheelInPuddleDepthFrontLeft(self): 
        return self.data_out[33]
    def getWheelInPuddleDepthFrontRight(self): 
        return self.data_out[34]
    def getWheelInPuddleDepthRearLeft(self): 
        return self.data_out[35]
    def getWheelInPuddleDepthRearRight(self): 
        return self.data_out[36]

    #Non-dimensional surface rumble values passed to controller force feedback
    def getSurfaceRumbleFrontLeft(self): 
        return self.data_out[37]
    def getSurfaceRumbleFrontRight(self): 
        return self.data_out[38]
    def getSurfaceRumbleRearLeft(self): 
        return self.data_out[39]
    def getSurfaceRumbleRearRight(self): 
        return self.data_out[40]

    #Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    def getTireSlipAngleFrontLeft(self): 
        return self.data_out[41]
    def getTireSlipAngleFrontRight(self): 
        return self.data_out[42]
    def getTireSlipAngleRearLeft(self): 
        return self.data_out[43]
    def getTireSlipAngleRearRight(self): 
        return self.data_out[44]

    #Tire normalized combined slip, = 0 means 100% grip and |slip| > 1.0 means loss of grip.
    def getTireCombinedSlipFrontLeft(self): 
        return self.data_out[45]    
    def getTireCombinedSlipFrontRight(self): 
        return self.data_out[46]
    def getTireCombinedSlipRearLeft(self): 
        return self.data_out[47]
    def getTireCombinedSlipRearRight(self): 
        return self.data_out[48]

    #Actual suspension travel in meters
    def getSuspensionTravelMetersFrontLeft(self): 
        return self.data_out[49]
    def getSuspensionTravelMetersFrontRight(self): 
        return self.data_out[50]
    def getSuspensionTravelMetersRearLeft(self): 
        return self.data_out[51]
    def getSuspensionTravelMetersRearRight(self): 
        return self.data_out[52]

    def getCarOrdinal(self):        #Unique ID of the car make/model
        return self.data_out[53]
    def getCarClass(self):          #Between 0 (D -- worst cars) and 7 (X class -- best cars) inclusive
        return self.data_out[54]
    def getCarPerformance(self):    #Between 100 (slowest car) and 999 (fastest car) inclusive
        return self.data_out[55]
    def getDriveTrain(self):        #Corresponds to EDrivetrainType; 0 = FWD, 1 = RWD, 2 = AWD
        return self.data_out[56]
    def getNumberOfCylinders(self): #Number of cylinders in the engine
        return self.data_out[57]
    def getCarCategory(self):       #
        return self.data_out[58]
    def getUnknown1(self):          #
        return self.data_out[59]
    def getUnknown2(self):          #
        return self.data_out[60]

    #Position (meters) on map
    def getPositionX(self): 
        return self.data_out[61]
    def getPositionY(self): 
        return self.data_out[62]
    def getPositionZ(self): 
        return self.data_out[63]

    def getSpeed(self, unit='default'):             #meters per second by default
        if unit == 'mph':
            return 2.237*self.data_out[64]          #return as mph
        elif unit == 'kph':
            return  3.6*self.data_out[64]           #return as kph
        else: 
            return self.data_out[64]
    def getPower(self, unit='default'):             #watts by default
        if unit == 'hp':                            #return as horsepower
            return self.data_out[65]/746
        else:
            return self.data_out[65]
    def getTorque(self, unit='default'):            #newton meter by default
        if unit == 'ftlb':
            return self.data_out[66]/1.356          #return as foot pounds
        else:
            return self.data_out[66]                    

    #return as Farenheit
    def getTireTempFrontLeft(self): 
        return self.data_out[67]
    def getTireTempFrontRight(self): 
        return self.data_out[68]
    def getTireTempRearLeft(self): 
        return self.data_out[69]
    def getTireTempRearRight(self): 
        return self.data_out[70]

    def getBoost(self): 
        return self.data_out[71]
    def getFuel(self): 
        return self.data_out[72]
    def getDistanceTraveled(self): 
        return self.data_out[73]
    def getBestLapTime(self): 
        return self.data_out[74]
    def getLastLapTime(self): 
        return self.data_out[75]
    def getCurrentLapTime(self): 
        return self.data_out[76]
    def getCurrentRaceTime(self):
        return self.data_out[77]
    def getLap(self): 
        return self.data_out[78] 
    def getRacePosition(self): 
        return self.data_out[79]

    def getAccelerator(self):           #Gas pedal 0-255
        return self.data_out[80] 
    def getBrake(self):                 #brake pedal 0-255
        return self.data_out[81]
    def getClutch(self):                #clutch 0-255
        return self.data_out[82]
    def getHandbrake(self):             #handbrake 0-255
        return self.data_out[83]
    def getGear(self):
        return self.data_out[84]
    def getSteer(self):                 #full left = -127, full right = 127 
        return self.data_out[85]
    def getNormalizedDrivingLine(self): 
        return self.data_out[86]
    def getNormalizedAIBrakeDifference(self): 
        return self.data_out[87]