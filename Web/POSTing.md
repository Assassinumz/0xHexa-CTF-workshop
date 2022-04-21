# Challenge
Use these cerdentials to login: Email: vikasana@presidencyuniversity.in Password: wordpass321

And get to the admin account (admin@presidencyuniversity.in) to get the flag.

http://167.172.153.242:8005/

# Solution
On opening the webapp we can see a login page, after using the provided credentials we can see a welcome page and a button redirecting to `/profile` which just prints the email and name of the user and we have nothing much after this point.

The name of the challenge emphasizes on the word POST so let's try analyzing the requests of the application. You can use any proxy of your choice for this or you could just stick with dev tools which allows you to edit post request. In your browser's dev tools head over to the network tab and analyze the redirects.

We can notice that the POST request for the page `/profile` is only using the email parameter to authenticate `email=vikasana@presidencyuniversity.in` so let's change the email to `email=admin@presidencyuniversity.in` since it's asked in the challenge to login with that email. After changing and sending a new request we get the flag instead of user details.

# Flag
hexaCTF{P0sT_R3qu3sT_T@mp3RiNg}