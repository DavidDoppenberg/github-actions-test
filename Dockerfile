FROM python:3.9-windowsservercore-1809
COPY ./app .
CMD "powershell"