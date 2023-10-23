# Define a list of classes and their durations
classes = [
    {"name": "INTEGRATED MATH 1A-1B", "duration": 2},
    {"name": "INTEGRATED MATH 2A-2B", "duration": 2},
    {"name": "INTEGRATED MATH 3A-3B", "duration": 2},
    {"name": "TRIGONOMETRY", "duration": 2},
    {"name": "ADVANCED FUNCTIONS ANALYSIS 1-2", "duration": 2},
    {"name": "PRE-CALCULUS 1-2", "duration": 2},
    {"name": "AP CALCULUS AB 1-2", "duration": 2},
    {"name": "BRIDGE TO AP CALCULUS BC", "duration": 2},
    {"name": "AP CALCULUS BC 1-2", "duration": 2},
    {"name": "AP STATISTICS 1-2", "duration": 2},
    {"name": "AP STATISTICS SEMINAR", "duration": 2},
    {"name": "BIOLOGY OF THE LIVING EARTH", "duration": 2},
    {"name": "AP BIOLOGY 3-4", "duration": 2},
    {"name": "AP BIOLOGY SEMINAR", "duration": 2},
    {"name": "PRINCIPLES OF BIOMEDICAL SCIENCES 1-2", "duration": 2},
    {"name": "HUMAN BODY SYSTEMS 1-2", "duration": 2},
    {"name": "HONORS MEDICAL INTERVENTIONS 1-2", "duration": 2},
    {"name": "FUNDAMENTALS OF PHYSICS & CHEMISTRY 1-2", "duration": 2},
    {"name": "CHEMISTRY IN THE EARTH SYSTEM 1-2", "duration": 2},
    {"name": "PHYSICS OF THE UNIVERSE", "duration": 2},
    {"name": "MARINE SCIENCE", "duration": 2},
    {"name": "AP CHEMISTRY 3-4", "duration": 2},
    {"name": "AP CHEMISTRY SEMINAR", "duration": 2},
    {"name": "AP ENVIRONMENTAL SCIENCE 1-2", "duration": 2},
    {"name": "AP ENVIRONMENTAL SCIENCE SEMINAR", "duration": 2},
    {"name": "AP PHYSICS C: MECHANICS 1A-1B", "duration": 2},
    {"name": "AP PHYSICS C: MECHANICS SEMINAR", "duration": 2},
    {"name": "AP PHYSICS C: ELECTRICITY & MAGNETISM 1-2", "duration": 2},
    {"name": "AP PHYSICS C: ELECTRICITY & MAGNETISM SEMINAR", "duration": 2},
    {"name": "WORLD HISTORY", "duration": 2},
    {"name": "AP WORLD HISTORY 1-2", "duration": 2},
    {"name": "WORLD GEOGRAPHY & CULTURES", "duration": 2},
    {"name": "US HISTORY 1-2", "duration": 2},
    {"name": "AP US HISTORY 1-2", "duration": 2},
    {"name": "AP US HISTORY SEMINAR", "duration": 2},
    {"name": "CIVICS", "duration": 2},
    {"name": "ECONOMICS", "duration": 2},
    {"name": "AP US GOVERNMENT & POLITICS 1-2", "duration": 2},
    {"name": "AP US GOVERNMENT SEMINAR", "duration": 2},
    {"name": "HIGH SCHOOL ENGLISH 1-2", "duration": 2},
    {"name": "HONORS HIGH SCHOOL ENGLISH 1-2", "duration": 2},
    {"name": "HONORS HUMANITIES 1-2", "duration": 2},
    {"name": "AMERICAN LITERATURE 1-2", "duration": 2},
    {"name": "ETHNIC LITERATURE 1-2", "duration": 2},
    {"name": "EXPOSITORY READING & WRITING 1-2", "duration": 2},
    {"name": "WORLD LITERATURE 1-2", "duration": 2},
    {"name": "AP ENGLISH LANGUAGE 1-2", "duration": 2},
    {"name": "AP ENGLISH LANGUAGE SEMINAR", "duration": 2},
    {"name": "AP ENGLISH LITERATURE 1-2", "duration": 2},
    {"name": "AP ENGLISH LITERATURE SEMINAR", "duration": 2},
    {"name": "CHINESE 1-2", "duration": 2},
    {"name": "CHINESE 3-4", "duration": 2},
    {"name": "CHINESE 5-6", "duration": 2},
    {"name": "CHINESE 7-8", "duration": 2},
    {"name": "AP CHINESE LANGUAGE", "duration": 2},
    {"name": "AP CHINESE LANGUAGE SEMINAR", "duration": 2},
    {"name": "SPANISH 1-2", "duration": 2},
    {"name": "SPANISH 3-4", "duration": 2},
    {"name": "SPANISH 5-6", "duration": 2},
    {"name": "SPANISH 7-8", "duration": 2},
    {"name": "AP SPANISH LANGUAGE 1-2", "duration": 2},
    {"name": "AP SPANISH LANGUAGE SEMINAR", "duration": 2},
    {"name": "DRAWING AND PAINTING 1-2", "duration": 2},
    {"name": "DRAWING AND PAINTING 3-4", "duration": 2},
    {"name": "3D COMPUTER ANIMATION 1-2", "duration": 2},
    {"name": "3D COMPUTER ANIMATION 3-4", "duration": 2},
    {"name": "CERAMICS 1-2", "duration": 2},
    {"name": "CERAMICS 3-4", "duration": 2},
    {"name": "DESIGN MIXED MEDIA 1-2", "duration": 2},
    {"name": "DIGITAL MEDIA PRODUCTIONS 1-2", "duration": 2},
    {"name": "DIGITAL MEDIA PRODUCTIONS 3-4", "duration": 2},
    {"name": "DRAMA 1-2", "duration": 2},
    {"name": "DRAMA 3-4", "duration": 2},
    {"name": "DRAMA 5-6", "duration": 2},
    {"name": "TECHNICAL PRODUCTION FOR THEATER 1-2", "duration": 2},
    {"name": "TECHNICAL PRODUCTON FOR THEATER 3-4", "duration": 2},
    {"name": "PHOTOGRAPHY 1-2", "duration": 2},
    {"name": "PHOTOGRAPHY 3-4", "duration": 2},
    {"name": "PHOTOGRAPHY 5-6", "duration": 2},
    {"name": "STUDIO ART", "duration": 2},
    {"name": "AP STUDIO ART: DRAWING 1-2", "duration": 2},
    {"name": "AP STUDIO ART: 2D", "duration": 2},
    {"name": "AP STUDIO ART: 3D", "duration": 2},
    {"name": "ORCHESTRA 1-2", "duration": 2},
    {"name": "CONCERT BAND 1-2", "duration": 2},
    {"name": "WIND ENSEMBLE 1-2", "duration": 2},
    {"name": "SYMPHONIC BAND 1-2", "duration": 2},
    {"name": "AP MUSIC THEORY 1-2", "duration": 2},
    {"name": "HARMONY", "duration": 2},
    {"name": "CONCERT CHOIR 1-2", "duration": 2},
    {"name": "CLASSICAL VOCAL ENSEMBLE", "duration": 2},
    {"name": "AVID 1-2", "duration": 2},
    {"name": "AVID 3-4", "duration": 2},
    {"name": "AVID 5-6", "duration": 2},
    {"name": "AVID SENIOR SEMINAR 1-2", "duration": 2},
    {"name": "ETHNIC STUDIES 1-2", "duration": 2},
    {"name": "BROADCAST JOURNALISM/TV PRODUCTION 1-2", "duration": 2},
    {"name": "BROADCAST JOURNALISM/TV PRODUCTION 3-4", "duration": 2},
    {"name": "BUSINESS LAW 1-2", "duration": 2},
    {"name": "INTRODUCTION TO FINANCE 1-2", "duration": 2},
    {"name": "MARKETING ECONOMICS 1-2", "duration": 2},
    {"name": "CHILD DEVELOPMENT & PSYCHOLOGY 1-2", "duration": 2},
    {"name": "CHILD DEVELOPMENT & PSYCHOLOGY 3-4", "duration": 2},
    {"name": "ROBOTICS 1-2", "duration": 2},
    {"name": "INTRODUCTION TO ENGINEERING DESIGN", "duration": 2},
    {"name": "HONORS PRINCIPLES OF ENGINEERING", "duration": 2},
    {"name": "COMPUTER SCIENCE & SOFTWARE ENGINEERING", "duration": 2},
    {"name": "AP COMPUTER SCIENCE PRINCIPLES 1-2", "duration": 2},
    {"name": "DATA STRUCTURES 1", "duration": 2},
    {"name": "AP COMPUTER SCIENCE A 1-2", "duration": 2},
    {"name": "DATA STRUCTURES 2", "duration": 2},
    {"name": "AP HUMAN GEOGRAPHY 1-2", "duration": 2},
    {"name": "AP HUMAN GEOGRAPHY SEMINAR", "duration": 2},
    {"name": "AP PSYCHOLOGY 1-2", "duration": 2},
    {"name": "PSYCHOLOGY 1", "duration": 2},
    {"name": "LINK CREW LEADERSHIP 1-2", "duration": 2},
    {"name": "YEARBOOK 1-2", "duration": 2},
    {"name": "ASB/PLANNING & LEADERSHIP", "duration": 2},
    {"name": "VOCATIONAL LEARNING ASSISTANT", "duration": 2},
    {"name": "ACADEMIC TUTOR", "duration": 2},
    {"name": "ACADEMIC LITERACY 1-2", "duration": 2},
    {"name": "ACADEMIC SUCCESS 9", "duration": 2},
    {"name": "ACADEMIC SUCCESS 10", "duration": 2},
    {"name": "ACADEMIC SUCCESS 11", "duration": 2},
    {"name": "ACADEMIC SUCCESS 12", "duration": 2},
    {"name": "WORK EXPERIENCE 1-2", "duration": 2},
    {"name": "INTERNSHIP", "duration": 2},
    {"name": "ENS 1-2", "duration": 2},
    {"name": "ENS 3", "duration": 2},
    {"name": "HEALTH", "duration": 2},
    {"name": "INTERMEDIATE BASKETBALL", "duration": 2},
    {"name": "COURT SPORTS", "duration": 2},
    {"name": "FIELD SPORTS", "duration": 2},
    {"name": "RACQUET SPORTS", "duration": 2},
    {"name": "AEROBICS WEIGHT TRAINING", "duration": 2},
    {"name": "WEIGHT TRAINING", "duration": 2},
    {"name": "MARCHING PE/BAND", "duration": 2},
    {"name": "MARCHING PE/TALL FLAGS", "duration": 2},
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
