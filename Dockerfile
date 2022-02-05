FROM public.ecr.aws/lambda/python:3.9
COPY download_decrypt.py requirements.txt /tmp/decrypted_file.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .
CMD [ "download_decrypt.main" ]