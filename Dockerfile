FROM python:3
WORKDIR /diabetes_trial
COPY /diabetes_trial .
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python app.py
