class IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            parts = ipaddress.split('.')
        else:
            parts = list(map(str, ipaddress))

        if len(parts) != 4:
            raise ValueError("Неверная длина IP-адреса")

        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                raise ValueError("Неверный формат IP-адреса")

        self.ipaddress = '.'.join(parts)

    def __repr__(self):
        return f'IPAddress(\'{self.ipaddress}\')'

    def __str__(self):
        return self.ipaddress
# Создаем два экземпляра класса IPAddress
ip1 = IPAddress("192.168.1.1")
ip2 = IPAddress([172, 16, 254, 1])

# Выводим объекты с помощью функции print
print(ip1)      # 192.168.1.1
print(ip2)      # 172.16.254.1

# Выводим результаты работы функции repr
print(repr(ip1))  # IPAddress('192.168.1.1')
print(repr(ip2))  # IPAddress('172.16.254.1')
