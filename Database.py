import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Here,the credetials of the database are removed on purpose to maintain the security of the database.

ref = db.reference('AttendanceDatabase')

data = {
    "CE102":
        {
            "Name": "Manan Patel",
            "RollNo": "CE102",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        },
    "CE153":
        {
            "Name": "Malay Vyas",
            "RollNo": "CE153",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        },
    "CE111":
        {
            "Name": "Ashish Prajapati",
            "RollNo": "CE111",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        },
    "CE014":
        {
            "Name": "Jainil Chauhan",
            "RollNo": "CE014",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        },
    "CE028":
        {
            "Name": "Mann Desai",
            "RollNo": "CE028",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        },
    "CE112":
        {
            "Name": "Tirth Parajapati",
            "RollNo": "CE112",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        },
    "CE030":
        {
            "Name": "Om Dhingara",
            "RollNo": "CE030",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        },
    "CE059":
        {
            "Name": "Vineet",
            "RollNo": "CE059",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        },
    "CE137":
        {
            "Name": "Mahipal Suchar",
            "RollNo": "CE137",
            "Semester": 4,
            "Department": "CE",
            "AttendedLectures": 0,
            "TotalLectures": 0,
            "PrecentAttendance": 0,
            "LastAttendanceTime": "2023-02-18 11:57:55"
        }

}


def add(name: str, rollno: str, sem: int, branch: str):
    data = {
        rollno:
            {
                "Name": name,
                "RollNo": rollno,
                "Semester": sem,
                "Deaprtment": branch,
                "AttendedLectures": 0,
                "TotalLectures": 0,
                "LastAttendanceTime": "2023-02-18 11:57:55"
            }
    }
    for key, value in data.items():
        ref.child(key).set(value)

# for key,value in data.items():
#     ref.child(key).set(value)
