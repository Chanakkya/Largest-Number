# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:33:44 2023

@author: CHANAKKYA
"""

import streamlit as st

st.title('Largest Of Three Number\n By Chanakkya S - 21F3003211')

number1 = st.number_input('Enter the first number')
number2 = st.number_input('Enter the second number')
number3 = st.number_input('Enter the third number')

if st.button('Find Largest'):
    largest = max(number1, number2, number3)
    st.success(f'The largest number is: {largest}')
