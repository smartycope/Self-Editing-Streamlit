import streamlit as st
from code_editor import code_editor

if 'code' not in st.session_state:
    st.session_state['code'] = {'text': "code_editor('code_editor(\"\", key=\"code\")', key='code')"}

_local = locals()
_global = globals()
try:
    exec(st.session_state['code']['text'], _global, _local)
except Exception as err:
    code_editor(st.session_state['code']['text'], key='code')
    st.exception(err)
globals().update(_global)
locals().update(_local)
