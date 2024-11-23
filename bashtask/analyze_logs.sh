#!/bin/bash

# Создание заголовка отчета
echo "Отчет о логе веб-сервера" | tee report.txt
echo "=========================" | tee -a report.txt

echo -e "\nОбщее количество запросов:" | tee -a report.txt
total_requests=$(wc -l < access.log)
echo $total_requests | tee -a report.txt

echo -e "\nКоличество уникальных IP-адресов:" | tee -a report.txt
unique_ips=$(awk '{ips[$1]++} END {print length(ips)}' access.log)
echo $unique_ips | tee -a report.txt


echo -e "\nКоличество запросов по методам:" | tee -a report.txt
awk '{method = $6; gsub(/"/, "", method); if (method != "") methods[method]++} END {for (method in methods) print method, methods[method]}' access.log | tee -a report.txt


echo -e "\nСамый популярный URL:" | tee -a report.txt
popular_url=$(awk '{urls[$7]++} END {max=0; for (url in urls) {if (urls[url] > max) {max = urls[url]; popular = url}} print popular}' access.log)
url_count=$(awk '{urls[$7]++} END {max=0; for (url in urls) {if (urls[url] > max) {max = urls[url]}} print max}' access.log)
echo "$popular_url" | tee -a report.txt
echo "Количество запросов: $url_count" | tee -a report.txt

echo -e "\nОтчет сохранен в файл report.txt"
