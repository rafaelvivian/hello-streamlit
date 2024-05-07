import streamlit as st
from pandas import read_csv

st.markdown('''

# Exibidor de arquivos

## Suba um arquivo e vejamos o que acontece 😄️❤️

''')

arquivo = st.file_uploader(
    'Suba seu aquivo aqui!',
    type=['jpg', 'png', 'py', 'csv', 'json']
)

st.text_input('Email', max_chars=20)
st.text_input('Senha', type='password')

if arquivo:
    print(arquivo.name)
    tipo = arquivo.name.split(".")[-1]
    if (tipo == 'png'):
        st.image(arquivo)
    if (tipo == 'py'):
        st.code(arquivo.read().decode())
    if (tipo == 'csv'):
        df = read_csv(arquivo).transpose()
        st.dataframe(df)
        st.line_chart(df)
        st.bar_chart(df)
else:
    st.error('Ainda não tenho arquivo!')
