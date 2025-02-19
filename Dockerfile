FROM python:3.8-slim

#set working directory
WORKDIR /app

#copy the code
COPY app.py requirements.txt ./

#install the dependencies
RUN pip install -r requirements.txt

#run the code
CMD ["python3", "app.py"]