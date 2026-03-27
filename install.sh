#!/bin/bash
# Script de Instalação Automática - Boti-Fix
# Grupo Boticário - Performance Linux

echo "------------------------------------------------"
echo "🚀 Iniciando Instalação/Atualização do Boti-Fix V9.2..."
echo "------------------------------------------------"

# 1. Instala dependências essenciais de sistema
echo "📦 Instalando pacotes necessários..."
sudo apt update
# Instalamos o curl primeiro para garantir o download do speedtest oficial
sudo apt install -y python3-rich btop lm-sensors smartmontools curl

# 1.1 Instalação do Speedtest Oficial (Ookla) para aceitar os parâmetros do seu script
if ! command -v speedtest &> /dev/null; then
    echo "⚡ Instalando Speedtest Oficial..."
    curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash
    sudo apt install speedtest -y
fi

# 2. Baixa o script mais recente e configura o executável
echo "⚙️ Configurando executável em /usr/local/bin/boti-fix..."
sudo curl -sSL -o /usr/local/bin/boti-fix https://raw.githubusercontent.com/EnricoVRodrigues/boti-linux-performance/main/painel_boti.py
sudo chmod +x /usr/local/bin/boti-fix

# 3. Cria o alias no .bashrc para facilitar o uso
if ! grep -q "alias boti-fix" ~/.bashrc; then
    echo "alias boti-fix='sudo /usr/local/bin/boti-fix'" >> ~/.bashrc
    echo "✨ Alias 'boti-fix' criado com sucesso!"
fi

echo "------------------------------------------------"
echo "✅ TUDO PRONTO! Versão 9.2 Ativa."
echo "👉 Feche e abra o terminal ou digite: source ~/.bashrc"
echo "👉 Depois, basta digitar: boti-fix"
echo "------------------------------------------------"
