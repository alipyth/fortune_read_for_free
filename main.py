#pip install streamlit
#pip install requests
#pip install selectolax



import streamlit as st
import requests
from selectolax.parser import HTMLParser


st.title('read Not Free fortune500 articles for free :)')

#r = 'https://fortune.com/crypto/2023/09/01/uniswap-class-action-dismissal-coinbase-tornado-cash-implications/'

r = st.text_input('paste the url of fortune article')
st.info('By Ali Jahani https://jahaniwww.com')
sub = st.button('read :)')
if r is not None and sub :
    rr = requests.get(r)
    #articleContent
    parser = HTMLParser(rr.content)
    
    p= parser.css_first('#article-content')
    links = []
    images = []
    for i in parser.css('.wp-block-image span img'):
        images.append(i.attributes.get('src'))
        #st.image(i.attributes.get('src'))
    for i in parser.css('.wp-block-image a'):
        links.append(i.attributes.get('href'))
        
    
    st.markdown(p.text())
    for l in links:
        st.info(l)
