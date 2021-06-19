FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Force new service deployment"
LABEL "org.opencontainers.image.description"="This task forces a new deployment of the service."
LABEL "com.puppet.nebula.sdk.version"="v1"