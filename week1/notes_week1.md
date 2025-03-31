<hr>
<div style="background-color: lightgray; padding: 20px; color: black;">
<div>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Coursera-Logo_600x600.svg/1024px-Coursera-Logo_600x600.svg.png" style="float: right; margin-right: 30px;" width="120"/> 
<font size="6.5" color="#0056D2"><b>Composing File and Data Solutions</b></font> <br>
<font size="5.5" color="#0056D2"><b>Linux and Bash for Data Engineering </b></font> 
</div>
<div style="text-align: left">  <br>
Edison David Serrano Cárdenas. <br>
MSc en Matemáticas Aplicadas <br>
CIMAT - Sede Guanajuato <br>
</div>

</div>
<hr>

##  <font color="#0056D2" >**Objetives**</font> 
In this module, you will learn to use Linux to compose file and data management solutions. You will also learn to search the filesystem, modify files, directories and control permissions. You will then process text in Bash and apply this knowledge to create a search solution in Bash.
## <font color="#0056D2" >**Introduction to Searching the Filesystem in Linux**</font> 
<font color="#0056D2" >**Objetives**</font> 

- Why would you want to search the filesystem?
- Using the locate and find commands to find files?
- Using xargs



 <font color="#0056D2" >**Key Points**</font> 

- Searching file systems is needed to locate files as data grows. Visual scanning fails.
- Live searches with find are slow but thorough. Use locate for fast searches if indexed.

- Tools like xargs allow acting on search results for automation.

<font color="#0056D2" >**Methods for Searching a Filesystem in Linux**</font> 


**visual**         <br>
|_____ foo.txt  <br>
|_____ dir      <br>

**live**            <br>
|_____ find .txt  <br>

**visual**          <br>
|_____ locate .txt  <br>


<font color="#0056D2" >**Using the Locate Command to Find Files in Linux**</font> 



Locate: `AWS CloudShell` 


>```console
> [cloudshell-user@... ]$ sudo yum install mlocate
> ...
> [cloudshell-user@... ]$ sudo updatedb
> [cloudshell-user@... ]$ locate .zshrc
> /etc/skel/.zshrc
> /home/cloudshell-user/.zshrc
> [cloudshell-user@... ]$ locate -c .zshrc
> 2
> [cloudshell-user@... ]$ locate -c .ZSHRC
>
> [cloudshell-user@... ]$ locate -i .ZSHRC
> /etc/skel/.zshrc
> /home/cloudshell-user/.zshrc
> ```
