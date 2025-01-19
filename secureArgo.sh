My example starts up unsecured you can secure with a self signed cert - 
openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes \
    -keyout argocd.key -out argocd.crt \
    -subj "/CN=localhost"
