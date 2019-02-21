import sublime
import sublime_plugin
import re
from datetime import datetime


class ConvertEpochToDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for region in view.sel():
            if region.empty():
                region = view.word(region)

            epoch_text = view.substr(region)
            if epoch_text and re.match(r'^(\d{10,13})$', epoch_text):
                result = datetime.fromtimestamp(int(str(epoch_text)[0:10])).strftime("%a %d %b %Y %I:%M:%S %p")

                if result:
                    milsec = str(epoch_text)[10:13]
                    if milsec:
                        milsec = format(int(float('0.' + milsec) * 1000), '03d')
                        result = re.sub(r' [AP]M$', '.' + str(milsec) + '\g<0>', result)

                    if view.is_read_only():
                        sublime.status_message('ConvertEpochToDate: ' + result + ' (Warning: View readonly. Can\'t make inline replacement)')
                    else:
                        view.replace(edit, region, result)
                        sublime.status_message('ConvertEpochToDate: ' + result)
                else:
                    sublime.status_message('ConvertEpochToDate: Conversion error')
            else:
                sublime.status_message('ConvertEpochToDate: Invalid epoch timestamp: \'' + epoch_text + '\'. Must be 10-13 digits')
