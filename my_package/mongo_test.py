from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Select database
db = client['mydatabase']

# Select collection (similar to a table in relational databases)
collection = db['mycollection']

def insert_data():
    # Insert a single document
    document = {"name": "Alice", "age": 25, "city": "New York"}
    collection.insert_one(document)

    # Insert multiple documents
    documents = [
        {"name": "Bob", "age": 30, "city": "Chicago"},
        {"name": "Charlie", "age": 35, "city": "San Francisco"}
    ]
    collection.insert_many(documents)
    print("Data inserted successfully")

def query_data():
    # Query a single document
    result = collection.find_one({"name": "Alice"})
    print("Single document:", result)

    # Query multiple documents
    results = collection.find({"age": {"$gt": 25}})
    print("Multiple documents:")
    for doc in results:
        print(doc)

def update_data():
    # Update a single document
    collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})
    print("Single document updated")

    # Update multiple documents
    collection.update_many({"city": "Chicago"}, {"$set": {"city": "Boston"}})
    print("Multiple documents updated")

def delete_data():
    # Delete a single document
    collection.delete_one({"name": "Alice"})
    print("Single document deleted")

    # Delete multiple documents
    collection.delete_many({"age": {"$lt": 30}})
    print("Multiple documents deleted")

def aggregate_data():
    # Aggregation operation
    pipeline = [
        {"$match": {"age": {"$gt": 20}}},
        {"$group": {"_id": "$city", "average_age": {"$avg": "$age"}}}
    ]
    results = collection.aggregate(pipeline)
    print("Aggregated data:")
    for doc in results:
        print(doc)

if __name__ == "__main__":
    insert_data()
    query_data()
    update_data()
    delete_data()
    aggregate_data()
