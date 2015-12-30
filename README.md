# RomDirCleaner
A hastily coded, single pass rom folder cleaner. Tries its darndest to get rid of duplicate roms.

This was a small project I decided to try late at night with no caffeine, please don't hurt me.
RomDirClean expects you to be tidy; the directory you provide must be sorted and any duplicates must come after eachother lexicographically.
To give an example, take for instance a directory with these files:

  688 Attack Sub (U) [!].zip
  688 Attack Sub (U) [h1].zip
  688 Attack Sub (U) [h2].zip
  688 Attack Sub (U) [h3].zip
  777 Casino (Unl) [c].zip
  777 Casino (Unl) [h1].zip

RomDirClean will keep 688 Attack Sub (U) [!].zip, but delete the rest. For 777 Casino, it will not be able to make a decision,
so in a case like this it will keep both.

Lastly, I am not responsible for damage caused by running this script after improper use, it won't go off and delete things randomly,
but if you manage to use it incorrectly you may delete a file or two you didn't mean to. Be safe, be smart!
