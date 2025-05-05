# cpcd_log_decoder
cpcd_log_decoder is a Python utility that decodes raw frames from a cpc-daemon log file to aid in debugging.

# Instructions
   1. Make sure frame trace is enabled in your cpcd.conf:

   2. Run cpcd_log_decoder.py on your cpcd log file which includes the frame traces:
   ```
   $ python3 cpcd_log_decoder.py <infile> <outfile>
   ```
   3. The resulting output file will include all the content from the original file, plus an extra line after each frame showing some additional decoding.

   4. The script at util/extract_spinel_props.py was used with spinel.h to build the list of properties from the C enums contained within spinel.h. The output of this was manually inserted into cpcd_log_decoder.py.

# Contacts
- Kris Young - kris.young@silabs.com

# License
This is an AS-IS example project. This code is licensed under a ZLIB license by Silicon Labs, Inc.