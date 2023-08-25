FROM python:3-slim

ADD https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth /segment-service/sam_vit_h_4b8939.pth

RUN apt update && \
    apt install -y libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

COPY . /segment-service
WORKDIR /segment-service
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./segment.py"]
