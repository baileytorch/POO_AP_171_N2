from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version


def menu_principal():
    print()
    print(f'{nombre_aplicacion} v{numero_version}')
    print('==============================')
    print('[1] Gestionar Empleados')
    print('[2] Gestionar Proyectos')
    print('[3] Configuración Sistema')
    print('[0] Salir')
