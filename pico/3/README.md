In this write-up, we will explore a PicoCTF challenge from the reverse engineering category, focusing on how to determine a favorite number encoded in hexadecimal format within a binary executable. The challenge requires us to analyze the binary file using Ghidra, a powerful reverse engineering tool, to uncover the hidden value.

## Overview of the Challenge

PicoCTF is an engaging platform designed for learning cybersecurity through Capture The Flag (CTF) challenges. The reverse engineering challenges on PicoCTF are particularly valuable for beginners, as they provide practical experience in analyzing and deciphering binary files. In this specific challenge, participants are tasked with identifying a favorite number that is embedded in the binary as a hexadecimal value within a conditional statement.

## Setting Up the Environment

1. **Registration**: Before starting, ensure you have registered on the PicoCTF platform.
2. **Download the Binary**: Navigate to the reverse engineering section and download the relevant binary file associated with this challenge.
3. **Install Ghidra**: If you haven’t already, download and install Ghidra on your machine. This tool will be essential for decompiling and analyzing the binary.

## Analyzing the Binary with Ghidra

Once you have Ghidra set up and the binary loaded, follow these steps:

1. **Open the Binary**: Launch Ghidra and import the downloaded binary file.
2. **Decompile**: Use Ghidra’s decompiler feature to convert the assembly code into a more readable C-like format. This will help in understanding the logic of the program.
3. **Locate Conditional Statements**: Search through the decompiled code for conditional statements that might reference numeric values. In this case, you are looking for comparisons that involve hexadecimal values.

### Example Code Analysis

In our analysis of the decompiled code, we might encounter a line similar to:

```c
if (favorite_number == 0x1A3F) {
    // some logic
}
```

Here, `0x1A3F` is the hexadecimal representation of our target number. 

4. **Identify Favorite Number**: Note down any hexadecimal values you find in conditional statements. These values may represent the favorite number that you need to extract.

## Conclusion

After identifying the hexadecimal value from the conditional statement, convert it to decimal if necessary for submission on PicoCTF. For instance, if you found `0x1A3F`, converting it gives:

$$
0x1A3F = 6719_{10}
$$

This process not only helps in solving this specific challenge but also enhances your skills in reverse engineering by familiarizing you with tools like Ghidra and techniques for analyzing binaries.

By practicing these steps on various challenges within PicoCTF, you'll build a strong foundation in reverse engineering and cybersecurity principles, preparing you for more complex scenarios in real-world applications.

