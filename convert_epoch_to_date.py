import sublime
import sublime_plugin
import re
from datetime import datetime


class ConvertEpochToDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                region = self.view.word(region)

            epoch_text = self.view.substr(region)
            if epoch_text and re.match(r'^(\d{10,13})$', epoch_text):
                milsec = str(epoch_text)[10:13]
                if milsec:
                    milsec = format(int(float('0.' + milsec) * 1000), '03d')
                result = datetime.fromtimestamp(int(str(epoch_text)[0:10])).strftime("%a %d %b %Y %H:%M:%S") + ('.' + str(milsec) if milsec else '')

                if result:
                    self.view.replace(edit, region, result)

                sublime.status_message('Converted: \'' + epoch_text + '\' --> \'' + result + '\'')
            else:
                sublime.status_message('Not a valid epoch time: \'' + epoch_text + '\'')
