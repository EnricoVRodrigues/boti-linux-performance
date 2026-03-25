# 🚀 Boti-Fix: Performance & Otimização Linux

Ferramenta interna desenvolvida para manutenção, limpeza e diagnóstico de notebooks Linux do **Grupo Boticário**. O objetivo é garantir a melhor performance para o time, resolvendo problemas comuns de rede, memória e cache de forma automatizada.

## 🛠 Como Instalar (Uso Interno)
Para instalar o **Boti-Fix** no seu notebook, abra o terminal e execute o comando abaixo:

```bash
curl -sSL https://raw.githubusercontent.com/EnricoVRodrigues/boti-linux-performance/main/install.sh | sudo bash
```
### 🔄 Como Atualizar
Se você já possui o Boti-Fix instalado, basta rodar o comando de instalação acima novamente para atualizar para a versão mais recente (**V9.2**).

---

### 📖 Manual de Uso: Funções do Painel

Após a instalação, basta digitar `boti-fix` no terminal para acessar as seguintes ações:

| Opção | Função | O que ele faz? |
| :--- | :--- | :--- |
| **1** | 🌐 **Rede** | Reseta DNS e conexões (resolve quedas de Wi-Fi). |
| **2** | 🛠️ **Super Correção** | Estabiliza o Cortex XDR e corrige erros de pacotes (DPKG). |
| **3** | 🧹 **Limpeza** | **Anti-Travamento:** Limpa cache e fecha os browsers. |
| **4** | ☁️ **Cloud** | Atalho para configurar o GDrive via rclone. |
| **5** | 🌡️ **Hardware** | Mostra temperatura da CPU, **Uptime** e saúde do SSD. |
| **6** | 🔄 **Update** | Ciclo completo de atualização do Ubuntu (APT). |
| **7** | 📊 **Monitor** | Abre o monitor de recursos em tempo real (BTOP). |
| **8** | 🚀 **RAM** | Limpa cache de memória física e reseta o Swap. |
| **9** | ⚡ **Speedtest** | Teste oficial de velocidade da internet (Ookla). |
| **0** | 🚪 **Sair** | Encerra o painel com segurança. |

> ⚠️ **Aviso:** Salve seu trabalho antes de usar a **Opção 3**, pois ela encerrará o Chrome e Firefox para uma limpeza completa de cache.

---
*Desenvolvido pela Equipe de Infraestrutura Linux - Grupo Boticário*
