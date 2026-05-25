def validate_registration(username, email, password):
    errors = []
    if len(username) < 3:
        errors.append("Username must be at least 3 characters long.")
    if "@" not in email:
        errors.append("Invalid email format.")
    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")

    return len(errors) == 0, errors

# Testing the result
is_valid, errors = validate_registration("js", "userexample.com", "123")
print("Validation successful:", is_valid)
print("Errors:", errors)