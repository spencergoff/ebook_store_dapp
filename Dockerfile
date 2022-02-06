FROM public.ecr.aws/lambda/python:3.9
COPY download_decrypt.py requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .
RUN yum install gpg
RUN type gpg
RUN python3 download_decrypt.py 
RUN gpg --yes --batch --passphrase=$secret_value test.txt.gpg 
CMD [ "download_decrypt.main" ]