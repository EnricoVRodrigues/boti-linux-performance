#!/bin/bash
# Script de Instalação Automática - Boti-Fix
# Grupo Boticário - Performance Linux

echo "------------------------------------------------"
echo "🚀 Iniciando Instalação/Atualização do Boti-Fix V9.2..."
echo "------------------------------------------------"

# 1. Instala dependências essenciais de sistema
echo "📦 Instalando pacotes necessários..."
sudo apt update && sudo apt install -y python3-rich btop speedtest-cli lm-sensors smartmontools

# 2. Baixa o script mais recente do GitHub e configura como comando de sistema
echo "⚙️ Configurando executável..."
# ESSA É A LINHA PRINCIPAL QUE VOCÊ DEVE ALTERAR:
sudo curl -sSL -o /usr/local/bin/boti-fix https://raw.githubusercontent.com/EnricoVRodrigues/boti-linux-performance/main/painel_boti.py
sudo chmod +x /usr/local/bin/boti-fix

# 3. Cria um atalho (alias) no perfil do usuário se não existir
if ! grep -q "alias boti-fix" ~/.bashrc; then
    echo "alias boti-fix='sudo /usr/local/bin/boti-fix'" >> ~/.bashrc
fi

echo "------------------------------------------------"
echo "✅ TUDO PRONTO! Versão 9.2 Ativa."
echo "👉 Para rodar, basta digitar: boti-fix"
echo "------------------------------------------------"
