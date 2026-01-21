from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = {}

    if request.method == "POST":
        Tamil = int(request.form.get("tamil"))
        English = int(request.form.get("english"))
        Maths = int(request.form.get("maths"))
        Science = int(request.form.get("science"))
        Social = int(request.form.get("social"))

        result["Tamil"] = "Pass" if Tamil >= 35 else "Fail"
        result["English"] = "Pass" if English >= 35 else "Fail"
        result["Maths"] = "Pass" if Maths >= 35 else "Fail"
        result["Science"] = "Pass" if Science >= 35 else "Fail"
        result["Social"] = "Pass" if Social >= 35 else "Fail"

        total = Tamil + English + Maths + Science + Social
        percentage = total // 5

        result["total"] = total
        result["percentage"] = percentage

        if (Tamil >=35 and English >=35 and Maths >=35 and Science >=35 and Social >=35):
            result["overall"] = "PASS"
        else:
            result["overall"] = "FAIL"

        if percentage >= 90:
            result["grade"] = "A+"
        elif percentage >= 80:
            result["grade"] = "A"
        elif percentage >= 70:
            result["grade"] = "B"
        elif percentage >= 60:
            result["grade"] = "C"
        elif percentage >= 50:
            result["grade"] = "D"
        else:
            result["grade"] = "No Grade"

        if (Tamil >=80 and English >=80 and Maths >=80 and Science >=80 and Social >=80):
            result["motivation"] = [
                "Padichaa varum mark",
                "Muyarchi panna spark",
                "Kashtam konjam irukkum",
                "Vetri kandippaa sirikkum"
            ]

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
