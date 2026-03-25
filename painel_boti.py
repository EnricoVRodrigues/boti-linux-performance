#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import time
import socket

# Verificação de dependência Rich
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt
except ImportError:
    os.system("sudo apt update && sudo apt install python3-rich -y")
    from rich.console import Console, Panel, Table, Text, Prompt

console = Console()

def run_cmd(command, title="Processando..."):
    try:
        with console.status(f"[bold green]{title}...", spinner="bouncingBar"):
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except: return False

def get_sys_info():
    try:
        # IP Local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_l = s.getsockname()[0]
        s.close()
        
        # IP Externo
        ip_e = subprocess.getoutput("curl -s --max-time 2 https://ifconfig.me").strip() or "Off-line"
        
        # Uptime formatado
        uptime = subprocess.getoutput("uptime -p").replace("up ", "")
        
        return ip_l, ip_e, uptime
    except: 
        return "Desconectado", "Off-line", "Indisponível"

def exibir_logo():
    os.system('clear')
    ip_l, ip_e, uptime = get_sys_info()
    logo = Text(r"""
 ____  ____ _______ _____ _____           _____  _____ ____  
|  _ \ / __ \__   __|_   _/ ____|    /\    |  __ \|_   _/ __ \ 
| |_) | |  | | | |     | || |        /  \   | |__) | | || |  | |
|  _ <| |  | | | |     | || |       / /\ \  |  _  /  | || |  | |
| |_) | |__| | | |    _| || |____  / ____ \ | | \ \ _| || |__| |
|____/ \____/  |_|   |_____\_____/_/    \_\_|  \_\_____\____/ 
    """, style="bold green")
    
    console.print(Panel(logo, subtitle="[bold blue]V9.2 - PERFORMANCE & ANTI-TRAVAMENTO", border_style="bright_magenta"))
    
    # Linha de Informações do Sistema
    info_line = f"[bold cyan]🏠 IP LOCAL:[/bold cyan] {ip_l}  |  [bold magenta]🌍 IP EXTERNO:[/bold magenta] {ip_e}  |  [bold yellow]⏱️ LIGADO HÁ:[/bold yellow] {uptime}"
    console.print(Panel(info_line, expand=False))

def limpeza_profunda_e_segura():
    exibir_logo()
    console.print(Panel("[bold green]🧹 LIMPEZA SISTEMA & NAVEGADOR (ANTI-TRAVAMENTO)[/bold green]", border_style="green"))
    
    # --- PARTE 1: FECHAMENTO SEGURO ---
    run_cmd("pkill -x chrome || true", "Encerrando Chrome com segurança")
    run_cmd("pkill -x firefox || true", "Encerrando Firefox com segurança")
    time.sleep(1)
    
    # --- PARTE 2: LIMPEZA DE APLICATIVOS ---
    run_cmd("rm -rf ~/.cache/google-chrome/*", "Limpando Cache do Chrome")
    run_cmd("rm -rf ~/.cache/thumbnails/*", "Limpando Miniaturas de Imagens")
    
    # --- PARTE 3: LIMPEZA DE SISTEMA ---
    run_cmd("sudo apt-get autoremove -y", "Removendo pacotes desnecessários")
    run_cmd("sudo apt-get clean", "Limpando cache de instaladores (APT)")
    run_cmd("sudo journalctl --vacuum-time=1d", "Limpando Logs antigos (Logs > 24h)")
    run_cmd("sudo rm -rf /tmp/*", "Limpando arquivos temporários (/tmp)")
    run_cmd("sudo rm -rf /var/crash/*", "Limpando relatórios de erro (Crashes)")
    run_cmd("rm -rf ~/.local/share/Trash/*", "Esvaziando Lixeira")
    
    console.print("\n[bold green]✅ Limpeza concluída! Sistema limpo e estável.[/bold green]")
    time.sleep(2)

def main():
    if os.getuid() != 0:
        print("Erro: Execute com sudo!"); sys.exit(1)

    while True:
        try:
            exibir_logo()
            menu = Table(title="PAINEL DE MANUTENÇÃO LINUX - GRUPO BOTICÁRIO", title_style="bold cyan", box=None)
            menu.add_column("Opção", style="bold magenta"); menu.add_column("Função", style="white")

            items = [
                ("1", "🌐 Rede: Reset DNS, Rotas e Conexão"),
                ("2", "🛠️ Super Correção: Reparar DPKG & Erros"),
                ("3", "🧹 Limpeza: Sistema & Cache (Anti-Travamento)"),
                ("4", "☁️ Cloud: Configurar/Sincronizar Rclone"),
                ("5", "🌡️ Hardware: Saúde SSD e Temperatura"),
                ("6", "🔄 Update: Atualizar Sistema (APT)"),
                ("7", "📊 Monitor: Monitorar CPU/RAM (BTOP)"),
                ("8", "🚀 RAM: Otimizar Memória (Drop Caches)"),
                ("9", "⚡ Speedtest: Testar Velocidade"),
                ("0", "🚪 Sair")
            ]

            for op, desc in items: menu.add_row(op, desc)
            console.print(menu)
            opcao = Prompt.ask("[bold yellow]Selecione uma opção[/bold yellow]")

            if opcao == "1":
                run_cmd("resolvectl flush-caches && nmcli networking off && sleep 1 && nmcli networking on", "Resetando Interface de Rede")
                time.sleep(2)
            elif opcao == "2":
                run_cmd("sudo rm -rf /var/crash/*", "Limpando logs de crash")
                run_cmd("sudo dpkg --configure -a", "Corrigindo pacotes interrompidos")
                time.sleep(1.5)
            elif opcao == "3":
                limpeza_profunda_e_segura()
            elif opcao == "4": 
                os.system("rclone config")
            elif opcao == "5":
                exibir_logo()
                os.system("sensors | grep 'Core'")
                disk = subprocess.getoutput("lsblk -dpno NAME | grep -vE 'loop|ram' | head -n1")
                os.system(f"sudo smartctl -H {disk} | grep 'assessment'")
                Prompt.ask("\n[bold blue]Pressione Enter para voltar[/bold blue]")
            elif opcao == "6": 
                os.system("sudo apt-get update && sudo apt-get dist-upgrade -y")
            elif opcao == "7": 
                os.system("btop")
            elif opcao == "8":
                run_cmd("sync && echo 3 > /proc/sys/vm/drop_caches", "Limpando Cache da RAM")
                run_cmd("swapoff -a && swapon -a", "Resetando Memória Swap")
                console.print("[bold green]✅ RAM otimizada![/bold green]"); time.sleep(2)
            elif opcao == "9":
                exibir_logo()
                console.print("[bold yellow]Iniciando Speedtest Ookla...[/bold yellow]\n")
                os.system("speedtest --accept-license --accept-gdpr")
                Prompt.ask("\n[bold blue]Pressione Enter para voltar[/bold blue]")
            elif opcao == "0": 
                console.print("[bold blue]Saindo... Até logo![/bold blue]")
                break
        except KeyboardInterrupt: 
            break

if __name__ == "__main__":
    main()
