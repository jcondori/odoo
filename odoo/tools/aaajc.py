import os

path_config = r'E:\Documents\GitHub\scripts\confs'
template_config = 'E:/Documents/GitHub/Scripts/confs/@template-16.conf'


def detect_configs(project_path: str) -> list[str]:
    confs = [template_config]
    if project_path and os.path.isdir(path_config) and os.path.exists(project_path):
        base_name = os.path.basename(os.path.normpath(project_path))
        projected_conf = f'{base_name}.conf'
        for file in os.listdir(path_config):
            file_dir = os.path.join(path_config, file)
            if file.lower() == projected_conf.lower() and os.path.isfile(file_dir):
                print(f'Archivo de configuración detectado: {file_dir}')
                confs.append(file_dir)
                break
    return confs


if __name__ == '__main__':
    my_confs = detect_configs(r'E:\Documents\GitHub\Arin')
    print(my_confs)
