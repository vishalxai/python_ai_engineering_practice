# Q48 — Production: FastAPI CRUD
# Build a full in-memory CRUD API for a "notes" resource.
#
# Models (Pydantic):
#   - NoteCreate: title (str), content (str)
#   - NoteResponse: id (int), title, content
#
# Endpoints:
#   GET    /notes          → return all notes
#   GET    /notes/{id}     → return one note, 404 if not found
#   POST   /notes          → create a note, return it with generated id
#   DELETE /notes/{id}     → delete a note, 404 if not found
#
# Store notes in a dict: notes_db = {}
# Use a counter for IDs.
#
# To run: uvicorn q48_fastapi_crud:app --reload
