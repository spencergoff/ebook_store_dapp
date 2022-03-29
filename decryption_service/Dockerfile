FROM public.ecr.aws/lambda/python:3.9
RUN yum -y install gcc
COPY decryption_service/download_decrypt.py decryption_service/requirements.txt ./compiled_contract.json ./
RUN python3.9 -m pip install -r requirements.txt -t .
CMD [ "download_decrypt.main" ]