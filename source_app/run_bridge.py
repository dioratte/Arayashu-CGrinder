import platform


RAISE_ERROR = False
BRIDGE_ERROR_MESSAGE = ""

if platform.system() == "Windows":
    from source.utils.os_windows_backend import _get_bridge

    try:
        _get_bridge()
    except Exception as e:
        BRIDGE_ERROR_MESSAGE = str(e)
        print(BRIDGE_ERROR_MESSAGE)
        RAISE_ERROR = True