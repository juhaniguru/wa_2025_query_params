from random import choice

from db import connect


if __name__ == '__main__':
    first_names = ["Olivia", "Noah", "Emma", "Liam", "Ava", "William", "Sophia", "Benjamin", "Isabella", "James", "Mia",
                   "Ethan", "Charlotte", "Alexander", "Amelia", "Daniel", "Abigail", "Michael", "Emily", "Elijah",
                   "Chloe", "Jackson", "Victoria", "Aiden", "Scarlett", "Lucas", "Madison", "Mason", "Lily", "Jackson",
                   "Avery", "Sofia", "Caleb", "Aubrey", "Evelyn", "Owen", "Addison", "Ezekiel", "Natalie", "Grayson",
                   "Brooklyn", "Lincoln", "Elizabeth", "Jaxon", "Hannah", "Asher", "Eleanor", "Julian", "Riley"]

    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
                  "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore",
                  "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Lewis",
                  "Robinson", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Green", "Baker", "Adams",
                  "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker",
                  "Evans", "Edwards", "Collins", "Stewart"]

    with connect() as conn:
        cur = conn.cursor()
        try:
            _qry = "INSERT INTO users(name, email, department_id) VALUES (?, ?, ?);"
            for i in range(1000):
                fname = choice(first_names)
                lname = choice(last_names)
                name = fname + " " + lname
                email = f'{fname}.{lname}@mail.example'
                cur.execute(_qry, (name, email, choice([1, 2, 3]) ))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cur.close()

