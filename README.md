# 🧠✨ AI-Powered Code Review Assistant

This project is an **AI-integrated web application** built with **Django**, **Python**, and **Google’s Gemini AI**.  
It helps developers automatically **analyze**, **review**, and **get natural language explanations** for their source code.

---

## 🚀 Features

✅ Paste any Python code snippet  
✅ Get a clear, beginner-friendly explanation using **Gemini AI**  
✅ Automatically detect common bugs and coding issues with **pylint**  
✅ Get improvement suggestions and a quality score  
✅ Built as an API backend with **Django REST Framework**

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework  
- **AI**: Google Gemini AI (`google-generativeai` SDK)  
- **Static Code Analysis**: Pylint  
- **Frontend**: Basic HTML form (can be expanded with React or Vue)

---

## 📂 Project Structure

![image](https://github.com/user-attachments/assets/05253c64-9b80-4166-a77d-3eba7799d38b)


---

## ⚙️ How It Works

1. **User** submits a Python code snippet.  
2. The backend runs `pylint` to detect errors and warnings.  
3. The code is sent to **Gemini AI** for a plain English explanation.  
4. The combined result is returned as JSON: explanation, bugs, suggestions, and a score.

---

## 🚦 How To Run Locally

```bash
# 1️⃣ Clone the repo
git clone https://github.com/<your-username>/code_review_ai.git
cd code_review_ai

# 2️⃣ Create & activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add your Gemini API key
export GOOGLE_API_KEY="YOUR_API_KEY"  # or set in your .env

# 5️⃣ Run the server
python manage.py runserver
```
---

## 🛠️ Requirements
- Python 3.10+ 
- Valid Gemini AI API key from Google AI Studio
- Pylint installed

---
## 📣 Future Improvements

✅ Add user authentication

✅ Add frontend code editor (Ace or Monaco)  

✅ Support for multiple languages (JavaScript, Java, etc.) 

✅ Dockerize for easy deployment 

---
## 👋 Author
Developed by **marysangeetha22** - Mary Sangeetha Anthony Adimai, Python Developer
- Email: marysangeetha22@gmail.com
- Linkedin: https://www.linkedin.com/in/mary-sangeetha/
