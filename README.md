# N3-dowloader

Python utility for downloading DeepZoom pyramids (```.zip```) from N3

Works with public blocks for now. Block identifier is specified as command-line parameter.  
Requires base Python only, developed and used with 3.9.1 embeddable.

Example usage:

    python n3dl.py 7430

will download image pyramids ```1362_5189_7430_D1R_P70_F_E16_s002.zip``` to ```1362_5189_7430_D1R_P70_F_E16_s023.zip```.