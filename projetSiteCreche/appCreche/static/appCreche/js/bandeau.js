 //Change la classe css de l'image pour la cacher.
      function cacher(im){
        im.classList.remove('visible');
        im.classList.add('cachee');
      }
//Change la classe css de l'image pour l'afficher.
      function afficher(im){
        im.classList.remove('cachee');
        im.classList.add('visible');
      }

// Selectionne la photo suivante
      function suivant(id){
        if(id<10){
          id++;
        }
        else{id=1;
        }
        return id;
      }


//La fonction change automatiquement la photo en appelant les fonctions ci dessus.
      function change_baniere(){

        var tab = document.getElementsByClassName('visible');
       
        n = tab[0].id;
        document.getElementById(n).style.transition = "opacity 2s";
        document.getElementById(suivant(n)).style.transition = "opacity 2s";
        cacher(document.getElementById(n));
        afficher(document.getElementById(suivant(n)));
      
      }

      var chb = setInterval(change_baniere,3000);