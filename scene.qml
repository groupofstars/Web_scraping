import QtQuick 2.0 as CoreItems

CoreItems.Rectangle {
    width: 100; height: 100

    CoreItems.Text { text: "Hello, world!" }

    // WRONG! No namespace prefix - the Text type won't be found
    Text { text: "Hello, world!" }
}