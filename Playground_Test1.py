def mapStatus(code):
    if (code == '0'):
        print ("Pending")
    elif (code == '1'):
        print ("Paid")
    elif (code == '2'):
        print ("Rejected")
    elif (code == '3'):
        print("Cancelled")
    else:
        print("Unknwon")

status_str = input("Status: ")
input = mapStatus (status_str)