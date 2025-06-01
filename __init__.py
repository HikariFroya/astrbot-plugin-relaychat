# AstrBot/data/plugins/astrbot_plugin_relaychat/__init__.py

# 这个文件可以将 astrbot_plugin_relaychat 目录标记为一个Python包。
# 对于插件加载，AstrBot 框架可能会查找并执行这个文件中的特定函数或导入特定的类，
# 例如，通过扫描所有插件包来找到插件的 Star 类。

# 如果 RelayChatPlugin (Star 类) 在 main.py 中，
# 并且 AstrBot 框架通过直接导入插件包名（例如 import astrbot_plugin_relaychat.main）来加载，
# 那么这个 __init__.py 通常不需要做太多事情。

# 你可以显式地从这里导出你的 Star 类，但这通常不是必需的，
# 因为框架的插件加载器会自己查找。
# 例如，如果需要：
# from .main import RelayChatPlugin
# __all__ = ["RelayChatPlugin"]

# 大多数情况下，保持为空即可。
