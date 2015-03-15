**Luminescence** is an application for generating HTML presentations from [Markdown](http://daringfireball.net/projects/markdown/) sources. It allows one to create simple presentations quickly.

A small and introductory example of what it can do is available [here](http://dl.dropbox.com/u/1823095/luminescence/tutorial.html).


**Installing**

Luminescence can be installed by running the following command, as root, at the terminal:

`easy_install luminescence`

(Requires Python and Setuptools.)

**Using**

`luminescence <source-file.yaml> <output-file.html>`


**Input Format**

`presentation.yaml`:
```
- contents: |
    Slide 1 Header
    ==============

    Slide 1 text.

- background-color: navy
  foreground-color: white
  contents: |
    Slide 2 Header
    ==============

    Slide 2 text.

    ![Image Alt Text](http://path/to/image.png)
```

A more detailed description is also [available](InputFormat.md).