print('''                                    
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
       .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'      
      ''')
print("Welcome to Minchu Game.")
print("Your mission is to find the best way to win her over!") 


#Write your code below this line 👇

first = input('You are in front of Minchu :), her eyes look like slit. Type "pet" to pet her or type "play" to play with her.').lower()

second = input('Do you want to pet her? Type "head" to pet her on her head or type "belly" to pet her on her belly.').lower()

third = input('Ooo you have pet her enough :) Now he eyes are like full moon ●. Type "pet" to pet her or type "play" to play with her.').lower()

if first == "pet":
  print("Hurry!! She's liking it she purring :)")
  
  if second == "head":
    print("Ooo, She loves it! She licks you ❤")
    
    if third == "pet":
      print('''
            Ahaa... she super playfull
            

(:`--..___...-''``-._             |`._
  ```--...--.      . `-..__      .`/ _\  
            `\     '       ```--`.    />
            : :   :               `:`-'
             `.:.  `.._--...___     ``--...__      
                ``--..,)       ```----....__,) ●●●●●

            
            ''')
    else:
      
      print('''
            Oh no. she doent lik it. she hits you with her paws.         
          
            Game Over
            ''')
  else:
    print('''
          Oh nooo, hisss she doent like petting on her belly

          Game over.          
          ''')
else:
  print('''
        Oh, she's not interested to play.

        Game Over
        ''')
  