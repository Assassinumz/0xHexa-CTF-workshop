# Challenge
Hey, I made a website which checks if the host is up by pinging it. Can you check if its working? http://167.172.153.242:8004/

# Solution
On opening a website we can see an input field which asks us to enter a host. On entering `www.google.com` we can see the output of a `ping` command, with this we can assume it's taking the host input from the webpage, passing it to a ping system command and returning the output to the webpage.

We can use `&&` and concatenate commands, after using `www.google.com && ls` we can see the directory listing and there is our `flag.txt` so let's read it's contents with the payload:

`www.google.com && cat flag.txt`

and we get the flag along with the other output.

# Flag
hexaCTF{iS_TH!s_RC3}