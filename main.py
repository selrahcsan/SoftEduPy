import os
import emoji


jogosEducacionais = ['org.kde.gcompris ', 'org.kde.ktuberling', 'org.kde.kbruch', 'net.minetest.Minetest',
                     'net.supertuxkart.SuperTuxKart', 'org.supertuxproject.SuperTux', 'forg.kde.blinken',
                     'org.gnome.Sudoku', 'org.seul.pingus', 'org.kde.kapman', 'org.kde.kmahjongg',
                     'com.endlessnetwork.frogsquash', 'com.github.avojak.paint-spill', 'io.gitlab.ballz.Ballz',
                     'net.freerct.FreeRCT', 'ro.go.hmlendea.DL-Desktop', 'org.gnome.gbrainy',
                     'net.sourceforge.ExtremeTuxRacer', 'cat.xtec.clic.JClic',
                     'com.endlessnetwork.frogsquash', 'org.leocad.LeoCAD']

debsJogosEducacional = ['gcompris-qt', 'ktuberling', 'kbruch', 'minetest', 'supertux', 'blinken', 'pingus', 'kapman',
                        'kmahjongg', 'gbrainy', 'extremetuxracer', 'jclic']

ensinoDeLinguas = ['org.kde.klettres', 'org.kde.ktouch', 'com.tux4kids.tuxtype', 'org.kde.kanagram', 'org.kde.khangman',
                   'net.sourceforge.Klavaro', 'com.identicalsoftware.anagramarama']

debsEnsinoDeLinguas = ['klettres', 'ktouch', 'tuxtype', 'kanagram', 'khangman', 'Klavaro']

debsGeografia = ['kgeography', 'stellarium', 'marble', 'kstars']

geografia = ['org.kde.kgeography', 'org.stellarium.Stellarium', 'org.kde.marble', 'org.kde.kstars']

debsMultimidia = ['audacity', 'cheese', 'minuet']

multimidia = ['org.audacityteam.Audacity', 'org.gnome.Cheese', 'org.kde.minuet']

criacao = ['org.inkscape.Inkscape', 'org.gimp.GIMP', 'org.gimp.GIMP.Plugin.Resynthesizer/x86_64/2-40',
           'org.gimp.GIMP.Plugin.LiquidRescale/x86_64/2-40', 'org.gimp.GIMP.Plugin.Lensfun/x86_64/2-40',
           'org.gimp.GIMP.Plugin.GMic/x86_64/2-40', 'org.gimp.GIMP.Plugin.Fourier/x86_64/2-40',
           'org.gimp.GIMP.Plugin.FocusBlur/x86_64/2-40', 'org.gimp.GIMP.Manual', 'org.tuxpaint.Tuxpaint',
           'org.kde.kolourpaint', 'org.kde.krita', 'com.orama_interactive.Pixelorama', 'com.jgraph.drawio.desktop',
           'org.musescore.MuseScore']

debsCriacao = ['inkscape', 'gimp', 'tuxpaint', 'kolourpaint', 'krita']

matematica = ['org.kde.kbruch', 'com.tux4kids.tuxmath', 'io.github.Qalculate.qalculate-qt', 'org.geogebra.GeoGebra']

debsMatematica = ['kbruch', 'tuxmath', 'geogebra']

quimica = ['org.kde.katomic', 'org.openchemistry.Avogadro2', 'forg.kde.kalzium']

debsQuimica = ['katomic', 'avogadro', 'kalzium']

fisica = ['eu.stethewwolf.gresistor', 'org.fritzing.Fritzing']

debFisica = ['Fritzing']

programacao = ['com.vscodium.codium', 'edu.mit.Scratch', 'org.kde.kturtle', ' io.gdevelop.ide']

acessibilidade = ['hu.irl.cameractrls']

geral = ['io.github.JaGoLi.ytdl_gui', 'io.github.webcam.Webcamoid', 'net.xmind.XMind',
         'org.learningequality.Kolibri']

debsGeral = ['orca', 'bleachbit', 'dreamchess', 'mbrola-br1', 'mbrola-br3', 'eviacam', 'gconjugue']


def main():
    """

    """

    print("Complete.")
    os.system('clear')
    verifica_flatpak()


def verifica_emoji():
    emojiinstalado = os.system('verificaEmoji=$(pip show emoji)')

    if emojiinstalado == 0:
        print(emoji.emojize("Emoji   ...:thumbs_up:"))


def verifica_flatpak():
    verifica_emoji()
    flatpakinslado = os.system('verificaFlatpak=$(dpkg -l | grep -i flatpak)')

    if flatpakinslado == 0:
        print(emoji.emojize("Flatpak ...:thumbs_up:"))
        verifica_flathub()
        menu()
        funcionalidades()
    else:
        print(emoji.emojize("Flatapk n??o est?? instalado ...:disappointed_face:"))
        menu_debs()


def verifica_flathub():
    flathubinstalado = os.system('verificaFlathub=$(flatpak remotes)')
    if flathubinstalado == 0:
        print(emoji.emojize("Flathub ...:thumbs_up:"))
    else:
        print("Deseja adicionar o remoto Flathub ? (S/N): ")
        opcao_flathub = str(input('Escolha uma op????o: '))
        if opcao_flathub.lower() == "s":
            instala_flathub()
        else:
            menu_debs()


def instala_flathub():
    os.system('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')


def menu():
    print(emoji.emojize('''
    :pencil:  MENU Principal:

    :eight-pointed_star: [F] - Instalar vers??o Educacional em Flatpaks 
    :eight-pointed_star: [R] - Instalar vers??o Educacional dos Reposit??rios (DEBs)
    :eight-pointed_star: [S] - Sair
        '''))


def funcionalidades():
    opcaomenu = str(input(emoji.emojize('Escolha uma op????o :thinking_face::  ')))
    if opcaomenu.lower() == "f":
        submenu_flatpaks()
    elif opcaomenu.lower() == "r":
        instalar_debs()
    else:
        print("finalizado")


def submenu_flatpaks():
    os.system('clear')
    print(emoji.emojize('''
    :pencil:  Instala????o FlatPaks:

     :right_arrow: [B] - Instalar vers??o B??sica
     :sparkle: [C] - Instalar vers??o Completa
            '''))
    funcionalidades_submenu_flatpaks()


def menu_debs():
    print("Instalando pacotes do reposi??rio da sua distro")
    instalar_debs()


def funcionalidades_submenu_flatpaks():
    opcao_submenu = str(input('Escolha uma op????o: '))
    if (opcao_submenu == "B") or (opcao_submenu == "b"):
        atualizar_flatpaks()
        instalar_jogos_edu()
    if (opcao_submenu == "C") or (opcao_submenu == "c"):
        instalar_flatpaks()


def instalar_debs():
    atualizar_debs()
    instalar_debs_geral()
    instalar_debs_jogos_edu()
    instalar_debs_ensino_de_linguas()
    instalar_debs_criacao()
    instalar_debs_fisica()
    instalar_debs_matematica()


def atualizar_debs():
    try:
        os.system("sudo apt update -y")
    except Exception:
        print("N??o foi poss??vel atualizar os reposit??rios")


def instalar_debs_geral():
    try:
        for listaG in debsGeral:
            os.system("sudo apt install -y " + listaG)
    except Exception:
        print("Erro na instala??ao dos debs Geral")


def instalar_debs_jogos_edu():
    try:
        for listaJ in debsJogosEducacional:
            os.system("sudo apt install -y " + listaJ)
    except Exception:
        print("Erro na instala??ao dos Jogos Educacionais")


def instalar_debs_ensino_de_linguas():
    try:
        for listaL in debsEnsinoDeLinguas:
            os.system("sudo apt install -y " + listaL)
    except Exception:
        print("Erro na instala??ao dos sofwares ensino de linguas")


def instalar_debs_criacao():
    try:
        for listaC in debsCriacao:
            os.system("sudo apt install -y " + listaC)
    except Exception:
        print("Erro na instala??ao dos sofwares cria????o")


def instalar_debs_matematica():
    try:
        for listaM in debsMatematica:
            os.system("sudo apt install -y " + listaM)
    except Exception:
        print("Erro na instala??ao dos sofwares de matem??tica")


def instalar_debs_quimica():
    try:
        for listaQ in debsQuimica:
            os.system("sudo apt install -y " + listaQ)
    except Exception:
        print("Erro na instala??ao dos sofwares de Qu??mica")


def instalar_debs_fisica():
    try:
        for listaF in debsMatematica:
            os.system("sudo apt install -y " + listaF)
    except Exception:
        print("Erro na instala??ao dos sofwares de F??sica")


def instalar_flatpaks():
    atualizar_flatpaks()
    instalar_jogos_edu()
    instalar_linguas()
    instalar_multimidia()
    instalar_cricao()
    instalar_quimica()
    instalar_geografia()
    instalar_geral()
    instalar_acessibilidade()
    instalar_programacao()


def atualizar_flatpaks():
    try:
        os.system("flatpak update -y --noninteractive ")
    except Exception:
        print("N??o foi poss??vel atualizar os flatpaks")


def instalar_jogos_edu():
    try:
        for listaJ in jogosEducacionais:
            os.system("flatpak install flathub -y --system " + listaJ)
    except Exception:
        print("Erro na instala??ao dos Jogos Educacionais")


def instalar_cricao():
    try:
        for listaC in criacao:
            os.system("flatpak install flathub -y --system " + listaC)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Cria????o")


def instalar_multimidia():
    try:
        for listaM in multimidia:
            os.system("flatpak install flathub -y --system " + listaM)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Multim??dia")


def instalar_linguas():
    try:
        for listaL in ensinoDeLinguas:
            os.system("flatpak install flathub -y --system " + listaL)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Ensino de Linguas")


def instalar_geografia():
    try:
        for listaG in geografia:
            os.system("flatpak install flathub -y --system " + listaG)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Geografia")


def instalar_matematica():
    try:
        for listaM in matematica:
            os.system("flatpak install flathub -y --system " + listaM)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Matem??tica")


def instalar_quimica():
    try:
        for listaQ in quimica:
            os.system("flatpak install flathub -y --system " + listaQ)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Qu??mica")


def instalar_fisica():
    try:
        for listaF in fisica:
            os.system("flatpak install flathub -y --system " + listaF)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de F??sica")


def instalar_programacao():
    try:
        for listaP in programacao:
            os.system("flatpak install flathub -y --system " + listaP)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Programacao")


def instalar_acessibilidade():
    try:
        for listaA in acessibilidade:
            os.system("flatpak install flathub -y --system " + listaA)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Programacao")


def instalar_geral():
    try:
        for listaG in geral:
            os.system("flatpak install flathub -y --system " + listaG)
    except Exception:
        print("Erro na instala??ao dos Aplicativos de Programacao")


main()
