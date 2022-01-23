#Telemetry server for using the data out option in Forza Horizon 5.  
#Not all formatted options have been throughly tested yet, but all default outputs are correct.
#
#
#quick example of use
#forzaData = Telemetry()
#forzaData.startServer(5300) - whatever valid port number will work 
#forzaData.dataRefresh()  - Will only refresh data a single time, if you're just doing a quick single data pull 
#print (forzaData.getCarOrdinal())
#
#forzaData.dataLoop() will set a background thread to loop data updates constantly
#set self.loop = False to end loop. Don't set to True outside of thread.
#

import socket
import struct
import csv 
import threading

#random null byte for testing
#initbyte =  b"\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

def convertMillis(millis):          #for timestampms readout
    seconds=round((millis/1000)%60,2)
    minutes=round((millis/(1000*60))%60)
    hours=round((millis/(1000*60*60))%24)
    return f'{hours}h:{minutes}m:{seconds}s'

name_list = [   #for logging
    #Race, time, and RPM info
    "is_race_on","time_stamp","max_rpm","idle_rpm","current_rpm",
    #Acceleration in 3 axes
     "x_accel","y_accel","z_accel",
    #Velocity in 3 axes
     "x_velocity","y_velocity","z_velocity",
    #Angular Velocity in 3 axes
     "x_ang_velocity","y_ang_velocity","z_ang_velocity",
    #Rotation
     "yaw","pitch","roll",
     #suspension
     "suspension_travel_front_left","suspension_travel_front_right","suspension_travel_rear_left","suspension_travel_rear_right",
     #tireslip
     "tire_slip_ratio_front_left","tire_slip_ratio_front_right","tire_slip_ratio_rear_left","tire_slip_ratio_rear_right",
     #wheelspeed
     "wheel_speed_front_left","wheel_speed_front_right","wheel_speed_rear_left","wheel_speed_rear_right",
     #wheelrumble
     "wheel_rumblestrip_speed_front_left","wheel_rumblestrip_speed_front_right","wheel_rumblestrip_speed_rear_left","wheel_rumblestrip_speed_rear_right",
    #WHEEL IN PUDDLE DEPTH#
     "wheel_in_puddle_depth_front_left","wheel_in_puddle_depth_front_right","wheel_in_puddle_depth_rear_left","wheel_in_puddle_depth_rear_right",
    #SURFACE RUMBLE#
     "surface_rumble_front_left","surface_rumble_front_right","surface_rumble_rear_left","surface_rumble_rear_right",
    #TIRE SLIP ANGLE#
     "tire_slip_angle_front_left","tire_slip_angle_front_right","tire_slip_angle_rear_left","tire_slip_angle_rear_right",
    #TIRE COMBINED SLIP#
     "tire_combined_slip_front_left","tire_combined_slip_front_right","tire_combined_slip_rear_left","tire_combined_slip_rear_right",
    #SUSPENSION TRAVEL METERS#
     "suspension_travel_meters_front_left","suspension_travel_meters_front_right","suspension_travel_meters_rear_left","suspension_travel_meters_rear_right",
    #VEHICLE STATS#
     "car_ordinal","car_class","car_pi","drivetrain","num_cylinders","car_category","unknown_1","unknown_2",
    #POSITION AXIS#
     "x_position","y_position","z_position",
    #VEHICLE ENGINE STATS#
     "engine_speed","engine_power","engine_torque",
    #TIRE TEMP#
     "tire_temp_front_left","tire_temp_front_right","tire_temp_rear_left","tire_temp_rear_right",
    #RACE STATS#
     "boost","fuel","distance_traveled","best_lap","last_lap","current_lap","current_race_time","lap_num","race_position",
    #MISC#
     "accelerator_position","brake_position","clutch_position","handbrake_position","gear","steering_position","driving_line","ai_brake_difference",
    ]

class Telemetry():
    def __init__(self):
        self.loop = False #variable for thread looping     
        self.hostname = socket.gethostname()          
        self.local_ip = socket.gethostbyname(self.hostname)#local ip to be used in Forza (eg 192.168.1.17)
    
    def setLocalIP(self,ip_address): #if for some reason ip set by gethostname doesn't work
        self.local_ip = ip_address 

    def startServer(self, port):
        self.port = port
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSock.bind((self.local_ip, self.port))
        print('[SERVER STARTING]\n[WAITING TO RECIEVE DATA]')
        self.dataRefresh()
        
    def dataRefresh(self): #get specified byte by index and size
        self.data_in, self.addr =  self.serverSock.recvfrom(324) #return raw byte data from UDP transmission
        self.data_out = struct.unpack("iifffffffffffffffffffffffffffffffffffffffffffffffffffiiiiiiiifffffffffffffffffHbbbbbbbBbb", self.data_in)
        if self.loop == True:
            while self.loop == True:
                self.data_in, self.addr = self.serverSock.recvfrom(324) #return raw byte data from UDP transmission
                self.data_out = struct.unpack("iifffffffffffffffffffffffffffffffffffffffffffffffffffiiiiiiiifffffffffffffffffHbbbbbbbBbb", self.data_in)
        return

    def dataLoop(self): #loop data refresh set self.loop = False to end
        self.loop = True
        self.thread = threading.Thread(target=self.dataRefresh, daemon=True)
        self.thread.start()
        return

    def dataLog(self, filename='log.csv'):       #save incomming data to log
        d = dict(zip(name_list,self.data_out))
        #not finished
        return

    def getIsRaceOn(self):                 #returns 0 if false, 1 if true
        if self.data_out[0] == 0:
            return False
        elif self.data_out[0] == 1:
            return True
    def getTimeStampMS(self, unit='default'): #returns a timestamp in miliseconds
        if unit == 'formatted':
            return convertMillis(self.data_out[1]) #returns as {hours}h:{minutes}m:{seconds}s to be easier to read
        elif unit == 'default':
            return self.data_out[1]
        else:
            return 'Null'
    
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
    #formatted returns output at 0-100%
    def getNormalizedSuspensionTravelFrontLeft(self, unit='default'): 
        if unit == 'formatted':
            unit = f'{round(self.data_out[17]*100,2)}%'
            return unit
        elif unit == 'default':
            return self.data_out[17]
    def getNormalizedSuspensionTravelFrontRight(self, unit='default'): 
        if unit == 'formatted':
            unit = f'{round(self.data_out[18]*100,2)}%'
            return unit
        elif unit == 'default':
            return self.data_out[18]
    def getNormalizedSuspensionTravelRearLeft(self, unit='default'): 
        if unit == 'formatted':
            unit = f'{round(self.data_out[19]*100,2)}%'
            return unit
        elif unit == 'default':
            return self.data_out[19]
    def getNormalizedSuspensionTravelRearRight(self, unit='default'): 
        if unit == 'formatted':
            unit = f'{round(self.data_out[20]*100,2)}%'
            return unit
        elif unit == 'default':
            return self.data_out[20]
        else:
            return 'Null'

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
    def getWheelRotationAverage(self):
        average = (self.data_out[25]+self.data_out[26]+self.data_out[27]+self.data_out[28])/4
        return average

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
    def getCarClass(self):          #Between 0 (D -- worst cars) and 6 (X class -- best cars) inclusive
        if self.data_out[54] == 0:
            if self.data_out[53] == 0: #check carOrdinal for 0 to verify if D class or no data/in menu
                return 0     #return 0 if in menu
            else:
                return 'D'   #return D if actually in a D class car
        elif self.data_out[54] == 1:
            return 'C'
        elif self.data_out[54] == 2:
            return 'B'
        elif self.data_out[54] == 3:
            return 'A'
        elif self.data_out[54] == 4:
            return 'S1'
        elif self.data_out[54] == 5:
            return 'S2'
        elif self.data_out[54] == 6:
            return 'X'
        else:
            return 'Null'
    def getCarPerformance(self):    #Between 100 (slowest car) and 999 (fastest car) inclusive
        return self.data_out[55]
    def getDriveTrain(self):        #Corresponds to Drivetrain Type; 0 = FWD, 1 = RWD, 2 = AWD
        if self.data_out[56] == 0:
            return 'FWD'
        elif self.data_out[56] == 1:
            return 'RWD'
        elif self.data_out[56] == 2:
            return 'AWD'
        else:
            return 'Null'
        return self.data_out[56]
    def getNumberOfCylinders(self): #Number of cylinders in the engine
        return self.data_out[57]
    def getCarCategory(self):       #
        return self.data_out[58]
    def getUnknown1(self):          #Unknown value
        return self.data_out[59]
    def getUnknown2(self):          #Unknown value
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
            return round(2.237*self.data_out[64],2)         #return as mph
        elif unit == 'kph':
            return  round(3.6*self.data_out[64],2)           #return as kph
        else: 
            return self.data_out[64]
    def getPower(self, unit='default'):             #watts by default
        if unit == 'hp':                            #return as horsepower
            return round(self.data_out[65]/746,2)
        else:
            return self.data_out[65]
    def getTorque(self, unit='default'):            #newton meter by default
        if unit == 'ftlb':
            return round(self.data_out[66]/1.356,2)        #return as foot pounds
        else:
            return self.data_out[66]                    

    #return as 
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
        x = self.data_out[80]/255
        return f'{x*100}%'
    def getBrake(self):                 #brake pedal 0-255
        x = self.data_out[81]/255
        return f'{x*100}%'
    def getClutch(self):                #clutch 0-255
        x = self.data_out[82]/255
        return f'{x*100}%'
    def getHandbrake(self):             #handbrake 0-255
        x = self.data_out[83]/255
        return f'{x*100}%'
    def getGear(self):
        return self.data_out[84]
    def getSteer(self):                 #full left = -127, full right = 127
        x = self.data_out[85]/127
        return f'{x*100}%'
    def getNormalizedDrivingLine(self): 
        return self.data_out[86]
    def getNormalizedAIBrakeDifference(self): 
        return self.data_out[87]