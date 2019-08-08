FROM python:3.7-stretch

# Install locales
RUN apt-get -y update && apt-get -y install locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.utf8
ENV LC_LANG en_US.utf8

# Let's upgrade PIP
RUN pip install pipenv

# Install dependences
ADD Pipfile* /
RUN pipenv install --system --deploy --ignore-pipfile

ADD src /app/src
ADD app.py /app
ADD settings.yaml /app
WORKDIR /app
