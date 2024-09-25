# Use Alpine Linux with Python 3.9 as the base image
FROM python:3.9-alpine

# Set up environment
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Install dependencies: bash, git, and Commitizen plugin
RUN apk add --no-cache bash git gcc musl-dev libffi-dev && \
    pip install --upgrade pip && \
    pip install czespressif

# Set entrypoint script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the working directory
WORKDIR /app

# Execute the entrypoint script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
