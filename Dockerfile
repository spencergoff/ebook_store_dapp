FROM public.ecr.aws/lambda/python:3.9
COPY fernet.py requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .
CMD [ "download_decrypt.py.main" ]