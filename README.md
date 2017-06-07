# zabbix_codis
通过zabbix监控codis

proxy使用supervisor守护，监控supervisor守护服务状态
codis server和原有的redis兼容，当作普通的redis监控，可参照redis监控方案

集群用量百分比监控使用zabbix的Calculated items特性完成

只上传了codis集群状态监控模版

 ![image](https://github.com/yuliu1212/zabbix_codis/blob/master/D676E7BB-BA88-47A2-B470-EA31DCD121AF.png)
