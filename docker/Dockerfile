FROM node:12-alpine as build
WORKDIR /app
COPY . .
RUN npm install
RUN npm run ng build -- --output-path=dist
FROM nginx:1.16.0-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
