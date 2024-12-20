from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database connection settings
DB_URI = os.getenv('DATABASE_URL', 'cockroachdb://root@localhost:26257/defaultdb?sslmode=disable')

# Create SQLAlchemy engine
engine = create_engine(DB_URI)

# Create declarative base
Base = declarative_base()

class TextContent(Base):
    __tablename__ = 'text_contents'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)

def init_db():
    """Initialize the database schema"""
    Base.metadata.create_all(engine)
    print("Database schema created successfully!")

def insert_text(title: str, content: str):
    """Insert text content into the database"""
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        new_content = TextContent(title=title, content=content)
        session.add(new_content)
        session.commit()
        print(f"Successfully inserted content with title: {title}")
    except Exception as e:
        session.rollback()
        print(f"Error inserting content: {str(e)}")
    finally:
        session.close()

def main():
    # Initialize the database
    init_db()
    
    # Example usage
    sample_text = """
    This is a sample text content that will be stored in the database.
    It can contain multiple lines and paragraphs.
    """
    
    insert_text("Sample Title", sample_text)

if __name__ == "__main__":
    main()
