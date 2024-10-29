# backend
This is the backend for bytesorcery.com. For now, it is mostly responsible for accepting contact requests and storing them in a database.

## Tech Stack
- Python
- Flask
- Rye
- SQLite

## DB Schema
| Field         | Type           | Notes     |
|--------------|----------------|-----------|
| First Name   | String         |           |
| Last Name    | String         |           |
| Email        | String         |           |
| Phone Number | String         | Optional  |
| Message      | String         |           |
