FROM python:3.14.0a5-alpine3.21

# Install system dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements first to leverage Docker cache
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

# Create user
RUN adduser --disabled-password egg_user

# Copy application code
COPY egg_price /egg_price

# Set working directory
WORKDIR /egg_price

# Set ownership of the workdir
RUN chown -R egg_user:egg_user /egg_price

# Expose port
EXPOSE 8000

# Switch to non-root user
USER egg_user

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
