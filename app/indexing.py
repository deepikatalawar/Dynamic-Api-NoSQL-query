from app.database import db  # Import your MongoDB connection object

def create_indexes():
    """
    Create necessary indexes for MongoDB collections.
    """
    try:
        # Index for the 'users' collection
        db["users"].create_index([("age", 1)])  # Ascending index on 'age'

        # Compound index for the 'orders' collection
        db["orders"].create_index([("category", 1), ("status", 1)])  # Index on 'category' and 'status'

        # Additional indexes as needed
        db["products"].create_index([("price", -1)])  # Descending index on 'price'

        print("Indexes created successfully!")
    except Exception as e:
        print(f"Error creating indexes: {e}")
