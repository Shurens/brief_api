FROM mongo:5.0
ARG DATABASE_URI
ARG USERNAME
ARG PASSWORD

ENV DATABASE_URI ${webapi}
ENV USERNAME ${root}
ENV PASSWORD ${example}

COPY Mammal.csv /Mammal.csv

CMD mongoimport --db=webapi --collection=mammals --file=Mammal.csv -u root -p example --host=mongo --port=27017 --authenticationDatabase admin --type csv  --headerline