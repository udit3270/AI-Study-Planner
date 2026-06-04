# AI Study Planner
An AI-powered study planning web application built using Django, PostgreSQL, and Groq AI. The platform helps students create personalized study roadmaps, track study sessions, maintain learning streaks, manage notes, and visualize study progress.

## Features

### AI Study Roadmap Generator
* Generate personalized study roadmaps using AI.
* Automatically creates learning topics for a subject.
* Generates day-wise study schedules.
* Supports target completion days.
* Generates revision plans.

### Subject Management
* Add subjects.
* Edit subjects.
* Delete subjects.
* Set difficulty level.
* Set target completion days.

### ⏱ Study Session Tracking
* Record study sessions.
* Track study duration.
* Mark sessions as completed.
* View study history.

### Pomodoro Timer
* Select study subject.
* Choose study duration.
* Start, pause, and reset timer.
* Automatically saves completed study sessions.

### Daily Streak System
* Current streak tracking.
* Longest streak tracking.
* Automatically updates after completed sessions.

### Notes Management
* Create notes.
* Upload files.
* Store study resources.
* Manage personal learning notes.

### Analytics Dashboard
* Total subjects.
* Total study sessions.
* Total study time.
* Current study streak.
* Subject-wise study charts using Chart.js.

### Modern UI
* Glassmorphism design.
* Responsive layout.
* Dark theme.
* Interactive dashboard.
* Smooth hover effects.

---

## 🛠 Tech Stack
### Backend
* Python
* Django

### Database
* PostgreSQL

### AI Integration
* Groq API
* Llama 3.3 70B Versatile

### Frontend
* HTML
* CSS
* JavaScript
* Chart.js

---

## Project Structure
```text
AI_Study_Planner/
│
├── accounts/
├── planner/
├── notes/
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Study-Planner.git
cd AI-Study-Planner
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## Future Enhancements
* PDF Export for AI Roadmaps
* Weekly Analytics Dashboard
* User Profile Settings
* Achievement Badges
* Email Reminders
* Mobile Responsive Improvements

---

## Author
Developed by Udit Virakt

