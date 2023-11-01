import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
from flask import Flask, jsonify
# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.players import initPlayers
import requests
from datetime import datetime, timezone

# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.player import player_api


# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(player_api)
app.register_blueprint(app_projects) # register app pages

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

@app.before_first_request
def activate_job():  # activate these items 
    initJokes()
    initUsers()
    initPlayers()

@app.route('/api/data')
def get_data():
    # start a list, to be used like a information database
    user_classes = []

    # add a row to list, an Info record
    user_classes.append({
        "user_id": 10000,
        "user_name": "Aidan Lau",
        "classes": ['AP CSP, Chinese, AP Calc, English, AP Bio'],
        "GPA": "3.9",
        "ap_count": "3",
    })

    user_classes.append({
        "user_id": 10001,
        "user_name": "Rayyan Darugar",
        "classes": ["AP CSP, Class2, Class3, Class4, Class5"],
        "GPA": "TBA",
        "ap_count": "TBA",
    })
    
    user_classes.append({
        "user_id": 10002,
        "user_name": "Daniel Choi",
        "classes": ["AP CSP, Class2, Class3, Class4, Class5"],
        "GPA": "TBA",
        "ap_count": "TBA",
    })
    
    user_classes.append({
        "user_id": 10002,
        "user_name": "Unknown Person",
        "classes": ["AP CSP, Class2, Class3, Class4, Class5"],
        "GPA": "TBA",
        "ap_count": "TBA",
    })
    
    user_classes.append({
        "user_id": 10002,
        "user_name": "Unknown Person",
        "classes": ["AP CSP, Class2, Class3, Class4, Class5"],
        "GPA": "TBA",
        "ap_count": "TBA",
    })
    
    user_classes.append({
        "user_id": 10002,
        "user_name": "Unknown Person",
        "classes": ["AP CSP, Class2, Class3, Class4, Class5"],
        "GPA": "TBA",
        "ap_count": "TBA",
    })
    
    user_classes.append({
        "user_id": 10002,
        "user_name": "Unknown Person",
        "classes": ["AP CSP, Class2, Class3, Class4, Class5"],
        "GPA": "TBA",
        "ap_count": "TBA",
    })
    
    return jsonify(user_classes)


API_TOKEN = '2573~mbqfLD2yTcQr8StVbsAHhSC695LjGUSw9SCeRd0x8qysh1uJ5Jvo77uu9IRez34d'
BASE_URL = 'https://poway.instructure.com/api/v1/'

# List of course IDs
course_ids = [141645, 141694, 141093, 141643, 144907]

def get_assignments_for_course(course_id):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    
    url = f'{BASE_URL}courses/{course_id}/assignments'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to retrieve assignments for Course {course_id}. Status code: {response.status_code}"}

@app.route('/assignments/user')
def get_assignments():
    assignments_data = {}
    for course_id in course_ids:
        assignments_data[course_id] = get_assignments_for_course(course_id)
    return jsonify(assignments_data)


base_url = 'https://poway.instructure.com/api/v1/'
headers = {
    'Authorization': 'Bearer 2573~mbqfLD2yTcQr8StVbsAHhSC695LjGUSw9SCeRd0x8qysh1uJ5Jvo77uu9IRez34d'
}

@app.route('/assignments')
def homework_list():
    try:
        response = requests.get(base_url + 'courses/141645/assignments', headers=headers)

        if response.status_code == 200:
            assignments = response.json()
            print(assignments)
          
            current_date = datetime.now(timezone.utc)

            # Filter assignments with due dates in the future
            # future_assignments = [assignment for assignment in assignments if assignment.get('due_at') and datetime.fromisoformat(assignment['due_at']) > current_date]
            
            return jsonify(assignments)  # Return JSON response
        else:
            return jsonify({"error": "Failed to retrieve assignments. Status code: " + str(response.status_code)})
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)})

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="5001")
