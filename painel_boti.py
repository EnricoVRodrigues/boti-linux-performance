#!/usr/bin/env python3
import os
import subprocess
import sys
import time
import socket

# --- DEPENDÊNCIAS ---
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt
except ImportError:
    print("📦 Instalando dependências visuais (python3-rich)...")
    os.system("sudo apt update && sudo apt install python3-rich -y")
    from rich.console import Console, Panel, Table, Text, Prompt

console = Console()

# --- FUNÇÕES DE SUPORTE ---

def run_cmd(command, title="Processando..."):
    """Executa comandos silenciosos com um spinner visual."""
    try:
        with console.status(f"[bold green]{title}...", spinner="bouncingBar"):
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def get_sys_info():
    """Obtém IPs e tempo de atividade para o cabeçalho."""
    try:
        # IP Local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_l = s.getsockname()[0]
        s.close()
        # IP Externo (timeout de 2s para não travar)
        ip_e = subprocess.getoutput("curl -s --max-time 2 https://ifconfig.me").strip() or "Off-line"
        # Uptime
        uptime = subprocess.getoutput("uptime -p").replace("up ", "")
        return ip_l, ip_e, uptime
    except:
        return "Desconectado", "Off-line", "Indisponível"

def exibir_logo():
    """Renderiza o banner principal v9.2."""
    os.system('clear')
    ip_l, ip_e, uptime = get_sys_info()
    logo = Text(r"""
 ____  ____ _______ _____ _____           _____  _____ ____  
|  _ \|  __ \__   __|_   _/ ____|    /\    |  __ \|_   _/ __ \ 
| |_) | |  | | | |     | || |        /  \   | |__) | | || |  | |
|  _ <| |  | | | |     | || |       / /\ \  |  _  /  | || |  | |
| |_) | |__| | | |    _| || |____  / ____ \ | | \ \ _| || |__| |
|____/ \____/  |_|   |_____\_____/_/    \_\_|  \_\_____\____/ 
    """, style="bold green")
    
    console.print(Panel(logo, subtitle="[bold blue]V9.2 - PERFORMANCE & ANTI-TRAVAMENTO", border_style="bright_magenta"))
    
    info_line = f"[bold cyan]🏠 LOCAL:[/bold cyan] {ip_l}  |  [bold magenta]🌍 EXTERNO:[/bold magenta] {ip_e}  |  [bold yellow]⏱️ LIGADO:[/bold yellow] {uptime}"
    console.print(Panel(info_line, expand=False))

# --- MÓDULOS ESPECÍFICOS ---

def limpeza_profunda():
    """Executa a rotina de limpeza anti-travamento."""
    exibir_logo()
    console.print(Panel("[bold green]🧹 INICIANDO LIMPEZA PROFUNDA[/bold green]", border_style="green"))
    
    # Fecha browsers para limpar cache
    run_cmd("pkill -x chrome || true", "Fechando Chrome")
    run_cmd("pkill -x firefox || true", "Fechando Firefox")
    
    # Limpezas
    run_cmd("rm -rf ~/.cache/google-chrome/*", "Limpando Cache Chrome")
    run_cmd("sudo apt-get autoremove -y && sudo apt-get clean", "Limpando APT")
    run_cmd("sudo journalctl --vacuum-time=1d", "Limpando Logs (>24h)")
    run_cmd("sudo rm -rf /tmp/*", "Arquivos Temporários")
    run_cmd("rm -rf ~/.local/share/Trash/*", "Esvaziando Lixeira")
    
    console.print("\n[bold green]✅ Sistema limpo e otimizado![/bold green]")
    time.sleep(2)

# --- MAIN LOOP ---

def main():
    if os.getuid() != 0:
        console.print("[bold red]❌ Erro: Execute com sudo (sudo python3 painel_boti.py)[/bold red]")
        sys.exit(1)

    while True:
        try:
            exibir_logo()
            menu = Table(title="PAINEL DE MANUTENÇÃO LINUX - GRUPO BOTICÁRIO", title_style="bold cyan", box=None)
            menu.add_column("Opção", style="bold magenta", justify="center")
            menu.add_column("Função", style="white")

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
                run_cmd("resolvectl flush-caches && nmcli networking off && sleep 1 && nmcli networking on", "Resetando Rede")
                time.sleep(2)

            elif opcao == "2":
                run_cmd("sudo dpkg --configure -a && sudo apt install -f -y", "Reparando Erros de Sistema")
                time.sleep(2)

            elif opcao == "3":
                limpeza_profunda()

            elif opcao == "4":
                os.system("rclone config")

            elif opcao == "5":
                exibir_logo()
                console.print("[bold cyan]🌡️ Temperaturas:[/bold cyan]")
                os.system("sensors | grep 'Core'")
                disk = subprocess.getoutput("lsblk -dpno NAME | grep -vE 'loop|ram' | head -n1")
                console.print(f"\n[bold cyan]🛡️ Saúde do Disco ({disk}):[/bold cyan]")
                os.system(f"sudo smartctl -H {disk} | grep 'assessment' || echo 'Instale smartmontools'")
                Prompt.ask("\n[bold blue]Pressione Enter para voltar[/bold blue]")

            elif opcao == "6":
                exibir_logo()
                console.print("[bold yellow]🔄 Iniciando Atualização (APT)...[/bold yellow]\n")
                os.system("sudo apt update && sudo apt dist-upgrade -y && sudo apt autoremove -y")
                Prompt.ask("\n[bold green]✅ Concluído! Enter para voltar[/bold green]")

            elif opcao == "7":
                os.system("btop")

            elif opcao == "8":
                run_cmd("sync && echo 3 > /proc/sys/vm/drop_caches", "Limpando RAM")
                console.print("[bold green]✅ Memória RAM liberada![/bold green]")
                time.sleep(2)

            elif opcao == "9":
                exibir_logo()
                os.system("speedtest --accept-license --accept-gdpr")
                Prompt.ask("\n[bold blue]Pressione Enter para voltar[/bold blue]")

            elif opcao == "0":
                console.print("[bold blue]Saindo... Até a próxima![/bold blue]")
                break
                
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
