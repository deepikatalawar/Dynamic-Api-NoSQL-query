# Dynamic API for NoSQL Query

## Overview
This project implements a dynamic backend API for querying NoSQL databases like MongoDB. The API allows users to specify collections, filter conditions, and fields to project, supporting complex queries, aggregation pipelines, and advanced query options such as sorting, limiting, and skipping results.

---

## Features
- Supports complex filter operations (e.g., `$and`, `$or`, `$gte`, `$lte`).
- Allows sorting, limiting, and skipping results.
- Validates user inputs to ensure robust and secure operations.
- Provides aggregation pipeline support for advanced queries like grouping and summation.
- Optimized database performance with proper indexing.

---

## Requirements
- Python 3.9+
- MongoDB (Compass or CLI)
- Dependencies listed in `requirements.txt`

---

## Installation and Setup

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-repo/dynamic-api-nosql-query.git
cd dynamic-api-nosql-query
```

---

### **Step 2: Set Up Python Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate     # For Windows
```

---

### **Step 3: Install Dependencies**
Install the necessary dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

Dependencies:
- `fastapi`: Framework for building APIs.
- `pymongo`: MongoDB driver for Python.
- `uvicorn`: ASGI server for running FastAPI applications.
- `python-dotenv`: Manage environment variables.

---

### **Step 4: Configure MongoDB**

#### **Option 1: Using MongoDB Compass**
1. Launch MongoDB Compass and create a database named `dynamic_api_db`.
2. Create the following collections: `orders`, `users`, `products`.
3. Import CSV files for each collection using the **Import Data** option in Compass.

#### **Option 2: Using MongoDB CLI**
```bash
mongoimport --uri "mongodb://localhost:27017/dynamic_api_db" --collection orders --type csv --headerline --file orders.csv
mongoimport --uri "mongodb://localhost:27017/dynamic_api_db" --collection users --type csv --headerline --file users.csv
mongoimport --uri "mongodb://localhost:27017/dynamic_api_db" --collection products --type csv --headerline --file products.csv
```

---

### **Step 5: Configure Environment Variables**
1. Create a `.env` file in the project root.
2. Add the following variables:
```env
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=dynamic_api_db
```

---

### **Step 6: Start the Application**
Run the application using Uvicorn:
```bash
uvicorn app.main:app --reload
```

The server will start at: `http://127.0.0.1:8000`

---

## Usage

### **API Endpoints**

#### **1. Query Data**
Endpoint: `POST /query`

**Payload Format:**
```json
{
  "collection": "orders",
  "filter": { "status": "completed" },
  "projection": { "order_id": 1, "total_amount": 1, "_id": 0 },
  "sort": { "total_amount": -1 },
  "limit": 5,
  "skip": 0
}
```

**Response Example:**
```json
{
  "status": "success",
  "data": [
    { "order_id": 1010, "total_amount": 5000 },
    { "order_id": 1007, "total_amount": 3000 }
  ]
}
```

#### **2. Aggregation Query**
Endpoint: `POST /query`

**Payload Format:**
```json
{
  "collection": "orders",
  "aggregation": [
    { "$match": { "status": "completed" } },
    { "$group": { "_id": "$category", "total_amount": { "$sum": "$total_amount" } } },
    { "$sort": { "total_amount": -1 } }
  ]
}
```

**Response Example:**
```json
{
  "status": "success",
  "data": [
    { "_id": "Electronics", "total_amount": 9500 },
    { "_id": "Furniture", "total_amount": 3000 }
  ]
}
```

---

### **Testing the API with Curl**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/query' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "collection": "orders",
  "filter": { "status": "completed" },
  "projection": { "order_id": 1, "total_amount": 1, "_id": 0 }
}'
```

---

## Additional Notes
- Ensure MongoDB is running locally or update `MONGO_URI` to point to your MongoDB instance.
- To secure the API, consider adding authentication mechanisms such as JWT.

---

## CSV Files for Collections
Ensure the following CSV files are prepared and imported:

### **1. Orders**
| _id | order_id | user_id | product_id | quantity | total_amount | status     | category           | order_date             |
|-----|----------|---------|------------|----------|--------------|------------|--------------------|------------------------|
| 1   | 1001     | 1       | 101        | 1        | 1000         | completed  | Electronics        | 2023-12-01T00:00:00Z  |
| 2   | 1002     | 2       | 102        | 2        | 2000         | completed  | Electronics        | 2023-12-02T00:00:00Z  |

### **2. Users**
| _id | user_id | name       | email              | address         |
|-----|---------|------------|--------------------|-----------------|
| 1   | 1       | John Doe   | john.doe@gmail.com | 123 Elm Street  |
| 2   | 2       | Jane Smith | jane.smith@gmail.com| 456 Oak Avenue |

### **3. Products**
| _id | product_id | name            | category     | price |
|-----|------------|-----------------|--------------|-------|
| 1   | 101        | Smartphone      | Electronics  | 500   |
| 2   | 102        | Laptop          | Electronics  | 1000  |

---

## License
This project is licensed under the MIT License.

