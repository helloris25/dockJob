#!/bin/bash

echo 'Inserting Example Jobs'

for i in `seq 0 59`;
do
  TN=$(printf "%03d" ${i})
  JSON="{    \"enabled\": true,    \"name\": \"Test ${TN}\",    \"repetitionInterval\": \"HOURLY:${i}\",    \"command\": \"echo %27Running Test ${TN}%27\necho %27Finished%27\"  }"
  curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d "${JSON}" 'http://127.0.0.1:80/api/jobs/'
done




