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

    print(x)
    print(y)
    print(z)
    CUBIC_cd = '[' + '0'*(6-len(str(x))) + str(x) + ', ' +'0'*(6-len(str(y))) + str(y) + ', ' + '0'*(6-len(str(z))) + str(z) + ']'
    print(CUBIC_cd)
    return(CUBIC_cd)


# testing
while(1):
    lat = input("lat : ")
    lon = input("lon : ")
    heg = input("heg : ")
    CUBIC_gps_to_cubic(lat, lon, heg)
