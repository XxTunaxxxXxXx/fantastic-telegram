


#rawbyteexample = b"\x01\x00\x00\x00\x9c\x85\x1a\x00\xf6\xff\xf9E\xfb\x7f\x89D\x08\x80\x89D\xf7\x18\x84\xb7'\xb5;\xb7q4\x8d6\x81\xf9\xea7?4\xef6\xd9m\x8b7\xda\x80!8\xe0!.3\xd0\x14\x86\xb8\xc3-\xa7?\xbbZ\xf1\xba\x06JS<\xdfo\xfe>`D\xfc>|\xfa\x02?`\xf9\x01?(\x81;\xbd\xa9\xb75\xbd\xab\xdc\xe9<\xd9\xcc\xea<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9e\xec\x8c;\xcd\x9a\x8b;\x17\x81B;URH;\x86T<=\xac\x8d6=W\x1f\xeb<\xb2!\xec<\x006\xac\xb9\x00\xa6M\xba\x80\x16\xa4:\x00\x84Y:\x00\x06\x00\x00\x01\x00\x00\x00&\x02\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00r\x10\x9e\xc5\x81\xf12C)\x05\x88\xc3\x0e\xd9\x0b8\xf8\xf3\xba\xba\x83\xbdO\xb7\x18\xf4\xbfBj\xa5\xc7B.\xab\xc0B.\xab\xc0B33k\xc1\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00wU\xb1D\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00"

def parse(format, message, index):
    if format == "f32":
        return struct.unpack('<f',message[index:index+4])
    else: 
        return int.from_bytes(message[index:index+4],"little")

#the only byte index I have set correctly atm is carOrdinal due to the one I needed. 
#Just typed out rest to have it in place for later


def getIsRaceOn(data_in):#boolean
    return parse('s32', data_in, 0)
def getTimeStampMS(data_in): #int
    return parse('u32', data_in, 0)

def getEngineMaxRPM(data_in): #float
    return parse('f32', data_in, 0)
def getEngineIdleRPM(data_in): #float
    return parse('f32', data_in, 0)
def getEngineCurrentRPM(data_in): #float
    return parse('f32', data_in, 0)

def getAccelerationX(data_in): #float
    return parse('f32', data_in, 0)
def getAccelerationY(data_in): #float
    return parse('f32', data_in, 0)
def getAccelerationZ(data_in): #float
    return parse('f32', data_in, 0)

def getVelocityX(data_in): #float
    return parse('f32', data_in, 0)
def getVelocityY(data_in): #float
    return parse('f32', data_in, 0)
def getVelocityZ(data_in): #float
    return parse('f32', data_in, 0)

def getAngularVelocityX(data_in): #float
    return parse('f32', data_in, 0)
def getAngularVelocityY(data_in): #float
    return parse('f32', data_in, 0)
def getAngularVelocity(data_in): #float
    return parse('f32', data_in, 0)

def getYaw(data_in): #float
    return parse('f32', data_in, 0)
def getPitch(data_in): #float
    return parse('f32', data_in, 0)
def getRoll(data_in): #float
    return parse('f32', data_in, 0)

def getNormalizedSuspensionTravelFrontLeft(data_in): #float
    return parse('f32', data_in, 0)
def getNormalizedSuspensionTravelFrontRight(data_in): #float
    return parse('f32', data_in, 0)
def getNormalizedSuspensionTravelRearLeft(data_in): #float
    return parse('f32', data_in, 0)
def getNormalizedSuspensionTravelRearRight(data_in): #float
    return parse('f32', data_in, 0)

def getTireSlipRatioFrontLeft(data_in): #float
    return parse('f32', data_in, 0)
def getTireSlipRatioFrontRight(data_in): #float
    return parse('f32', data_in, 0)
def getTireSlipRatioRearLeft(data_in): #float
    return parse('f32', data_in, 0)
def getTireSlipRatioRearRight(data_in): #float
    return parse('f32', data_in, 0)

def getWheelRotationSpeedFrontLeft(data_in): #ffloat
    return parse('f32', data_in, 0)
def getWheelRotationSpeedFrontRight(data_in): #float
    return parse('f32', data_in, 0)
def getWheelRotationSpeedRearLeft(data_in): #float
    return parse('f32', data_in, 0)
def getWheelRotationSpeedRearRight(data_in): #float
    return parse('f32', data_in, 0)

def getWheelOnRumbleStripFrontLeft(data_in): #float
    return parse('s32', data_in, 0)
def getWheelOnRumbleStripFrontRight(data_in): #float
    return parse('s32', data_in, 0)
def getWheelOnRumbleStripRearLeft(data_in): #float
    return parse('s32', data_in, 0)
def getWheelOnRumbleStripRearRight(data_in): #float
    return parse('s32', data_in, 0)

def getWheelInPuddleDepthFrontLeft(data_in): #float
    return parse('f32', data_in, 0)
def getWheelInPuddleDepthFrontRight(data_in): #float
    return parse('f32', data_in, 0)
def getWheelInPuddleDepthRearLeft(data_in): #float
    return parse('f32', data_in, 0)
def getWheelInPuddleDepthRearRight(data_in): #float
    return parse('f32', data_in, 0)

def getSurfaceRumbleFrontLeft(data_in): #float
    return parse('f32', data_in, 0)
def getSurfaceRumbleFrontRight(data_in): #float
    return parse('f32', data_in, 0)
def getSurfaceRumbleRearLeft(data_in): #float
    return parse('f32', data_in, 0)
def getSurfaceRumbleRearRight(data_in): #float
    return parse('f32', data_in, 0)

def getTireSlipAngleFrontLeft(data_in): #float
    return parse('f32', data_in, 0)
def getTireSlipAngleFrontRight(data_in): #float
    return parse('f32', data_in, 0)
def getTireSlipAngleRearLeft(data_in): #float
    return parse('f32', data_in, 0)
def getTireSlipAngleRearRight(data_in): #float
    return parse('f32', data_in, 0)

def getSuspensionTravelMetersFrontLeft(data_in): #float
    return parse('f32', data_in, 0)
def getSuspensionTravelMetersFrontRight(data_in): #float
    return parse('f32', data_in, 0)
def getSuspensionTravelMetersRearLeft(data_in): #float
    return parse('f32', data_in, 0)
def getSuspensionTravelMetersRearRight(data_in): #float
    return parse('f32', data_in, 0)

def getCarOrdinal(data_in): #int
    return parse('s32', data_in, 212)
def getCarClass(data_in): #int 
    return parse('s32', data_in, 0)
def getCarPerformance(data_in): #int
    return parse('s32', data_in, 0)
def getDriveTrain(data_in): #int
    return parse('s32', data_in, 0)
def getNUmberOfCylinders(data_in): #int
    return parse('s32', data_in, 0)
def getCarCategory(data_in): #int
    return parse('s32', data_in, 0)
def getUnknown1(data_in): #int
    return parse('s32', data_in, 0)
def getUnknown2(data_in): #int
    return parse('s32', data_in, 0)

def getPositionX(data_in): #float
    return parse('f32', data_in, 0)
def getPositionY(data_in): #float
    return parse('f32', data_in, 0)
def getPositionZ(data_in): #float
    return parse('f32', data_in, 0)

def getSpeed(data_in): #float
    return parse('f32', data_in, 0)
def getPower(data_in): #float 
    return parse('f32', data_in, 0)
def getTorque(data_in): #float
    return parse('f32', data_in, 0)

def getTireTempFrontLeft(data_in): #float
    return parse('f32', data_in, 0)
def getTireTempFrontRight(data_in): #float
    return parse('f32', data_in, 0)
def getTireTempRearLeft(data_in): #float
    return parse('f32', data_in, 0)
def getTireTempRearRight(data_in): #float
    return parse('f32', data_in, 0)

def getBoost(data_in): #float
    return parse('f32', data_in, 0)
def getFuel(data_in): #float
    return parse('f32', data_in, 0)
def getDistanceTraveled(data_in): #float
    return parse('f32', data_in, 0)
def getBestLap(data_in): #float
    return parse('f32', data_in, 0)
def getLastLap(data_in): #float
    return parse('f32', data_in, 0)
def getCurrentLap(data_in): #float
    return parse('f32', data_in, 0)
def getLapNumber(data_in): #short? 
    return parse('u16', data_in, 0)

def getRacePosition(data_in): #byte?
    return parse('u8', data_in, 0)
def getAccel(data_in): #byte?
    return parse('u8', data_in, 0)
def getBrake(data_in): #byte?
    return parse('u8', data_in, 0)
def getClutch(data_in): #byte?
    return parse('u8', data_in, 0)
def getHandbrake(data_in): #byte
    return parse('u8', data_in, 0)
def getGear(data_in): #byte?
    return parse('u8', data_in, 0)
def getSteer(data_in): #byte?
    return parse('u8', data_in, 0)
def getNormalizedDrivingLine(data_in): #byte?
    return parse('s8', data_in, 0)
def getNormalizedAIBrakeDifference(data_in): #byte?
    return parse('s8', data_in, 0)























