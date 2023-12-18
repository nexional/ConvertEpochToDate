import sublime
import sublime_plugin
import re
from datetime import datetime
# TODO: switch to zoneinfo after upgrading to Python 3.9
import pytz

def get_settings(string):
    return sublime.load_settings("ConvertEpochToDate.sublime-settings").get(string)

class ConvertEpochToDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        msgs = []
        for region in view.sel():
            if region.empty(): region = view.word(region)
            epoch_text = view.substr(region)
            if epoch_text and re.match(r'^(\d{10,13})$', epoch_text):

                dt = datetime.fromtimestamp(int(epoch_text[0:10]))
                dt = dt.astimezone()

                tz_pref = get_settings("timezone")
                if tz_pref:
                    try: dt = dt.astimezone(pytz.timezone(tz_pref))
                    except pytz.UnknownTimeZoneError:
                        msgs.append(f""" (Warning: Invalid timezone "{tz_pref}" defined, using local time)""")

                output_date_format = get_settings("output_date_format")
                try: 
                    result = dt.strftime(output_date_format)
                except ValueError:
                    msgs.append(f""" (Warning: Invalid format string "{output_date_format}" defined, using default)""")
                    output_date_format = "%a %d %b %Y %I:%M:%S %Z %p"
                    result = dt.strftime(output_date_format)

                if result:
                    if get_settings("show_milliseconds"):
                        milsec = epoch_text[10:13] or "0"
                        result = f"""{result} + {milsec.ljust(3, "0")}ms"""

                    if view.is_read_only():
                        if not get_settings("show_message_box") and get_settings("show_message_box_for_readonly"): sublime.message_dialog(result)
                        msgs.append(""" (Warning: View readonly{", can't make in-place replacement" if get_settings("in_place_replacement") else ""})""")
                    elif not get_settings("in_place_replacement"): msgs.append(" (Warning: in-place replacement disabled)")
                    else: view.replace(edit, region, result)

                    if get_settings("show_message_box"): sublime.message_dialog(result)

                    msgs.append(f"ConvertEpochToDate: {result}")
                else: msgs.append(f"ConvertEpochToDate: Conversion error")
            else: msgs.append(f"""ConvertEpochToDate: Invalid epoch timestamp: "{epoch_text}"; must be 10-13 digits""")

            sublime.status_message(" ".join(msgs))