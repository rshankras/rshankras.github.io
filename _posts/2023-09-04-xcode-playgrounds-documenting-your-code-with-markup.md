---
title: "Xcode Playgrounds: Documenting Your Code with Markup"
date: "2023-09-04"
---

One of the coolest features of [Xcode Playgrounds](https://rshankar.com/xcode-6-and-playground/) is the ability to add rich, formatted documentation right alongside your code. This is done using a special kind of comment called "markup".

### Basic Markup

To use markup, start a line with `//:`. This tells Playground that this line is markup, not code. Here's an example:

```
//: # Welcome to My Playground
//: This is a paragraph explaining what this playground does.

let greeting = "Hello, World!"
print(greeting)

//: ## Next Section
//: Here's a list of things we'll cover:
//: * Item 1
//: * Item 2
//: * Item 3
```

### Rendering Markup

To see your markup rendered:

1. Click on the "Editor" menu in Xcode

3. Select "Show Rendered Markup"

Now you'll see your comments beautifully formatted, with headings, paragraphs, and lists!

### Advanced Markup Features

Playground markup supports many Markdown features:

1. **Links**:

```
   //: [Apple's Swift Page](https://swift.org)
```

2. **Images**:

```
   //: ![Alt text](image_name.png)
```

Note: The image needs to be in your Playground's resources.

3. **Code blocks**:

```
   //: ```swift
   //: let code = "This is a code block"
   //: ```
```

4. **Emphasis**:

```
   //: This is *italicized* and this is **bold**.
```

### Documentation and Experiments

You can use markup to create interactive tutorials:

```
//: # Experiment: Changing Colors
//: Try changing the color values below and see what happens!

import UIKit
import PlaygroundSupport

let view = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
view.backgroundColor = .red  // Try changing this to .blue or .green

PlaygroundPage.current.liveView = view
```

This creates a mini-lesson right in your playground!

## Using Markup for Better Learning

1. **Document Your Thought Process**: Use markup to explain your code as you write it.

3. **Create Tutorials**: Make step-by-step guides for yourself or others.

5. **Organise Your Playground**: Use headings to separate different concepts or experiments.

7. **Add Context**: Explain why you're doing something, not just what you're doing.

By combining code, live views, and rich documentation, Playgrounds become not just a place to experiment, but a powerful learning tool.
