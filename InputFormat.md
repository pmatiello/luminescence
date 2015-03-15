### Introduction ###

Luminescence input files are a combination of both [YAML](http://en.wikipedia.org/wiki/Yaml) and [Markdown](http://daringfireball.net/projects/markdown/). The YAML part will structure the presentation, defining each slide and its properties. Then, every slide is expected to have a `contents` field, which should describe the slide's contents in Markdown format.

This document describes the expected syntax of input files in a abstract, semi-formal, fashion. A concrete example is available at the [source code](http://code.google.com/p/luminescence/source/browse/docs/tutorial.yaml) of the [introductory tutorial](http://dl.dropbox.com/u/1823095/luminescence/tutorial.html).

### Slide Syntax ###

Slides are expected to be described in the following syntax:

```
- property1: value 1
  property2: value 2
  contents: |
    Slide contents.
```

The leading dash in the first line is required, as it signals a new slide. Properties are optional.

### Presentation Syntax ###

Presentations are composed by a ordered set of slides. The following example should illustrate the expected format:

```
- property: value
  contents: |
    Slide 1 Header
    ==============

    Slide 1 text.

- contents: |
    Slide 2 Header
    ==============

    Slide 2 text.
```

### Supported Properties ###

Properties are encoded in the output file, and managed by Javascript code defined by the template. Currently, the following properties are supported by the default template:

| **Property Name**      | **Description**                    | **Default value**            | **Usage example**               |
|:-----------------------|:-----------------------------------|:-----------------------------|:--------------------------------|
| **`background-color`** | Background color                 | white                      | `background-color: "#ffffff"` |
| **`foreground-color`** | Default color for text           | black                      | `foreground-color: "#000000"` |
| **`link-color`**       | Color for links                  | same as `foreground-color` | `link-color: "#0000ff"`       |
| **`fade-in`**          | Fade-in effect duration (in ms)  | 0 ms (no effect)           | `fade-in: 200`                |
| **`fade-out`**         | Fade-out effect duration (in ms) | 0 ms (no effect)           | `fade-in: 200`                |