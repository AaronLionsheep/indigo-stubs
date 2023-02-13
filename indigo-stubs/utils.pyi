def return_static_file(file_path: str,
                       status: int = 200,
                       path_is_relative: bool = True,
                       content_type: str = "") -> dict:
    """
    This function will accept a file path and an optional `content_type` and
    return the correctly structured dictionary that the Indigo Web Server will
    interpret as a directive to stream back the specified file.

    The response looks something like::

        {
            "status": 404,
            "headers": {
                "Content-Type": "text/html"
            },
            "file_path": "/Library/Application Support/Perceptive Automation/Indigo 2022.1/Plugins/Example HTTP Responder.indigoPlugin/Contents/Resources/static/html/static_404.html"
        }

    Parameters
    ----------
    file_path: str
        A string that represents the path to a file.

    status: int
        The HTTP status code to return, defaults to 200.

    path_is_relative: bool
        The path a full path or relative to the plugin, defaults to True.

    content_type: str
        A string to return as the mime type of the content, returns the
        appropriate type based on the file extension if none is specified.

    Returns
    -------
    response: dict
        An indigo-stubs.Dict that can be passed directly back to the Indigo Web
        Server from an HTTP processing call to your plugin.

    Raises
    ------
    indigo-stubs.utils.FileNotFoundError
        If the file doesn't exist.

    TypeError
        If file_path isn't a list of path parts or a string.
    """
    ...