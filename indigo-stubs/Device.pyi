class Device:
    """
    This base class provides for all the common properties of a device
    (including devices defined by Server plugins) and each subclass also
    inherits all the commands in the device command namespace
    (``indigo.device.*``).

    Like other high-level objects in Indigo, there are rules for modifying
    devices.

    For Scripters and Plugin Developers:

    - To create, duplicate, delete, and send commands to a device, use the
      appropriate command namespace as defined below
    - To modify an device's definition get a copy of the device, make the
      necessary changes, then call ``myDevice.replaceOnServer()``

    For Plugin Developers:

    - To update a plugin's props on a device on the server, call
      ``myDevice.replacePluginPropsOnServer(newPropsDict)`` rather than try to
      update them on the local device
    - To change a device's state on the server, use
      ``myDevice.updateStateOnServer(key='keyName', value='Value')``
    - To change multiple device states on the server at one time, use
      ``myDevice.updateStatesOnServer(update_list)`` passing a dictionary that
      looks like this::

          # New code equivalent that is much more efficient:
          key_value_list = [
              {'key':'someKey1', 'value':True},
              {'key':'someKey2', 'value':456},
              {'key':'someKey3', 'value':789.123, 'uiValue':"789.12 lbs", 'decimalPlaces':2}
          ]
          dev.updateStatesOnServer(key_value_list)
    """