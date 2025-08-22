# 📘 UIU Faculty Schedule App

![GitHub repo size](https://img.shields.io/github/repo-size/TashinParvez/uiu-faculty-schedule-app)
![GitHub contributors](https://img.shields.io/github/contributors/TashinParvez/uiu-faculty-schedule-app)
![GitHub last commit](https://img.shields.io/github/last-commit/TashinParvez/uiu-faculty-schedule-app)
![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=TashinParvez.uiu-faculty-schedule-app)

A modern, mobile-friendly web application to **search and view faculty schedules** at **United International University (UIU)**.
Students can easily find `faculty information`, see their **undergrad & grad routines**, and quickly check **today’s availability/free slots** to plan visits.

---

## ✨ Features

- **Smart Search** – Search by **faculty name** or **code** with live suggestions
- **Faculty Info** – Quick access to name, designation, room, and **email**
- **Today’s Availability** – Automatically highlights today’s classes, counseling, and free time slots
- **Routine Tables** – Separate **Undergrad** and **Graduate** schedules in a clean tabular view

- **Color-coded Routine**

  - 🟩 **Class (CH)** → Blue
  - 🟦 **Counseling Hour (CnH)** → Green
  - 🟨 **Office Hour (OH)** → Yellow
  - ⬜ **Empty Slot** → White

- **Responsive UI** – Looks great on **mobile devices** as well as desktops

---

## 🖼️ Demo Preview

<img width="1920" height="932" alt="1" src="https://github.com/user-attachments/assets/bcd2a3f6-f7cd-4824-b164-d1a59e3359f3" />
<img width="1304" height="734" alt="2" src="https://github.com/user-attachments/assets/b1a2b5fe-0276-42da-9a23-5892dfa1753e" />
<img width="1734" height="867" alt="3" src="https://github.com/user-attachments/assets/a9721ac5-49e5-46f7-b44d-4923862a5ca4" />
<img width="1880" height="925" alt="4" src="https://github.com/user-attachments/assets/74119c5e-f567-4b66-8754-71c6cc76a713" />


---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (Bootstrap + custom styles), JavaScript
- **Data Source**: `UIU Class Routine - Summer25 by UIU CSE Dept`
- **Responsive Design**: Mobile-first approach

---

## 📂 Project Structure

```
faculty-schedule-app/
│
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── faculty_data.json        # Generated JSON file with parsed faculty schedules
├── templates/               # HTML templates for web pages
│   ├── index.html           # Search page (Main Page)
│   ├── schedule.html        # Faculty schedule display page
│   ├── admin.html           # Admin upload page (local only)
├── uploads/                 # Temporary folder for uploaded XLSX files
└── .gitignore               # Git ignore file
```

---

## 🚀 Getting Started

1. **Clone this repo**

   ```bash
   git clone https://github.com/yourusername/uiu-faculty-schedule-app.git
   cd uiu-faculty-schedule-app
   ```

2. **Open in Browser**
   Just double-click `index.html` or run with a simple server:

   ```bash
   python -m http.server 8080
   ```

   Then go to 👉 `http://localhost:8080`

---

## 📖 Usage

- Start typing a **faculty name** or **code** in the search bar.
- Suggestions will appear — select a faculty.
- Instantly see:

  - Personal details (designation, room, email)
  - **Today’s free/busy schedule**
  - Full **Undergrad & Grad routines**

---

## 📊 Example JSON Data

```json
{
  "MdTH": {
    "code": "MdTH",
    "name": "Md. Tarek Hasan",
    "designation": "Lecturer",
    "room": "319",
    "email": "tarek@cse.uiu.ac.bd",
    "undergrad": {
      "times": [
        "08:31 AM - 09:50 AM",
        "09:51 AM - 11:10 AM",
        "11:11 AM - 12:30 PM"
      ],
      "schedule": {
        "SAT": ["CnH", "CnH", "CSE 2216 (A): 427"],
        "SUN": ["DS 3885 (BA): 405", "CnH", "CSE 2215 (G): 308"]
      }
    },
    "grad": {
      "times": ["08:00 AM - 10:30 AM", "10:30 AM - 01:00 PM"],
      "schedule": {}
    }
  }
}
```

---

## 🤝 Contributing

We love contributions! 🎉 Whether it's reporting a bug, suggesting a feature, or improving the project, your help is welcome.

### How to Contribute

1. **Report Bugs**

   - Open an **issue** describing the bug clearly. Include steps to reproduce and screenshots if possible.

2. **Suggest Features**

   - Open an **issue** with a clear description of the feature and its benefits.

3. **Submit Improvements**

   - Fork the repository.
   - Create a new branch: `git checkout -b feature/your-feature-name`
   - Make your changes and commit: `git commit -m "Add your message"`
   - Push to your branch: `git push origin feature/your-feature-name`
   - Open a **pull request** and explain your changes.

---

## 👨‍💻 Author

**Md. Tashin Parvez** – CSE Student & Competitive Programmer

- 🌐 [GitHub](https://github.com/TashinParvez)
- 📖 Blog: [Hashnode](https://tashinparvez.hashnode.dev/)

---

#### 🌐 Contact Me

Reach out for questions, suggestions, or feedback:

<p align="left">
  <a href="mailto:tashinparvez2002@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://linkedin.com/in/tashinparvez" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://www.youtube.com/@tashinparvez" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube" />
  </a>
</p>

#### 🏆 Competitive Programming Profiles

<p align="left">
  <a href="https://codeforces.com/profile/tashin.parvez" target="_blank">
    <img src="https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=Codeforces&logoColor=white" alt="Codeforces" />
  </a>
  <a href="https://leetcode.com/tashinparvez/" target="_blank">
    <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=white" alt="LeetCode" />
  </a>
  <a href="https://www.hackerrank.com/tashinparvez?hr_r=1" target="_blank">
    <img src="https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white" alt="HackerRank" />
  </a>
  <a href="https://auth.geeksforgeeks.org/user/tashinparvez" target="_blank">
    <img src="https://img.shields.io/badge/GeeksforGeeks-0F9D58?style=for-the-badge&logo=GeeksforGeeks&logoColor=white" alt="GeeksforGeeks" />
  </a>
  <a href="https://www.codechef.com/users/tashin_parvez" target="_blank">
    <img src="https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=CodeChef&logoColor=white" alt="CodeChef" />
  </a>
</p>
