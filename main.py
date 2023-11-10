import streamlit as st
from code_editor import code_editor

resp = code_editor('st.markdown("hello world")', key='this')
_local = {}
_global = globals()
exec(resp['text'], _global, _local)
globals().update(_global)
locals().update(_local)
