FROM python:3.9-windowservercore-1809

# $ docker ps -q -a --filter "status=running" --filter "ancestor=ca-portal:dev" | ForEach-Object { docker kill $_ }
# $ docker ps -q -a --filter "status=exited" --filter "ancestor=ca-portal:dev" | ForEach-Object { docker rm $_ }

CMD "powershell"