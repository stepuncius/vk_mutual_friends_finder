# vk_mutual_friends_finder
It finds mutual friends of some set of people.  
###  Installation
It requires sashgorokhov/python-vkontakte library v 1.1.2  
  ```pip install python-vkontakte```
Then you need download and install this package.
```
git clone https://github.com/stepuncius/vk_mutual_friends_finder.git
python3 ./vk_mutual_friends_finder/setup.py install
```
Now it's ready to work.
###  Usage
It needs at least two arguments - two links on vkontakte profile in any form (link, id or alias).
Examples:
```Bash
python3 -m vk_mutual_friends_finder durov vk.com/id5
python3 -m vk_mutual_friends_finder https://vk.com/durov 5
python3 -m vk_mutual_friends_finder durov 5
python3 -m vk_mutual_friends_finder durov vk.com/id5 http://vk.com/id8
```
**Caution**: Result can't consist from more than 1000 users if it has more only first thousand will be shown. It's vkapi's feature.
###  Requirements
It requires sashgorokhov/python-vkontakte library. It was written and tested on python 3.4, I can't ensure normal work on other python versions.
