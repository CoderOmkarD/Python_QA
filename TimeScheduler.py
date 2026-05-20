import schedule
import time
import datetime


def fun_minute():
    print("Current time is:", datetime.datetime.now())
    print("Scheduler executed after 1 minute\n")


def fun_hour():
    print("Current time is:", datetime.datetime.now())
    print("Scheduler executed after 1 hour\n")


def fun_day():
    print("Current time is:", datetime.datetime.now())
    print("Scheduler executed on specific day\n")


def fun_afternoon():
    print("Current time is:", datetime.datetime.now())
    print("Scheduler executed at 12:00\n")


def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")
    print("Python Job Scheduler Started")
    print("Start time:", datetime.datetime.now(), "\n")

    # Scheduling jobs
    schedule.every(1).minutes.do(fun_minute)
    schedule.every(1).hour.do(fun_hour)
    schedule.every().day.at("12:00").do(fun_afternoon)
    schedule.every().sunday.do(fun_day)
    schedule.every().saturday.at("18:30").do(fun_day)

    # Infinite loop to keep scheduler running
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
