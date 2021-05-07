# Blind Date

The France CyberSecurity Challenge (FCSC) had some really interesting challenges this year. One of them was a classic blind ROP exploitation but because it was my first one, I was so hyped to solve it that I thought it would be really nice to explain the exploit step by step.

<p align="center">
    <img src="images/chall.png">
</p>

## Entry point

So we only have a remote service that we can connect to. Let's see if we can abuse it.

![intro](images/intro.png)

It just asks for our name and exits. From there we can imagine 2 possible vulnerabilities: a format string attack using the output with our input and a potential buffer overflow on the name buffer.

### The format string

The format string vulnerability is a well known vulnerability concerning an unsafe usage of a `printf` function which supports formatting, such as `printf`, `sprintf`, `fprintf`... We will not go into details there because as we will see down below, there are no such vulnerability here, but I highly suggest to check [LiveOverflow video](https://www.youtube.com/watch?v=0WvrSfcdq1I) on the topic to learn more.

The cool part about this vulnerability is that it is very easy to test, we only have to pass some formatting characters as input such as `%x` and check if we can dump the memory. If so then we can conclude that the binary is vulnerable and that the running code must be something like this:

```c
char username[SIZE];
// [...] <--- get input with `scanf` or `gets` or whatever
printf("Thanks ");
printf(username); // <--- unsafe line
printf("\nBye!\n");
```

![fmt](images/fmt.png)

Erf, sometime you win, sometime you lose, nothing here, the code is safe and must look like:

```c
char username[SIZE];
// [...] <--- get input with `scanf` or `gets` or whatever
printf("Thanks %s\nBye!\n", username); // <--- safe line
```
