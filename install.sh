#!/bin/bash
# Script de Instalação Automática - Boti-Fix
# Grupo Boticário - Performance Linux

echo "------------------------------------------------"
echo "🚀 Iniciando Instalação do Boti-Fix..."
echo "------------------------------------------------"

# 1. Instala dependências essenciais de sistema
echo "📦 Instalando pacotes necessários..."
sudo apt update && sudo apt install -y python3-rich btop speedtest-cli lm-sensors smartmontools

# 2. Configura o script como um comando de sistema
echo "⚙️ Configurando executável..."
sudo cp painel_boti.py /usr/local/bin/boti-fix
sudo chmod +x /usr/local/bin/boti-fix

# 3. Cria um atalho (alias) no perfil do usuário
if ! grep -q "alias boti-fix" ~/.bashrc; then
    echo "alias boti-fix='sudo /usr/local/bin/boti-fix'" >> ~/.bashrc
    source ~/.bashrc 2>/dev/null
fi

echo "------------------------------------------------"
echo "✅ INSTALAÇÃO CONCLUÍDA COM SUCESSO!"
echo "👉 Para rodar, basta digitar: boti-fix"
echo "------------------------------------------------"
