import os
import importlib.util


class PluginsManager:

    def __init__(self, app):
        self._app = app
        self._plugins_path = '/'.join(os.path.realpath(__file__).split('/')[:-2]) + '/plugins'

        self._plugins = {}

    def reload_plugins(self):
        for plugin in os.listdir(self._plugins_path):
            spec = importlib.util.spec_from_file_location('', location=self._plugins_path + '/' + plugin)

            # __pycache__
            if plugin.startswith('__'):
                continue

            _plugin = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(_plugin)
            try:
                _plugin = _plugin.Plugin()
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
