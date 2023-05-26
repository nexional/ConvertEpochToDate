# Convert Epoch To Date
Sublime Text 3 plugin to convert Epoch timestamps to Date

This plugin converts Epoch timestamps to human readable date. It works on the selection or the word under cursor. The replacement is done inline & can be undone using ctrl+z (undo) command.

10-13 digits are expected as Epoch timestamp. Anything else is ignored. Output Date has the format `%m/%d/%y %H:%M:%S.ms` e.g.
`01/02/19 14:00:30.786`.

There are 3 ways you can invoke the command -

* Edit Menu > "Convert Epoch to Date"
* Context menu on selection/word & choose "Convert Epoch to Date"
* Use following keyboard shortcuts:
  * `ctrl+alt+,` (Windows)
  * `super+alt+,` (OSX)
  * `ctrl+alt+,` (Linux)
  
You can also override the default binding in your User Keybinding file e.g.

`    { "keys": ["ctrl+alt+t"], "command": "convert_epoch_to_date" }`
