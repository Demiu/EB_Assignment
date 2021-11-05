<?php
/* Smarty version 3.1.39, created on 2021-10-30 13:50:06
  from '/var/www/html/admin123456/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_617d316edf4640_69200604',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'c01e838167e7b33a5f22d4bc2edc1219781771e2' => 
    array (
      0 => '/var/www/html/admin123456/themes/default/template/content.tpl',
      1 => 1633363913,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_617d316edf4640_69200604 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
