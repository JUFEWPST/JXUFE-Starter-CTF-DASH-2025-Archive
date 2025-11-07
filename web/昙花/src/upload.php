<?php
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    highlight_file(__FILE__);
    exit;
}

define('UPLOAD_PATH', __DIR__ . '/uploads');

if (!is_dir(UPLOAD_PATH)) {
    mkdir(UPLOAD_PATH, 0755, true);
}

$allowed_ext = ['jpg', 'png', 'gif'];
$file_name = $_FILES['upload_file']['name'] ?? '';
$tmp_file = $_FILES['upload_file']['tmp_name'] ?? '';
if (!$file_name || !is_uploaded_file($tmp_file)) {
    die('No file uploaded.');
}

$file_ext = strtolower(substr(strrchr($file_name, '.'), 1));
$target = UPLOAD_PATH . '/' . basename($file_name);

move_uploaded_file($tmp_file, $target);

if (in_array($file_ext, $allowed_ext)) {
    echo 'Upload success.';
} else {
    @unlink($target);
    echo 'Only .jpg, .png, .gif allowed.';
}