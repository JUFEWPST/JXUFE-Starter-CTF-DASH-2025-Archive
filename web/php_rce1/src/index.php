<?php
highlight_file(__FILE__);

if (isset($_POST['cmd'])) {
    $cmd = $_POST['cmd'];

    $banned = ['cat', 'flag', 'more', 'less', 'head', 'tail', 'nl', 'tac', 'od', 'strings'];
    foreach ($banned as $word) {
        if (stripos($cmd, $word) !== false) {
            die("我不喜欢你！");
        }
    }
    system($cmd);
}
?>