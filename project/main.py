import mysql.connector as ms


conn = ms.connect(host="localhost", user="root", password="nkbps", database="project")
cursor = conn.cursor()


def calc_mission_outcome():
    total, successful = 0, 0
    cursor.execute("SELECT MissionOutcome FROM Launches;")
    outcomes = cursor.fetchall()
    for outcome in outcomes:
        if "Success" in str(outcome):
            successful += 1
        total += 1
    success_rate = round(successful / total * 100, 2)
    print(f"Success rate for mission is {success_rate} %")


def calc_landing_outcome():
    total, successful = 0, 0
    cursor.execute("SELECT LandingOutcome FROM Launches;")
    outcomes = cursor.fetchall()
    for outcome in outcomes:
        if "Success" in str(outcome):
            successful += 1
        total += 1
    success_rate = round(successful / total * 100, 2)
    print(f"Success rate for landing is {success_rate} %")


def main():
    calc_mission_outcome()
    calc_landing_outcome()


if __name__ == "__main__":
    main()
