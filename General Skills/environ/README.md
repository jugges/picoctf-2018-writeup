## Question
>Sometimes you have to configure environment variables before executing a program. Can you find the flag we've hidden in an environment variable on the shell server?

### Hint
>unix [env](https://www.tutorialspoint.com/unix/unix-environment.htm)

## Solution
Listing all all environment variables is as easy as executing `env`, but because we are lazy, we are going to use some grep magic:
```bash
pico-2018-shell:~$ env | grep -E "picoCTF{.+}"                                     
SECRET_FLAG=picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}
```

### Flag
`picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}`
