from flask import Flask, request, render_template_string, send_file
import os
import tarfile

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./uploads"

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>拿去吧！水手服</title>
</head>
<body>
    <h2>听说，在 / 下，有件セーラー服（serafuku）</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept=".tar">
        <input type="submit" value="上传并提取">
    </form>
    
    {% if files %}
    <h3>提取的文件:</h3>
    <ul>
    {% for file in files %}
        <li><a href="/download/{{ file }}">{{ file }}</a></li>
    {% endfor %}
    </ul>
    {% endif %}
    
    {% if error %}
    <p style="color:red">{{ error }}</p>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template_string(HTML, error="请选择文件")

        file = request.files["file"]
        if file.filename == "":
            return render_template_string(HTML, error="请选择文件")

        if not file.filename.endswith(".tar"):
            return render_template_string(HTML, error="只支持TAR文件")

        filename = file.filename
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        try:
            extract_dir = os.path.join(
                app.config["UPLOAD_FOLDER"], filename.replace(".tar", "")
            )
            os.makedirs(extract_dir, exist_ok=True)

            with tarfile.open(filepath, "r") as tar:
                tar.extractall(extract_dir)

            extracted_files = os.listdir(extract_dir)
            return render_template_string(HTML, files=extracted_files)

        except Exception as e:
            return render_template_string(HTML, error="文件提取失败")

    return render_template_string(HTML)


@app.route("/download/<filename>")
def download_file(filename):
    if filename is None or filename == "":
        return "文件名不能为空"

    if ".." in filename or "/" in filename:
        return "非法文件名"

    upload_dir = app.config["UPLOAD_FOLDER"]

    for root, dirs, files in os.walk(upload_dir):
        filepath = os.path.join(root, filename)
        if os.path.exists(filepath):
            try:
                return send_file(filepath, as_attachment=False)
            except Exception as e:
                return f"读取文件失败: {str(e)}"

    return "文件不存在"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
