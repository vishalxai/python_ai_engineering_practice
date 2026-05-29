# Q58 — AI Engineering: MongoDB Basics
# MongoDB is used in AI apps for storing documents, chat history, and metadata.
#
# Write functions for a "documents" collection:
#
# 1. insert_document(collection, data: dict) → inserts and returns the inserted id
#
# 2. find_by_field(collection, field, value) → returns list of matching documents
#
# 3. find_recent(collection, n=10) → returns last n documents by created_at
#
# 4. update_metadata(collection, doc_id, metadata: dict) → updates the metadata field
#
# 5. delete_document(collection, doc_id) → deletes by _id
#
# Use pymongo. Connect to local MongoDB: mongodb://localhost:27017
# Database: "ai_app", Collection: "documents"
#
# from pymongo import MongoClient
# from bson import ObjectId
# from datetime import datetime
#
# pip install pymongo
