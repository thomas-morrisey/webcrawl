import os

def directoryHousekeeping():

    os.system("rm -rf ./data")
    os.system("rm -rf ./session_data")

    os.system("mkdir data")
    os.system("mkdir session_data")
        
    return



def main():

    directoryHousekeeping()
    return



if __name__ == "__main__":
    main()
