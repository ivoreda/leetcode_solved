def time_conversion(s: str) -> str:
    if 'PM' in s:
        firstVal = int(s[:2])
        if firstVal < 12:
            newFirstVal = firstVal + 12
            fullStr = s[2:]
            finalStr = str(newFirstVal) + fullStr
            newOne = finalStr.replace("PM", "")
            print(newOne)
        elif firstVal > 12:
            newOne = s.replace("PM", "")
            print(newOne)
        elif firstVal == 12:
            newOne = s.replace("PM", "")
            print(newOne)
    elif 'AM' in s:
        firstVal = int(s[:2])
        if firstVal == 12:
            fullStr = s[2:]
            finalStr = "00" + fullStr
            newOne = finalStr.replace("AM", "")
            print(newOne)
        else:
            newOne = s.replace("AM", "")
            print(newOne)


    #     print("there is PM here")
    # else:
    #     print("there is no PM here")

time_conversion("01:05:45AM")
