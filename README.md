# picoCTF 2018 Writeup
Note that I started solving the CTF before making this write up so I'll start documenting from my current position in the CTF.
Special thanks to [@PlatyPew](https://github.com/PlatyPew) for his README I copied for my own write up!

# Content Page
- [Binary Exploitation](#binary-exploitation)
- [Cryptography](#cryptography)
- [Forensics](#forensics)
- [General Skills](#general-skills)
- [Reversing](#reversing)
- [Web Exploitation](#web-exploitation)

## Binary Exploitation
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/buffer%20overflow%200">buffer overflow 0</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/leak-me">leak-me</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/shellcode">shellcode</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/got-2-learn-libc">got-2-learn-libc</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/echooo">echooo</a></td>
            <td markdown="span">300</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Binary%20Exploitation/got-shell%3F">got-shell?</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>

## Cryptography
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Cryptography/Crypto%20Warmup%201">Crypto Warmup 1</a></td>
            <td markdown="span">75</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/Crypto%20Warmup%202">Crypto Warmup 2</a></td>
            <td markdown="span">75</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/HEEEEEEERE%27S%20Johnny!">HEEEEEEERE'S Johnny!</a></td>
            <td markdown="span">100</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/caesar%20cipher%201">caesar cipher 1</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/hertz">hertz</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Cryptography/rsa-madlibs">rsa-madlibs</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>

## Forensics
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Forensics/Forensics%20Warmup%201">Forensics Warmup 1</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Forensics%20Warmup%202">Forensics Warmup 2</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Desrouleaux">Desrouleaux</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Reading%20Between%20the%20Eyes">Reading Between the Eyes</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Recovering%20From%20the%20Snap">Recovering From the Snap</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/admin%20panel">admin panel</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/hex%20editor">hex editor</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Truly%20an%20Artist">Truly an Artist</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/now%20you%20don%27t">now you don't</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Ext%20Super%20Magic">Ext Super Magic</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Lying%20Out">Lying Out</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/What%27s%20My%20Name%3F">What's My Name?</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/Malware%20Shops">Malware Shops</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Forensics/LoadSomeBits">LoadSomeBits</a></td>
            <td markdown="span">550</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>

## General Skills
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="General%20Skills/General%20Warmup%201">General Warmup 1</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/General%20Warmup%202">General Warmup 2</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/General%20Warmup%203">General Warmup 3</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/Resources">Resources</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/grep%201">grep 1</a></td>
            <td markdown="span">75</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/net%20cat">net cat</a></td>
            <td markdown="span">75</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/strings">strings</a></td>
            <td markdown="span">100</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/pipe">pipe</a></td>
            <td markdown="span">110</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/grep%202">grep 2</a></td>
            <td markdown="span">125</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/Aca-Shell-A">Aca-Shell-A</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/environ">environ</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/ssh-keyz">ssh-keyz</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/what%20base%20is%20this%3F">what base is this?</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/you%20can%27t%20see%20me">you can't see me</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/absolutely%20relative">absolutely relative</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/in%20out%20error">in out error</a></td>
            <td markdown="span">275</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/learn%20gdb">learn gdb</a></td>
            <td markdown="span">300</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/store">store</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="General%20Skills/script%20me">script me</a></td>
            <td markdown="span">500</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>

## Reversing
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Reversing/Reversing%20Warmup%201">Reversing Warmup 1</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/Reversing%20Warmup%202">Reversing Warmup 2</a></td>
            <td markdown="span">50</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/assembly-0">assembly-0</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Reversing/be-quick-or-be-dead-1">be-quick-or-be-dead-1</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>

## Web Exploitation
<table>
    <thead>
        <tr class="header">
            <th>Challenges</th>
            <th>Points</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation%2FInspect%20Me">Inspect Me</a></td>
            <td markdown="span">125</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Client%20Side%20is%20Still%20Bad">Client Side is Still Bad</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Logon">Logon</a></td>
            <td markdown="span">150</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Irish%20Name%20Repo">Irish Name Repo</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Mr.%20Robots">Mr. Robots</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Solved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/No%20Login">No Login</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Secret%20Agent">Secret Agent</a></td>
            <td markdown="span">200</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Buttons">Buttons</a></td>
            <td markdown="span">250</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Artisinal%20Handcrafted%20HTTP%203">Artisinal Handcrafted HTTP 3</a></td>
            <td markdown="span">300</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Flaskcards">Flaskcards</a></td>
            <td markdown="span">350</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/fancy-alive-monitoring">fancy-alive-monitoring</a></td>
            <td markdown="span">400</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Secure%20Logon">Secure Logon</a></td>
            <td markdown="span">500</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/Help%20Me%20Reset%202">Help Me Reset 2</a></td>
            <td markdown="span">600</td>
            <td markdown="span">Unsolved</td>
        </tr>
        <tr>
            <td markdown="span"><a href="Web%20Exploitation/A%20Simple%20Question">A Simple Question</a></td>
            <td markdown="span">650</td>
            <td markdown="span">Unsolved</td>
        </tr>
    </tbody>
</table>
