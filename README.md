### 🚢 **Titanic Survival Prediction – Flask Web App**
This project is an end-to-end data science and web development solution for predicting Titanic passenger survival. It combines data analysis, machine learning, and a user-friendly Flask web application with authentication.
---
**Features**
- User Signup & Login: Secure registration and login system with session management.
- Prediction Page: Users can enter passenger details and get a prediction (“Survived” or “Died”).
- Logout: Users can securely log out, returning to the login page.
- Beautiful UI: Titanic-themed design with a modern, responsive interface.
- File-based User Storage: User credentials are stored in a JSON file for demonstration purposes.
---
**How It Works**
**User Authentication:**
Users sign up and log in to access the prediction page. Sessions are managed using Flask’s session system.

**Prediction:**
After logging in, users fill out a form with passenger details (class, sex, age, siblings/spouses, parents/children, fare, embarkation port). The app uses a pre-trained machine learning model to predict survival.

**Result Display:**
The app displays a clear message: “Survived” or “Died,” based on the model’s prediction.

**Logout:**
Users can log out at any time, which ends their session and returns them to the login page.

---

**Tools & Technologies**
Python (Flask, pickle, numpy, json)
scikit-learn (for model training and serialization)
HTML/CSS (with Jinja2 templating)
Bootstrap/Custom CSS (for styling)
Git & GitHub (for version control and collaboration)
