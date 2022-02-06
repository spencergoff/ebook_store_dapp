FROM public.ecr.aws/lambda/python:3.9
COPY download_decrypt.py requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .
RUN yum install gpg
RUN type gpg
CMD [ "download_decrypt.main" ]