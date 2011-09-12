use inc::Module::Install;

name 'mha4mysql-node';

version_from 'lib/MHA/NodeConst.pm';

requires 'DBI';
requires 'DBD::mysql';

license 'GPL v2';
author 'Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>';

install_script(glob 'bin/*');
auto_install;
WriteAll;
