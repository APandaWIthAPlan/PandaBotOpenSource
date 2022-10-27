def channelcheck(mssg):
    mssg = str(mssg)
    varlist = mssg.split(" ")
    if varlist[0] == "Direct" and varlist[1] == "Message":
        return True
    else:
        return False