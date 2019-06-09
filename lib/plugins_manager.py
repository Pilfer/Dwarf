import os
import inspect
import importlib.util
from lib.plugin import DwarfPlugin

class PluginsManager:

    def __init__(self, app):
        self._app = app
        self._plugins_path = os.path.join(os.path.sep.join(os.path.realpath(__file__).split(os.path.sep)[:-2]), 'plugins')

        self._plugins = {}

    def reload_plugins(self):
        for _, plugin_dirs, _ in os.walk(self._plugins_path):
            for plugin in [x for x in plugin_dirs if x != '__pycache__']:
                plugin_folder = [y for y in os.listdir(os.path.join(self._plugins_path, plugin)) if y != '__pycache__']
                for plugin_file in plugin_folder:
                    spec = importlib.util.spec_from_file_location('', location=self._plugins_path + os.path.sep + plugin + os.path.sep + plugin_file)
                    _plugin = importlib.util.module_from_spec(spec)

                    if not spec:
                        continue

                    _plugin = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(_plugin)

                    _classes = inspect.getmembers(_plugin, predicate=inspect.isclass)
                    for _, _class in _classes:
                        if inspect.isclass(_class) and not inspect.isabstract(_class):
                            if not _class.__name__.endswith('Plugin'):
                                continue

                            if _class.__name__ == 'DwarfPlugin':
                                continue

                            if not isinstance(_class(), DwarfPlugin):
                                continue

                            try:
                                _plugin = _class()
                                self._plugins[_plugin.get_name()] = _plugin
                                _plugin.on_plugin_loaded()
                            except Exception as e:
                                print('failed to load plugin %s: %s' % (plugin, str(e)))

    def on_session_started(self):
        for plugin_name in self._plugins.keys():
            plugin = self._plugins[plugin_name]
            plugin.on_session_started(self._app)

    def on_attached(self, package):
        for plugin_name in self._plugins.keys():
            plugin = self._plugins[plugin_name]
            plugin.on_attached(self._app, package)
