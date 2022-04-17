import streamlit
import ipaddress

streamlit.title('IPアドレス計算')

streamlit.sidebar.write("""
## 数値入力
""")

first_octet = streamlit.sidebar.number_input('第1オクテット', 0)
second_octet = streamlit.sidebar.number_input('第2オクテット', 0)
third_octet = streamlit.sidebar.number_input('第3オクテット', 0)
fourth_octet = streamlit.sidebar.number_input('第4オクテット', 0)



come = ipaddress.ip_address('%sです。'%(ip))
streamlit.title(come)