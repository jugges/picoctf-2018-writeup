## Question
>What does asm0(0x2a,0x4f) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](//2018shell.picoctf.com/static/9dd737e97ccbb554569020e205ffa5c8/intro_asm_rev.S) located in the directory at /problems/assembly-0_3_b7d6c21be1cefd3e53335a66e7815307.

### Hint
>basical assembly [tutorial](https://www.tutorialspoint.com/assembly_programming/assembly_basic_syntax.htm)
>assembly [registers](https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm)

## Solution
Opening up `intro_asm_rev.S` we can see the so called `asm0` procedure that we run with `(0x2a,0x4f)` as parameters.
```asm
.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8]
	mov	ebx,DWORD PTR [ebp+0xc]
	mov	eax,ebx
	mov	esp,ebp
	pop	ebp	
	ret
```
We start by pushing `ebp` into the stack and moving `esp` to `ebp`.
![Image](https://www.cs.virginia.edu/~evans/cs216/guides/stack-convention.png)
[Source](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)
Moving parameter 1 at `ebp+0x8` and parameter 2 at `ebp+0xc` to `eax` and `ebx` respectivly we get:
```
eax = 0x2a
eab = 0x4f
```
To finish it off we move `ebx` to `eax`:
```
eax = eab = 0x4f
```
And move `ebp` back to `esp`, pop `ebp` and return `eax`.

### Flag
`0x4f`
