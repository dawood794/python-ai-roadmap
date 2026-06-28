import sqlite3
from passlib.context import CryptContext

# Setup password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class NexusDatabase:
    def __init__(self, db_name="nexus_secure.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            conn.commit()
        print("📁 Nexus Secure Database Schema initialized successfully.")

    def create_user(self, email, password):
        hashed_password = pwd_context.hash(password)
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (email, password) VALUES (?, ?)",
                    (email.lower().strip(), hashed_password)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False  # Email already exists

    def verify_user(self, email, password):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE email = ?", (email.lower().strip(),))
            row = cursor.fetchone()
            
            if row and pwd_context.verify(password, row[0]):
                return {"email": email.lower().strip()}
            return None