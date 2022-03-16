from faker import Faker
import uuid
import sqlite3

fake = Faker()

print(fake.name())
print(fake.first_name())
print(fake.email())
print(fake.password())

users = [
    {
        "user_id": str(uuid.uuid4()),
        "user_name": fake.first_name(),
        "user_email": fake.email(),
        "user_password": fake.password()
    }
    for _ in range(2)
]


with sqlite3.connect("database.db") as session:
    counter = session.executemany(
        "INSERT INTO users VALUES(:user_id, :user_name, :user_email, :user_password)", users
    ).rowcount
    if not counter:
        print("Oops :D")
    session.commit()
