import CONAGUA
import paths
import ERROR

try:
    temperatura = CONAGUA.conagua('temperatura')
except Exception as e:
    error_message = str(e)
    print(error_message)
    ERROR.handle_error('CONAGUA', 'temperatura', error_message)

try:
    temperatura = CONAGUA.conagua('velocidad')
except Exception as e:
    error_message = str(e)
    print(error_message)
    ERROR.handle_error('CONAGUA', 'velocidad', error_message)

try:
    temperatura = CONAGUA.conagua('precipitacion')
except Exception as e:
    error_message = str(e)
    print(error_message)
    ERROR.handle_error('CONAGUA', 'precipitacion', error_message)
