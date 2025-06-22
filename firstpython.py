with open("textexample.txt", "r") as file:
    for line in file:
        splits = line.split('Application')
        if '12-16 08:35:14.484  3340  3389 E DialerDialerBaseApplication' in line:
            print(f"The rest of the text is {splits[1]}")
