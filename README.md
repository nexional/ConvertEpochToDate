# Convert Epoch To Date
Sublime Text 3 plugin to convert Epoch timestamps to Date

This plugin converts Epoch timestamp to human date timestamp. It works on the selection or the word under cursor. The replacement is done inline & can be undone using ctrl+z (undo) command.

10-13 digits are expected as Epoch timestamp. Anything else is ignored. Output Date has the format `%a %d %b %Y %H:%M:%S.ms` e.g.
`Tue 01 Jan 2019 01:02:34.786`.

There are 3 ways you can invoke the command:

* "Tools" Menu > "Convert Epoch to Date"
* Right click Context menu on selection/word & choose "Convert Epoch to Date"
* Use following keyboard shortcuts:
  * `ctrl+alt+,`  (Windows)
  * `super+alt+,` (macOS/OSX)
  * `ctrl+alt+,`  (Linux)

You can also override the default binding in your User Keybinding file e.g.

`    { "keys": ["ctrl+alt+t"], "command": "convert_epoch_to_date" }`
