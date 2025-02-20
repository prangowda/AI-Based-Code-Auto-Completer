
# 🚀 AI-Based Code Auto-Completer

## 📌 Overview  
This project is an **AI-based Code Auto-Completer** that predicts and generates code snippets based on user input using OpenAI's **Codex API** (GPT-3.5).  
It helps developers by suggesting **code completions** for various programming languages.

---

## **🛠️ Technologies Used**  
| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **OpenAI Codex API** | AI model for code generation |
| **Flask** | API development |
| **Transformers** | NLP processing |
| **dotenv** | Storing API keys securely |

---

## **📂 Project Structure**  
```
/AI_Code_Auto_Complete
│── main.py                     # API server
│── model_loader.py             # AI model integration
│── .env                        # API Key (DO NOT SHARE!)
│── requirements.txt            # Project dependencies
│── README.md                   # Documentation
```

---

## **🚀 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
gh repo clone prangowda/AI-Based-Code-Auto-Completer
cd AI_Code_Auto_Complete
```

### **2️⃣ Install Dependencies**  
```sh
pip install openai flask transformers python-dotenv
```

### **3️⃣ Set Up OpenAI API Key**  
Create a **.env** file and add your OpenAI API Key:  
```sh

Get OpenAI API Key
Sign up on OpenAI
Get your API Key from OpenAI Codex or GPT-3.
Store the key in an .env file:
  OPENAI_API_KEY="your_api_key_here"

```

### **4️⃣ Run the Flask Server**  
```sh
python main.py
```
This will launch the API at **http://127.0.0.1:5000/**.

---

## **📡 API Usage**  

### **📝 Example Request (Using Postman or cURL)**  
Send a **POST request** to `/autocomplete` with the input code.

#### **Request:**
```json
{
  "input_code": "def factorial(n):"
}
```

#### **Response:**
```json
{
  "suggestion": " if n == 0:\n    return 1\n else:\n    return n * factorial(n-1)"
}
```

---

## **🌟 Features**
✅ **AI-powered code completion** using OpenAI Codex  
✅ **Supports multiple programming languages**  
✅ **Can be integrated into VS Code as an extension**  
✅ **Fast and efficient code predictions**  

---

## **🚀 Enhancements & Future Improvements**
✅ Add **VS Code integration** for real-time AI suggestions  
✅ Train a **custom CodeBERT model** for better accuracy  
✅ Extend support for **multiple languages like C++, Java, JavaScript**  
✅ Deploy as a **browser extension** for online IDEs  

---

## **🤖 Contributions**
Want to improve this project?  
1. **Fork** this repository  
2. **Make your changes**  
3. **Create a pull request** 🚀  

---

## **💡 Conclusion**
This **AI-Based Code Auto-Completer** is a powerful tool to **enhance developer productivity** by providing **real-time AI-driven code predictions**.  
It can be integrated into **IDE extensions, web editors, and coding platforms** for a **seamless AI-powered coding experience**.

---

🚀 **Happy Coding!** 🚀  
