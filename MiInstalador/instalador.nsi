!define APP_NAME "USBFormatter"
!define INSTALL_DIR "$PROGRAMFILES\${APP_NAME}"

Outfile "Instalador_${APP_NAME}.exe"
InstallDir ${INSTALL_DIR}
RequestExecutionLevel admin  

Page directory
Page instfiles

Section "Instalar ${APP_NAME}"
    ; Crear carpeta de instalación
    CreateDirectory "${INSTALL_DIR}"

    ; Copiar ejecutable
    SetOutPath "${INSTALL_DIR}"
    File "USBFormatter.exe"

    ; Copiar icono
    File "icono.ico"

    ; Copiar la carpeta _internal completa
    SetOutPath "${INSTALL_DIR}\_internal"
    File /r "_internal\*.*"

    ; Crear acceso directo en el escritorio
    CreateShortcut "$DESKTOP\${APP_NAME}.lnk" "${INSTALL_DIR}\USBFormatter.exe" "" "${INSTALL_DIR}\icono.ico"

SectionEnd
