FROM python:3.6.7-alpine3.8

ENV MAIN_APP /COH-form
WORKDIR ${MAIN_APP}
COPY . ${MAIN_APP}

RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python", "-m", "flask", "run"]