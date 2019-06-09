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
        for _, directories, _ in os.walk(self._plugins_path):
            for directory in [x for x in directories if x != '__pycache__']:
                plugin_dir = os.path.join(self._plugins_path, directory)
                plugin_file = os.path.join(plugin_dir, directory + '.py')
                # check if {pluginname}.py exitsts
                if plugin_file and os.path.exists(plugin_file):
                    spec = importlib.util.spec_from_file_location('', location=plugin_file)

                    if not spec:
                        continue

                    try:
                        _plugin = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(_plugin)
                    except Exception as e: # pylint: disable=broad-except, invalid-name
                        print('failed to load plugin %s: %s' % (plugin_file, str(e)))
                        return

                    _classes = inspect.getmembers(_plugin, predicate=inspect.isclass)
                    for _, _class in _classes:
                        if inspect.isclass(_class) and not inspect.isabstract(_class):
                            if not _class.__name__.endswith('Plugin'):
                                continue

                            if _class.__name__ == 'DwarfPlugin':
                                continue

                            _has_required_funcs = False
                            _funcs = inspect.getmembers(_class, predicate=inspect.isfunction)

                            # TODO: check for all
                            for function_name, _ in _funcs:
                                if function_name == 'get_name':
                                    _has_required_funcs = True

                            if _has_required_funcs:
                                try:
                                    _instance = _class()
                                except Exception as e: # pylint: disable=broad-except, invalid-name
                                    print('failed to load plugin %s: %s' % (plugin_file, str(e)))
                                    return

                                if not isinstance(_instance, DwarfPlugin):
                                    continue

                                try:
                                    self._plugins[_instance.get_name()] = _instance
                                    _instance.on_plugin_loaded()
                                except Exception as e: # pylint: disable=broad-except, invalid-name
                                    print('failed to load plugin %s: %s' % (plugin_file, str(e)))

    def on_session_started(self):
        for plugin_name in self._plugins.keys():
            plugin = self._plugins[plugin_name]
            plugin.on_session_started(self._app)

    def on_attached(self, package):
        for plugin_name in self._plugins.keys():
            plugin = self._plugins[plugin_name]
            plugin.on_attached(self._app, package)
