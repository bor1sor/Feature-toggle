from faker import Faker

fake = Faker()

def test_generate_name():
    name = fake.name()
    assert len(name) > 0

def test_generate_email():
    email = fake.email()
    assert "@" in email

if __name__ == "__main__":
    test_generate_name()
    test_generate_email()
    print("All tests passed successfully!")