import streamlit
import ipaddress

streamlit.title('IPアドレス計算')

streamlit.sidebar.write("""
## 数値入力
""")

first_octet = streamlit.sidebar.number_input('第1オクテット', min_value=0, max_value=255)
second_octet = streamlit.sidebar.number_input('第2オクテット', min_value=0, max_value=255)
third_octet = streamlit.sidebar.number_input('第3オクテット', min_value=0, max_value=255)
fourth_octet = streamlit.sidebar.number_input('第4オクテット', min_value=0, max_value=255)

subnet = streamlit.sidebar.selectbox(
    'サブネットマスク',
    ('/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8'
    '/9', '/10', '/11', '/12', '/12', '/13', '/14',
    '/15', '/16', '/17', '/18', '/19', '20', '/21',
    '/22', '/23', '/24', '/25', '/26', '/27', '/28',
    '/29', '/30', '/31', '/32'))

streamlit.write(f'''
                ### IPアドレス
                #### {first_octet}.{second_octet}.{third_octet}.{fourth_octet}{subnet}''')


come = ipaddress.ip_address('%sです。'%(ip))
streamlit.title(come)