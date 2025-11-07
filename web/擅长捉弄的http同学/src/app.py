from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

with open("/flag", "r") as file:
    FLAG = file.read()


@app.route("/", methods=["GET", "POST"])
def index():
    user_agent = request.headers.get("User-Agent")
    x_forwarded_for = request.headers.get("X-Forwarded-For")
    date = request.headers.get("Date")
    Takagi = request.headers.get("Takagi")
    if user_agent != "Nishikata":
        return render_template(
            "index.html",
            msg="你必须使用Nishikata客户端才能前往夏祭！",
            bg_path="1.webp",
        )
    if x_forwarded_for != "127.0.0.1":
        return render_template("index.html", msg="本地人才能去夏祭！", bg_path="1.webp")
    if date is None:
        return render_template(
            "index.html",
            msg="你必须在2019年8月24日18点前到达夏祭现场...",
            bg_path="1.webp",
        )

    try:
        request_date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT")
        correct_date = datetime(2019, 8, 24, 17, 0, 0)
        end_date = datetime(2019, 8, 24, 18, 0, 0)
        if request_date < correct_date:
            return render_template("index.html", msg="会不会太早了", bg_path="1.webp")
        elif request_date > end_date:
            return render_template(
                "index.html", msg="夏祭已经开始了！！", bg_path="1.webp"
            )
    except ValueError:
        return render_template("index.html", msg="日期格式不对哦，要RFC 822格式")
    if Takagi != "holding hands":
        return render_template(
            "index.html",
            msg="你必须和 Takagi 同学牵手（holding hands）才行",
            bg_path="1.webp",
        )
    if request.method != "POST":
        return render_template(
            "index.html",
            msg="如果是POST就更好了",
            bg_path="1.webp",
        )
    return render_template("index.html", msg=FLAG, bg_path="2.webp")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
