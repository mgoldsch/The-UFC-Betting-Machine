FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends build-essential r-base littler python3.6 python3-pip python3-setuptools python3-dev

WORKDIR /app

RUN Rscript -e "install.packages('PlayerRatings')"

COPY . .

CMD ["python3", "glicko_fight_prediction.py"]