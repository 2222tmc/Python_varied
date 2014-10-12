# converts 8 bit to decimal
def bit_dec(octet):
    """Converts 8 bit octet to decimal"""
    powerof2 = (128,64,32,16,8,4,2,1)
    b = 0
    shortotal = 0
    for e in octet:
        t = e * powerof2[b]
        shortotal = shortotal + t
        b = b + 1      
    return shortotal

# converts a number 0-255 to binary list[]

def dec_bit(num):
    """Converts decimal number to binary list"""
    powerof2 = (128,64,32,16,8,4,2,1)
    z = 0
    newoct = []
    k = 0
    for r in powerof2:
        if r <= num:
            num = num - r
            z = 1
        else:
            z = 0
        newoct.append(z) 
    return newoct

# combine 4 binary list to 1
def combine(a,s,d,f):
    list = []
    for i in a:
        list.append(i)
    for i in s:
        list.append(i)
    for i in d:
        list.append(i)
    for i in f:
        list.append(i)
    return list

# take dec num and make binary list ensuring bit number is met

def bit_leng_bin(bits,num):
    """ input bit length request(bitreq) and decimal number"""
    m = bits / 1
    ty = []

    while m > 0:
        m -= 1
        x = num % 2
        ty.append(int(x))
        num -= x
        num /= 2
    ty.reverse()
    return ty

# function insert_subnet(IP,subnet)
def insert_subnet(IP,subnet):
    """ IP is calculatable IP, and subnet is binary output of bin_leng_bin()"""
    cntr = 0
    cntr2 = 0
    for i in IP:
        if i == 3:
            r = subnet[cntr2]
            IP[cntr] = r
            cntr2 += 1
        else:
            True
        cntr += 1
    return IP

def lo(IPbin):
    """ takes IP 32 bit and returns low IP"""
    cntr = 0
    lo = IPbin
    for i in lo:
        if i == 5:
            lo[cntr] = 0
            cntr += 1
        else:
            cntr += 1          
    return lo


def hi(IPbin):
    """ takes IP 32 bit and returns hi IP"""
    cntr = 0
    hi = IPbin
    for i in hi:
        if i == 5:
            hi[cntr] = 1
            cntr += 1
        else:
            cntr += 1
    return hi

#  break 32 bit binary into 4 octet then to dot.dec
def breakdown(long):
    """break 32 bit binary into 4 x 8 dot.dec"""
    sect1 = long[:8]
    sect2 = long[8:16]
    sect3 = long[16:24]
    sect4 = long[24:32]
    dec1 = bit_dec(sect1)
    dec2 = bit_dec(sect2)
    dec3 = bit_dec(sect3)
    dec4 = bit_dec(sect4)
    dot_dec = str(dec1) + '.' + str(dec2) + '.' + str(dec3) + '.' + str(dec4)
    return dot_dec
# Main ---------------------------------------------------------------------
pin = ''
while pin == '':
    
# 1 takes IP address input from user
    print("Subnet Calculator")
    print("Enter IP address one octet at a time.")
    oc1 = int(input("Octet 1: "))
    oc2 = int(input("Octet 2: "))
    oc3 = int(input("Octet 3: "))
    oc4 = int(input("Octet 4: "))

# 2 takes octet 1 - 4 and itemizes them into a list "dotdec"

    dotdec = [oc1,oc2,oc3,oc4]

# 3 Confirm IP address
   
    print("\nYou entered ",dotdec,"for your IP address.")
    conf1 = input("Is this correct?  ")
    if "y" in conf1:
        None
    else:
        continue
    
# 4 IP classification
    ipclass = ''
    oc1int = int(oc1)
    if oc1int > 0:
        if oc1int < 127:
            ipclass = 'a'
        elif oc1int == 127:
            print('This is a Loop Back address and is invalid.')
            input('Press enter to restart')
            continue
        elif oc1int < 192:
            ipclass = 'b'
        elif oc1int < 224:
            ipclass = 'c'
        else:
            print('Invalid IP address')
            continue
    else:
        print('Ivalid IP address')
        continue

   
# 5 assign Default Subnet Mask and available subnet bits and dsm in binary
    dsm = None
    if ipclass:
        if ipclass == 'a':
            dsm = [255,0,0,0]
            bitsav = 22
            bin_dsm = (1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        elif ipclass == 'b':
            dsm = [255,255,0,0]
            bitsav = 14
            bin_dsm = (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        elif ipclass == 'c':
            dsm = [255,255,255,0]
            bitsav = 6
            bin_dsm = (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0)
        else:
            print('error')
            input()
            continue

# 6 B inform user of bits available and subnet options and dsm

    print('\nIP Class: ',ipclass.upper())
    print('\nDefault Subnet Mask: ', dsm)
    print('\nYou have', bitsav, 'bits available from host ID to use for subnetting.\n\
Entering 1 bit allows for 2 subnets. \nFor each additional bit the amount of subnets doubles.')
    reqtest = False
    while reqtest == False:
        bitreq = int(input('\nEnter subnet bit request: '))
        if bitreq <= bitsav:
            reqtest = True
    
    
# 7 return new sub mask(binary) and calc sub mask
    calc_sm = list(bin_dsm)
    new_sm = list(bin_dsm)
    subbits = bitreq / 1
    cntr = 0

    for i in calc_sm:
        if i == 1:
            calc_sm[cntr] = 1
            new_sm[cntr] = 1       
        if i == 0:
            if subbits > 0:
                calc_sm[cntr] = 3
                new_sm[cntr] = 1
                subbits = subbits - 1
               
        cntr = cntr + 1

   
    
# 8 breakdown to dot dec
    news = breakdown(new_sm)
    print('\nNew Subnet: ', news)
    
# 10 convert IP address octets from dec to binary
    bin_IP1 = dec_bit(oc1)
    bin_IP2 = dec_bit(oc2)
    bin_IP3 = dec_bit(oc3)
    bin_IP4 = dec_bit(oc4)
    bin_IP_list = combine(bin_IP1,bin_IP2,bin_IP3,bin_IP4)
    

# 11 takes calc_sm and binIP and creates calculatable IP
    cntr = 0 
    for i in calc_sm:
        if i == 1:
            True
        elif i == 3:
            bin_IP_list[cntr] = 3
        elif i == 0:
            bin_IP_list[cntr] = 5
        cntr += 1
    
    
# 12 takes subnet request and calculates amount of subnets
    amnt_nets = 2 ** bitreq
    print('\nAmount of Subnets: ',amnt_nets)

# 15, (final steps) take functions and info and return series of IP ranges.
    cntr_final = 0
    list_final = []
    while cntr_final < amnt_nets:
        lo_IP = []
        hi_IP = []
        new_IP = []
        for i in bin_IP_list:
            new_IP.append(i)
        vader = bit_leng_bin(bitreq,cntr_final)
        update_IP = insert_subnet(new_IP,vader)
        for i in update_IP:
            lo_IP.append(i)
        for i in update_IP:
            hi_IP.append(i)           
        lip = lo(lo_IP)
        hip = hi(hi_IP)
        dec_lip = breakdown(lip)
        dec_hip = breakdown(hip)
        label = 'Subnet: ' + str(cntr_final)
        list_final.append(label)
        
        label_lo = 'Low: ' + str(dec_lip)
        list_final.append(label_lo)
        
        label_hi = 'Hi: ' + str(dec_hip)
        list_final.append(label_hi)
        list_final.append(' ')      
        cntr_final += 1

    put_in = open('Ranges.txt', 'w')
    for i in list_final:
        put_in.write(str(i))
        put_in.write('\n')
    put_in.close()
    print('\nSee Folder for text file containing subnet ranges.')
    input('\nPress Enter to Repeat.')
    
      
