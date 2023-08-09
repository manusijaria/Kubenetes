# Use a Python base image
FROM python:3.8

# Install Docker client
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get install -y docker-ce-cli

# Set the working directory
WORKDIR /app

# Copy the app files to the container
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY api.py /app/

# Expose the port on which the Flask app will run (if necessary)
EXPOSE 5000

# Run the Flask app
CMD ["python", "api.py"]