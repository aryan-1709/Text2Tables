
---

# Text2Tables

[![Python](https://img.shields.io/badge/Python-100%25-blue.svg)](https://www.python.org/)  
This project provides a seamless way to convert natural language text prompts into SQL queries and execute them on a vehicle dataset created using SQLite3. It leverages the power of **LangChain** and **SQLite3** to bridge the gap between human language and database management.

---

## ✨ Features

- **Natural Language to SQL Conversion:** Generate SQL queries from simple text prompts.
- **SQL Query Execution:** Execute the generated SQL queries directly on a vehicle dataset stored in SQLite3.
- **LangChain Integration:** Utilize advanced language models for accurate query generation.
- **SQLite3 Support:** Lightweight and efficient database management.
- **User-Friendly:** Simplifies database interactions for non-technical users.

---

## 🔧 Technologies Used

- **Python:** The core language used for implementation.
- **LangChain:** A framework for building applications powered by large language models.
- **SQLite3:** A lightweight and self-contained database engine.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aryan-1709/Text2Tables.git
   cd Text2Tables
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Input your natural language prompt when prompted, and the system will:
   - Generate the corresponding SQL query.
   - Execute the query on the vehicle dataset stored in SQLite3.
   - Display the results of the query.

---

## 📂 Project Structure
```plaintext
Text2Tables/
├── main.py            # Main script to run the application
├── requirements.txt   # List of dependencies
├── README.md          # Project documentation
├── DB                 # csv files of vehicle dataset
└── CreateDB           # Scripts to create sqlite3 database

```

---

## 🛠 Future Enhancements
- Support for additional database engines (e.g., MySQL, PostgreSQL).
- Enhanced language model capabilities for complex queries.
- Web-based interface for broader accessibility.
