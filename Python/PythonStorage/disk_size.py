import psutil

def get_disk_size():
    disk = psutil.disk_usage('/')
    total_size = disk.total / (1024**3)  # в гигабайтах
    return total_size

disk_size = get_disk_size()
print(f"Размер жесткого диска: {disk_size:.2f} ГБ")