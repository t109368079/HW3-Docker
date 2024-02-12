FROM python:3.6

RUN mkdir -p /home

RUN cd home

RUN mkdir -p /home/data

ADD main.py /home

RUN mkdir -p /home/output

CMD [ "python", "/home/main.py" ]