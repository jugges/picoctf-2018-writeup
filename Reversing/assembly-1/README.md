## Question
>What does asm1(0xc8) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](//2018shell.picoctf.com/static/88fdf76b0f4d3f3bf9eff14ef98bbaa9/eq_asm_rev.S) located in the directory at /problems/assembly-1_4_99ac7ff5dfe75417ed616e35bfc2c023.

### Hint
>assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution
Lets follow the function asm1 with a parameter of `0xc8`:
```asm
.intel_syntax noprefix
.bits 32
	
.global asm1

asm1:
	push	ebp
	mov	ebp,esp
	cmp	DWORD PTR [ebp+0x8],0x9a
	jg 	part_a	
	cmp	DWORD PTR [ebp+0x8],0x8
	jne	part_b
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x2c
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
	cmp	DWORD PTR [ebp+0x8],0xc8
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp
	ret
```
```asm
	cmp	DWORD PTR [ebp+0x8],0x9a
	jg 	part_a	
```
Compare `0xc8`(our parameter) with `0x9a`, if greater - jmp -> `part_a`, so we jmp!
```asm
part_a:
	cmp	DWORD PTR [ebp+0x8],0x2c
	jne	part_c
```
Compare `0xc8`(our parameter) with `0x2c`, if not equal - jmp -> `part_c`, so we jmp!
```asm
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp
	ret
```
Move `0xc8`(our parameter) to `eax`, add `0x3` to `eax`:
`eax = (0xcb)`

And we continue to `ret` which returns `eax`.

### Flag
`(0xcb)`
