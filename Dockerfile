# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install Jupyter and the scientific Python stack
RUN pip install --no-cache-dir jupyterlab pandas numpy matplotlib seaborn nltk spacy scikit-learn openai

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Define environment variables
ENV JUPYTER_ENABLE_LAB=yes

# Run jupyter lab when the container launches
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
