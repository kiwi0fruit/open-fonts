import execnet

MODULE = "ff_funcs"
FF_PYTHON = "C:/Program Files (x86)/FontForgeBuilds/bin/ffpython.exe"


def ff(*args):
    """
    function_name: str=args[0]
    Code adapted from https://stackoverflow.com/a/44965570
    """
    gw = execnet.makegateway("popen//python=" + FF_PYTHON)
    channel = gw.remote_exec("""
        from {} import {} as the_function
        channel.send(the_function(*channel.receive()))
    """.format(MODULE, args[0]))
    channel.send(args[1:])
    return channel.receive()
