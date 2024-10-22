FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-IgnacioMilutin.git

WORKDIR /ajedrez-2024-IgnacioMilutin

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m cli"]

#ejecutar desde terminalk de carpeta
# docker buildx build -t first-circleci-dqmdz-um .
# docker images
# docker run -i first-circleci-dqmdz-um