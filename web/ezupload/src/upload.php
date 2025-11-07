<?php
error_reporting(0);
$uploadDir = 'uploads/';

if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

if ($_FILES['uploadFile']['error'] === UPLOAD_ERR_OK) {
    $filename = basename($_FILES['uploadFile']['name']);
    $targetPath = $uploadDir . $filename;
    $allowedMime = ['image/jpeg', 'image/png', 'image/gif'];
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $fileMime = $finfo->file($_FILES['uploadFile']['tmp_name']);

    if (in_array($fileMime, $allowedMime)) {
        if (move_uploaded_file($_FILES['uploadFile']['tmp_name'], $targetPath)) {
            echo "上传成功！文件路径：<a href='$targetPath'>$targetPath</a>";
        } else {
            echo "上传失败，请重试";
        }
    } else {
        echo "文件类型不支持";
    }
} else {
    echo "上传出错（错误码：{$_FILES['uploadFile']['error']}）";
}
?>