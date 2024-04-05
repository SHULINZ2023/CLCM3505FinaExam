# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY tictactoe-c2c.py /app

# Install any needed dependencies specified in requirements.txt
RUN pip install openai
RUN pip install anthropic

# Run the Python script when the container launches
CMD ["python", "tictactoe-c2c.py"]