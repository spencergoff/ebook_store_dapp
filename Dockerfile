FROM public.ecr.aws/lambda/python:3.9
RUN yum -y install gcc
COPY download_decrypt.py requirements.txt compiled_code.json ./
RUN python3.9 -m pip install -r requirements.txt -t .
CMD [ "download_decrypt.main" ]