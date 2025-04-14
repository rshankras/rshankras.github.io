---
title: "Convert SVG to PNG on macOS the Easy Way with sips"
date: 2025-04-14
description: "Learn how to quickly convert SVG vector files to PNG raster images directly from your macOS Terminal using the built-in sips command, including generating @1x and @2x assets."
categories: 
  - "macos"
  - "development"
  - "tips"
  - "terminal"
tags: 
  - "svg"
  - "png"
  - "conversion"
  - "sips"
  - "command-line"
  - "graphics"
  - "macos-dev"
---

Need to turn those crisp SVG vector files into PNGs on your Mac? Maybe for an app icon, a website, or just general use? Forget installing extra software! macOS comes with a handy command-line tool called `sips` (Scriptable Image Processing System) that gets the job done quickly.

Let's dive in.

## Basic SVG to PNG Conversion

First, open your Terminal application. Let's say you have an SVG file named `my_icon.svg` on your Desktop.

1.  **Navigate to the directory:**
    ```bash
    cd ~/Desktop
    ```

2.  **Run the `sips` command:**
    ```bash
    sips -s format png my_icon.svg -o my_icon.png
    ```

Just like that! You'll find `my_icon.png` on your Desktop. `sips` does a good job preserving transparency, which is crucial for icons.

*   `-s format png`: Tells `sips` to set the output format to PNG.
*   `my_icon.svg`: Your input file.
*   `-o my_icon.png`: Specifies the output file name.

## Generating @1x and @2x PNGs

Often, especially for app development, you need images at different resolutions (pixel densities). For instance, a 20x20 point icon needs a 20x20 pixel PNG (@1x) and a 40x40 pixel PNG (@2x) for Retina displays. `sips` can handle this too with the `--resampleHeightWidth` option.

Let's create @1x and @2x versions for a desired 20-point size:

1.  **Calculate pixel dimensions:**
    *   @1x: 20 points * 1 = 20x20 pixels
    *   @2x: 20 points * 2 = 40x40 pixels

2.  **Run `sips` for each size (assuming `icon.svg` is your input):**
    ```bash
    # Generate @1x version (20x20 pixels)
    sips --resampleHeightWidth 20 20 -s format png icon.svg -o icon.png

    # Generate @2x version (40x40 pixels)
    sips --resampleHeightWidth 40 40 -s format png icon.svg -o icon@2x.png
    ```

Now you have `icon.png` (20x20) and `icon@2x.png` (40x40), perfectly named for Xcode's Asset Catalog.

**A Note on Quality:** While `sips` is convenient, it might sometimes struggle with very complex SVGs, potentially causing distortion at small sizes. If you need pixel-perfect results, especially for intricate status bar icons, consider simplifying your SVG or using a dedicated graphics application (like Sketch, Figma, Illustrator) to export the PNGs directly at the target pixel sizes.

## Creating Standard App Icon Sizes (16px to 1024px)

Need the full set of PNGs for a macOS application icon (the one you see in the Dock and Finder)? That typically requires sizes like 16x16, 32x32, 64x64, 128x128, 256x256, 512x512, and 1024x1024 pixels.

You can generate these with `sips` too. If you have separate SVGs for light and dark modes (e.g., `appicon_light.svg`, `appicon_dark.svg`), you'll run the commands for each.

Here's how you'd generate the sizes for `appicon_light.svg`:

```bash
sips --resampleHeightWidth 16 16 -s format png appicon_light.svg -o appicon_light_16x16.png
sips --resampleHeightWidth 32 32 -s format png appicon_light.svg -o appicon_light_32x32.png
sips --resampleHeightWidth 64 64 -s format png appicon_light.svg -o appicon_light_64x64.png
sips --resampleHeightWidth 128 128 -s format png appicon_light.svg -o appicon_light_128x128.png
sips --resampleHeightWidth 256 256 -s format png appicon_light.svg -o appicon_light_256x256.png
sips --resampleHeightWidth 512 512 -s format png appicon_light.svg -o appicon_light_512x512.png
sips --resampleHeightWidth 1024 1024 -s format png appicon_light.svg -o appicon_light_1024x1024.png
```

Repeat the process for `appicon_dark.svg`, changing the input and output filenames accordingly.

Once you have all these PNGs, you typically drag them into an "AppIcon" set within your Xcode project's `Assets.xcassets` file. Xcode then compiles them into the final `.icns` file for your application.

## Want to Learn More About `sips`?

`sips` can do much more than just format conversion and resizing! Check out its options in the Terminal:

*   `man sips`: The full manual page.
*   `sips -h`: Short help summary.
*   `sips -H`: Longer help summary.
*   `sips --formats`: See all image formats `sips` understands.

## Conclusion

The built-in `sips` command is a powerful and convenient tool for quick image manipulations on macOS, especially for converting SVGs to PNGs and generating standard asset sizes. While dedicated graphics apps offer more control, `sips` is fantastic for straightforward tasks and automation right from your Terminal. Give it a try! 