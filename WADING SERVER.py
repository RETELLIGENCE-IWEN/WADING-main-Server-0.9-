###############################################################################################
## WAD SERVER (DRONE JONGHAP GUWANJE SYSTEM)                                                  #
##                                                                                            #
## Isaac Kim   leader of team RETELLIGENCE                                                    #
##                                                                                            #
##    MIT License                                                                             #
##                                                                                            #
##    Copyright (c) [2016] [Isaac Kim]                                                        #
##                                                                                            #
##    Permission is hereby granted, free of charge, to any person obtaining a copy            #
##    of this software and associated documentation files (the "Software"), to deal           #
##    in the Software without restriction, including without limitation the rights            #
##    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell               #
##    copies of the Software, and to permit persons to whom the Software is                   #
##    furnished to do so, subject to the following conditions:                                #
##                                                                                            #
##    The above copyright notice and this permission notice shall be included in all          #
##    copies or substantial portions of the Software.                                         #
##                                                                                            #
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR              #
##    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                #
##    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE             #
##    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                  #
##    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,           #
##    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE           #
##    SOFTWARE.                                                                               #
##                                                                                            #
## import RETELLIGENCE                                                                        #
##                                                                                            #
###############################################################################################


###############################################################################################
##                                                                                            #
## Recommended operating system                                                               #
## OS : over windows 10 home                                                                  #
## cpu : over 8 hardware threads, over 3.2Ghz clock speed                                     #
## Internet connention : over 1GB/s                                                           #
## Required software : python 3.5.2                                                           #
##                                                                                            #
## Socket port 12000 ~ 48000 unused                                                           #
##                                                                                            #
###############################################################################################


###############################################################################################
##                                                                                            #
## Project Definition Keywords                                                                #       
##                                                                                            #      
## WADING : World-wide Assocciation of Drones via Interconnected Network Integration          #
## WAD : chip that enables WADING, will be attached to Drones                                 #
## APP : mobile app for drone owners. used for WADING operation                               #
## PPG(Platform Programm) : programm for atonomos drone owners like amazone                   #
##                                                                                            #      
###############################################################################################


# importing modules
import threading
from socket import *
import time
import os
import random
from datetime import datetime
from urllib.request import urlopen


# Hello WADING
server_start_time = datetime.now()
print('**************************************************************************')
print('*     start THE First WADING Connection via RETELLIGENCE IEZANOV IWEN    *')
print('*                                                                        *')
print('*                     ', str(server_start_time), '                       *')
print('**************************************************************************')
print('\n \n \n \n')


# Master Passward, must be secured in all cases.
# Use your own. Do not use default pw.
# You can change Master Passward on main menu
# but please read manual carefully
Master_Key_Pw = 'Iezanov_RETELLIGENCE_Iwen'
# 1. open admin menu on main menu
# 2. enter current Master Passward
# 3. enter new Master Passward
# 4. hit 'enter' again
# Master Passward Changed


# Pin data is used to identify numerical order of registration
F_pinI_h = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\WAD_pinList(i).txt', 'r') # loading pin data(i) from DBMS
F_pinS_h = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\WAD_pinList(s).txt', 'r') # loading pin data(s) from DBMS

WAD_pinList_i = [] # list for pin numbers
WAD_pinList_s = [] # list for pin numbers

R_pinI_h = F_pinI_h.read() # reading file handle
R_pinS_h = F_pinS_h.read() # reading file handle

C_pinI_h = R_pinI_h  # copy read handle of pin data
C_pinS_h = R_pinS_h  # copy read handle of pin data


while(1): # loading pin data for making user ID 
    try:        
        for i in range(len(C_pinI_h)):
            if (C_pinI_h[i]=='#') and (C_pinI_h[i+1]=='#') and (C_pinI_h[i+2]=='#'):
                WAD_pinList_i.append((C_pinI_h[i+3:i+12])
            if (C_pinS_h[i]=='#') and (C_pinS_h[i+1]=='#') and (C_pinS_h[i+2]=='#'):
                WAD_pinList_s.append((C_pinS_h[i+3:i+12])
    except:
        break


#######  Default socket port list (may differ by hardware or operating system)
#######  12000~24000  : WAD-chip
#######  24000~36000  : mobile app
#######  36000~48000  : platform program


# VIA ID
LIVE_WAD_list = [] # online wad list
LIVE_APP_list = [] # online app list
LIVE_PPG_list = [] # online platform program list

    # Examples
    # WAD ID : i86-12345678999-ks9 (type-pin-zip) (17 characters)
    # APP ID : xfj-123456789-1609-110308 (equivalent to USER_code)
    # PPG ID : xfj-123456789-1609-110308 (equivalent to USER_code)

# One user can only use either one of app or ppg to control or moniter one 'WAD' attached vehicle



## HIgh-level Secrete code for TCP/IP communication
x_code = '###WAD*#*'  # Server Rx / WAD Tx
xx_code = '###WAD#*#' # Server Tx / WAD Rx




# global functoin for printing on consol // enable/disable via global pharameter : prints 
def printQ(sent):
    global prints
    if prints == True:
        print(sent)
           

def check_multi_id(id_give): # check if some one is using same id (register sequence on app)
    if id_give in R_users_h:
        return (1)
    else:
        return(0)


def getadr(): # get operating systems ipv4 address : used as server IP address
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("gmail.com",80))
    r = s.getsockname()[0]
    s.close()
    print('Server IP address : ', r)
    return (r)


def disconnect_all(pL): # disconecting all open sockets used by WADING, ::== emergency shut down
    for i in range(12000, pL+1):
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(getadr(), i)
        s.close()
    for i in range(24000, pL+1):
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(getadr(), i)
        s.close()
    for i in range(36000, pL+1):
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(getadr(), i)
        s.close()
    sys.exit()
    print("Manually disconnected..")
    time.sleep(0.5)
    for i in range(9)
        print("Programm will automaticly quit in %s seconds.." % str(9-int(i)))
        time.sleep(1)
    quit()
    

def save_leftover(): # saving all data before emegency shut down
    pass
    # under developement


# The altimate CUBIC system
def CUBIC_system(check_cooedinate, book_coordinate, book_start_time, book_duration):
    pass
    # under developement 
    # master algorithm system of WADING
    # will be updated in several months


# Change GPS coordinate to Cubic coordinate
def CUBIC_gps_to_cubic(lat, lon, height):
    
    # lat_dms 30m = 1sec
    # lon_dms 30m = 1.25sec
    # lat_dd 30m = 0.000277
    # lom_dd 30m = 0.000347

    lt_1 = 0.000277
    lo_1 = 0.000347

    Ground_Zero = [37.60000, 126.86466, 0]
    Ground_Zero_as_CUBIC = [0, 0, 0]

    x = int(0 - ((Ground_Zero[0]-float(lat))//lt_1))
    y = int(0 - ((Ground_Zero[1]-float(lon))//lo_1))
    z = int(0 - ((Ground_Zero[2]-float(height))//30))-1

    CUBIC_cd = '[' + '0'*(6-len(str(x))) + str(x) + ', ' +'0'*(6-len(str(y))) + str(y) + ', ' + '0'*(6-len(str(z))) + str(z) + ']'
    return(CUBIC_cd)

    # return example : [0-2166, 003272, 000000] // as string


# Change Cubic coordinate to GPS coordinate
def CUBIC_cubic_to_gps(x, y, z):

    # lat_dms 30m = 1sec
    # lon_dms 30m = 1.25sec
    # lat_dd 30m = 0.000277
    # lom_dd 30m = 0.000347

    lt_1 = 0.000277
    lo_1 = 0.000347

    Ground_Zero = [37.60000, 126.86466, 0]
    Ground_Zero_as_CUBIC = [0, 0, 0]

    x_c = Ground_Zero [0]+ ((0 - (Ground_Zero_as_CUBIC[0]-x))*lt_1)
    y_c = Ground_Zero [1]+ ((0 - (Ground_Zero_as_CUBIC[1]-x))*lo_1)
    z_c = Ground_Zero [2]+ ((0 - (Ground_Zero_as_CUBIC[2]-x))*30)+15

    x_cd = round(x_c, 6)
    y_cd = round(y_c, 6)
    z_cd = round(z_c, 6)

    GPS_cd = '[' + x_cd + ', ' + y_cd + ', ' + '0'*(6-len(str(z_cd))) + z_cd + ']'
    return(GPS_cd)

    # return example : [37.600000, 1286.86466, 15] // as string



# view complexity of surrounding air space. over 60 means no flight recommended
# checks 10*10*5 cubics
# target_cd example : [000012, 003400, 000003]
def Complexity_check(target_cd): # Extremely heavy file hand!! system must have RAM over 32GB
    
    complexity = 0
    x_start = int(target_cd[1:7])
    y_start = int(target_cd[9:15])

    if (int(target_cd[1:7])>=-5) and (int(target_cd[9:15])>=-5):
        fh1 = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\CUBIC_sys_1.txt', 'r')
    if (int(target_cd[1:7])>=-5) and (int(target_cd[9:15])<=5):
        fh2 = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\CUBIC_sys_2.txt', 'r')
    if (int(target_cd[1:7])<=5) and (int(target_cd[9:15])>=-5):
        fh3 = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\CUBIC_sys_3.txt', 'r')
    if (int(target_cd[1:7])<=5) and (int(target_cd[9:15])<=5):
        fh4 = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\CUBIC_sys_4.txt', 'r')

    rh1 = fh1.read()
    rh2 = fh2.read() 
    rh3 = fh3.read()
    rh4 = fh4.read()

    if i in range(len(rh1)-24):
        if target_cd == rh1[i:i+24]:
            if rh1[i+25] == '1':
                complexity += 1



""" Main Function Algorithms Source code below """

# test module of WAD communication
# temporary and only for short demonstration
def WADING_t(port):

    global LIVE_WAD_list

    while(1):
        server_adr = getadr()
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind((server_adr, port))
        serverSocket.listen(1)
        connectionSocket, addr = serverSocket.accept()
        # accept connection request from WAD chip (which is embeded in drone)

        LIVE_WAD_list.append('test WAD 1')

        
        # from WAD : ###WAD*#*i01-0000000000-kr1 + gps_x + gps_y + WAD_altitude
        while(1):

            in_1 = connectionSocket.recv(1024) # recieve from wsad

            # index input and get gps data
            # //                        //
            WAD_altitude = 10
            CUBIC_cd = CUBIC_gps_to_cubic(GPS_x, GPS_y, WAD_altitude)
            fh1 = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\WADING_link\\link_test.txt', 'w')
            fh2 = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\User_registor.txt', 'r')
            rh2 = fh2.read()

            for i in range(len(rh2)-18):
                if WAD_id == rh2[i:i+18]:
                    link_id = rh2[i-94:i-69]
                    writing = link_id + wad_id + CUBIC_cd
                    fh1.write()
                    # example out : xfj-123456789-1609-110308i01-0000000000-kr1[000023, 0-2345, 000001]
            fh1.close()
            fh2.close()


def WADING(port):
    global LIVE_WAD_list

## WAD Communication Protocall ##

    # step 1
    """
    Server_Rx_prot =
        1.[9]  ###WAD*#*
        2.[9]  ID : _ _ _  _ _ _ _  _ _
        3.[6]  PW : _ _ _ _ _ _
        """

    # step 2n
    """
    Server_Tx_prot =
        1.[9]  ###WAD#*#
        2.[5]  New Port number
        3.[6]  PW : _ _ _ _ _ _
        4.[5]  command : _ _ _ _ _
        """

    # step 2n+1
    """
    Server_Rx_data =
        1.[9]   x_code (###WAD*#*)
        2.[9]   ID
        3.[6]   PW
        4.[6]   status
        5.[128]  beacon
        """









def APP(port): # via thread, this fuction communiacates with mobile app
    global LIVE_APP_list

#1#    new user registration function
    

##    USER_Code : xfj-123456789-1609-110308                                                     User_Code ::::::::: via server
##    random 3-length character + numerical pin number + y/m + zip code
##            
##            - user info                                                                       user info ::::::::: via app
##                    - user real name
##                    - user id (9 characters)
##                    - user pw (6 numbers)
##                    - user phone number
##                    - user e-mail address
##
##            - property of WAD 
##                    - WAD_id : i86-12345678999-ks9 (type-pin-zip) (17 characters)             WAD_id ::::::::: via server
##                    - WAD_pw (6 numbers)                                                      WAD_pw ::::::::: via app
##                    


## communication code with app and server
    log_CODE = qwe123 # can I login? yes you can login
    register_CODE = asd123 # can I registor? yes you may
    geo_data_CODE = zxc123 # I want to see geological data arround me! sure
    trace_CODE = rty123 # I want to trace my drone! here you go
    flight_reg_CODE = fgh123 # I want to register cubics! go ahead
    donate_CODE = vbn123 # I want to donate! thanks

    # login fail : ewq321
    # real time tracking fail (invalid id or pw) : ytr123
    # real time tracking fail (WAD offline) : ytr321
    # cubic sys fail (WAD offline) : hgf321
    # cubic sys fail (already in use) : hgf123
    # fail to registor (use different id) : dsa123 




    def new_registor_code(zip_code): # making new user register
        def ran():
            code = ''
            for i in range(3): # for 3 random alphabets at fromt of 'USER_Code'
                x = random.randint(97, 122)
                code += chr(x)
            return(code)

        def pin(): # numerical numbers to identify order of registeration 
            f = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\User_pinList.txt', 'r')
            r = f.read()
            pin = r[-10:-1]
            while(1):
                if pin in r:
                    pin = str(int(pin)+1)
                    pin = ('0'*(9-len(pin))) + pin
                    continue
                else:
                    break
            f.close()
            return(pin)

        def ym(): # year and month
            n = datetime.now()

            ym = ''
            ym += str(n.year)[2:]
            if len(str(n.month)) == 1:
                t = '0' + str(n.month)
            else:
                t = str(n.month)
            ym+=t
            return(ym)

        pin = pin()
        code = ran() + pin + ym() + str(zip_code)
        printQ('Code : ', code)
        ff = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\User_pinList.txt', 'a')
        ff.write((pin + "\n")) # add PIN to Database
        ff.close()
        return(code)

    # about login
    # app send  :  ###WAD*#*(x_code) + qwe123(app wants to log in) + id(9characters) + passward(6numbers)
    # if id and passward is valid
    # server sends : ###WAD#*#(xx_code) + qwe123(app may login)
    # if not valid : ###WAD#*#(xx_code) + ewq321(app dont login) 
    def Log_in(inin): # login
        idid = inin[15:24]
        pwpw = inin[24: 30]

        printQ("$$ Port", port, 'connected for app :: ', id_1, str(datetime.now())
        if idid not in registors_id_list:
            send1 = xx_code + '312ewq' 
        else:
            if pwpw not in registors_pw_list:
                send1 = xx_code + '312ewq' 
            else:
                send1 = xx_code + 'qwe123'
                for i in range(len(r)):
                    if r[i:i+6]==idid:
                        ff = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\LOGin_timestamp.txt', 'a')
                        timenow = datetime.now()
                        appending = r[i-38:i-13]
                        appending = 'Log in  :  ' + appending + '   ' + str(timenow)
                        ff.write(appending)
                        ff.close()
                        LIVE_APP_list.append(idid)
        connectionSocket.send(send1.encode())


    # about realtime tracking
    # app send  :  ###WAD*#*(x_code) + rty123(app wants to moniter WAD) + id + pw
    # if WAD is operating and id + pw matches
    # server sends : ###WAD#*#(xx_code) + rty123(monitering permited) 
    # + gps + cubic + speed + altitude + temperature + WAD status + flight environment information 
    # if not valid Id, Pw : ###WAD#*#(xx_code) + ytr123(wrong id or pw)
    # if WAD offline :  ###WAD#*#(xx_code) + ytr321(WAD not online) 
    def realTime_track(inin):
        idid = inin[15:24]
        pwpw = inin[24: 30]

        if (idid not in registors_id_list) or (pwpw not in registors_pw_list):
            rq = 'ytr123' 
        else:
            f = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\User_registor.txt', 'r')
            r = f.read()
            for i in range(len(r+9)):
                if idid == r[i:i+9]:
                    link_id = r[i-38:i-22]
                    ff = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\WADING_link\\link_test.txt', 'w')
                    rr = ff.read()
                    rq = ytr312
                    for i in range(len(rr)):
                        try:
                            if link_id == rr[i:i+16]:
                                rq = rty123
                                # example item on rr : xfj-123456789-1609-110308i01-0000000000-kr1[000023, 0-2345, 000001]
                                cur_cd = rr[i+44:i+66]
                        except:
                            break
                        else: 
                          
        send1 = xx_code + rq + cur_cd
        connectionSocket.send(send1.encode())
        # sending to app : current location of WAD chip (which belongs to the app user)




    # about Flight registoration
    # app send  :  ###WAD*#*(x_code) + fgh123(app wants to registor cubic) +  + [0, 0, 1][0, 0, 2][0, 0, 3] (requested cubics)
    # if WAD is operating 
    # server sends : ###WAD#*#(xx_code) + fgh123(WAD may fly)
    # if not valid : ###WAD#*#(xx_code) + hgf321(WAD not online)
    # if other WAD is using already :  ###WAD#*#(xx_code) + hgf123(unusable) + [0, 0, 1](unusable cubics)
    def Flight_reg(inin): # booking cubic via cubic system
        request = inin[15:]
        # comming soon...
        # if Cubic is unused : registor selected cubic
        # if Cubic is used   : registor denial
        pass # under developement
 

    # about GEO data
    # app send  :  ###WAD*#*(x_code) + fgh123(app wants to see Geo data) + /xxx.xxxxx/xxx.xxxxx/ (gps coordinate(19 characters))
    # server sends : ###WAD#*#(xx_code) + fgh123(Oh why not)
    #  + magnetic field data (ex : '#g/0/3/4/3/4#' - cKP, cKK, mKP, mKK)
    #  + user's location based on CUBIC system (ex : #c/0/0/0/1# - means coordinate is [0, 0, 0], and it is in use currently)
    #  + wether you can fly or not in your Cubic (ex : #f/0#) (1 : dont fly, 0 : u may fly)
    #  + compelity of suround Cubics (ex : #p/065#) (000%~100%)
    # 
    # total example 
    # 
    # APP : ###WAD*#*fgh123/xxx.xxxxx/xxx.xxxxx/
    #
    # Server : ###WAD*#*fgh123#g/0/3/4/3/4##c/0/0/0/1##f/0##p/065#
   
    def Geo_data(inin):

        # aka 'EMF'
        # Earth's magnat field data api : http://spaceweather.rra.go.kr/api/kindex
        response = urlopen('http://spaceweather.rra.go.kr/api/kindex')
        scrawl_d = (response.read().decode('utf-8'))
        current_KP = scrawl_d[114]
        current_KK = scrawl_d[127]
        max24_KP = scrawl_d[138]
        max24_KK = scrawl_d[149]
        error_code = scrawl_d[57:62]
        error_ox = 0
        if error_code != 'NOERR':
            error_ox = 1
        # data array for EMF = start sign [#g#] for identifying magnetic field data, '/' in between values, # at the end
        magnatic_field_d = '#g/'+ error_ox + '/' + current_KP + '/' + current_KK + '/' + max24_KP + '/' + max24_KK + '#'
        
        # get gps coordinate from app 
        Latitude = float(inin[16:25])
        Longitude = float(inin[26:35])
        cubic_c= CUBIC_gps_to_cubic(Latitude, Longitude, 10)

        # if can_fly == '1': wad can fly // else : can't fly
        #can_fly = '#f/' + str(CUBIC_system(cubic_c,0,0,0)) + '#'
        #complexity = '#p/' + str(Complexity_check(cubic_c)) + '#'
        can_fly = '#f/0#' # for testing
        complexity = '#p/010#' # for testing

        send1 = xx_code + geo_data_CODE + magnatic_field_d + cubic_c + can_fly + complexity

        connectionSocket.send(send1.encode())
        

    def Donnate(inin): # we welcome donations :)
        money = connectionSocket.recv(1024)
        if money[:9] == x_code:
            name_of_donater = money[15:]
            f = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\donators.txt', 'a')
            f. write(name_of_donater)
        connectionSocket.send(('Thank you')).encode()


    def initial_connection():
        ## starting communication

        ff = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\User_registor.txt', 'a')
        rr = ff.read()
        registors_id_list = []
        registors_pw_list = []

        for i in range(len(rr)):
            if rrr[i]=='#' and rrr[i+1]=='#' and rrr[i+2]=='#':
                registors_id_list.append(rrr[i+32:i+41])
        for i in range(len(rr)):
            if rrr[i]=='#' and rrr[i+1]=='#' and rrr[i+2]=='#':
                registors_pw_list.append(rrr[i+43:i+49])
        
        server_adr = getadr()
        serverSocket = socket(AF_INET,SOCK_STREAM) # make socket object
        serverSocket.bind((server_adr, port))
        serverSocket.listen(1)
        
        while(1):
            # main algorithm
            while(1):
                connectionSocket, addr = serverSocket.accept() # accepted connection
                in_1 = connectionSocket.recv(1024) # recieve from app
                if in_1[:9] != x_code: # if authorised
                    printQ("!!! Unidentified connection", port, str(datetime.now())
                    connectionSocket.close()
                    continue
                else:
                    break                  

            printQ("$ connection WADING ", in_1[15:24], port, str(datetime.now())
            while(1):
                try:
                    if in_1[9:15] == log_CODE:
                        Log_in(in_1)

                    if in_1[9:15] == donate_CODE:
                        Donnate(in_1)
                    
                    if in_1[9:15] == geo_data_CODE:
                        Geo_data(in_1)
                    
                    if in_1[9:15] == register_CODE:
                        new_registor_code(in_1)
                    
                    if in_1[9:15] == trace_CODE:
                        realTime_track(in_1)
                    
                    if in_1[9:15] == flight_reg_CODE:
                        Flight_reg(in_1)

                    in_1 = connectionSocket.recv(1024)
                
                except:
                    printQ("$ connection failed ", in_1[15:24], port, str(datetime.now())
                    LIVE_APP_list.remove(in_1[15:24])
                    break
                else:
                    continue













def PLATFORM(port):
    pass
                   
    def Make_id_s(): 
        global WAD_pinlist

        type_WAD = 's'
        year_WAD = str((time.localtime(time.time()))[0])
        pin_WAD = str(int(WAD_pinList[-1]) + 1)
        if len(pin_WAD) > 4:
            pin_WAD = pin_WAD[0:4]

        ID_WAD = type_WAD + year_WAD[-2] + year_WAD[-1] + '0'*(4-len(pin_WAD)) + str(random.randint(11,99))

        while(1):
            if check_multi_id(ID_WAstD) = 1:
                ID_WAD = ID_WAD[0, 7] + str(random.randint(11,99))
                continue
            else:
        while(1):
            passward = input("Enter PW (6 numbers): ")
            try:
                passward = int(passward)
            except:
                continue
            else:
                if len(passward) != 6:
                    continue
                elif len(passward) == 6:
                    break
                break
        print(ID_WAD)
        print(passward)
        stat = ('Confirm?(y/n) : ')
        if stat == 'y':
            write_info = '[' + ID_WAD + +', ' + str(passward) + ']'

            F_users_h.write('\n')
            F_users_h.write(write_info)
            F_users_h.write('\n')
            WAD_pinList.append(pin_WAD)



    server_adr = getadr()
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((server_adr, port))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    
    in_1 = connectionSocket.recv(1024) # recieve from platform
    id_1 = in_1[9:15]
    printQ("$$ Port", port, 'connected for platform :: ', id_1, str(datetime.now())

    pass
    # Under developement


           

def initial_WAD(portLim): # initialize multi-threading for WADING chips
    global test
    global tport
    if test != 1:
        for i in range(12000, portLim):
            (threading.Thread(WADING(i))).start()
    else:
        (threading.Thread(WADING_t(tport))).start()



def initial_APP(portLim): # initialize multi-threading for mobile apps
    global test
    global tport
    if test != 1:
        for j in range(24000, portLim):
            (threading.Thread(APP(i))).start()
    else:
        (threading.Thread(APP(tport+12000))).start()



def initial_PLATFORM(portLim): # initialize multi-threading for platform programms
    for k in range(36000, portLim):
        (threading.Thread(PLATFORM(i))).start()


       
def initialize(portLim): # called by main()
    
    # thread classified for each type of connection setting
    init_wad = threading.Thread(target=initial_WAD(portLim))
    init_app = threading.Thread(target=initial_APP(portLim))
    init_platform = threading.Thread(target=initial_PLATFORM(portLim))

    # starting tread for initializing step 1
    init_wad.start()
    init_app.start()
    init_platform.start()


# test mode for special cases like small demonstrations
def test_mode():
    port = int(input('$ Enter test port : '))
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((server_adr, port))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    in_1 = connectionSocket.recv(1024) # recieve from platform
    


def main(): # main function
    # global pharameters
    global prints
    global server_adr
    global tport
    global test
    
    # get operating system's ipv4 address
    server_adr = getadr()

    while(1):
        stst = input('$ Enable Test Mode ? : ')
        test = 0
        if stst == '':
            tport = int(input('$ Enter test port : '))
            test = 1
        pL = input("$ Port limitation set : ") # port limitation for each type of connections (ex. if pL==3 : socket for wad + for app + for pp = 9)
        stat = input("$ Initialize(enter)? : ")
        try:
            pL = int(pL)
        except:
           continue
        else:
           if stat=='':
               break
        
    initialize(pL) # calling initializing mode in sub-background


    while(1):

        # start managing server
        
        stat = input('$ [ Server Setup : s ]  [ Variable Setings : v ]  [ Admin Menu : a ]  [ Live view : i ]  [ Emergency Proxy Shut-down : e ] ')

        if (stat == 's')or(stat == 'v'):
            print('$ Comming soon...')

        if (stat == 'a'):
            pew = input("$ Access denied ") # little trick
            if pew == Master_Key_Pw:
                while(1):
                    Master_Key_Pw= input("$ ") # enter new master passward
                    if input("$ _____________ WAD ")=='': # enter 'Enter' to confirm or else to retry
                        break
                    else:
                        continue
            else:
                continue
                # if wrong passward : go to main menu again

        if stat == 'i':
            while(1):
                print_ask = input("$ Press 'enter' to go on") # enter = allow background functions to print status on consol
                if print_ask='':
                    prints = True  # global var to alow system to print on consol about system flow
                else:
                    prints = False
                    break
                t1 = (str(datetime.now()))[14:19]
                tt1 = int(t1[0:2])*60 + int(t1[3:])
                while(tttx1<10): # to wait 10 seconds on print enabled
                    t2 = (str(datetime.now()))[14:19]
                    tt2 = int(t2[0:2])*60 + int(t2[3:])
                    tttx1 = tt2-tt1
                                  
        if stat == 'e':
            status2 = input("$ Shut down may cause sky caos. must carefully encounter : ") # must type in password
            if status2 == Master_Key_Pw:
                # call emergency shut down (close all using sockets)
                disconnect_all(pL)
            


if (__name__ == "__main__"): # modulize
    main()

        
