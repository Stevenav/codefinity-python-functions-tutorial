def generate_report(*args, **kwargs):
    label = kwargs.get("label", "Report")
    avg = sum(args) / len(args)

    if "passing_score" in kwargs:
        status = "Pass" if avg >= kwargs["passing_score"] else "Fail"
        return f"{label} | Average: {avg:.2f} | Status: {status}"

    return f"{label} | Average: {avg:.2f}"

# Testing the result
print(generate_report(80, 90, 70, label="Math", passing_score=75))
print(generate_report(50, 60, 40, passing_score=65))
print(generate_report(95, 88, 92, label="Science"))