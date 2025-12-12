FROM node:20-alpine

WORKDIR /app

# Salin package.json dan package-lock.json
COPY package*.json ./

# Instal dependensi
RUN npm install

# Salin kode aplikasi (penting untuk build/final image)
COPY . .

# Port yang akan diekspos (sesuai Vite default)
EXPOSE 3000

# Perintah menjalankan dilakukan di docker-compose untuk development hot-reload