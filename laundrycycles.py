# Simulations of multiple laundry machines
# to explore how their cycles overlap and
# to find "optimal" numbers of machines.

# Anthony Kozar
# August 10, 2013

import sys

def DoLaundry(numLoads, numOfWashers, washerTime, numOfDryers, dryerTime, timeIncrement = 10, outputOn = True):
    def InitMachines(num, cycletime):
        machines = []
        nextDone = []
        for i in range(num):
            machines.append(cycletime)
            nextDone.append(-1)
        return (machines, nextDone)

    def RunMachines(loads, timeIncrement):
        curTime = 0
        loadsToWash = loads
        loadsWashed = 0   # and waiting to be dried
        loadsDried = 0
        idleCount = 0
        # load the washers
        for i in range(numOfWashers):
            if loadsToWash > 0:
                washersNextDone[i] = washers[i]
                loadsToWash -= 1
        # run machines until all loads dried
        while loadsDried < loads:
            # check each washer's status
            for i in range(numOfWashers):
                if washersNextDone[i] == curTime:
                    # washer just finished a load
                    loadsWashed += 1
                    if outputOn: print "Washer %d finished a load at time %d" % (i+1, curTime)
                    if loadsToWash > 0:
                        # start another load
                        washersNextDone[i] = curTime + washers[i]
                        loadsToWash -= 1
            # check each dryer's status
            for i in range(numOfDryers):
                if dryersNextDone[i] == curTime:
                    # dryer just finished a load
                    loadsDried += 1
                    if outputOn: print "Dryer  %d finished a load at time %d" % (i+1, curTime)
                if dryersNextDone[i] <= curTime:
                    # dryer is waiting for a load
                    if loadsWashed > 0:
                        # start another load
                        dryersNextDone[i] = curTime + dryers[i]
                        loadsWashed -= 1
                        if outputOn: print "Dryer  %d started  a load at time %d" % (i+1, curTime)
                    else:
                        # if outputOn: print "Dryer  %d is idle at time %d" % (i+1, curTime)
                        idleCount += 1
            curTime += timeIncrement
        # correct for last time increment
        curTime -= timeIncrement
        dryerIdleTime = (idleCount*timeIncrement)
        if outputOn:
            print "%d loads done at time %d" % (loadsDried, curTime)
            print "Dryers were idle for a total of %d" % dryerIdleTime
        return curTime, dryerIdleTime

    washers, washersNextDone = InitMachines(numOfWashers, washerTime)
    dryers, dryersNextDone = InitMachines(numOfDryers, dryerTime)
    timeDone, idleTime = RunMachines(numLoads, timeIncrement)
    return timeDone, idleTime

def FindOptimalTime(numLoads, maxWashers, washerTime, maxDryers, dryerTime, outputOn = True):
    minTime = sys.maxint
    optimalWashers = 0
    optimalDryers = 0
    for numOfWashers in range(1, maxWashers+1):
        for numOfDryers in range(1, maxDryers+1):
            time = DoLaundry(numLoads, numOfWashers, washerTime, numOfDryers, dryerTime, False)
            if time < minTime:
                minTime = time
                optimalWashers = numOfWashers
                optimalDryers = numOfDryers
    if outputOn:
        print "Minimum time for %d loads is %d" % (numLoads, minTime)
        print "Optimal washers: %d" % optimalWashers
        print "Optimal dryers: %d" % optimalDryers
    return minTime

# For 2 washers with a cycle time of 30 minutes and dryers with
# cycle time of 70 minutes, either 5 or 6 dryers give optimal times.
# However, this table shows that there is only a 10-minute improvement
# with 2W+6D over 2W+5D when num loads is even and no improvement
# when num loads is odd!  And ratio of idle time between 6 and 5
# dryers increases with the number of loads.  
def Compare5vs6Dryers(maxloads):
    print "#loads  W  D  time  idletime  idle-ratio"
    print "----------------------------------------"
    for loads in range(5,maxloads+1):
        for dryers in [5,6]:
            time, idle = DoLaundry(loads, 2, 30, dryers, 70, 10, False)
            # percentIdle = ((idle*1.0/dryers) / time) * 100
            if dryers == 5:
                idle5 = idle
                print "%6.d  %1.d  %1.d  %4.d  %8.d" % (loads, 2, dryers, time, idle)
            else:
                idle6 = idle
                ratio6to5 = ((idle6 * 1.0) / idle5)
                print "%6.d  %1.d  %1.d  %4.d  %8.d  %.4f" % (loads, 2, dryers, time, idle, ratio6to5)
 
