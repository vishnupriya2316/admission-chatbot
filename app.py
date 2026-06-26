from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    question = request.form['question'].lower()

    if "fees" in question:
        answer = "💰 Fees depend on course & university"

    elif "courses" in question:
        answer = "📘 Courses: AI, CSE, Data Science, MBA"

    elif "eligibility" in question:
        answer = "🎯 Eligibility: Minimum marks + entrance exam"

    elif "admission" in question:
        answer = "📝 Admission: Apply → Counselling → Seat allotment"

    elif "hostel" in question:
        answer = "🏠 Hostel facilities are available for both boys and girls."

    elif "placement" in question:
        answer = "💼 The university provides placement support with top companies."

    elif "campus" in question:
        answer = "🏫 The campus has modern labs, library and sports facilities."

    elif "scholarship" in question:
        answer = "🎓 Scholarships are available for meritorious students."

    elif "contact" in question:
        answer = "📞 Contact: +91 9876543210"

    elif "location" in question:
        answer = "📍 The university is located in Chennai."

    else:
        answer = "Sorry, I don't understand the question."

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)