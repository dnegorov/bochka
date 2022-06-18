#!/bin/bash

API_KEY="b69aa9bd-7e86-42ab-9c51-4c493ae3c5e2"
API_URL="https://api.weather.yandex.ru/v2/informers"
API_PARAMS="lat=55.163333&lon=38.376865&lang=ru_RU"

HTTP_HEADER='-H "X-Yandex-API-Key:'$API_KEY'"'

function url_decode() {
echo -e "$@" | sed -E 's/%([0-9a-fA-F]{2})/\\x\1/g;s/\+/ /g'
}



DATE_TIME=$(date '+%y-%m-%d-%H-%M-%S')
echo $DATE_TIME
url_decode $(curl -s -H "X-Yandex-API-Key:$API_KEY" -H "Content-Type:application/json" $API_URL?$API_PARAMS) > $DATE_TIME.json
