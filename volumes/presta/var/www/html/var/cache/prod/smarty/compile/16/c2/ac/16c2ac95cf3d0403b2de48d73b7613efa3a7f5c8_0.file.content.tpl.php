<?php
/* Smarty version 3.1.39, created on 2021-10-22 17:19:12
  from '/var/www/html/admin123456/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6172d6708723b9_75636832',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '16c2ac95cf3d0403b2de48d73b7613efa3a7f5c8' => 
    array (
      0 => '/var/www/html/admin123456/themes/new-theme/template/content.tpl',
      1 => 1633363913,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6172d6708723b9_75636832 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
