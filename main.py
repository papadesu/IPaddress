import streamlit
from ipaddress import ip_interface

streamlit.title('IPアドレス計算')

streamlit.sidebar.write("""
## 数値入力
""")

first_octet = streamlit.sidebar.number_input('第1オクテット', min_value=0, max_value=255, value=192)
second_octet = streamlit.sidebar.number_input('第2オクテット', min_value=0, max_value=255, value=168)
third_octet = streamlit.sidebar.number_input('第3オクテット', min_value=0, max_value=255, value=0)
fourth_octet = streamlit.sidebar.number_input('第4オクテット', min_value=0, max_value=255, value=0)

subnet = streamlit.sidebar.number_input('サブネットマスク', min_value=1, max_value=32, value=24)

ip = ip_interface(f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}/{subnet}')
network = ip.network.network_address

streamlit.write(f'''
                ### IPアドレス
                #### {first_octet}.{second_octet}.{third_octet}.{fourth_octet}/{subnet}
                ''')

streamlit.write(f'''
                ### ネットワークアドレス
                #### {network}
                ''')

start_address = list(ip.network.hosts())[0]
last_address = list(ip.network.hosts())[-1]

streamlit.write(f'''
                ### 使用可能アドレス
                #### {start_address} ~ {last_address}
                ''')


