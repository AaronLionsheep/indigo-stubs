from typing import List

from indigo import PluginBase

def getPlugin(identifier: str) -> PluginBase:
    """
    Returns a plugin object given the plugin id.

    Parameters
    ----------
    identifier: str
        The identifier of the plugin to retrieve.

    Returns
    -------
    plugin: indigo.PluginBase
    """
    ...

def getPluginList() -> List[PluginBase]:
    """
    Returns a list of all enabled plugin object instances.

    Returns
    -------
    plugins: list(PluginBase)
        A list of active plugin objects.
    """