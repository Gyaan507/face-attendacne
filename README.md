# 🎯 Face Recognition Attendance System

A real-time face recognition–based attendance system built using Python and OpenCV. It detects and recognizes faces via webcam and automatically marks attendance into a Firebase Realtime Database or Firestore.

---

## 🛠️ Features

- Real-time face detection using webcam
- Automatic attendance marking in Firebase
- Student registration via image and JSON
- Avoids duplicate attendance entries
- UI display with background and mode overlay
- Fast face matching with cached encodings (`pickle`)

---

## 🚀 Tech Stack

- Python 3.10+
- OpenCV
- face_recognition
- Firebase Admin SDK
- NumPy
- SQLAlchemy (optional)

---

## 🔥 Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project
3. Generate a service account key (Project Settings → Service Accounts)
4. Download and save it as `serviceAccountKey.json` in the root folder
5. Use either Firestore or Realtime Database:
   - `students` collection (id, name, roll_no, department)
   - `attendance` collection (student_id, timestamp)

---

## ⚙️ How to Run

```bash
pip install opencv-python face_recognition numpy firebase-admin
python EncodeGenerator.py
python sync_students.py  # optional
python main.py
