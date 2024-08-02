# Use the official Python 3.11.9 image as the base image
FROM python:3.11.9

# Set the working directory in the container
WORKDIR /streamlit_immoeliza

# Update pip to the latest version
RUN pip install --upgrade pip

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment and install dependencies
# Use /bin/bash -c to execute the activation and installation in a single layer
RUN /bin/bash -c "source venv/bin/activate && pip install --no-cache-dir -r requirements.txt"

# Copy the application code into the container
COPY . .

# Expose port 8501 to the outside world
EXPOSE 8501

# Activate the virtual environment and run the Streamlit application
# Use /bin/bash -c to activate the environment and start the application
CMD ["/bin/bash", "-c", "source venv/bin/activate && streamlit run streamlit_immoeliza.py --server.port 8501"]
