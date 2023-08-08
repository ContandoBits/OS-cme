def extract_ip_and_os(line):
    ip_start = line.find("SMB") + 4
    ip_end = line.find("445", ip_start) - 1
    ip = line[ip_start:ip_end].strip()

    os_start = line.find("[*]") + 4
    os_end = line.find("(name:")
    os = line[os_start:os_end].strip()

    return ip, os

def classify_by_os_and_ip(output_lines):
    os_ip_dict = {}
    for line in output_lines:
        ip, os = extract_ip_and_os(line)
        ip = ip.replace(" ", "")  # Eliminar espacios en blanco de la IP
        os_ip_dict.setdefault(os, []).append(ip)
    return os_ip_dict

def format_output(result):
    formatted_output = ""
    for os, ips in result.items():
        ips_str = ",".join(ips)
        formatted_output += f"{os}: {ips_str}\n"
    return formatted_output

# Nombre del archivo que contiene la salida
file_name = "output-cme.txt"

# Leer el contenido del archivo
with open(file_name, "r") as file:
    output_lines = file.readlines()

# Clasificar por sistema operativo y dirección IP
result = classify_by_os_and_ip(output_lines)

# Formatear la salida en el formato solicitado
formatted_output = format_output(result)

# Mostrar el resultado
print(formatted_output)
