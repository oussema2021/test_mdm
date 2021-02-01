FROM python:3.7
COPY ./submission_mdm/SparseArray.py
COPY ./submission_mdm/main.py
ENV STRINGS=aa,bb,cc
ENTRYPOINT ["python3","main.py"]
