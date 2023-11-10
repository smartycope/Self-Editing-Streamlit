import streamlit as st
from code_editor import code_editor

resp = code_editor('st.markdown("Hello world!")')
_local = locals()
_global = globals()
exec(resp['text'], _global, _local)
globals().update(_global)
locals().update(_local)
