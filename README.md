Find the posibles soluction for the play DrawSomthing. Django - Python


If you don´t speak english and you are playing this game <strong>DrawSomthing</strong> with just draw and random letters, some words are hard to find, so  I developed this way to
find the correct words. If you look the game, provides two kind, one it´s the exact number of letters of the correct answer and the most important of all the letter choices. So,
we these facts we can easily tell if a candidate word is a subset of the letter choices


But you may ask where to get those candidate words to compare with letter choices? so because, If I put the exact number of the letters of the correct answer  and all the letter
choice with this code <strong>itertools.permutations</strong> generate a list a thousands of words of posible soluctions, but How can I get or How can I reduce this number,
so luckily we are <strong>NLTK Data</strong> and we need to install this package.

SentiWordNet can be imported like this:

>>> from nltk.corpus import sentiwordnet as swn


<p>
  <strong>Requirements.</strong>
</p>
<ol>
   <li>
    <p>
      Python 3.5+ (Developed with Python 3.8).
    </p>  
  </li>
  
  
   <li>
    <p>
    Django 2.2.
    </p>  
  </li>
  
 
  
   <li>
    <p>
    Installing NLTK Data <strong>pip3 install nltk</strong> Read here <a href="https://www.nltk.org/data.html">https://www.nltk.org/data.html</a>
    </p>  
  </li>
 
</ol>



Example Question

  Word length:5
  Letter Choices: RUFTGFISTZLX
  Answer: FRUIT
  


<p>
  The code return 42 word candidate. COOL!
</p>


<img src="https://i.ibb.co/gTjGgWR/Whats-App-Image-2021-04-13-at-5-18-59-PM.jpg">


