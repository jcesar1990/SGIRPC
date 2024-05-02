import CONAGUA
import paths
import ERROR

try:
    temperatura = CONAGUA.conagua('temperatura')
except Exception as e:
    error_message = str(e)
    print(error_message)
    ERROR.handle_error('CONAGUA', 'temperatura', e)
