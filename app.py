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

    else:
        answer = "Sorry, I don't understand your question"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)