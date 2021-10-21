<?php
/* Smarty version 3.1.39, created on 2021-10-21 00:16:53
  from '/var/www/html/modules/ps_metrics/views/templates/admin/metricsSettings.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_61709555274d68_76898041',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'b2f4a124d76676b62c8278c4f01c4c2291129ce6' => 
    array (
      0 => '/var/www/html/modules/ps_metrics/views/templates/admin/metricsSettings.tpl',
      1 => 1634678212,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_61709555274d68_76898041 (Smarty_Internal_Template $_smarty_tpl) {
?>
<link href="https://js.chargebee.com/v2/chargebee.js" rel=preload as=script>
<link href="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['pathSettingsVendor']->value,'htmlall','UTF-8' ));?>
" rel=preload as=script>
<link href="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['pathSettingsApp']->value,'htmlall','UTF-8' ));?>
" rel=preload as=script>

<div id="settingsApp"></div>
<?php echo '<script'; ?>
 src="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['pathSettingsVendor']->value,'htmlall','UTF-8' ));?>
"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['pathSettingsApp']->value,'htmlall','UTF-8' ));?>
"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="https://js.chargebee.com/v2/chargebee.js"><?php echo '</script'; ?>
>

<style>
  /** Hide native multistore module activation panel, because of visual regressions on non-bootstrap content */
  #content.nobootstrap div.bootstrap.panel {
    display: none;
  }
</style>
<?php }
}
