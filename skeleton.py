from socket import *
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8
TIMEOUT_MESSAGE = "Request timed out."

def checksum(str):
    csum = 0
    countTo = (len(str) / 2) * 2

    count = 0
    while count < countTo:
        thisVal = ord(str[count+1]) * 256 + ord(str[count])
        csum = csum + thisVal
        count = count + 2

    if counTo < len(str):
        csum = csum + ord(str[len(str) - 1])
        csum = csum & 0xffffffffL

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout

    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []: # Timeout
            return TIMEOUT_MESSAGE, 0

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        #Fill in start
        # Fetch the ICMPHeader from the IP, extract the various header fields
        #Biold the "Reply from" message and return it
        #Fill in end

        time left = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return TIMEOUT_MESSAGE, 0

def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)

    myChecksum = 0
    # Make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header
    myChecksum = checksum(header + data)

    # Get the right checksum, and put it in the header
    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network byte order
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data

    mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple not str
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object

def doOnePing(destAddr, timeout):
    icmp = getprotobyname("icmp")
    # SOCK_RAW is a powerful socket type. For more details: http://sockraw.org/papers/sock_raw

    #Fill in start
    # Create raw socket here
    #Fill in end

    myID = os.getpid() & 0xFFFF  # Return the current process i
    sendOnePing(mySocket, destAddr, myID)
    feedback, delayValue = receiveOnePing(mySocket, myID, timeout, destAddr)

    mySocket.close()
    return feedback, delayValue

def ping(host, maxIter, timeout=1):
    # timeout=1 means: If one second goes by without a reply from the server,
    # the client assumes that either the client's ping or the server's ping is lost
    dest = gethostbyname(host)
    print ""
    print "Pinging " + host + " [" + dest + "] using Python:"
    print ""
    # Send ping requests to a server separated by approximately one second
    numIter = 0
    while numIter < maxIter:
        feedback, delayValue = doOnePing(dest, timeout)
        print feedback
        time.sleep(1) # one second
        numIter = numIter + 1
    return feedback

ping("localhost", 3) # To test the code
ping("google.com", 3)
ping("utexas.edu", 3)
ping("www.u-tokyo.ac.jp", 3)
ping("telecom-paris.fr", 3)