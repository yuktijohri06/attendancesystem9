import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{

'databaseURL':"https://attendancesystem-ae597-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "300190":
        {
            "name": "elon musk",
            "major": "Robotics",
            "starting_year":2020 ,
            "total_attendance":6,
            "standing": "E",
            "year":4,
            "last_attendance_time": "2024-04-20 00:54:34"
        },

    "300191":
        {
            "name": "barbara pelvin",
            "major": "Faishon designing",
            "starting_year":2023,
            "total_attendance":9,
            "standing": "G",
            "year":1,
            "last_attendance_time": "2024-04-20 00:54:34"
        },
    "300192":
        {
            "name": "Rihanna",
            "major": "music",
            "starting_year":2022,
            "total_attendance":18,
            "standing": "B",
            "year":2,
            "last_attendance_time": "2024-04-20 00:54:34"
        },
    "300193":
        {
            "name": "Selena Gomez",
            "major": "Medical",
            "starting_year": 2020,
            "total_attendance": 30,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2024-04-20 00:54:34"
        },
    "300194":
        {
            "name": "Lakshmi Johri",
            "major": "Astrology",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2024-04-20 00:54:34"

        },
    "300195":
        {
            "name": "Khyati Johri",
            "major": "Devlopment",
            "starting_year": 2020,
            "total_attendance": 40,
            "standing": "E",
            "year": 4,
            "last_attendance_time": "2024-04-20 00:54:34"

        },
    "300196":
        {
            "name": "BB Johri",
            "major": "Economics",
            "starting_year": 2020,
            "total_attendance": 40,
            "standing": "E",
            "year": 4,
            "last_attendance_time": "2024-04-20 00:54:34"

        }

}

for key,value in data.items():
    ref.child(key).set(value)