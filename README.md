## 📌 Project Overview
The **Virtual Fashion Agent** is a Python-based shopping assistant that helps users find fashion products based on price, availability, shipping deadlines, and discounts. It also performs competitor price comparisons and return policy checks.

## 📁 Project Structure
```
📂 Project/  
│── 📂 src/  
│   │── 📂 logs/  
│   │   │── interactions.log  # Annotated logs of agent queries and responses  
│   │── tools.py  # Mock functions for tools  
│   │── agent.py  # Agent logic and integration  
│── README.md  # Project documentation  
│── requirements.txt  # Dependencies  
│── .gitignore  # Files to exclude from GitHub  

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository


git clone https://github.com/UmangSonika/Project.git
cd Project


### 2️⃣ Create a Virtual Environment (Recommended)
#### **For Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **For Mac/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## 🚀 Running the Agent
To start the Virtual Fashion Agent, run:
```sh
python src/agent.py
```

## 🛠 Features & Supported Queries
### ✅ **Task A: Basic Item Search + Price Constraint**
- **Query:** “Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code ‘SAVE10’?”
- **Tools Used:** `search_products`, `apply_discount`

### ✅ **Task B: Shipping Deadline**
- **Query:** “I need white sneakers (size 8) for under $70 that can arrive by Friday.”
- **Tools Used:** `search_products`, `estimate_shipping`

### ✅ **Task C: Competitor Price Comparison**
- **Query:** “I found a ‘casual denim jacket’ at $80 on SiteA. Any better deals?”
- **Tools Used:** `compare_prices`

### ✅ **Task D: Returns & Policies**
- **Query:** “I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?”
- **Tools Used:** `get_return_policy`

### ✅ **Task E: Multi-Tool Query Handling**
- **Query:** “Find sneakers under $80 that can arrive by Friday, and check if a discount applies.”
- **Tools Used:** `search_products`, `estimate_shipping`, `apply_discount`

## 📜 Logging Interactions
All interactions are logged in `logs/interactions.log`. If logs are not appearing, ensure the `logs/` folder exists:
```sh
mkdir logs
```

## 🛑 Stopping the Agent
To exit, type:
```sh
exit
```
