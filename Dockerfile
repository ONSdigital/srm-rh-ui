ARG  python_pipenv_build_image=europe-west2-docker.pkg.dev/ons-ci-rm/docker/python-pipenv:latest
FROM ${python_pipenv_build_image} as build

ENV PIPENV_VENV_IN_PROJECT=1

WORKDIR /app
COPY Pipfile* /app/

RUN /root/.local/bin/pipenv sync

FROM python:3.11.7-slim@sha256:89c610d12fe12b3e06f35d070f79e57cf14e2bd89c071435ee3678419b691603

RUN groupadd -g 984 respondenthome && useradd -r -u 984 -g respondenthome respondenthome

WORKDIR /app

RUN mkdir -v /app/venv && chown respondenthome:respondenthome /app/venv

COPY --chown=respondenthome:respondenthome --from=build /app/.venv/ /app/venv/
COPY --chown=respondenthome:respondenthome . /app/

EXPOSE 9092

USER respondenthome

ENTRYPOINT ["/app/venv/bin/python"]
CMD ["/app/venv/bin/gunicorn"]