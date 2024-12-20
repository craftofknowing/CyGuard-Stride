# CockroachDB Text Content Storage

This Python program provides functionality to create a database schema in CockroachDB and store text content.

## Prerequisites

- Python 3.7+
- CockroachDB instance
- Required Python packages (install using `pip install -r requirements.txt`):
  - psycopg2-binary
  - sqlalchemy

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your CockroachDB connection:
   - Set the `DATABASE_URL` environment variable with your CockroachDB connection string
   - Or modify the default connection string in `db_operations.py`

## Usage

1. Run the program:
   ```bash
   python db_operations.py
   ```

2. To use in your own code:
   ```python
   from db_operations import init_db, insert_text
   
   # Initialize the database schema
   init_db()
   
   # Insert text content
   insert_text("Your Title", "Your content here")
   ```

## Database Schema

The program creates a table called `text_contents` with the following columns:
- `id`: Integer (Primary Key)
- `title`: String (100 characters max)
- `content`: Text
