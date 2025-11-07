<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>图片上传系统</title>
    <script>
        function validateFile() {
            const fileInput = document.getElementById('file');
            const fileName = fileInput.value;
            const allowedExtensions = ['.jpg', '.jpeg', '.png', '.gif'];
            const ext = fileName.slice(fileName.lastIndexOf('.')).toLowerCase();
            if (!allowedExtensions.includes(ext)) {
                alert('错误：仅支持上传 .jpg/.jpeg/.png/.gif 格式的图片！');
                return false;
            }
            return true;
            s
        }
    </script>
</head>

<body>
    <h2>图片上传</h2>
    <form action="upload.php" method="POST" enctype="multipart/form-data" onsubmit="return validateFile()">
        <input type="file" name="uploadFile" id="file" required>
        <button type="submit">上传图片</button>
    </form>
</body>

</html>