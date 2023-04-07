import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
st.write('DataFrame')

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラム')
if button:
  right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味:', text

condition = st.sidebar.slider('あなたの今の調子は', 0, 100, 50)
'コンディション：', condition


# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.bar_chart(df)

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# st.write(df)
# # widthとheightが選択できる
# st.dataframe(df.style.highlight_max(axis=0), width=1000, height=500)
# # 静的なテーブル
# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
