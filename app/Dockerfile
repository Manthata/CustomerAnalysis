FROM node:12-alpine

#Create app directory 
WORKDIR /usr/src/app
COPY package*.json ./

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "node", "app.js" ]

