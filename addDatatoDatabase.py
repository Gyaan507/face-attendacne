import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Gyaneshwar Kumar",
            "major": "Robotics",
            "starting_year": 2001,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Virat Kohli",
            "major": "Economics",
            "starting_year": 2022,
            "total_attendance": 18,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "963852":
        {
            "name": "M S Dhoni",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "632042":
        {
            "name": "Elon Musk",
            "major": "Robotics",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)