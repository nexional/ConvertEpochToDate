# Convert Epoch To Date
Sublime Text plugin to convert [Epoch timestamps](https://www.wikiwand.com/en/Unix_time) to human date. Works with Sublime Text v2.x or v3.x

This plugin converts Epoch timestamp to human date timestamp in your local time zone. It works on the selection or the word under caret (not mouse pointer). The replacement is done inline & can be undone using Undo (ctrl+z) command. Output date message is also shown in Status bar.

If the view/file is readonly or inline replacement can't be made then only the status bar message is shown.

10-13 digits are expected as Epoch timestamp. Anything else is ignored. Output Date has the format `%a %d %b %Y %I:%M:%S.ms %p` e.g.
`Tue 01 Jan 2019 01:02:34.786 AM`.

There are 4 ways you can invoke the command:

* Tools > "Convert Epoch to Date"
* Context menu (Right click) > "Convert Epoch to Date"
* Command Palette (_Ctrl + Shift + P_ on Windows or _Cmd + Shift + P_ on Mac) > Input "Convert Epoch To Date"
* Use following keyboard shortcuts:
    * `ctrl+alt+,`  (Windows)
    * `super+alt+,` (macOS/OSX)
    * `ctrl+alt+,`  (Linux)

You can also override the default binding in your User Keybinding file e.g.

`    { "keys": ["ctrl+alt+t"], "command": "convert_epoch_to_date" }`

## Installation

* Install the [Sublime Text Package Control](https://packagecontrol.io) plugin. Ignore if installed already
* Tools > Command Palette > Input/select `Package Control: Install Package`
* Enter `ConvertEpochToDate`

## License

GNU General Public License v3.0. [More details](https://github.com/nexional/ConvertEpochToDate/blob/master/LICENSE)

## Links

* PackageControl: [ConvertEpochToDate](https://packagecontrol.io/packages/ConvertEpochToDate)
* GitHub: [ConvertEpochToDate](https://github.com/nexional/ConvertEpochToDate)
