FROM python:3.7
COPY ./SparseArray.py
COPY ./main.py
ENV STRINGS=aa,bb,cc
ENTRYPOINT ["python3","main.py"]
