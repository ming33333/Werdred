districts = ["Marina","Semba","Dewmist","Ellum"," Centerlight"]
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
jobs = ["Engineer", "Doctor", "Accountant", "Teacher", "Lawyer", "Business Analyst"]
jobs = {
    "Engineer": {
        1: 100,
        2: 150,
        3: 200,
        4: 250,
        5: 300},
    "Doctor": {
        1: 200,
        2: 250,
        3: 400,
        4: 550,
        5: 700},
    "Accountant": {
        1: 100,
        2: 150,
        3: 200,
        4: 250,
        5: 300},
    "Teacher": {"levels": {
        1: 60,
        2: 80,
        3: 100,
        4: 120,
        5: 140},
    "Lawyer": {"levels": {level: 100 + level * 50 for level in range(5)}},
    "Business Analyst": {"levels": {level: 100 + level * 50 for level in range(5)}}
}}
grid = [
    ["Dewmist", "Semba", 0, 0],
    [0, 0, 0, 0],
    [0, "Centerlight", "Ellum", 0],
    [0, "Marina", 0, 0]
]
