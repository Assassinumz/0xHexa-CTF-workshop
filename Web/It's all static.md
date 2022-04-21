# Challenge
This webpage seems to be hiding something http://167.172.153.242:8001/

# Solution
Open the source code of the webpage with ctrl/cmd + u or right click and hit view source, if you're using a mobile just prefix the url like this `view-source:http://167.172.153.242:8001/`

After viewing the source code you can see the first part of the flag in a comment of the html document 

`<!-- Flag part 1/3: hexaCTF{St@TIc -->`

To get the second part open the `styles.css` file http://167.172.153.242:8001/styles.css you can see a comment again with part 2 of the flag in here
```
/*
* Flag part 2/3: _PAg3
*/
```
To get the final part open the `script.js` file http://167.172.153.242:8001/script.js and once more you can find the last part in a comment

`// Flag part 3/3: _Fl@G}`

# Flag
hexaCTF{St@TIc_PAg3_Fl@G}