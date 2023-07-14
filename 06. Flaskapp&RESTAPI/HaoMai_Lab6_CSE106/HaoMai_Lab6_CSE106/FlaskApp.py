import json
from flask_cors import CORS
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)
CORS(app)

@app.route('/StudentGrades')
def get_StudentGrades():
    with open("StudentGrades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    StudentGrades_dict = json.loads(readString)
    response = jsonify(StudentGrades_dict)
    return response

@app.route('/StudentGrades/<lastName>')
def find_grade(firstName):
    with open("StudentGrades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    StudentGrades_dict = json.loads(readString)
    if firstName in StudentGrades_dict:
        response = jsonify({firstName: str(StudentGrades_dict[firstName])})
        return response
 

@app.route('/StudentGrades', methods=["POST"])
def input_StudentGrades():
    with open("StudentGrades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    StudentGrades_dict = json.loads(readString)
    StudentGrades_dict[request.json["name"]] = request.json["grade"]
    with open("StudentGrades.txt", "w") as writer:
        json_dump = json.dumps(StudentGrades_dict)
        print(json_dump)
        writer.write(json_dump)
    return StudentGrades_dict

@app.route('/StudentGrades/<firstName>', methods=["PUT"])
def update_grade(firstName):
    with open("StudentGrades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    StudentGrades_dict = json.loads(readString)
    StudentGrades_dict[firstName] = request.json["grade"]
    with open("StudentGrades.txt", "w") as writer:
        json_dump = json.dumps(StudentGrades_dict)
        print(json_dump)
        writer.write(json_dump)
    return StudentGrades_dict

@app.route('/StudentGrades/<firstName>', methods=["DELETE"])
def del_grade(firstName):
    with open("StudentGrades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    StudentGrades_dict = json.loads(readString)
    if firstName in StudentGrades_dict:
        del StudentGrades_dict[firstName]
    else:
        abort(404)
    with open("StudentGrades.txt", "w") as writer:
        json_dump = json.dumps(StudentGrades_dict)
        print(json_dump)
        writer.write(json_dump)
    return StudentGrades_dict


if __name__ == '__main__':
    app.run()