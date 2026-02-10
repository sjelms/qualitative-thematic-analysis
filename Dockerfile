# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies from a dedicated requirements file
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Create a non-root user for running Jupyter
RUN useradd --create-home --shell /bin/bash appuser && chown -R appuser:appuser /app

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Define environment variables
ENV JUPYTER_ENABLE_LAB=yes

# Switch to non-root user
USER appuser

# Run jupyter lab when the container launches
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
