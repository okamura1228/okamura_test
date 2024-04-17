import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

# text = st.text_input('あなたの趣味を教えて下さい、')
# condition = st.slider('あなたの今の調子は', 0, 100, 50)

# 'あなたの趣味は、', text, 'です。'
# 'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='Koji Okamura', use_column_width=True)
# df = pd.DataFrame(
#     np.random.rand(100, 2),
#     columns=['lat', 'lon']
# )

# st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)