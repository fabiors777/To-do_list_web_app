# Django To-Do CRUD App

A clean, class-based Django app to manage tasks with a simple business rule:  
**tasks are ordered by deadline; once a task is completed, the Edit and Complete actions are disabled (only Delete remains available).**

![App Screenshot – List View](docs/screenshot-list.png)
![App Screenshot – Form View](docs/screenshot-form.png)

---

## Features

- **Create / Read / Update / Delete** tasks (CRUD)
- **Business rule**:
  - Tasks are **sorted by delivery date (deadline)**
  - When a task is **completed**, the buttons **Edit** and **Complete** are **disabled**
  - Completed tasks can **only be deleted**
- **Class-Based Views** with clean URL patterns
- **Bootstrap 5** UI + **django-crispy-forms** for elegant forms

---

## Tech Stack

- **Python** (Django)
- **Django Class-Based Views**: `ListView`, `CreateView`, `UpdateView`, `DeleteView`, and a custom `View` for completion
- **Bootstrap 5** and **crispy-forms**
- SQLite (default) or any Django-supported DB

---

## Quick Start

### 1) Clone and set up the environment
```bash
git clone <your-repo-url>.git
cd <your-project-folder>

# (optional) create a virtual env
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
