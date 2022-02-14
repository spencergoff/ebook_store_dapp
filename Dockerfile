FROM public.ecr.aws/lambda/python:3.9
RUN yum -y install python3-devel
COPY download_decrypt.py requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .
CMD [ "download_decrypt.main" ]