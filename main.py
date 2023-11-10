import streamlit as st
from code_editor import code_editor

if 'code' not in st.session_state:
    st.session_state['code'] = {'text': "code_editor('code_editor(\"\", key=\"code\", buttons=[{\\n\\t\"name\": \"Run\",\\n\\t\"feather\": \"Play\",\\n\\t\"commands\": [\"submit\"],\\n\\t\"alwaysOn\": True\\n}])', key=\'code\', buttons=[{'name':'Run','feather':'Play','commands':['submit'],'alwaysOn':True}])"}

_local = locals()
_global = globals()
try:
    exec(st.session_state['code']['text'], _global, _local)
except Exception as err:
    try:
        code_editor(st.session_state['code']['text'], key='code')
    except st.errors.DuplicateWidgetID:
        pass
    st.exception(err)
globals().update(_global)
locals().update(_local)
