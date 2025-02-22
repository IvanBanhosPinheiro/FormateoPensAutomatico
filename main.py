import win32file
import time
import subprocess
from ctypes import windll

def get_drives():
    """Obtiene la lista de unidades disponibles"""
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in range(65, 91):
        if bitmask & 1:
            drives.append(chr(letter))
        bitmask >>= 1
    return drives

def is_removable(drive):
    """Comprueba si la unidad es removible"""
    drive_type = win32file.GetDriveType(drive + ":\\")
    return drive_type == win32file.DRIVE_REMOVABLE

def format_drive(drive_letter):
    """Formatea la unidad especificada"""
    try:
        print(f"\nFormateando unidad {drive_letter}:")
        cmd = f'format {drive_letter}: /Q /Y'
        subprocess.run(cmd, shell=True, capture_output=True)
        print(f"Formato completado en unidad {drive_letter}:")
        return True
    except Exception as e:
        print(f"Error al formatear: {str(e)}")
        return False



if __name__ == "__main__":
    print("Monitor de formateo automático iniciado")
    print("Presione Ctrl+C para detener")
    print("Esperando dispositivos USB...")
    
    current_drives = set(get_drives())
    
    try:
        while True:
            new_drives = set(get_drives())
            # Detectar nuevas unidades
            added_drives = new_drives - current_drives
            
            for drive in added_drives:
                if is_removable(drive):
                    print(f"\nNuevo dispositivo USB detectado en unidad {drive}:")
                    format_drive(drive)
                    
            current_drives = new_drives
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario")