import os

os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.tgz")
os.system("tar -xzvf ngrok-stable-linux-386.tgz")
os.system("./ngrok authtoken 21C37ILhHmrN3LpkxWNBZ3p9TTq_4XquCTmDafA1ko2ETvKYR")
os.system("./ngrok http file:////app/site")
