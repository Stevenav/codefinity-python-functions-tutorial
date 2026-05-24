users_db = []

def add_user(name, age, role="user", status="active"):
    # Check if the user already exists
    for user in users_db:
        if  user["name"] == name:
            # Update the user if they already exist
            user["age"] = age
            user["role"] = role
            user["status"] = status
            return f"User {name} updated successfully!"
    
    # Add a new user if they don't exist
    new_user = {
        "name": name,
        "age": age,
        "role": role,
        "status": status
    }
    users_db.append(new_user)
    return f"User {name} added successfully!"

# Testing the result
print(add_user("Alice", 30))
print(add_user("Bob", 25, role="admin"))
print(add_user("Alice", 31, status="inactive")) 

# Check the list of users
print(users_db)