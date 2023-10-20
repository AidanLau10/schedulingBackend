# Define a list of classes and their durations
classes = [
    {"name": "Math", "duration": 2},
    {"name": "History", "duration": 1.5},
    {"name": "Science", "duration": 2},
    # Add more classes as needed
    # Add more time depending on how long you need to study
]

print("Here's your optimized schedule!")

while True:
    input("Press Enter for a personalized schedule")
    total_study_time = 4  # Total time allocated for studying (in hours)

    # Sort classes by duration in descending order
    classes.sort(key=lambda x: x["duration"], reverse=True)

    # Initialize a schedule
    schedule = []
    remaining_study_time = total_study_time

    for course in classes:
        course_name = course["name"]
        course_duration = course["duration"]

        # Check if there's enough time left for the class
        if remaining_study_time >= course_duration:
            # Add the class to the schedule
            schedule.append(f"Class: {course_name} ({course_duration} hours)")
            schedule.append(f"Study: {course_name} ({course_duration} hours)")
            remaining_study_time -= course_duration

    # Print the schedule
    print("\n".join(schedule))

    if remaining_study_time <= 0:
        print("You've used up all your study time. Take a break to recharge!")
        print("You may also add more time with the buttons below!")
        break
