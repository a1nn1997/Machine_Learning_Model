From python:3.9.10-alpine3.15
WORKDIR /app
COPY . requirements.txt
COPY . housing_data.joblib
COPY . main.py
EXPOSE 5000 
RUN pip install  -r requirements.txt 
CMD python main.py

