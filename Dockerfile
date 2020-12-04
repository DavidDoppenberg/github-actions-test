FROM python:3.9-windowsservercore-1809
COPY ./app .
CMD "powershell"
# $ docker ps -q -a --filter "status=running" --filter "ancestor=ca-portal:dev" | ForEach-Object { docker kill $_ }
# $ docker ps -q -a --filter "status=exited" --filter "ancestor=ca-portal:dev" | ForEach-Object { docker rm $_ }