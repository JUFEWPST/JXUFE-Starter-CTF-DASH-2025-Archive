<?php
error_reporting(0);
highlight_file(__FILE__);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
$dom = new DOMDocument();
$dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
$user = simplexml_import_dom($dom);
echo $user->name;
?>