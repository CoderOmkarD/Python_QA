import schedule

import time
import datetime


def fun():
    print("Inside fun at :", datetime.datetime.now())


def main():
    print("Inside Marvellous Automation Script At :", datetime.datetime.now())

    schedule.every(20).seconds.do(fun)
    #issue

if __name__ == "__main__":
    main()
