#!/bin/bash
#diskarray=(`cat /proc/diskstats |grep -E "\bsd[abcdefg]\b|\bxvd[abcdefg]\b|\bvd[a-z]\b|\bvda[1-9]\b"|grep -i "\b$1\b"|awk '{print $3}'|sort|uniq   2>/dev/null`)
namespcae_json=`codis-admin --dashboard-list --zookeeper=codis-master.xxx.io:2181 2> /dev/null`
namespace_num=`echo $namespcae_json|jq length`
printf "{\n"
printf '\t'"\"data\":["
for ((i=0;i<$namespace_num;i++))
do
    name=`echo $namespcae_json|jq .[$i].name`
    printf '\n\t\t{'
    printf "\"{#PRODUCT_NAME}\":${name}}"
    if [ $i -lt $[$namespace_num-1] ];then
        printf ','
    fi
done
printf "\n\t]\n"
printf "}\n"
