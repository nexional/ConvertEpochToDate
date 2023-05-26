# Convert Epoch To Date

## Installation

* Install [Sublime Text Package Control](https://packagecontrol.io). Ignore if installed already
* Tools > Command Palette > Input/select `Package Control: Install Package`
* Enter `ConvertEpochToDate`

## Documentation

Sublime Text package to convert [Epoch timestamps](https://www.wikiwand.com/en/Unix_time) to human date. Works with Sublime Text v2.x or v3.x

This package converts Epoch timestamp to human date in your local time zone. It works on the selection or the word under caret (not mouse pointer). The replacement is done in-place & can be undone using Undo (ctrl+z) command. In-place replacement can be disabled if desired (refer **Customization** section below).

If the view/file is readonly or in-place replacement can't be made then only the status bar message is shown. A message box is displayed in this case which can be disabled.

10-13 digits are expected as Epoch timestamp. Anything else is ignored.

Default output date format is `%a %d %b %Y %I:%M:%S %p + XXXms` e.g.
`Tue 01 Jan 2019 01:02:34 AM + 123ms`. It can be customized to the format you want (refer **Customization** section below).

Any output/messages/errors are always displayed in Status bar.

## How to use

There are 4 ways you can invoke the command:

* Tools > "Convert Epoch to Date"
* Context menu (Right click) > "Convert Epoch to Date"
* Command Palette (_Ctrl + Shift + P_ on Windows or _Cmd + Shift + P_ on Mac) > Input "Convert Epoch To Date"
* Use following keyboard shortcuts:
  * `ctrl+alt+,`  (Windows)
  * `super+alt+,` (macOS/OSX)
  * `ctrl+alt+,`  (Linux)

You can also override the default binding in your User Key Binding file e.g.

`{ "keys": ["ctrl+alt+t"], "command": "convert_epoch_to_date" }`

## Customization

Following parameters can be overridden in User Settings file (_Preferences > Package Settings > ConvertEpochToDate > Settings - User_) to the value desired:

```json
{
    // in-place replacement to date
    "in_place_replacement": true,

    // defines custom output date format. visit http://strftime.org for possible format directives
    "output_date_format": "%a %d %b %Y %I:%M:%S %p",

    // if set to true, appends milliseconds at the end of output date
    "show_milliseconds": true,

    // shows message box for output date
    "show_message_box": false,

    // shows message box only for readonly views. not used if show_message_box set to true
    "show_message_box_for_readonly": true
}
```

## License

[GNU General Public License v3.0](https://github.com/nexional/ConvertEpochToDate/blob/master/LICENSE)

## Issues

Please report any bugs/issues [here](https://github.com/nexional/ConvertEpochToDate/issues/new)

## Links

* ConvertEpochToDate on [GitHub](https://github.com/nexional/ConvertEpochToDate) and [PackageControl](https://packagecontrol.io/packages/ConvertEpochToDate)
* [Epoch timestamp](https://www.wikiwand.com/en/Unix_time)
* [Date format directives](http://strftime.org)
