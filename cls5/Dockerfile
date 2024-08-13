# Use an official Node.js runtime as a parent image
FROM node:20

# Set the maintainer label
LABEL maintainer="a@hotmail.com"
# Set the working directory in the container
WORKDIR /code

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the app will run
EXPOSE 3000

# Define the command to run your application
CMD ["node", "backend/index.js"]
