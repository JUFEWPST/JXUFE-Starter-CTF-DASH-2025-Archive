from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>红魔馆不会爆炸2</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a2e; color: #fff; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { color: #e94560; text-align: center; }
        .quote { background: #16213e; padding: 20px; border-radius: 10px; margin: 20px 0; }
        form { text-align: center; margin: 30px 0; }
        input[type="text"] { padding: 10px; width: 300px; border: none; border-radius: 5px; }
        input[type="submit"] { background: #e94560; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin-left: 10px; }
        .hint { background: #0f3460; padding: 15px; border-radius: 8px; margin: 20px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>红魔馆不会爆炸2</h1>
        
        <div class="quote">
            "红魔馆不会爆炸，这是绝对的真理。" by 蕾米莉亚·斯卡雷特<br>
            "但某些冰之妖精似乎总想挑战这个真理..."
        </div>

        <form action="/check" method="GET">
            <input type="text" name="query">
            <input type="submit" value="最强妖精">
        </form>
    </div>
</body>
</html>
"""


@app.route("/check")
def check():
    query = request.args.get("query", "")

    blacklist = [
    "import",
    "eval",
    "exec", 
    "os",
    "sys",
]
    for forbidden in blacklist:
        if forbidden in query.lower():
            return "呜呜呜被拦了"

    template_content = f"""
            <p>baka炸弹：{query}</p>
            <p>红魔馆不会爆炸</p>
"""

    template = """
<!DOCTYPE html>
<html>
<head>
    <title>⑨的报告</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a2e; color: #fff; }
        .container { max-width: 800px; margin: 0 auto; }
        .result { background: #16213e; padding: 20px; border-radius: 10px; margin: 20px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>最强妖精的行动报告</h1>
        <div class="result">
""" + template_content + """
        </div>
        <a href="/">返回</a>
    </div>
</body>
</html>
"""
    return render_template_string(template)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")