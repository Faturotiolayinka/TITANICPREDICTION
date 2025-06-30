
## 🚢 **Titanic Survival Prediction – End-to-End Flask Web App**

**Project Type:** Machine Learning · Web Development · User Authentication
**Goal:** Predict whether a Titanic passenger survived based on their personal details, wrapped in a secure and interactive web application.

---

### ✅ **Problem Statement**

Predicting passenger survival on the Titanic is a classic binary classification problem. This project goes beyond building a machine learning model by delivering a **complete, production-style Flask web app** with **user authentication** and **interactive prediction**.

---

### 🎯 **Objective**

To create an end-to-end application that allows users to:

* **Register/Login securely**
* **Input passenger details**
* **Get real-time survival predictions**
* **Log out safely**
  All within a **responsive, themed user interface**.

---

### 🌟 **Key Features**

* **🔐 User Signup & Login:** Secure authentication system with session tracking
* **📊 Prediction Page:** Fill in passenger data and get a live prediction: *Survived* or *Died*
* **🚪 Logout Functionality:** Ends user sessions cleanly and redirects to login
* **🎨 Titanic-Themed UI:** Modern, responsive design with Bootstrap and custom CSS
* **🗃️ JSON-based Storage:** Lightweight file-based system for user credentials (demo-friendly)

---

### ⚙️ **How It Works**

1. **Authentication:**
   Users create an account or log in using Flask sessions. JSON file simulates basic credential storage.
2. **Prediction Workflow:**

   * User fills a form: `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`
   * Form data is passed to a **pre-trained ML model** (serialized with `pickle`)
   * Model returns either **"Survived"** or **"Died"**
3. **Logout:**
   Session is cleared and the user is safely redirected to the login screen.

---

### 🛠️ **Tools & Technologies**

* **Backend:** Python, Flask, Flask Sessions, JSON
* **ML Model:** Trained with `scikit-learn` (e.g., Logistic Regression or Random Forest)
* **Frontend:** HTML, CSS, Bootstrap, Jinja2
* **Utilities:** Pickle (model storage), Git & GitHub (version control)

---

### 🧰 **Skills Demonstrated**

* End-to-end machine learning implementation
* Web application development using Flask
* User authentication with session management
* Data preprocessing, model training, and deployment
* Clean UI/UX design principles
* Integration of ML into web environments

---

### 🚀 **Impact & Portfolio Value**

This project simulates a **real-world web product** that:

* Engages users interactively
* Showcases the full ML lifecycle (from training to deployment)
* Demonstrates practical implementation of **user authentication + ML in production**

 
