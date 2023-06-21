# Use a base image that supports your application's runtime (e.g., Python, Node.js, etc.)
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies and -r is used to specify the req.txt file
RUN pip install -r requirements.txt

# Specify the command to run your application
CMD [ "python", "app.py" ]

