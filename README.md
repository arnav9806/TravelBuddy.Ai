# TravelBuddy AI - Project Setup ✈️

## Prerequisites

Make sure you have:

* Python 3.11.0 installed
* PostgreSQL installed and running

Check Python version:

```bash
python --version
```

---

# Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd TravelBuddy.Ai
```

---

# Step 2: Create Virtual Environment

```bash
py -3.11 -m venv venv
```

OR

```bash
python -m venv venv
```

---

# Step 3: Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

# Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

---

# Step 5: Create `.env` File

Create a `.env` file in the root directory and add:

```env
AVIATIONSTACK_API_KEY=""
TAVILY_API_KEY=""
GROQ_API_KEY=""

DATABASE_URL=""
```

---

# Step 6: Run the Project

```bash
streamlit run frontend/app.py
```

The application will start locally in your browser.
