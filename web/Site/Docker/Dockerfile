# Use a imagem oficial do Nginx como base
FROM nginx:latest

# Copie os arquivos gerados pelo Jekyll para o diretório padrão do Nginx
COPY _site /usr/share/nginx/html

# Exponha a porta 80 para acessar o site
EXPOSE 80

# Comando padrão para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]