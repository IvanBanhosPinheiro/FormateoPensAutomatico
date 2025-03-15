# USB Auto Formatter

Programa para formatear automáticamente dispositivos USB cuando son conectados al sistema.

## Características

- ✨ Detección automática de dispositivos USB
- 🚀 Formateo rápido automático
- 📝 Interfaz por consola con mensajes de estado
- 🛑 Detención segura con Ctrl+C

## Versión ejecutable

En la carpeta `dist/USBFormatter` encontrarás el ejecutable `USBFormatter.exe` listo para usar:
1. No requiere instalación ni dependencias
2. Solo necesita permisos de administrador
3. Ejecutar haciendo doble clic (como administrador)

## Versión código fuente

### Requisitos previos
- Python 3.x
- Windows OS
- Permisos de administrador

### Instalación
```bash
pip install -r requirements.txt
```

### Ejecución desde código
```bash
python main.py
```

## Uso

1. Ejecute el programa (`.exe` o código fuente)
2. Verá el mensaje "Monitor de formateo automático iniciado"
3. Conecte cualquier dispositivo USB
4. El programa detectará y formateará automáticamente
5. Para detener, presione Ctrl+C

## ⚠️ Advertencias importantes

- Formatea automáticamente SIN CONFIRMACIÓN
- Elimina TODOS los datos del dispositivo
- Use bajo su propia responsabilidad
- Haga copias de seguridad de datos importantes

## Mensajes del programa

- 🟢 "Monitor iniciado": Programa listo
- ⌛ "Esperando dispositivos...": En espera
- 🔄 "Formateando unidad X:": Formateo en proceso
- ✅ "Formato completado": Operación exitosa
- 🛑 "Programa detenido": Cierre con Ctrl+C

## Licencia

[MIT License](LICENSE)