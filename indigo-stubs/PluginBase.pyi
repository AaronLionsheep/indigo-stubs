from typing import List, Dict
from logging import Logger

from indigo import Device

class PluginBase:
    """
    This is the class that will define all the entry points into your plugin
    from the host process and the object bridge between your Python objects
    and the host process’s C++ objects. Your class must inherit from the
    ``indigo.PluginBase`` class. A quick note here - all bridge objects and
    communication with the IndigoServer will be done through the indigo-stubs
    module. Because it’s so important, we automatically import it for you so
    you don’t need an import statement.

    There are a few methods that the host process will call at various times
    during your plugin's lifecycle, some required and others are optional.

    Note: some of these methods may require you to subscribe to object changes.
    Specifically, if they're objects that your plugin didn't directly create
    (devices of other types) or other object types (triggers, schedules,
    variables).
    """


    def __init__(self,
                 pluginId: str,
                 pluginDisplayName: str,
                 pluginVersion: str,
                 pluginPrefs: dict):
        """
        This method gets a dictionary of preferences that the server read from disk.
        You have the opportunity here to use them or alter them if you like
        although you most likely will just pass them on to the plugin base class::

            def __init__(self, pluginPrefs):
                indigo.PluginBase.__init__(self, pluginPrefs)

        You'll most likely use the startup method, described below, to do your
        global plugin initialization.

        Parameters
        ----------
        pluginId: str
            The identifier of the plugin.

        pluginDisplayName: str
            The name of the plugin display in the user interface.

        pluginVersion: str
            The version of the plugin.

        pluginPrefs: dict
            The user preferences for the plugin.
        """
        self.stopThread: bool = False
        self.StopThread: Exception
        self.logger: Logger
        ...

    def __del__(self) -> None:
        """
        This is the destructor for the class. Again, you’ll probably just call the super class’s method::

            def __del__(self):
                indigo.PluginBase.__del__(self)
        """
        ...

    def startup(self):
        """
        This method will get called after your plugin has been initialized.

        This is really the place where you want to make sure that everything
        your plugin needs to do gets set up correctly.

        If you’re storing a config parameter that’s not editable by the user,
        this is a good place to make sure it’s there and set to the right value.

        This is not, however, where you want to initialize devices and triggers
        that your plugin may provide - those are handled after this method
        completes.

        Example::

            def startup(self):
                indigo.server.log(u"Startup called")
        """
        ...

    def shutdown(self) -> None:
        """
        This method will get called when the IndigoServer wants your plugin to
        exit. If you define a global shutdown variable, this is the place to
        set it. Other things you might do in this method: if your plugin uses
        a single interface to talk to multiple devices, this is the place where
        you would want to shut down that interface (close the serial port or
        network connection, etc.). Each device and trigger will already have had
        a chance to shut down by the time this method is called.

        **Note**: ``shutdown`` will be called after ``runConcurrentThread`` so
        cleanup here will be after any changes that might result from a loop in
        ``runConcurrentThread``.
        """
        ...

    def runConcurrentThread(self) -> None:
        """
        This method is called in a newly created thread after the ``startup()``
        method finishes executing. It’s expected that it should run a loop
        continuously until asked to shut down::

            def runConcurrentThread(self):
                try:
                    while True:
                        # Do your stuff here
                        self.sleep(60) # in seconds
                except self.StopThread:
                    # do any cleanup here
                    pass

        You must call ``self.sleep()`` with the number of seconds to delay
        between loops. ``self.sleep()`` will raise a ``self.StopThread``
        exception when you should end ``runConcurrentThread``.

        You don’t have to catch that exception if you don’t need to do any
        cleanup before returning - it will just throw out to the next level.

        **Note**: ``shutdown`` will be called after ``runConcurrentThread``
        finishes processing, so you can do your cleanup there.
        """
        ...

    def stopConcurrentThread(self) -> None:
        """
        This method will get called when the IndigoServer wants your plugin to
        stop any threads that it may have created. The default implementation
        (shown below) will set the ``stopThread`` instance variable which
        causes the ``self.sleep()`` method to throw the exception that you
        handle in ``runConcurrentThread``. In most circumstances, your plugin
        won't need to implement this method.

        Default implementation::

            def stopConcurrentThread(self):
                self.stopThread = True
        """
        ...

    def prepareToSleep(self) -> None:
        """
        The default implementation of this method will call
        ``deviceStopComm()`` for each device instance and
        ``triggerStopProcessing()`` for each trigger instance provided by your
        plugin.

        You can of course override them to do anything you like.
        """
        ...

    def wakeUp(self) -> None:
        """
        The default implementation of this method will call
        ``deviceStartComm()`` for each device instance and
        ``triggerStartProcessing()`` for each trigger instance provided by your
        plugin.

        You can of course override them to do anything you like.
        """
        ...

    def getDeviceStateList(self, dev: Device) -> List[Dict]:
        """
        If your plugin defines custom devices, this method will be called by the
        server when it tries to build the state list for your device. The
        default implementation just returns the <States> element (reformatted as
        an ``indigo.List()`` that's available to your plugin via
        ``devicesTypeDict[“yourCustomTypeIdHere”])`` in your Devices.xml file.

        You can, however, implement the method yourself to return a custom set
        of states. For instance, you may want to allow the user to create custom
        labels for the various inputs on your device rather than use generic
        “Input 1”, “Input 2”, etc., labels. Check out the EasyDAQ plugin for an
        example.

        Parameters
        ----------
        dev: indigo.Device
            The device to get the state list for.
        """

    def getDeviceDisplayStateId(self, dev):
        """

        :param dev:
        :return:
        """

    def deviceStartComm(self, dev):
        """

        :param dev:
        :return:
        """

    def deviceStopComm(self, dev):
        """

        :param dev:
        :return:
        """

    def didDeviceCommPropertyChange(self, origDev, newDev):
        """

        """

    def deviceUpdated(self, origDev, newDev):
        """

        :param origDev:
        :param newDev:
        :return:
        """

    def deviceDeleted(self, dev):
        """

        :param dev:
        :return:
        """

    def triggerStartProcessing(self, trigger):
        """

        :param trigger:
        :return:
        """

    def triggerStopProcessing(self, trigger):
        """

        :param trigger:
        :return:
        """

    def didTriggerProcessingPropertyChange(self,
                                   origTrigger,
                                   newTrigger):
        """

        :param origTrigger:
        :param newTrigger:
        :return:
        """

    def triggerCreated(self,
               trigger):
        """

        :param trigger:
        :return:
        """

    def triggerUpdated(self,
               origTrigger,
               newTrigger):
        """

        :param origTrigger:
        :param newTrigger:
        :return:
        """

    def triggerDeleted(self,
               trigger):
        """

        :param trigger:
        :return:
        """

    def variableCreated(self, var):
        """

        :param var:
        :return:
        """

    def variableUpdated(self, origVar, newVar):
        """

        :param origVar:
        :param newVar:
        :return:
        """

    def variableDeleted(self, var):
        """

        :param var:
        :return:
        """

    def applicationWithBundleIdentifier(self,
                                bundleID):
        """

        :param bundleID:
        :return:
        """

    def browserOpen(self,
            url):
        """

        :param url:
        :return:
        """

    def debugLog(self,
         msg):
        """

        :param msg:
        :return:
        """

    def errorLog(self,
         msg):
        """

        :param msg:
        :return:
        """

    def openSerial(self,
         ownerName,
         portUrl, baudrate, bytesize,
         parity, stopbits, timeout,
         xonxoff, rtscts, writeTimeout,
         dsrdtr, interCharTimeout):
        """

        :param ownerName:
        :param portUrl:
        :param baudrate:
        :param bytesize:
        :param parity:
        :param stopbits:
        :param timeout:
        :param xonxoff:
        :param rtscts:
        :param writeTimeout:
        :param dsrdtr:
        :param interCharTimeout:
        :return:
        """

    def sleep(self, seconds: float) -> None:
        """
        This method should be called from within your plugin's
        ``runConcurrentThread()`` defined method, if it is defined. It will
        automatically raise the ``StopThread`` exception when the Indigo Server
        is trying to shut down or restart the plugin.

        Parameters
        ----------
        seconds: float
            The sleep duration.
        """

    def substituteVariable(self,
                   inString,
                   validateOnly=False):
        """

        :param inString:
        :param validateOnly:
        :return:
        """

    def substituteDeviceState(self,
                      inString,
                      validateOnly=False):
        """

        :param inString:
        :param validateOnly:
        :return:
        """

    def substitute(self,
           inString,
           validateOnly=False):
        """

        :param inString:
        :param validateOnly:
        :return:
        """