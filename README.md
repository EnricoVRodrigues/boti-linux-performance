# 🚀 Boti-Fix: Performance & Otimização Linux

Ferramenta interna desenvolvida para manutenção, limpeza e diagnóstico de notebooks Linux do **Grupo Boticário**. O objetivo é garantir a melhor performance para o time, resolvendo problemas comuns de rede, memória e cache de forma automatizada.

## 🛠 Como Instalar (Uso Interno)
Para instalar o **Boti-Fix** no seu notebook, abra o terminal e execute o comando abaixo:

```bash
git clone https://github.com/EnricoVRodrigues/boti-linux-performance.git && cd boti-linux-performance && chmod +x install.sh && ./install.sh

### 📖 Manual de Uso: Funções do Painel

Após a instalação, use o menu interativo para as seguintes ações:

| Opção | Função | O que ele faz? |
| :--- | :--- | :--- |
| **1** | 🌐 **Rede** | Reseta DNS e conexões. (Ficará offline por 3s). |
| **2** | 🛠️ **Super Correção** | Estabiliza o Cortex XDR e corrige erros de pacotes. |
| **3** | 🧹 **Limpeza** | **Anti-Travamento:** Limpa cache e fecha os browsers. |
| **4** | ☁️ **Cloud** | Atalho para configurar o GDrive via rclone. |
| **5** | 🌡️ **Hardware** | Mostra temperatura da CPU e saúde do SSD. |
| **6** | 🔄 **Update** | Ciclo completo de atualização do Ubuntu. |
| **7** | 📊 **Monitor** | Abre o monitor de recursos BTOP. |
| **8** | 🚀 **RAM** | Limpa cache de memória e reseta o Swap. |
| **9** | ⚡ **Speedtest** | Teste oficial de velocidade da internet. |

> ⚠️ **Aviso:** Salve seu trabalho antes de usar a **Opção 3**, pois ela encerrará o Chrome e Firefox para uma limpeza completa.
