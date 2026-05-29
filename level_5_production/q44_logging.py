# Q44 — Production: Logging
# print() is for practice. In production code, use the logging module.
#
# 1. Set up a logger for a module called "rag_pipeline":
#    - Log to both console AND a file called "app.log"
#    - Format: "2024-01-01 12:00:00 - rag_pipeline - INFO - message"
#    - Console shows INFO and above, file captures DEBUG and above
#
# 2. Write a function process_query(query) that:
#    - logs DEBUG: "Processing query: {query}"
#    - logs INFO: "Query processed successfully"
#    - logs ERROR if query is empty: "Empty query received"
#
# import logging
