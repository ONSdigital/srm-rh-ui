ARG  python_pipenv_build_image=europe-west2-docker.pkg.dev/ons-ci-rm/docker/python-pipenv:3.12
FROM ${python_pipenv_build_image} as build

ENV PIPENV_VENV_IN_PROJECT=1

WORKDIR /app
COPY Pipfile* /app/

RUN /root/.local/bin/pipenv sync

FROM python:3.12.13-slim@sha256:a9e4190f02729f01e5b3719bd8b3ea0f8d9350dc17d01a1ce1ca6e3fbfcf7a99

RUN groupadd -g 984 respondenthome && useradd -r -u 984 -g respondenthome respondenthome

WORKDIR /app

RUN mkdir -v /app/venv && chown respondenthome:respondenthome /app/venv

COPY --chown=respondenthome:respondenthome --from=build /app/.venv/ /app/venv/
COPY --chown=respondenthome:respondenthome . /app/

EXPOSE 9092

USER respondenthome

ENTRYPOINT ["/app/venv/bin/python"]
CMD ["/app/venv/bin/gunicorn"]